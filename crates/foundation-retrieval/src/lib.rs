use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RankedNeighbor {
    pub id: String,
    pub score: f64,
}
