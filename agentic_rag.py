from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb
from agno.embedder.google import GeminiEmbedder

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    name="rag",
    model=Gemini(id="gemini-2.0-flash", api_key=google_api_key),
    description="You are a Thai Cuisine Expert.",
    instructions=[
        'Search your knowledge base for the answer.',
        'If you cannot find the answer, say "I do not know."',
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=['https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf'],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            embedder=GeminiEmbedder(id="text-embedding-004", api_key=google_api_key),
        )
    ),
    # tools=[DuckDuckGoTools()],
    show_tool_calls=True
)

agent.knowledge.load(recreate=False)

agent.print_response("is there a recipe for a thai dish with onions?", stream=True)
# print(response.content)