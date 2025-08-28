import streamlit as st
import datetime
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

# --- LangChain 초기화 ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = FAISS.from_documents([], embeddings)

# --- Streamlit UI ---
st.title("📅 LangChain AI 달력 Q&A")

# 오늘 날짜
today = datetime.date.today()
date = st.date_input("날짜 선택", today)

# 메모 입력
memo = st.text_area("메모 입력")
if st.button("저장"):
    if memo.strip():
        doc = Document(page_content=memo, metadata={"date": str(date)})
        st.session_state.vectorstore.add_documents([doc])
        st.success(f"{date} 메모 저장 완료!")

# 전체 메모 보기
st.subheader("📂 전체 메모")
all_docs = st.session_state.vectorstore.similarity_search("", k=100)
for d in all_docs:
    st.markdown(f"**{d.metadata['date']}** : {d.page_content}")

# AI에게 질문
st.subheader("❓ AI에게 질문하기")
question = st.text_input("질문을 입력하세요")
if st.button("질문하기"):
    if question.strip():
        retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 5})
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        answer = qa.run(question)
        st.write("🧠 AI 답변:", answer)
