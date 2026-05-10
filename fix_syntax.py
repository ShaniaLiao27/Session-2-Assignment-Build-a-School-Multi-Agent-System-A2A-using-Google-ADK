import glob
import re

agent_files = glob.glob("*_agent/agent.py")

for file_path in agent_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it uses single quotes for instruction
    if "instruction='" in content:
        content = content.replace("instruction='", "instruction='''")
        # Fix the closing quote which is before tools= or sub_agents= or just )
        content = content.replace("',\n    tools=", "''',\n    tools=")
        content = content.replace("',\n    sub_agents=", "''',\n    sub_agents=")
        # If it doesn't have tools or sub_agents, it might end with '\n)
        content = content.replace("'\n)", "'''\n)")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file_path}")
    elif "instruction='''" in content:
        print(f"Already using triple quotes: {file_path}")
