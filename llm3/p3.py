import time

import streamlit as st

# Sidebar
st.sidebar.markdown("Clicked Page 3")

# Page
st.title("page 3")

text = st.text_area(label="질문 입력: ",placeholder="질문을 입력 하세요: ")

selected_option = st.radio("옵션을 선택하세요", ("java", "python", "c++"))

st.write(f"선택된 옵션: {selected_option}")

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

        result=geminiTxt(text(selected_option))
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")

