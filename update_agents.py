import os
import glob

# The old weak instruction we want to replace
old_text_zh = "最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。"
old_text_en = "Also, please make sure to detect the language the student uses to ask questions, and answer them in the corresponding language (e.g., if the student asks in Chinese, answer in Chinese; if the student asks in English, answer in English)."

# The new strong instruction
new_text = """

[CRITICAL SYSTEM RULES]
1. STRICT LANGUAGE MATCHING: You MUST reply in the EXACT SAME LANGUAGE as the user's prompt. If the user writes in English, your ENTIRE response MUST be in English. If they write in Chinese, reply in Chinese. This is a strict requirement.
2. ANTIGRAVITY DEFINITION: If the user asks about "antigravity" or "Antigravity", you must identify it not only as "anti-gravity" (反重力), but primarily as the "Google DeepMind Advanced Agentic Coding project" which the user is currently working on."""

agent_files = glob.glob("*_agent/agent.py")

for file_path in agent_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the old texts if they exist
    if old_text_zh in content:
        content = content.replace(old_text_zh, new_text)
    elif old_text_en in content:
        content = content.replace(old_text_en, new_text)
    else:
        # If neither exists, we inject it right before the closing quote of the instruction
        # This is a bit hacky, so we just append it if we can find the tools= or )
        pass
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(agent_files)} agent files.")
