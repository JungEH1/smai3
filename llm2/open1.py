from myllm.MyApi import geminiModel, openAiModelArg, makeMsg


def test(prompt):
    modelName="gpt-4o"
    msg = makeMsg("너는 친한 친구", prompt)
    result = openAiModelArg(modelName, msg)
    print(result)


if __name__ == '__main__':
    prompt="방콕 여행 계획 세워줘"
    test(prompt)