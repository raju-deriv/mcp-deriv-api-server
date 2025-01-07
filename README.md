# Deriv API Server

A Model Context Protocol (MCP) server and OpenAI function calling service for interacting with the Deriv API.

## Features

- Active symbols list
- Get Account Balance

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Environment Setup

Create a `.env` file in your project root:

```env
DERIV_API_TOKEN=your_api_key_here
```

## Usage with Claude Desktop

Claude Desktop provides full support for MCP features. To use this server:

1. Install [Claude Desktop](https://claude.ai/download)

2. Add to your Claude Desktop configuration:
   - On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - On cline VSCode: `/Users/raju/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
   - On Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
        "deriv-api-mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/raju/Sites/deriv/mcp-deriv-api-server",
                "run",
                "server.py"
            ]
        }
  }
}
```

3. Restart Claude Desktop

The server provides the following tools:
- `active-symbols`: Get a list of active symbols


## Usage with OpenAI Function Calling


## Rate Limits

Please refer to the [Deriv API documentation](https://api.deriv.com) for current rate limits and usage guidelines.

## License

MIT 