import sys
import os
import asyncio

from School_Coordinator_agent.agent import root_agent

async def main():
    print("Sending query to School Coordinator...")
    try:
        response = ""
        async for chunk in root_agent.run_async("what's antigravity"):
            response += chunk
        print("Final Response:")
        print(response)
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
