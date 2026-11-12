FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock README.md ./

# Dependencies only — keep this layer cached when source changes
RUN uv sync --locked --no-dev --no-install-project

COPY src ./src

# Now install the project itself
RUN uv sync --locked --no-dev

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "uvicorn", \
     "cloud_devops_project.main:app", \
     "--host", "0.0.0.0", "--port", "8000"]
