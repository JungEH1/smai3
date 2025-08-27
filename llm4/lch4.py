from langchain.agents import load_tools, initialize_agent, AgentType
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools(['wikipedia','llm-math'], llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True

    )

    txt="귀멸의 칼날 무한열차편 주인공이 누구야? 2025년 8월25일 기준으로 개봉 이후 몇 개월이 됐어?"
    print(agent.run(txt))
