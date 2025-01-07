import json
import os
import sys
from mcp.server.fastmcp import FastMCP
from deriv_api import DerivAPI

from services.tools import get_symbols, get_balance
# Initialize FastMCP server
mcp = FastMCP("deriv-api-mcp")
# Load the .env file

@mcp.tool()
async def get_active_symbols() -> dict:
    active_symbols = await get_symbols()
    return active_symbols

@mcp.tool()
async def get_account_balance() -> dict:
    response = await get_balance()
    return response


if __name__ == "__main__":
    # Initialize and run the server
    print("Deriv MCP server running on stdio", file=sys.stderr)
    mcp.run(transport='stdio')
