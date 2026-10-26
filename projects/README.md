# Project Roadmap: Beginner → Pro

Build each project in stages. Don't jump to a framework before you can solve the core problem with the standard library.

## Level 1 — Beginner

### 1. Number Guessing Game
- Random number and bounded guesses
- Input validation and helpful feedback
- Difficulty modes and attempt counter
- Stretch: high-score file saved as JSON

### 2. CLI Calculator
- Add, subtract, multiply, divide
- Reject invalid numbers and division by zero
- Repeat until the user exits
- Stretch: unit tests and calculation history

### 3. Quiz Application
- Questions stored in JSON
- Score summary and retry option
- Stretch: categories, shuffled questions, and leaderboard

**Done when:** normal inputs, invalid inputs, and edge cases work.

## Level 2 — Intermediate

### 4. Expense Tracker
- Add, edit, delete, and list transactions
- Save/load CSV or JSON data
- Filter by date/category and summarize spending
- Stretch: SQLite, export, and tests

### 5. File Organizer
- Group files by extension with a dry-run mode
- Avoid overwriting existing files
- Log every planned or completed move
- Stretch: recursive mode, undo manifest, and duplicate hashing

### 6. Log Analyzer
- Parse timestamps, levels, and messages
- Count errors by level and time window
- Handle malformed lines without crashing
- Stretch: generate a JSON report and charts

**Done when:** persistence is reliable and errors are handled explicitly.

## Level 3 — Advanced

### 7. Async URL Health Checker
- Accept a list of URLs
- Use asynchronous HTTP requests and bounded concurrency
- Add timeout handling and a concise status report
- Stretch: retries with backoff, structured logs, and CSV export

### 8. FastAPI Task Manager
- CRUD endpoints for tasks
- Request validation and consistent error responses
- SQLite persistence and pagination/filtering
- Tests for success, not-found, and invalid requests
- Stretch: authentication, migrations, rate limiting, Docker

### 9. Duplicate File Detector
- Walk directories safely
- First group candidates by file size
- Hash files in chunks, not all at once
- Support dry-run reports; never delete files by default
- Stretch: parallel hashing, JSON output, and benchmarks

## Level 4 — Pro Capstone

### 10. Production-style Data Processing API
- FastAPI + SQLite/PostgreSQL
- Clear service/repository separation
- Pydantic validation and typed functions
- Structured logging and environment-based configuration
- Unit and API integration tests
- Ruff linting/formatting and CI on multiple Python versions
- Dockerfile, health endpoint, README, and deployment notes
- Security review: secrets, input limits, safe errors, least privilege

## Standard project checklist

- [ ] Clear README with setup and examples
- [ ] Small functions with meaningful names
- [ ] Type hints on public functions
- [ ] Input validation and useful exceptions
- [ ] Tests for normal, edge, and failure cases
- [ ] No secrets committed to Git
- [ ] Lint and formatting checks pass
- [ ] CI runs automatically on pushes and pull requests
- [ ] Document limitations and future improvements
