from PIL import Image

from myllm.MyApi import geminiModel


def test():
    img=Image.open("img/nero.jpg")

    model = geminiModel()

    response = model.generate_content(["제시한 이미지에 있는 고양이의 종 알려줘",img])

    print(response.text)


if __name__ == '__main__':
    test()