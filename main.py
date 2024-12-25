import streamlit as st
from loader import Doc_loader
from llm import OllamaModel

# Streamlit UI Elements
st.title("LLM-based Q&A")
st.write("Enter your prompt, web URL (for context), and select a model from the dropdown.")

# Input: Prompt from the user
user_prompt = st.text_area("Enter your Prompt", "Disadvantage of RNN compared to LSTM are as follows :")

# Input: Web URL from the user
web_url = st.text_input("Enter a URL to scrape content from", "https://colah.github.io/posts/2015-08-Understanding-LSTMs/")

# Dropdown to select the mode of response
dropdown_option = st.selectbox("Select Response Mode", ["gemma:2b", "llama3.2"])

submit_button = st.button("Submit")

# Handling the Submit button click
if submit_button:
    # Displaying the inputs entered by the user
    if user_prompt:
        st.write("Prompt entered: ", user_prompt)
    else:
        st.write("Please enter a valid prompt.")
    
    if web_url:
        loader = Doc_loader(web_url)
        if loader.verify() != "Url is Valid":
            st.write("Please enter a valid URL.")
            st.write(loader.verify())
        else:
            st.write("Web URL entered: ", web_url)
            loader.split()
            print(loader.documents," ",loader.res)
            model = OllamaModel(dropdown_option,loader.documents)
            if user_prompt:
                st.write(f"Response Mode selected: {dropdown_option}")
                with_context = model.result_context(user_prompt)
                without_context = model.result_without_context(user_prompt)
        
                # Placeholder for results (to be populated later with actual logic)
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Result from Web Content:")
                    st.write(with_context[0])
                    st.subheader("Context from Web Content:")
                    st.write(with_context[1])

                with col2:
                    st.subheader("Result based on Prompt:")
                    st.write(without_context)

    else:
        st.write("Please enter a valid URL.")    

else:
    st.write("Click 'Submit' to get results.")
