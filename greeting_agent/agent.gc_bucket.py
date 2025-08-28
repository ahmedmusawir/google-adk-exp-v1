from google.adk.agents import Agent
from utils.gcs_utils import fetch_instructions


root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash",
    description="Greeting agent",
    instruction=fetch_instructions("greeting_agent"),

)