import base64
import streamlit as st
from PIL import Image

from MYLLM import save_uploadedfile, progressBar, openAiModelArg, openAiModel, encode_image, makeAudio

# Sidebar
st.sidebar.markdown("Clicked Page 9")

# Page
st.title("Page 9")

file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file, st)

    text=st.text_area(label="질문입력:", placeholder="질문을 입력 하세요")

    # OpenAI에게 물어 본다.
    if st.button("SEND"):
        base64img = encode_image("img/" + file.name)
        model = openAiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
                {"role": "user", "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{base64img}"}
                     }
                ]}
            ],
            temperature=0.0,
        )
        my_bar.empty()
        st.info(response.choices[0].message.content)
        makeAudio(response.choices[0].message.content, "imgresult.mp3")
        st.audio("audio/imgresult.mp3", autoplay=True)

