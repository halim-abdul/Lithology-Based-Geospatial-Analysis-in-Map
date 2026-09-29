# Contributing

Contributions should keep the project reproducible, source-aware, and free of personal assessment metadata.

## Development
1. Create a focused branch.
2. Install with `pip install -e ".[geo,dev]"`.
3. Add tests for reusable transformations.
4. Run `ruff check src scripts tests` and `pytest -q`.
5. Keep generated outputs deterministic and document data provenance.

Do not commit student names, IDs, course titles, deadlines, grading instructions, or other assessment-specific metadata.
