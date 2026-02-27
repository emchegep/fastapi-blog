FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set project working directory
WORKDIR /app

# Copy deps and packages files
COPY pyproject.toml uv.lock /app/

# Install Packages and deps.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY . .

# Create a non-root user.
RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["/app/.venv/bin/uvicorn"]
# Run the application.
CMD ["main:app", "--port", "8000", "--host","0.0.0.0"]