from myllm.MyApi import geminiModel, openAiModelArg, makeMsg, openAiModel


def test(prompt):
    promptMp3="prompt.mp3"
    model = openAiModel()
    response = model.audio.speech.create(
        model="tts-1",
        input= prompt,
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )
    response.stream_to_file(promptMp3)

    modelName="gpt-4o"
    msg = makeMsg("너는 친한 친구", prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

#   결과를 음성으로 변환하시오
    resultMp3 = "result.mp3"
    response = model.audio.speech.create(
        model="tts-1",
        input=result,
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )


if __name__ == '__main__':
    prompt="우간다의 수도가 어디야"
    test(prompt)