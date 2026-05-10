<img width="1363" height="872" alt="cs adk web" src="https://github.com/user-attachments/assets/c7b19c2a-97f9-4210-a627-854c4afa887a" />
<img width="1844" height="915" alt="science agent" src="https://github.com/user-attachments/assets/53ecb92e-1825-4f17-a0a9-61ec056631b7" />
<img width="1192" height="999" alt="science adk" src="https://github.com/user-attachments/assets/3f29e65d-f757-4530-a479-daf1d0a62250" />
<img width="1844" height="915" alt="math agent" src="https://github.com/user-attachments/assets/0be977a4-9c28-4c00-9534-748a8e2b09bb" />
<img width="1349" height="999" alt="math adk" src="https://github.com/user-attachments/assets/7535a424-4dcb-4a5c-97b5-5ff90bb9a666" />
<img width="1192" height="999" alt="math adk 2" src="https://github.com/user-attachments/assets/ea976d20-724a-4e73-933d-60e5b08f3e16" />
<img width="1844" height="915" alt="history agent" src="https://github.com/user-attachments/assets/e730c0e8-d4d6-4c27-a078-9a1ec1308f42" />
<img width="1192" height="999" alt="history adk" src="https://github.com/user-attachments/assets/beacaa9c-392a-4a98-a7e0-787f82052b7a" />
<img width="1844" height="915" alt="english agent" src="https://github.com/user-attachments/assets/6d479b3e-04f2-4f62-a75d-0cfb8c8a4537" />
<img width="1113" height="874" alt="english adk web" src="https://github.com/user-attachments/assets/e8a967e5-f859-40e2-90ad-717c03bbd802" />
<img width="1113" height="999" alt="english adk 2" src="https://github.com/user-attachments/assets/88225de8-744b-41b9-b9c0-68d475f70bd6" />
<img width="1844" height="915" alt="coordinator agent" src="https://github.com/user-attachments/assets/cd9f1e2b-1a93-4c67-a224-7a1395ce787a" />
<img width="1626" height="915" alt="antigravity" src="https://github.com/user-attachments/assets/63737950-3e95-4506-8d85-f36d51a6caa0" />
# 🎓 School Multi-Agent System (A2A)

This project is a hierarchical Multi-Agent System built using the **Google Agent Development Kit (ADK)**. It features a central routing agent and multiple specialized subject-matter agents equipped with custom tools.

## 🌟 Project Architecture

### 1. Root Agent (School Coordinator)
- **Role**: Acts as the central router.
- **Function**: Analyzes the user's intent and language, then intelligently delegates the query to the most appropriate subject teacher.

### 2. Subject Agents (Sub-Agents)
The system contains 6 highly specialized sub-agents:
- 📖 **English Teacher**: Focuses on grammar and phonetic breakdowns. Equipped with YouTube search tools for pronunciation guides.
- 🧮 **Maths Teacher**: Provides step-by-step logic. Equipped with a `calculator` tool to verify answers and a `generate_math_visualization` tool for Desmos/GeoGebra links.
- 🔬 **Science Teacher**: Uses everyday analogies. Equipped with a search tool for fact-checking and a `search_science_reference` tool to recommend documentaries (e.g., BBC Earth).
- 🏛️ **History Teacher**: A master storyteller. Equipped with search tools for timeline accuracy and a tool to recommend educational YouTube videos (e.g., Taiwan Bar, HOOK).
- 🌍 **Geography Teacher (Bonus Level 1)**: Equipped with a `search_google_maps` tool to provide street view and map links for interactive exploration.
- 💻 **Computer Science Teacher (Bonus Level 1)**: Equipped with a `mock_code_execution` tool to "run" code in a sandbox and explain the output.

## 🚀 Features Implemented
- ✅ **Core Requirement**: 1 Root Agent + 4 Core Subject Agents.
- ✅ **Bonus Level 1**: Added Geography and Computer Science Agents.
- ✅ **Bonus Level 2**: Implemented custom Tools (`tools.py`) for agents to use (Calculator, Google Maps Search, Video Search, etc.).
- ✅ **Multi-Language Support**: Agents dynamically detect the user's input language and respond in the matching language.

## 🛠️ How to Run
1. Ensure you have activated your virtual environment: `source venv/bin/activate`
2. Make sure you have your `GEMINI_API_KEY` set in the `.env` file.
3. Start the Google ADK Web UI:
   ```bash
   adk web
   ```
4. Open your browser and interact with the School Coordinator!
