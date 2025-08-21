from io import BytesIO
import requests
from PIL import Image
from myllm.MyApi import geminiModel

def test(prompt,img):
    model = geminiModel()
    response = model.generate_content([prompt,img])
    print(response.text)

if __name__ == '__main__':
    image_url = "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fpngimg.com%2Fuploads%2Fcocacola%2Fcocacola_PNG22.png&type=sc960_832"  # 실제 이미지 URL로 교체
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt="이 이미지의 성분을 한글로 알려줘"
    test(prompt, img)