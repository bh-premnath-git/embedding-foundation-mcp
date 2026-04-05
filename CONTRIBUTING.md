# Contributing

## Scope

This repository is an embedding-first MCP server scaffold. Contributions should preserve these constraints:

- Rust owns deterministic compute kernels and heavy-worker execution.
- Python owns orchestration, teaching, symbolic handling, and visualization formatting.
- MCP-facing contracts stay stable and typed.

## Workflow

1. Open an issue for major architecture changes.
2. Keep changes scoped to one layer when possible.
3. Add tests under `tests/` for any new API contract or compute behavior.
4. Update `README.md` when public interfaces or structure change.

## Development

- Python: `pip install -r requirements.txt`
- Rust: `cargo check`
- Tests: `pytest`
