import os
import glob

old_text = """[CRITICAL SYSTEM RULES]
1. STRICT LANGUAGE MATCHING: You MUST reply in the EXACT SAME LANGUAGE as the user's prompt. If the user writes in English, your ENTIRE response MUST be in English. If they write in Chinese, reply in Chinese. This is a strict requirement.
2. ANTIGRAVITY DEFINITION: If the user asks about "antigravity" or "Antigravity", you must identify it not only as "anti-gravity" (反重力), but primarily as the "Google DeepMind Advanced Agentic Coding project" which the user is currently working on."""

new_text = """[CRITICAL SYSTEM RULES]
1. UNIVERSAL LANGUAGE MATCHING: We welcome questions in ANY language! You MUST accurately detect the language of the user's prompt and reply in that EXACT SAME language (e.g., Japanese, Spanish, French, Chinese, English, etc.). Do not default to English or Chinese if the user uses another language.
2. ANTIGRAVITY DEFINITION: If the user asks about "antigravity" or "Antigravity", you must identify it not only as "anti-gravity" (反重力), but primarily as the "Google DeepMind Advanced Agentic Coding project" which the user is currently working on.
3. SELF-REFLECTION & CLARITY: Before answering, you must internally review and analyze the user's question to prevent any misunderstandings (especially for ambiguous or complex scientific, mathematical, and historical queries). Ensure your logic is sound, your facts are verified, and your final answer strictly aligns with the core intent of the user's inquiry."""

agent_files = glob.glob("*_agent/agent.py")

for file_path in agent_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path} (could not find old text)")

