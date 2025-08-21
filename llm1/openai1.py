from myllm.MyApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test():
    model=openAiModel()

    response=openAiModelArg("gpt-4o",makeMsg("한국 선생님","더현대 맛집 알려줘"))

    print(response)

if __name__ == '__main__':
    test()