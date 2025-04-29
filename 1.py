from PIL import Image
import os

def process_image_with_pil(image_path):
    # 이미지 열기
    try:
        with Image.open(image_path) as img:
            img.show()  # 이미지를 보여주기
            # 추가적인 이미지 처리 로직을 여기에 넣을 수 있음
            print(f"이미지 처리 성공: {image_path}")
    except Exception as e:
        print(f"이미지 처리 실패: {image_path} ({e})")

# 이미지 경로 설정
image_dir = r'D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Validation\01.원천데이터\VS_EO_SU_DT'
image_name = 'EO_SU_DT_W7_H7_E4_0028.jpg'
image_path = os.path.join(image_dir, image_name)

# 이미지 처리 함수 호출
process_image_with_pil(image_path)
