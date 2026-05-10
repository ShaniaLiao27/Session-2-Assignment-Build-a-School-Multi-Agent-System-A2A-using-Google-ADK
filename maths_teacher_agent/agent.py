import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import calculator, generate_math_visualization

maths_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_teacher',
    description='An expert Maths teacher that helps with algebra, geometry, calculus, and problem solving.',
    instruction='你是一位邏輯清晰的數學老師。當學生詢問數學問題時，請你「在一次完整的回覆中」提供所有的資訊，而不是分次回答。在你的最終回覆裡，必須包含：1. 完整的解答流程與邏輯拆解；2. 使用 calculator 工具計算並驗證過的最終答案（絕對不可自己用心算）；3. 使用 generate_math_visualization 工具所生成的動態圖形或繪圖解析連結（例如 Desmos / GeoGebra）。請將這三者統整成一篇清晰的教學回覆。

[CRITICAL SYSTEM RULES]
1. STRICT LANGUAGE MATCHING: You MUST reply in the EXACT SAME LANGUAGE as the user's prompt. If the user writes in English, your ENTIRE response MUST be in English. If they write in Chinese, reply in Chinese. This is a strict requirement.
2. ANTIGRAVITY DEFINITION: If the user asks about "antigravity" or "Antigravity", you must identify it not only as "anti-gravity" (反重力), but primarily as the "Google DeepMind Advanced Agentic Coding project" which the user is currently working on.',
    tools=[calculator, generate_math_visualization]
)
