# LLM-Based-Q/A-on-Web-Context

This application answers the query submitted by user with reference to Web Context.

The video shows the demonstration.

https://github.com/user-attachments/assets/a1c736d2-8ed1-4813-bdd6-ad190abee72e

On the left column it returns the answer based on context while on the right column it answers the query based on its own knowledge.

*Steps to Replicate*

create new python env
`conda create -n myenv python=3.10`

install requirements
`pip install -r requirements.txt`

download and install OLLAMA. This code is for the models gemma:2b and llama 3.2 . One can use other models as well but one has to change line 16 in llm.py.
OLLAMA needs to run in the local for the LLM to work.

Now run
`streamlit run main.py`
