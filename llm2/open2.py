from myllm.MyApi import geminiModel, openAiModelArg, makeMsg


def test(prompt):
    modelName="gpt-4o"
    msg = makeMsg("너는 내 친한 친구", prompt)
    result = openAiModelArg(modelName, msg)
    print(result)


if __name__ == '__main__':
    prompt="SK하이닉스에 대해서 알려줘"
    test(prompt)