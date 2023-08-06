use arrow::array::Array;
use arrow::array::StringArray;
use arrow::datatypes::{DataType, Field, Schema};
use arrow::record_batch::RecordBatch;
use quick_xml::events::Event;
use quick_xml::reader::Reader;
use quick_xml::Error as XmlError;
use std::borrow::Cow;
use std::collections::{HashMap, HashSet};
use std::error::Error;
use std::fmt;
use std::fs::File;
use std::io::{BufWriter, Error as IoError};
use std::str::Utf8Error;
use std::sync::Arc;
use std::time::Instant;

const MISSING: &str = "null";

#[derive(Debug)]
pub enum CustomError {
    QuickXml(quick_xml::Error),
    GetTags(GetTagsError),
}
impl From<Utf8Error> for CustomError {
    fn from(err: Utf8Error) -> CustomError {
        CustomError::QuickXml(quick_xml::Error::from(err))
    }
}

impl fmt::Display for CustomError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            CustomError::QuickXml(err) => write!(f, "QuickXmlError: {}", err),
            CustomError::GetTags(err) => write!(f, "GetTagsError: {:?}", err),
        }
    }
}

impl Error for CustomError {}

impl From<quick_xml::Error> for CustomError {
    fn from(err: quick_xml::Error) -> CustomError {
        CustomError::QuickXml(err)
    }
}

impl From<GetTagsError> for CustomError {
    fn from(err: GetTagsError) -> CustomError {
        CustomError::GetTags(err)
    }
}
#[derive(Debug)]
pub enum GetTagsError {
    Io(IoError),
    Utf8(Utf8Error),
    Xml(XmlError),
}

impl From<IoError> for GetTagsError {
    fn from(error: IoError) -> Self {
        GetTagsError::Io(error)
    }
}

impl From<Utf8Error> for GetTagsError {
    fn from(error: Utf8Error) -> Self {
        GetTagsError::Utf8(error)
    }
}

impl From<XmlError> for GetTagsError {
    fn from(error: XmlError) -> Self {
        GetTagsError::Xml(error)
    }
}


fn get_map_vec(keys: HashSet<String>) -> HashMap<String, Vec<String>> {
    let map: HashMap<String, Vec<String>> =
        HashMap::from_iter(keys.into_iter().map(|key| (key.clone(), Vec::new())));
    map
}

fn create_arrow_schema_vec(entities: &HashMap<String, Vec<String>>) -> arrow::datatypes::Schema {
    let fields = entities
        .iter()
        .map(|(col_name, _)| {
            Field::new(col_name, DataType::Utf8, true) // Assuming all fields are nullable
        })
        .collect::<Vec<Field>>();
    Schema::new(fields)
}

pub fn parse_xml(file_path: &str, start: &str, output: &str) -> Result<RecordBatch, CustomError> {
    println!("Starting parsing xml ...");
    let st = Instant::now();

    // Intialize all variables
    let mut record_batch: Option<RecordBatch> = None;
    let mut reader = Reader::from_file(&file_path)?;
    reader.trim_text(true);
    let mut buf = Vec::new();
    let mut path: Vec<Cow<'static, str>> = Vec::new();
    let mut found_tags: HashSet<String> = HashSet::new();
    let output_file = File::create(output).expect("could not create file");
    let mut bufwriter = BufWriter::new(output_file);


    // First pass to detect the tags contained in the xml file
    let st_two = Instant::now();
    let unique_keys = get_tags(file_path, start)?;
    let first_pass_time = st_two.elapsed().as_millis();
    println!("get tags took {} ms", &first_pass_time);

    // Create the variables that will store the parsed data
    // entities is a hashmap that essentially resembles a dataframe
    // the keys are the name of the columns and the entries are
    // the columns
    let mut entities = get_map_vec(unique_keys.clone());
    let schema = create_arrow_schema_vec(&entities);
    let mut writer = arrow::ipc::writer::StreamWriter::try_new(&mut bufwriter, &schema).unwrap();

    // Typically the xml does not start with the tag we care about, 
    // so we ignore everything until the provided {start} value is found
    // and then flip this to "true" in order to start the actual parsing
    let mut start_tag_found = false;

    println!(
        "setup took {} ms",
        st.elapsed().as_millis() - first_pass_time
    );

    loop {
        match reader.read_event_into(&mut buf)? {
            Event::Start(e) => {
                let tag_name = std::str::from_utf8(e.name().as_ref())?.to_owned();
                path.push(Cow::Owned(tag_name.clone()));

                if tag_name == start {
                    start_tag_found = true;
                }
            }
            Event::Text(_) => {
                if !start_tag_found {
                    continue;
                }
                let child = path.pop().unwrap();
                let parent = path.last().unwrap();
                let col = format!("{}/{}", parent, child);
                let text = std::str::from_utf8(&buf)?.to_string();
                found_tags.insert(col.clone());
                let storage = entities.entry(col).or_default();
                storage.push(text);
            }
            Event::End(e) => {
                if e.name().as_ref() == start.as_bytes() {
                    let max_len = found_tags
                        .iter()
                        .map(|tag| entities.get(tag).unwrap().len())
                        .max()
                        .unwrap_or(0);

                    let not_found_tags = unique_keys.difference(&found_tags);
                    not_found_tags.into_iter().for_each(|x| {
                        let series = entities.entry(x.clone()).or_default();
                        let missing_count = max_len - series.len();
                        for _ in 0..missing_count {
                            series.push(MISSING.to_string());
                        }
                    });

                    found_tags.clear();
                    let rows = get_current_rows_vec(&entities);

                    if rows > 100 {
                        let mut new_vec: Vec<(String, Arc<dyn Array>)> = entities
                            .iter()
                            .map(|(name, array)| {
                                (
                                    name.clone(),
                                    Arc::new(StringArray::from(array.clone())) as Arc<dyn Array>,
                                )
                            })
                            .collect();

                        new_vec.sort_by_key(|(name, _)| name.clone());
                        // println!("sorting took {} ms", sort_time.elapsed().as_millis());

                        record_batch = Some(RecordBatch::try_from_iter(new_vec).unwrap());
                        writer
                            .write(record_batch.as_ref().unwrap())
                            .expect("Failed to write record batch");

                        entities = get_map_vec(unique_keys.clone());
                        found_tags.clear();
                    }
                }
            }
            Event::Eof => break,
            _ => (),
        }

        buf.clear();
    }
    let mut new_vec: Vec<(String, Arc<dyn Array>)> = entities
        .iter()
        .map(|(name, array)| {
            (
                name.clone(),
                Arc::new(StringArray::from(array.clone())) as Arc<dyn Array>,
            )
        })
        .collect();
    new_vec.sort_by_key(|(name, _)| name.clone());
    // println!("sorting took {} ms", sort_time.elapsed().as_millis());
    record_batch = Some(RecordBatch::try_from_iter(new_vec).unwrap());
    writer
        .write(record_batch.as_ref().unwrap())
        .expect("failed to write");

    // println!("parsing took {} ms", st.elapsed().as_millis());
    writer.finish().expect("failed to finish streamwriter");

    println!("time to parse: {:?}", st.elapsed());

    Ok(record_batch.unwrap())
}

fn get_current_rows_vec(entities: &HashMap<String, Vec<String>>) -> usize {
    entities
        .values()
        .next()
        .map(|series| series.len())
        .unwrap_or(0)
}

// need to export to library
fn get_tags(file_path: &str, tag: &str) -> Result<HashSet<String>, GetTagsError> {
    let mut reader = Reader::from_file(file_path)?;
    reader.trim_text(true);
    let mut tags = HashSet::new();
    let mut path: Vec<Cow<'static, str>> = Vec::new();
    let mut tmp_buf = Vec::new();
    let start = tag;
    let mut start_tag_found = false;

    loop {
        match reader.read_event_into(&mut tmp_buf)? {
            Event::Start(e) => {
                let tag_name = std::str::from_utf8(e.name().as_ref())?.to_owned();
                path.push(Cow::Owned(tag_name.clone()));
                if tag_name == start {
                    start_tag_found = true;
                }
            }
            Event::Text(_) => {
                if !start_tag_found {
                    continue;
                }
                let child = path.pop().unwrap();
                let parent = path.last().unwrap();
                // find a solution for this
                // formatting is slow
                let col = format!("{}/{}", parent, child);
                tags.insert(col.clone());
            }
            Event::Eof => break,
            _ => (),
        }
        tmp_buf.clear();
    }
    Ok(tags)
}
