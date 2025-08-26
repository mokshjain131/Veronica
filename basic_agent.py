from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
import os
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    name="basic",
    model=Gemini(id="gemini-2.0-flash", api_key=google_api_key),
    description="agent which answers a question.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True
    # instructions=[
    #     'Search your knowledge base for the answer.',
    #     'If you cannot find the answer, say "I do not know."',
    # ],
)

agent.print_response("what is mpstme? what computer engineering programs do they offer?", stream=True)

# response = agent.run("What is the capital of France?")
# print(response.content)