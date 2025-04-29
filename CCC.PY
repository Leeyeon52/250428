import os
import json
import shutil
from PIL import Image

# === YOLOv8 형식 디렉토리 생성 ===
output_image_dir = r"D:\yolo_dataset\images"
output_label_dir = r"D:\yolo_dataset\labels"

for phase in ['train', 'val']:
    os.makedirs(os.path.join(output_image_dir, phase), exist_ok=True)
    os.makedirs(os.path.join(output_label_dir, phase), exist_ok=True)

# === 데이터 경로 설정 ===
sets = {
    'train': {
        'json_folder': r'D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Training\02.라벨링데이터',
        'image_folder': r'D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Training\01.원천데이터',
    },
    'val': {
        'json_folder': r'D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Validation\02.라벨링데이터',
        'image_folder': r'D:\52.군 경계 작전 환경 합성데이터\3.개방데이터\1.데이터\Validation\01.원천데이터',
    }
}

# === 클래스 매핑 ===
label_dict = {
    'person': 0,
    'vehicle': 1,
    'unknown': 2,
}

def convert_and_copy(phase, json_folder, image_folder):
    out_img_dir = os.path.join(output_image_dir, phase)
    out_lbl_dir = os.path.join(output_label_dir, phase)

    for file in os.listdir(json_folder):
        if not file.endswith('.json'):
            continue

        json_path = os.path.join(json_folder, file)
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        image_name = data['images'][0]['file_name']
        image_path = os.path.join(image_folder, image_name)
        image = Image.open(image_path)
        w, h = image.size

        # 이미지 복사
        shutil.copy(image_path, os.path.join(out_img_dir, image_name))

        # 라벨 생성
        label_file = os.path.join(out_lbl_dir, image_name.replace('.jpg', '.txt'))
        with open(label_file, 'w', encoding='utf-8') as f_out:
            for ann in data['annotations']:
                class_name = ann['category_name']
                cls_id = label_dict[class_name]

                x, y, width, height = ann['bbox']
                x_center = (x + width / 2) / w
                y_center = (y + height / 2) / h
                norm_w = width / w
                norm_h = height / h

                f_out.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}\n")

for phase in ['train', 'val']:
    print(f"📂 처리 중: {phase}")
    convert_and_copy(phase, sets[phase]['json_folder'], sets[phase]['image_folder'])

# === data.yaml 생성 ===
data_yaml = """
path: D:/yolo_dataset
train: images/train
val: images/val
nc: 3
names: ['person', 'vehicle', 'unknown']
"""

with open(r"D:\yolo_dataset\data.yaml", 'w', encoding='utf-8') as f:
    f.write(data_yaml.strip())

print("📝 data.yaml 생성 완료: D:/yolo_dataset/data.yaml")
