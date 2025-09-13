# Agent Development Guidelines for Synapse

This document provides guidelines for AI agents working on the Synapse codebase.

## Project Structure

The project is a FastAPI application structured as follows:

-   `requirements.txt`: Lists the Python dependencies for the project.
-   `README.md`: Contains setup, installation, and usage instructions.
-   `synapse/`: This is the main Python package for the application.
    -   `__init__.py`: Makes the `synapse` directory a Python package.
    -   `main.py`: The main entry point of the FastAPI application. It defines the API endpoints.
    -   `schemas.py`: Contains all Pydantic models used for data validation (request and response bodies). This ensures a strict data contract for the API.
    -   `security.py`: Contains authentication and authorization logic, such as API key verification.

## Development Principles

1.  **Separate Concerns:**
    -   API endpoint definitions belong in `main.py`.
    -   Data structures (Pydantic models) belong in `schemas.py`.
    -   Authentication logic belongs in `security.py`.
    -   Complex business logic for handling specific actions should be moved to its own module (e.g., `synapse/actions.py`) in the future to keep `main.py` clean.

2.  **Use Pydantic for Validation:** All data entering or leaving the API must be validated by a Pydantic model defined in `schemas.py`.

3.  **Secure Endpoints:** Any endpoint that performs actions or accesses sensitive data must be protected. Use the dependencies from `security.py`.

4.  **Keep Mocking Simple:** The current business logic is mocked directly in `main.py`. As the project grows, this logic should be abstracted away, but for now, it's acceptable to keep it there for simplicity.

5.  **Update Documentation:** If you add a new dependency, add it to `requirements.txt`. If you add a new feature or change how the API is run/tested, update the `README.md`.
