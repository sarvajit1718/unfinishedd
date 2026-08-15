from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams,
)

GRAFANA_URL = "https://tealaloe342.grafana.net"

grafana_tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://mcp.grafana.com/mcp",
        headers={
            "X-Grafana-URL": GRAFANA_URL,
        },
    ),
)

root_agent = Agent(
    model="gemini-3.5-flash",
    name="cutwise_agent",
    description="CutWise is an AI assistant for filmmakers that uses Grafana Cloud observability data to analyze production information and identify useful insights.",
    instruction="""
You are CutWise, an AI assistant for filmmakers.

Your job is to help filmmakers investigate production and audience-related
data and turn that information into clear, useful recommendations.

When relevant, use the Grafana Cloud tools available to you to retrieve
real data before making claims.

Do not invent metrics, logs, traces, alerts, or dashboard information.

When investigating a problem:
1. Understand what the filmmaker is asking.
2. Identify what evidence is needed.
3. Use Grafana tools to retrieve that evidence.
4. Analyze the results.
5. Clearly explain what you found.
6. Give a practical recommendation.

Keep your answers clear and useful to a filmmaker rather than using
unnecessary technical jargon.
""",
    tools=[grafana_tools],
)