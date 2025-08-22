import os
import time

import streamlit as st
from PIL import Image
from openai import images
from MYLLM import geminiModel, save_uploadedfile, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 2")

# Page
st.title("page 2 Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file, st)

    text=st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")

    if st.button("SEND"):
        img=Image.open("img/"+file.name)
        model=geminiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response=model.generate_content([text,img])
        my_bar.empty()
        st.info(response.text)