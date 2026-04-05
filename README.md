
# Embedding-First Foundation MCP

**A hybrid Rust+Python engine for learning, computing, verifying, visualizing, and reasoning about AI math and algorithms—centered on embeddings, built for real-world AI engineering.**

---

## Why This Project?

Modern AI engineering requires more than just vector math or generic tutoring. This MCP is:
- **Embedding-first**: Every concept is taught and computed through the lens of embeddings.
- **Multi-level**: Supports intuition, worked examples, formal math, and real-world AI applications.
- **Hybrid compute**: Rust for speed, Python for pedagogy and flexibility.
- **Structured**: Every tool and response is schema-driven and deterministic.

---

## Badges

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Rust](https://img.shields.io/badge/rust-1.70%2B-orange)

---

## Quickstart

> **Note:** Full setup instructions coming soon. For now, ensure you have Python 3.10+ and Rust 1.70+ installed.

```sh
# Clone the repo
git clone https://github.com/bh-premnath-git/embedding-foundation-mcp
cd embedding-foundation-mcp

# (Optional) Set up Python venv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install Python dependencies
pip install -r requirements.txt

# Build Rust components
cd crates/foundation-python
maturin develop  # or use maturin build
```

---

## Example API Usage

**Request:** Teach cosine similarity at L2 and compute for two vectors

```json
{
	"mode": "learn",
	"level": "L2",
	"topic": "cosine_similarity",
	"input": {"a": [1, 2], "b": [3, 4]},
	"options": {}
}
```

**Response:**

```json
{
	"concept": "cosine_similarity",
	"level": "L2",
	"core_explanation": "Cosine similarity measures the angle between two vectors...",
	"embedding_explanation": "Used to compare semantic similarity between embeddings...",
	"real_world_use_cases": ["search ranking", "recommendation"],
	"worked_example": {"a": [1,2], "b": [3,4], "cosine_similarity": 0.9839},
	"common_mistakes": ["Not normalizing vectors", "Confusing with dot product"],
	"next_topics": ["dot_product", "vector_norm"]
}
```

---

## Multi-Level Topic Support

Every concept/tool supports four levels:

| Level | Description           | Example Output Type         |
|-------|-----------------------|-----------------------------|
| L1    | Intuition             | Analogy, visual, plain text |
| L2    | Worked Example        | Step-by-step calculation    |
| L3    | Formal/Math Depth     | Equations, proofs           |
| L4    | AI-System Application | Real-world code, system use |

The same concept (e.g., cosine similarity, gradient descent, Bayes theorem, DAG scheduling, HNSW) supports both exact execution and adaptive teaching.

---

## MCP Model

MCP is easiest to reason about as three roles:

- **Host**: The application that the user is working in. Examples include an IDE, chat surface, or agent runtime.
- **Client**: The MCP-aware connector inside the host that discovers tools/resources and sends requests.
- **Server**: The system that implements MCP capabilities and returns structured results.

In this project:

- the **host** is whichever MCP-compatible environment connects to this project
- the **client** is the MCP integration used by that host
- this repository provides the **server**, including the teaching, compute, verification, visualization, and reasoning capabilities

That separation matters because this project should stay host-agnostic: stable MCP contracts on the server side, no assumptions about any one UI or client runtime.

---

## Architecture Overview

```
MCP Client / Host
		↓
MCP Server Interface
		↓
FastAPI Gateway
		├── Auth / quotas / policy
		├── Pydantic validation
		├── Task routing
		├── Learning/teaching formatter
		├── Visualization service
		└── Observability
		↓
Execution Router
		├── Rust in-process engine (PyO3) for low-latency kernels
		├── Rust worker service for large/parallel jobs
		└── Python symbolic/teaching layer
		↓
Result Normalizer
		↓
MCP tool/resource response
```


---

### Execution Paths

- **Sync Fast Path**: Tiny, deterministic workloads (e.g., cosine similarity, top-k)
- **Async Compute Path**: Medium workloads (e.g., matrix decomposition, batch gradients)
- **Job Path**: Large, long-running jobs (e.g., ANN index build, huge DAGs)


---

## Tech Stack

- **Python**: FastAPI, Pydantic, SymPy, Matplotlib/Plotly, OpenTelemetry
- **Rust**: Tokio, PyO3 + maturin, rayon, ndarray/nalgebra, petgraph, serde, tracing


---

## Tool Model

All tools share a contract:

```json
{
	"mode": "learn | compute | verify | visualize | reason",
	"level": "L1 | L2 | L3 | L4",
	"topic": "cosine_similarity",
	"input": {},
	"options": {}
}
```

Tools are namespaced and versioned (e.g., la.vector_ops, calc.gradient, retrieval.ann_search, learn.concept).


---

### Core MCP Tools

- **Math**: la.vector_ops, la.matrix_ops, la.cosine_similarity, la.eigendecompose, la.svd
- **Calculus**: calc.differentiate, calc.partial_derivative, calc.gradient, calc.gradient_descent_step
- **Probability & Statistics**: stats.distribution_summary, stats.bayes_update, stats.confidence_interval, stats.hypothesis_test, stats.sampling
- **Algorithms**: algo.complexity_analyze, algo.top_k, algo.graph_traverse, algo.dag_schedule, algo.dp_trace
- **Retrieval/Vector Systems**: retrieval.build_index, retrieval.ann_search, retrieval.similarity_rank, retrieval.embedding_analyze
- **Learning/Meta**: learn.concept, learn.problem_set, learn.verify_solution, learn.map_to_ai_system, learn.study_plan


---

## Reliability Rules

1. **Strict schemas everywhere** (dimensions, types, formulas, bounded sizes)
2. **Deterministic compute core** (same input → same output, fixed seeds)
3. **Separate symbolic from numeric** (proof vs. compute)
4. **Resource guards** (reject/queue giant jobs)
5. **Graceful shutdown/cancellation** (Tokio, FastAPI best practices)
6. **Host-agnostic**: stable tool names, UI-optional, structured JSON-first


---

## Internal Content Model

For each concept, store:
- definition
- intuition
- math_form
- worked_examples
- embedding_relevance
- real_use_case_families
- visualization_templates
- common_errors
- prerequisites
- next_topics


---

## Folder Structure

```
foundation-mcp/
	apps/
		api/                    # FastAPI MCP gateway
		worker-rust/            # Rust service for heavy jobs
	crates/
		foundation-core/        # pure compute kernels
		foundation-graph/       # graph + DAG logic
		foundation-linalg/      # matrix/vector ops
		foundation-retrieval/   # ANN + ranking primitives
		foundation-python/      # PyO3 bindings
	python/
		app/
			routes/
			mcp/
			schemas/
			services/
			learning/
			visualization/
			observability/
	tests/
		contract/
		load/
		correctness/
		evals/
```


---

## First Curriculum Sequence

1. **Vector intuition:** vectors, dimensions, norms, dot product, cosine similarity
2. **Embedding foundations:** what embeddings are, dense vs sparse, similarity metrics, nearest neighbors, ranking
3. **Matrix and reduction:** matrix multiplication, eigen intuition, SVD, PCA
4. **Retrieval systems:** top-k, ANN, HNSW, recall vs latency, reranking
5. **Learning and optimization:** derivatives, gradients, gradient descent, loss functions, contrastive learning
6. **Evaluation and uncertainty:** score distributions, thresholds, precision/recall, statistical thinking, experiment design


---

## Request Flow Example

User asks: “Teach cosine similarity at L2, compute for these vectors, explain embedding relevance.”

1. FastAPI validates payload
2. Calls Rust PyO3 kernel for computation
3. Python learning layer formats L2 explanation
4. System-mapping layer explains embedding usage
5. Visualization renders vector angle chart (optional)
6. MCP returns structured response


---

## Stack

- FastAPI as orchestration and teaching layer
- Rust as deterministic compute engine
- PyO3 for low-latency kernels
- Rust worker service for heavy parallel jobs
- Python visualization and pedagogy on top


---

## Design

- Host-agnostic
- Typed
- Deterministic
- Observable

---

## Contributing

Contributions are welcome! Please open issues or pull requests for features, bugfixes, or documentation improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (coming soon).

---

## Roadmap

- [ ] Job queue and streaming progress
- [ ] Automated evaluation harness
- [ ] More visualization templates
- [ ] Expanded curriculum modules
- [ ] REST/gRPC API documentation

---

## References & Links

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyO3](https://pyo3.rs/)
- [Tokio](https://tokio.rs/)
- [Maturin](https://github.com/PyO3/maturin)
- [NumPy](https://numpy.org/)
- [nalgebra](https://nalgebra.org/)
- [petgraph](https://github.com/petgraph/petgraph)
- [OpenTelemetry](https://opentelemetry.io/)

---