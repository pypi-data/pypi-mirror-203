use arrow::ipc::writer::StreamWriter;
use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::wrap_pyfunction;

mod parser;
use crate::parser::parser::parse_xml;

#[pyfunction]
fn parse_xml_py(file_path: &str, tag: &str, output: &str) -> PyResult<PyObject> {
    Python::with_gil(|py| {
        let record_batch = parse_xml(file_path, tag, output).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyException, _>(format!(
                "Error occurred while parsing XML: {}",
                e
            ))
        })?;

        let mut buf: Vec<u8> = Vec::new();
        {
            let mut writer = StreamWriter::try_new(&mut buf, &record_batch.schema()).unwrap();
            writer
                .write(&record_batch)
                .expect("Failed to write record batch");
            writer.finish().expect("failed to finish streamwriter");
        }

        let py_bytes = PyBytes::new(py, &buf);

        Ok(py_bytes.into())
    })
}

#[pymodule]
fn jxml(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_xml_py, m)?)?;
    Ok(())
}
