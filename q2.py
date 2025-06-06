from PIL import Image
from PIL import ImageEnhance

def change_brightness(img, factor):
    # TODO: [지시사항 1번] 이미지의 밝기를 변화시키는 코드를 완성하세요.
    bright_enhancer = None
    img_bright = None
    
    return img_bright
    
def change_contrast(img, factor):
    # TODO: [지시사항 2번] 이미지의 대조를 변화시키는 코드를 완성하세요.
    contrast_enhancer = None
    img_contrast = None
    
    return img_contrast
    
def change_grayscale(img):
    # TODO: [지시사항 3번] 이미지를 흑백 이미지로 변경하는 코드를 완성하세요.
    img_gray = None
    
    return img_gray
    
def show_image(img, name):
    img.save(name)
    elice_utils.send_image(name)

def main():
    img = Image.open("Lenna.png")
    
    # TODO: [지시사항 4번] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    
    # 이미지 밝게 하기
    img_bright = None
    
    # 이미지 어둡게 하기
    img_dark = None
    
    # 이미지 대조 늘리기
    img_high_contrast = None
    
    # 이미지 대조 줄이기
    img_low_contrast = None
    
    # 이미지 흑백 변환
    img_gray = None
    
    print("=" * 50, "밝은 이미지", "=" * 50)
    show_image(img_bright, "bright.png")
    
    print("=" * 50, "어두운 이미지", "=" * 50)
    show_image(img_dark, "dark.png")
    
    print("=" * 50, "강한 대조 이미지", "=" * 50)
    show_image(img_high_contrast, "high_contrast.png")
    
    print("=" * 50, "약한 대조 이미지", "=" * 50)
    show_image(img_low_contrast, "low_contrast.png")
    
    print("=" * 50, "흑백 이미지", "=" * 50)
    show_image(img_gray, "gray.png")
    
    return img_bright, img_dark, img_high_contrast, img_low_contrast, img_gray

if __name__ == "__main__":
    main()
