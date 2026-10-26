# Setup Guide

## Requirements

- Python 3.11 or newer
- Git
- A code editor (VS Code or another editor)
- Basic command-line access

Check Python:

```bash
python --version
```

On some systems, use `python3` instead of `python`.

## Create an isolated environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the lab and development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run exercises and tests

```bash
python exercises/01_beginner.py
pytest
ruff check .
ruff format --check .
```

## Practice loop

1. Read one topic.
2. Complete the TODOs.
3. Try at least one edge case.
4. Run the tests.
5. Refactor unclear code.
6. Commit your work.

## Common issues

- **Command not found:** check that Python is installed and available on PATH.
- **Wrong Python environment:** activate `.venv` before installing dependencies.
- **PowerShell activation blocked:** use a terminal where activation is permitted, or run the environment's Python directly (for example, `.venv\Scripts\python.exe -m pytest`).
- **Import errors:** run commands from the repository root and install with `python -m pip install -e ".[dev]"`.