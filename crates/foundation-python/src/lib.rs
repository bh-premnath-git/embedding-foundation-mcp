use foundation_linalg::cosine_similarity;
use pyo3::prelude::*;

#[pyfunction]
fn cosine_similarity_py(left: Vec<f64>, right: Vec<f64>) -> PyResult<f64> {
    cosine_similarity(&left, &right)
        .ok_or_else(|| pyo3::exceptions::PyValueError::new_err("invalid vectors for cosine similarity"))
}

#[pymodule]
fn foundation_python(_py: Python<'_>, module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(cosine_similarity_py, module)?)?;
    Ok(())
}
