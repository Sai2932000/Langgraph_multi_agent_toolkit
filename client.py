from langgraph_sdk import get_sync_client, get_client

from langgraph_sdk.client import SyncLangGraphClient
from langchain_core.messages import HumanMessage,SystemMessage




# Point SDK to your running graph server
client = get_sync_client(url="http://127.0.0.1:3000")

thread = client.threads.create()

graph = client.assistants.get_graph("b54c0545-9d79-5688-bc81-269c46247a52")



for chunk in client.runs.stream(
    thread_id=thread["thread_id"],
    assistant_id="b54c0545-9d79-5688-bc81-269c46247a52",
    input={
        "messages": [
            {"role": "user", "content": "Sachin Tendulkar"}
        ]
    },
):
    print(chunk)
