import time
import streamlit as st
from MYLLM import geminiTxt, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 1")

# Page
st.title("page 1")
text = st.text_area(label="질문 입력: ",placeholder="질문을 입력 하세요: ")
if st.button("SEND"):
    if text:

        my_bar = progressBar("Operation in progress. Please wait.")
        result=geminiTxt(text)
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")