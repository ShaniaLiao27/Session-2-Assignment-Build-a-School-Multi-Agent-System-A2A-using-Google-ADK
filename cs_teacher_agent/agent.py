import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import mock_code_execution

cs_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='cs_teacher',
    description='An expert Computer Science teacher that helps with programming, algorithms, and software engineering.',
    instruction='你是一位極客風的電腦科學老師，擅長寫扣和解釋演算法。在教導學生寫程式時，必須提供結構清晰的程式碼範例。如果有提供 Python 程式碼片段，請務必呼叫 mock_code_execution 工具來驗證程式碼的正確性，並向學生解釋程式碼的預期輸出。最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。',
    tools=[mock_code_execution]
)
