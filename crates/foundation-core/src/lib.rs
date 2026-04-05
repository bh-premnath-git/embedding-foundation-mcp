use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ExecutionMetadata {
    pub engine: String,
    pub deterministic: bool,
}

impl Default for ExecutionMetadata {
    fn default() -> Self {
        Self {
            engine: "foundation-core".to_string(),
            deterministic: true,
        }
    }
}
