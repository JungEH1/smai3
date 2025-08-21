import urllib

from jinja2.utils import urlize

from myllm.MyApi import geminiModel, openAiModelArg, makeMsg, openAiModel

def test(prompt):
    openModel=openAiModel()
    response = openModel.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)
    imgName="img/bluecat.png"
    urllib.request.urlretrieve(image_url, imgName)

if __name__ == '__main__':
    prompt="파란 눈을 가진 흰색 고양이 사진 만들어줘"
    test(prompt)