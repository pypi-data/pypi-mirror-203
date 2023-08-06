from setuptools import setup
from setuptools_rust import Binding, RustExtension

rust_extension = RustExtension(
    "jxml",
    binding=Binding.PyO3,
    path="Cargo.toml",
    debug=False,
)

setup(
    name="jxml",
    version="0.1.1",
    rust_extensions=[rust_extension],
    setup_requires=["setuptools-rust"],
    zip_safe=False,
)
