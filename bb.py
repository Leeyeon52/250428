import os
import json
import shutil
from PIL import Image

# 기본 경로 (Validation 폴더로 기준 잡기)
base_path = r"D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Validation"

# JSON, 이미지 폴더 경로 (수정된 버전)
sets = {
    'train': {
        'json_folder': os.path.join(base_path.replace('Validation', 'Training'), '02.라벨링데이터'),
        'image_folder': os.path.join(base_path.replace('Validation', 'Training'), '01.원천데이터'),
    },
    'val': {
        'json_folder': os.path.join(base_path, '02.라벨링데이터'),
        'image_folder': os.path.join(base_path, '01.원천데이터'),
    }
}

# YOLO 학습용 출력 경로
output_base = r"D:\yolo_dataset"
image_exts = ['.jpg', '.jpeg', '.png']

# 변환 및 복사 함수
def convert_and_copy(phase, json_folder, image_folder):
    label_output = os.path.join(output_base, 'labels', phase)
    image_output = os.path.join(output_base, 'images', phase)
    os.makedirs(label_output, exist_ok=True)
    os.makedirs(image_output, exist_ok=True)

    for file in os.listdir(json_folder):
        if file.endswith('.json'):
            base_name = os.path.splitext(file)[0]

            # JSON 로드
            with open(os.path.join(json_folder, file), 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 이미지 찾기
            image_path = None
            for ext in image_exts:
                candidate = os.path.join(image_folder, base_name + ext)
                if os.path.exists(candidate):
                    image_path = candidate
                    break

            if not image_path:
                print(f"⚠️ 이미지 없음: {base_name}")
                continue

            # 이미지 복사
            shutil.copy(image_path, os.path.join(image_output, os.path.basename(image_path)))

            # 이미지 크기 얻기
            with Image.open(image_path) as img:
                img_width, img_height = img.size

            # YOLO 포맷 변환
            yolo_lines = []
            for ann in data.get("annotations", []):
                if ann.get("shape") == "Bounding Box":
                    (x1, y1), (x2, y2) = ann["points"]
                    cx = (x1 + x2) / 2 / img_width
                    cy = (y1 + y2) / 2 / img_height
                    w = abs(x2 - x1) / img_width
                    h = abs(y2 - y1) / img_height
                    yolo_lines.append(f"0 {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

            # YOLO 라벨 파일 저장
            label_txt_path = os.path.join(label_output, base_name + ".txt")
            with open(label_txt_path, "w", encoding='utf-8') as f:
                f.write("\n".join(yolo_lines))

            print(f"✅ 변환 및 복사 완료: {phase} - {base_name}")

# 경로 체크
for phase, paths in sets.items():
    for name, path in paths.items():
        if not os.path.exists(path):
            print(f"❌ 경로 없음: {path}")

# 세트별 처리
for phase, paths in sets.items():
    print(f"\n📂 처리 중: {phase}")
    convert_and_copy(phase, paths['json_folder'], paths['image_folder'])


# --- 추가: data.yaml 자동 생성 ---
# YOLO 학습을 위한 config 파일 만들기
data_yaml_path = os.path.join(output_base, "data.yaml")
yaml_content = f"""train: {os.path.join(output_base, 'images', 'train').replace(os.sep, '/')}
val: {os.path.join(output_base, 'images', 'val').replace(os.sep, '/')}

nc: 1
names: ['object']
"""

with open(data_yaml_path, "w", encoding="utf-8") as f:
    f.write(yaml_content)

print(f"\n📝 data.yaml 생성 완료: {data_yaml_path}")
