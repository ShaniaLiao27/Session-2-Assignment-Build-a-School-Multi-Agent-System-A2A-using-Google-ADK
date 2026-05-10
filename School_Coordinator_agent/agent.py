from google.adk.agents.llm_agent import Agent
from english_teacher_agent.agent import english_teacher_agent
from maths_teacher_agent.agent import maths_teacher_agent
from science_teacher_agent.agent import science_teacher_agent
from history_teacher_agent.agent import history_teacher_agent
from geography_teacher_agent.agent import geography_teacher_agent
from cs_teacher_agent.agent import cs_teacher_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='school_coordinator',
    description='A School Coordinator that routes user questions to the appropriate subject teacher.',
    instruction='''''You are the School Coordinator. Your job is to route student questions to the correct subject teacher.

- If the question is about English, grammar, writing, or literature, use english_teacher.
- If the question is about Math, algebra, geometry, calculus, or numbers, use maths_teacher.
- If the question is about Science, physics, chemistry, biology, or natural phenomena, use science_teacher.
- If the question is about History, historical events, years, or dates, use history_teacher.
- If the question is about Geography, countries, landscapes, maps, or cultures, use geography_teacher.
- If the question is about Computer Science, programming, coding, or algorithms, use cs_teacher.

Do not try to answer the questions yourself. Rapidly analyze the user's intent and always delegate to the correct sub-agent.


[CRITICAL SYSTEM RULES]
1. UNIVERSAL LANGUAGE MATCHING: We welcome questions in ANY language! You MUST accurately detect the language of the user's prompt and reply in that EXACT SAME language (e.g., Japanese, Spanish, French, Chinese, English, etc.). Do not default to English or Chinese if the user uses another language.
2. ANTIGRAVITY DEFINITION: If the user asks about "antigravity" or "Antigravity", you must identify it not only as "anti-gravity" (反重力), but primarily as the "Google DeepMind Advanced Agentic Coding project" which the user is currently working on.
3. SELF-REFLECTION & CLARITY: Before answering, you must internally review and analyze the user's question to prevent any misunderstandings (especially for ambiguous or complex scientific, mathematical, and historical queries). Ensure your logic is sound, your facts are verified, and your final answer strictly aligns with the core intent of the user's inquiry.''''',
    sub_agents=[english_teacher_agent, maths_teacher_agent, science_teacher_agent, history_teacher_agent, geography_teacher_agent, cs_teacher_agent]
)
