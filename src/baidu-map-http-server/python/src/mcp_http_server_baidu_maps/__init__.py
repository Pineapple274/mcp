# __init__.py
from .map import mcp

def main():
    """MCP Baidu Maps Server - HTTP call Baidu Map API for MCP"""
    mcp.run(transport="sse")

if __name__ == "__main__":
    main()