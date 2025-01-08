# Query Answering with Web Context

This application answers user-submitted queries by referring to web context. The interface offers two perspectives:

Left Column: Returns answers based on the given web context.
Right Column: Returns answers based on the application's own knowledge base.

## Demonstration
The video below illustrates the application in action:

[Demo Video: streamlit-main-2025-01-06-09-01-02.1.mov](https://github.com/user-attachments/assets/a1c736d2-8ed1-4813-bdd6-ad190abee72e
)

Steps to Reproduce
Create a New Python Environment
Use Conda to create a new Python environment:

`conda create -n myenv python==3.10
conda activate myenv`

Install Dependencies
Install the necessary packages from `requirements.txt`:

`pip install -r requirements.txt`

Download and Install OLLAMA

This app uses OLLAMA with the gemma:2b and llama 3.2 models.
Other models can be used but you will have to change line 16 in llm.py.

Note: OLLAMA must be running locally for the LLMs to work.
Run the Application

Run the Streamlit app:
`streamlit run main.py`

## Features
* Dual Answering Approach: Compare answers derived from web context and internal knowledge.
* Model Flexibility: Easy to use multiple models only by updating configuration.
* Streamlit Integration: Nice UI of querying and compare answers.
