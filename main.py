from langgraph.graph import StateGraph, MessagesState,START,END
from langchain.chat_models import init_chat_model
from langchain.tools import Tool
from langchain_tavily import TavilySearch
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langgraph.prebuilt import ToolNode,create_react_agent
from langchain_google_vertexai import ChatVertexAI
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langchain_community.utilities.twilio import TwilioAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.tools import YouTubeSearchTool
from langchain_community.utilities import WikipediaAPIWrapper
from typing import Optional
from dotenv import load_dotenv
load_dotenv()
import os



llm = ChatVertexAI(model="gemini-2.0-flash-lite-001")


#Tavily search tool
tavily_search_tool = TavilySearch(
    max_results=2,
    topic="finance",
    include_images=True,
    
)



#Twilio Api tool
twilio = TwilioAPIWrapper(
    from_number=os.getenv("TWILIO_PHONE_NUMBER")
)

twilio_tool = Tool(
    name="twilio_sms",
    func=lambda to, message: twilio.run(message, to),
    description="Send an SMS via Twilio. Input must include `to` (phone number) and `message` (text)."
)



#Youtube search tool
yt_search = YouTubeSearchTool()


youtube_tool = Tool(
    name="YouTubeSearch",
    func=yt_search.run,
    description="Search YouTube videos based on a query. Input should be a search string."
)


#Wikipedia tool
wiki_wrapper = WikipediaAPIWrapper()


wikipedia_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)


wiki_tool = Tool(
    name="WikipediaSearch",
    func=wikipedia_tool.run,
    description="Useful for answering questions about people, events, or concepts using Wikipedia"
)

#Tool Node
tools = ([tavily_search_tool,twilio_tool,youtube_tool,wiki_tool])


#memory
memory = InMemorySaver()


#Re-Act agent
agent_node = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    prompt="Act as a helpful assistant. Pick the right tool according to the user query."
)


#Graph
graph = StateGraph(MessagesState)

#Nodes
graph.add_node("agent", agent_node)


# Edges
graph.add_edge(START, "agent")
graph.add_edge("agent", END)


app = graph.compile()