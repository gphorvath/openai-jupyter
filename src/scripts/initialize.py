"""Initialize the OpenAI vector store and assistant. This only needs to be done once."""

import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OPENAI_API_URL"), api_key=os.getenv("OPENAI_API_KEY")
)

# Upload a file and create a vector store
create_file_response = client.files.create(
    file=Path("data/test_file.md"),
    purpose="assistants",
)

file_id = create_file_response.model_dump().get("id")

create_vector_store_response = client.beta.vector_stores.create(
    file_ids=[file_id], name="jack_and_diane"
)

vector_store_id = create_vector_store_response.model_dump().get("id")

create_assistant_response = client.beta.assistants.create(
    name="jack_and_diane",
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}],
    tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
)

assistant_id = create_assistant_response.model_dump().get("id")

print(
    f"Assistant ID: {assistant_id} \nVector Store ID: {vector_store_id} \nFile ID: {file_id}"
)
