from langchain.model_laboratory import ModelLaboratory
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    model_lab = ModelLaboratory.from_llms([openllm,genllm])
    model_lab.compare("귀멸의 칼날 무한열차편 주인공이 누구야? 2025년 8월25일 기준으로 개봉 이후 몇 개월이 됐어?")



