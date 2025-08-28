from google.adk.agents import Agent
from google.adk.tools import built_in_code_execution
from utils.gcs_utils import fetch_instructions

def get_live_instructions(ctx) -> str:
    """This function is passed to the Agent and called on every run."""
    return fetch_instructions("calc_agent")

# Create the agent, passing the function object to the 'instruction' parameter.
# The 'tools' parameter is preserved as it's specific to this agent.
root_agent = Agent(
    name="calc_agent",
    model="gemini-2.5-flash",
    description="A calculator agent",
    instruction=get_live_instructions,
    tools=[built_in_code_execution]
)