import sys
import os

from School_Coordinator_agent.agent import root_agent

print(f"Root Agent Name: {root_agent.name}")
print(f"Number of Sub-Agents: {len(root_agent.sub_agents)}")
for sub_agent in root_agent.sub_agents:
    print(f" - {sub_agent.name}: Loaded with {len(sub_agent.tools)} tools.")
print("\nSuccess! All agents are successfully linked.")
