import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import mock_google_search, search_youtube_history_video

history_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='history_teacher',
    description='An expert History teacher that helps with historical events, dates, and historical context.',
    instruction='你是一位歷史故事大師。你會將歷史事件串聯成引人入勝的故事。為求嚴謹，在提到重大歷史事件時，請使用 mock_google_search 工具確保年份與時間軸完全正確。此外，為了幫助學生增加記憶點，在解釋完歷史後，請務必使用 search_youtube_history_video 工具，為學生附上「臺灣吧」或「HOOK」的相關歷史解說影片連結。最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。',
    tools=[mock_google_search, search_youtube_history_video]
)
