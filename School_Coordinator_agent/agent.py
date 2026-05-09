from google.adk.agents.llm_agent import Agent
from english_teacher_agent.agent import english_teacher_agent
from maths_teacher_agent.agent import maths_teacher_agent
from science_teacher_agent.agent import science_teacher_agent
from history_teacher_agent.agent import history_teacher_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='school_coordinator',
    description='A School Coordinator that routes user questions to the appropriate subject teacher.',
    instruction='''You are the School Coordinator. Your job is to route student questions to the correct subject teacher.

- If the question is about English, grammar, writing, or literature, use english_teacher.
- If the question is about Math, algebra, geometry, calculus, or numbers, use maths_teacher.
- If the question is about Science, physics, chemistry, biology, or natural phenomena, use science_teacher.
- If the question is about History, historical events, years, or dates, use history_teacher.

Do not try to answer the questions yourself. Rapidly analyze the user's intent and always delegate to the correct sub-agent.
Also, please make sure to detect the language the student uses to ask questions, and answer them in the corresponding language (e.g., if the student asks in Chinese, answer in Chinese; if the student asks in English, answer in English).''',
    sub_agents=[english_teacher_agent, maths_teacher_agent, science_teacher_agent, history_teacher_agent]
)
