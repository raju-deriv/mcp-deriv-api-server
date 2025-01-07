import json
import os
import sys
from mcp.server.fastmcp import FastMCP
from deriv_api import DerivAPI
from dotenv import load_dotenv

# Initialize FastMCP server
mcp = FastMCP("deriv-api-mcp")


@mcp.tool()
async def get_active_symbols() -> dict:
    # Load the .env file
    load_dotenv()   
    api_token = os.getenv("DERIV_API_TOKEN")
    if not api_token:
        raise ValueError("DERIV_API_TOKEN environment variable is required")
    
    app_id = os.getenv("DERIV_APP_ID", "1089")  # Default to app_id 16929
    api = DerivAPI(app_id=app_id)

    response = await api.ping({'ping': 1})
    if response['ping']:
        print(response['ping'])

    active_symbols = await api.active_symbols({"active_symbols": "brief", "product_type": "basic"})
    return active_symbols


if __name__ == "__main__":
    # Initialize and run the server
    print("Deriv MCP server running on stdio", file=sys.stderr)
    mcp.run(transport='stdio')
    



