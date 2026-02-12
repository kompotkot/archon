# Requirements

**Programming language:** Python

**Packaging**: `pyproject.toml` (uv); runtime deps must be declared under `[project].dependencies`

**Package layout**: `src/archon`

**Dependencies:**:

- `langchain`
- `langchain-ollama`
- `langchain-openai`
- `langgraph`

**Development dependencies:**

- `black` - formatting
- `isort` - imports formatting
- `mypy` - lint

- **CLI**: `archon` entrypoint (`archon.__main__:main`) using `argparse`.

## LLM orchestration

**Orchestration**: LangGraph

**LLM integration**: LangChain

**Providers**: Must support OpenAI-compatible chat models and Ollama-backed local models.

## C4 Model

C4 is the sole framework used for visualizing the project architecture.

Levels in scope:

- `docs/diagrams/context/` - Level 1 System Context - shows the system in its environment, highlighting users and external dependencies;
- `docs/diagrams/containers/` - Level 2 Containers - identify the high-level technology building blocks (runnable and deployable units) of the system such as applications, databases;
- `docs/diagrams/components/` - Level 3 Components - Describes how a container is internally structured into modules or controllers and how those collaborate.

## User Stories

Ignore `_template.md`. Use only actual stories (`USxxx.md`) located in:

- `docs/user-stories/` — text-based stories;
- `docs/diagrams/user-stories/` — diagram-based stories.
