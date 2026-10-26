# Python Lab — Beginner to Pro 🚀

A hands-on Python learning lab that takes you from your first `print()` statement to production-style projects. Learn by reading a concept, solving exercises, building projects, and testing your code.

## Learning path

| Level | Topics | Practice |
|---|---|---|
| 00 — Setup | Python 3.11+, terminal, virtual environments, Git | [Setup guide](docs/SETUP.md) |
| 01 — Beginner | Variables, types, input/output, conditions, loops | [Beginner exercises](exercises/01_beginner.py) |
| 02 — Core Python | Strings, lists, tuples, sets, dictionaries, functions | [Core exercises](exercises/02_core_python.py) |
| 03 — Intermediate | Files, JSON, exceptions, modules, OOP, type hints | [Intermediate exercises](exercises/03_intermediate.py) |
| 04 — Advanced | Iterators, generators, decorators, context managers, async | [Advanced exercises](exercises/04_advanced.py) |
| 05 — Projects | CLI apps, APIs, databases, automation, data processing | [Project roadmap](projects/README.md) |
| 06 — Professional | Testing, linting, packaging, CI, documentation, security | [Professional checklist](docs/PRO_WORKFLOW.md) |

## Quick start

```bash
python --version
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

Run a practice file:

```bash
python exercises/01_beginner.py
```

Each exercise has a TODO. Try it yourself first, then compare with the solution hints in the comments. Keep your own solutions in a separate branch or file.

## Projects by difficulty

- **Beginner:** Number guessing game, calculator, quiz app, unit converter
- **Intermediate:** Expense tracker with CSV/JSON, contact book, file organizer, log analyzer
- **Advanced:** FastAPI task API, async URL checker, duplicate-file detector, SQLite analytics pipeline
- **Pro:** Tested package, Dockerized API, CI/CD, structured logging, configuration via environment variables

Project requirements and acceptance criteria: [projects/README.md](projects/README.md).

## Repository structure

```text
Python-Lab/
├── docs/                 # Setup and professional workflow
├── exercises/            # Guided practice from beginner to advanced
├── projects/             # Project briefs and milestones
├── src/python_lab/       # Reusable, tested Python code
├── tests/                # Automated tests
├── .github/workflows/    # Continuous integration
├── pyproject.toml        # Project metadata and developer tools
└── README.md
```

## Quality checks

```bash
pytest
ruff check .
ruff format --check .
```

## How to learn effectively

1. Spend 20–30 minutes on a concept.
2. Solve exercises without copying.
3. Add input validation and useful error messages.
4. Write tests for normal, edge, and invalid inputs.
5. Explain your solution in your own words.
6. Commit small, meaningful changes.

**Goal:** build a portfolio of working, tested projects—not just collect code snippets.

## License

This repository is for learning and practice. Add a license file if you plan to distribute or reuse it publicly.