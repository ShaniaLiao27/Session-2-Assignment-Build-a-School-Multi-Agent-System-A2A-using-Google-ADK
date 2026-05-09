def calculator(expression: str) -> str:
    """A calculator tool. Used to calculate any mathematical expression and return the result."""
    try:
        answer = eval(expression)
        return f"Calculation result: {answer}"
    except Exception as e:
        return f"Calculation error, please check the expression. Error: {e}"

def mock_google_search(query: str) -> str:
    """A search tool. Use it when you need to verify historical years or scientific discoveries."""
    return f"(System searched for keyword: {query}. Please use your general knowledge to summarize and answer the student.)"

def search_youtube_history_video(topic: str) -> str:
    """A tool to search for educational history YouTube videos from famous creators like Taiwan Bar (臺灣吧) or Hook."""
    return f"推薦影片：想看更多有趣的解說嗎？請參考【臺灣吧 / HOOK】關於「{topic}」的專屬解說影片！ (影片連結：https://www.youtube.com/results?search_query={topic}+臺灣吧+HOOK)"

def search_youtube_english_pronunciation_video(word: str) -> str:
    """A tool to search for English pronunciation or speaking practice videos from channels like BBC Learning English or Rachel's English."""
    return f"發音練習影片：想聽聽母語人士怎麼唸嗎？請看【BBC Learning English / Rachel's English】關於「{word}」的發音教學！ (影片連結：https://www.youtube.com/results?search_query=how+to+pronounce+{word}+BBC+learning+english+or+Rachel's+english)"

def search_science_reference(topic: str) -> str:
    """A tool to search for credible science references, articles, or documentaries from sources like BBC Earth, National Geographic, or academic journals."""
    return f"延伸閱讀與文獻：想更深入了解嗎？請參考【BBC Earth / 國家地理頻道 (National Geographic) / Google 學術搜尋】關於「{topic}」的優質科普內容與學術依據！ (搜尋連結：https://www.google.com/search?q={topic}+BBC+Earth+OR+National+Geographic)"

def generate_math_visualization(equation: str) -> str:
    """A tool to generate a visual graph, chart, or animation link for a mathematical equation using tools like Desmos or GeoGebra."""
    # Desmos uses URL encoding for equations, but here we just mock it for the agent.
    encoded_eq = equation.replace(" ", "+").replace("=", "%3D")
    return f"視覺化圖表：想要直觀地看懂這道題目嗎？請參考這份【動態視覺化圖表】！ (繪圖連結：https://www.desmos.com/calculator?math={encoded_eq})"
