import streamlit as st

from MYLLM import save_uploadedfile

# Sidebar
st.sidebar.markdown("Clicked Page 6")

# Page
st.title("Page 6 File Uplaod")
menu=st.selectbox("파일 타입 선택:",["image","pdf","csv"])

if menu == "image":
    st.subheader(menu)
    file = st.file_uploader("이미지를 선택", type=["jpg","png","jpeg"])
    if file:
        save_uploadedfile("img",file,st)
        st.download_button(
            label="파일 다운로드",
            data=file,
            file_name=file.name,
            mime="image/jpg"
        )

elif menu == "pdf":
    st.subheader(menu)
    file = st.file_uploader("pdf를 선택", type=["pdf"])
    if file:
        save_uploadedfile("pdf", file, st)
        st.download_button(
            label="파일 다운로드",
            data=file,
            file_name=file.name,
            mime="application/pdf"
        )

elif menu == "csv":
    st.subheader(menu)
    file = st.file_uploader("csv를 선택", type=["csv"])
    if file:
        save_uploadedfile("csv", file, st)
        st.download_button(
            label="파일 다운로드",
            data=file,
            file_name=file.name,
            mime="text/text"
        )
