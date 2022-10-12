import streamlit as st
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from streamlit.components.v1 import iframe
import os
import openai
from annotated_text import annotated_text
import pyperclip

openai.api_key = "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"

st.set_page_config(layout="centered",
                   page_title="GPT 3 Academy")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}footer:after {
	content:'Made by Patrick Mauboussin'; 
    padding: 1500px;
	visibility: visible;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


@st.cache
def load_response(user_prompt='Explain to me that I need to paste some text before the AI will work.'):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    return response['choices'][0]['text']


header = st.header('GPT 3 Academy')
text = st.text_area('Paste/Write text')


option = st.selectbox(
    'Change capability',
    ('Summarize for a 2nd grader', 'Make an outline', 'Fact Check', 'Make a quiz given a topic'))

if st.button('Run AI'):

    if not text:
        st.text('Enter a prompt')
    if not option:
        st.text('Enter a capability')

    if text and option:
        if len(text) > 1500:
            st.text('Max input 1500.')
            text = text[0, 1500]
        ai_response = load_response(option + ':\n' + text)

        st.write(ai_response)
