## AI Crew Multi Agent TO Create A Multi Agent to Research, Write and Perform Examination

# Introduction

Welcome to the AI Crew Multi-Agent System! This project leverages multiple intelligent agents to perform comprehensive tasks including research, writing, and examination. The system is designed to facilitate the creation of structured and engaging educational content, ensuring a robust learning experience.

# Overview

The AI Crew Multi-Agent System is composed of three specialized agents:

Research Agent: Develops comprehensive teaching plans for various subjects, providing a structured approach with topics, resources, and a step-by-step guide.
Writer Agent: Uses the teaching plan to create clear and engaging textual explanations that are easy for beginners to understand.
Examiner Agent: Crafts evaluation questions to assess understanding and retention of the material covered in the explanations.
By integrating these agents, the system ensures a holistic approach to content creation, making it an invaluable tool for educators, students, and content creators.

# Features

Automated Research: Generates detailed and structured teaching plans for any given subject.
Engaging Writing: Produces beginner-friendly explanations based on the research outputs.
Effective Assessment: Creates targeted questions to evaluate comprehension and retention.

## Getting Started
Follow these steps to set up and run the AI Crew Multi-Agent System
1. **Download and Install Ollama**
2. **execute llama2.;** `ollama run llama2`
3. **Make the create-llama2-model-file.sh Accessible:** `chmod +x ./setup/create-llama2-model-file.sh`
4. **Execute create-llama2-model-file.sh script:** `./create-llama2-model-file.sh`
5. **Install Poetry:** `pip3 install poetry`
6. **Install Dependencies with Poetry:** `poetry install --no-root`
7. **Activate the Python Virtual Environment:** `emulate bash -c '. /Users/adigweleo/Library/Caches/pypoetry/virtualenvs/markdown-validation-crew-T_Z_lDTx-py3.11/bin/activate'`
8. **Run the Main Script**
Navigate to the directory where your main.py file is located and run: `python3 main.py "subject"`
Replace "subject" with the specific subject you want to generate content for.
Note: Don’t forget to add your OpenAI key to main.py.
