import time

import streamlit as st
from PIL import Image

from MYLLM import geminiModel, progressBar
from MYLLM import save_carpturefile

# Sidebar
st.sidebar.markdown("Clicked Page 5")

# Page
st.title("Page 5")
picture = st.camera_input("Take a picture")

if picture:
    st.info("이미지를 캡쳐 했습니다.")
    save_carpturefile("capture",picture,"temp.png", st)
    text = st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        img=Image.open("capture/temp.png")
        model = geminiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.generate_content([text, img])
        my_bar.empty()
        st.info(response.text)