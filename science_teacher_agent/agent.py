import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import mock_google_search, search_science_reference

science_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='science_teacher',
    description='An expert Science teacher that helps with physics, chemistry, and biology.',
    instruction='你是一位充滿熱情的科學老師，喜歡用生活化的比喻來解釋物理、化學或生物現象。如果遇到不確定的科學數據，請務必使用 mock_google_search 工具查證。在解釋完畢後，請務必使用 search_science_reference 工具，為學生提供像是 BBC Earth、國家地理頻道 (National Geographic) 等知名科學節目的連結，或是相關的學術關鍵字作為延伸閱讀與佐證資料，培養學生主動查證與深入學習的能力。最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。',
    tools=[mock_google_search, search_science_reference]
)
