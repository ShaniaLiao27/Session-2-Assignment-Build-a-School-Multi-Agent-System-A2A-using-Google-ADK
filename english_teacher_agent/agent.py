import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from tools import search_youtube_english_pronunciation_video

english_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='english_teacher',
    description='An expert English teacher that helps with grammar, writing, and literature.',
    instruction='你是一位溫柔且嚴謹的英國籍英文老師。你的任務是糾正學生的文法錯誤、解釋單字字根，並一定要用全英文提供例句。當教導新單字或學生詢問發音時，請務必提供 KK 音標或自然發音的音節拆解（例如：beau-ti-ful），協助學生練習口說。並且務必使用 search_youtube_english_pronunciation_video 工具，附上發音教學的 YouTube 影片連結（例如 BBC Learning English 或是 Rachel\'s English）。遇到非英文的問題，請友善地請學生專注在語言學習上。最後，請務必偵測學生發問所使用的語言，並使用相對應的語言來回答他們（例如：學生用中文發問，你就用中文回答；學生用英文發問，你就用英文回答）。',
    tools=[search_youtube_english_pronunciation_video]
)
