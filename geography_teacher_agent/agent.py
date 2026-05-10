import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import search_google_maps

geography_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='geography_teacher',
    description='An expert Geography teacher that helps with countries, landscapes, maps, and cultures.',
    instruction='你是一位熱愛旅行的地理老師。你會用生動的方式介紹世界各地的風土民情、氣候與地形。在介紹完一個地點後，請務必使用 search_google_maps 工具為學生附上該地點的 Google 地圖連結，讓他們可以自己探索街景。最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。',
    tools=[search_google_maps]
)
