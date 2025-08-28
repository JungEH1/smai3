import streamlit as st

page_2 = st.Page("p2.py", title="개념 학습하기", icon="📖")
page_3 = st.Page("p3.py", title="학습자료로 질문하기", icon="🙋")
page_4 = st.Page("p4.py", title="녹음 내용 요약하기", icon="🎙️")
page_8 = st.Page("p8.py", title="채팅하기", icon="💬")
page_111 = st.Page("p111.py", title="달력에 메모하기", icon="📅")

page = st.navigation([page_2, page_3, page_4, page_8, page_111])

page.run()