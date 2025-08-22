from platform import system
import streamlit as st
from MYLLM import save_uploadedfile
from MYLLM import makeMsg, openAiModelArg, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 7")

# Page
st.title("Page 7")

system = st.text_input("SYSTEM",placeholder="system 을 입력")
text = st.text_input("질문을 입력",placeholder="질문을 입력")

if st.button("SEND"):
    if system and text:
        st.info(f"{system}에게 {text} 문의 합니다.")
        msg=makeMsg(system, text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = openAiModelArg("gpt-4o",msg)
        my_bar.empty()

        st.info(result)
    else:
        st.info("입력하세요")