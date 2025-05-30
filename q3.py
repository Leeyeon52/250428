from PIL import Image
from PIL import ImageFilter

def sharpening(img):
    # TODO: [지시사항 1번] 이미지에 샤프닝 필터를 적용시키는 코드를 완성하세요.
    img_sharpen = None
    
    return img_sharpen
    
def blur(img):
    # TODO: [지시사항 2번] 이미지에 블러 필터를 적용시키는 코드를 완성하세요.
    img_blur = None
    
    return img_blur
    
def detect_edge(img):
    # TODO: [지시사항 3번] 이미지의 경계선을 탐지하는 코드를 완성하세요.
    img_edge = None
    
    return img_edge
    
def show_image(img, name):
    img.save(name)
    elice_utils.send_image(name)

def main():
    img = Image.open("Lenna.png")
    
    # TODO: [지시사항 4번] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    
    # 이미지 샤프닝 한번 적용하기
    img_sharpen_1 = None
    
    # 이미지 샤프닝 5번 적용하기
    img_sharpen_5 = None
    
    # 이미지 블러 한번 적용하기
    img_blur_1 = None
    
    # 이미지 블러 5번 적용하기
    img_blur_5 = None
    
    # 이미지 경계선 찾기
    img_edge = None
    
    print("=" * 50, "샤프닝 한번 적용한 이미지", "=" * 50)
    show_image(img_sharpen_1, "sharpen_1.png")
    
    print("=" * 50, "샤프닝 다섯번 적용한 이미지", "=" * 50)
    show_image(img_sharpen_5, "sharpen_5.png")
    
    print("=" * 50, "블러 한번 적용한 이미지", "=" * 50)
    show_image(img_blur_1, "blur_1.png")
    
    print("=" * 50, "블러 다섯번 적용한 이미지", "=" * 50)
    show_image(img_blur_5, "blur_5.png")
    
    print("=" * 50, "경계선 이미지", "=" * 50)
    show_image(img_edge, "edge.png")
    
    return img_sharpen_1, img_sharpen_5, img_blur_1, img_blur_5, img_edge


if __name__ == "__main__":
    main()
