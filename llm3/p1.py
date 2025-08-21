import time
import streamlit as st
from MYLLM import geminiTxt

# Sidebar
st.sidebar.markdown("Clicked Page 1")

# Page
st.title("page 1")
text = st.text_area(label="질문 입력: ",placeholder="질문을 입력 하세요: ")
if st.button("SEND"):
    if text:
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------

        result=geminiTxt(text)
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")