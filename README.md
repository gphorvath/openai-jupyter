# OpenAI API in Jupyter

This is a Jupyter Notebook project that demonstrates how to use the various OpenAI API endpoints.

## Requirements

- OpenAI API access (costs $$) - get your [API Key here](https://platform.openai.com/api-keys)
  - Expert: There are free tools that shadow the OpenAI API, but API conformity isn't guaranteed.

## OpenAI Playground

If you are using OpenAI as your target, you can use the [Open Playground](https://platform.openai.com/playground/assistants) to inspect your assistants.

You can also use the [OpenAI Playground](https://platform.openai.com/storage) to inspect your files in storage and vector stores.

## Getting started

``` bash
python -m venv .venv
source .venv/bin/activate
make install # installs dependencies from pyproject.toml
```

### Running this project

Run `src/scripts/initialize.py` to setup your first assistant, file, and vector store.

Checkout the Jupyter Notebook at `src/main.py` to use the file_search capability of the OpenAI API.
