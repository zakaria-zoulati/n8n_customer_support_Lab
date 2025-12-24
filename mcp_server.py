from fastapi import FastAPI
from mcp.server.fastapi import MCPServer

app = FastAPI()
mcp = MCPServer(app)

@mcp.tool()
def get_order_status(order_id: str):
    return {
        "order_id": order_id,
        "status": "Shipped",
        "delivery": "2 days"
    }

@mcp.tool()
def process_refund(order_id: str):
    return {
        "order_id": order_id,
        "refund_status": "Approved",
        "amount": "$49.99"
    }
