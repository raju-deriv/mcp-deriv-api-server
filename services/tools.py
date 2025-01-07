# run it like PYTHONPATH=. python3 examples/simple_bot1.py
import sys
import asyncio
import os
from deriv_api import DerivAPI
from deriv_api import APIError
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('DERIV_API_TOKEN', '')
if not api_token:
    raise ValueError("DERIV_API_TOKEN environment variable is required")

app_id = os.getenv("DERIV_APP_ID", "1089")  # Default to app_id 16929


async def get_symbols():
    api = DerivAPI(app_id=app_id)

    response = await api.ping({'ping': 1})
    if response['ping']:
        print(response['ping'])

    active_symbols = await api.active_symbols({"active_symbols": "brief", "product_type": "basic"})
    return active_symbols

async def get_balance() -> dict:
    api = DerivAPI(app_id=app_id)
    try:
        # Authorize
        authorize = await api.authorize(api_token)
        print(authorize)

        # Get Balance
        response = await api.balance()
        return response['balance']
    finally:
        await api.clear()
