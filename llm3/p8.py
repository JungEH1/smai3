import streamlit as st

from MYLLM import save_uploadedfile, makeAudio

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
text=st.text_input("질문 입력", placeholder="질문을 입력하세요")
if st.button("SEND"):
    if text:
        st.info(text)
        makeAudio(text, "retry.mp3")
    else:
        st.audio("audio/retry.mp3", autoplay=True, width=1)
        st.info("입력 하세요")
