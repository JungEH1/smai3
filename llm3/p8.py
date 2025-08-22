import streamlit as st

from MYLLM import save_uploadedfile, makeAudio, progressBar, geminiTxt, makeMsg, openAiModelArg

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
system = st.text_input("SYSTEM",placeholder="system 을 입력")
text=st.text_input("질문 입력", placeholder="질문을 입력하세요")

if st.button("SEND"):
    if system and text:
        st.info(text)
        makeAudio(text, "temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True)

        my_bar = progressBar("Operation in progress. Please wait.")
        msg=makeMsg(system, text)
        result = openAiModelArg("gpt-4o", msg)

        makeAudio(result, "result.mp3")
        my_bar.empty()
        st.info(result)
        st.audio("audio/result.mp3", autoplay=True)
    else:
        st.audio("audio/retry.mp3", autoplay=True, width=1)
        st.info("입력 하세요")
