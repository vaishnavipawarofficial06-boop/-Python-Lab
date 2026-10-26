# Professional Python Workflow

## Design
- Keep functions focused and avoid unnecessary global state.
- Separate user interface, business logic, and persistence.
- Prefer standard-library tools until a dependency solves a real need.
- Add type hints to public interfaces and document non-obvious behavior.

## Reliability
- Validate data at system boundaries.
- Raise specific exceptions; don't hide errors with broad `except Exception` blocks.
- Never log passwords, tokens, or personal secrets.
- Use context managers for files and resources.
- Use timeouts for network operations and bounded concurrency for async work.

## Testing
- Test expected behavior, boundaries, invalid input, and failure paths.
- Keep tests deterministic and independent.
- Mock external services rather than depending on live networks.
- Run `pytest` before committing.

## Code quality

```bash
ruff check .
ruff format --check .
pytest
```

## Git habits
- Use a feature branch for each substantial improvement.
- Make small commits with descriptive messages.
- Keep secrets in environment variables, never in source control.
- Review diffs before pushing.

## Release readiness
- Document supported Python versions and installation steps.
- Pin or constrain dependencies where appropriate.
- Add CI, a license, and changelog when the project is ready for public use.
- Measure performance before optimizing.
