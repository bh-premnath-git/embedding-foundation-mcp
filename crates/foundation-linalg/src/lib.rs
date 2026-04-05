use ndarray::Array1;

pub fn cosine_similarity(left: &[f64], right: &[f64]) -> Option<f64> {
    if left.len() != right.len() || left.is_empty() {
        return None;
    }

    let left = Array1::from_vec(left.to_vec());
    let right = Array1::from_vec(right.to_vec());

    let dot = left.dot(&right);
    let left_norm = left.dot(&left).sqrt();
    let right_norm = right.dot(&right).sqrt();

    if left_norm == 0.0 || right_norm == 0.0 {
        return None;
    }

    Some(dot / (left_norm * right_norm))
}
