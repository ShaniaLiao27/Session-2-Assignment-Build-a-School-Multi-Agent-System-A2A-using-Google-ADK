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
