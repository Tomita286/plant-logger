import cv2
import numpy as np
import csv
from datetime import datetime
import os

# --- 設定 ---
IMAGE_PATH = "retasunogazou.jpg" 
CSV_PATH = "growth_log.csv"
MASK_OUTPUT_PATH = "mask_result.jpg" # ← マスク画像の保存先を追加
LOWER_GREEN = np.array([35, 40, 40])
UPPER_GREEN = np.array([85, 255, 255])
# --- 設定ここまで ---

image = cv2.imread(IMAGE_PATH)

if image is None:
    print(f"エラー: 画像ファイル '{IMAGE_PATH}' が見つかりません。")
else:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, LOWER_GREEN, UPPER_GREEN)
    
    # ↓↓↓↓ この行を追加しました ↓↓↓↓
    cv2.imwrite(MASK_OUTPUT_PATH, mask) # マスクを画像として保存
    
    green_pixel_count = np.count_nonzero(mask)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode='a', newline='') as csv_file:
        fieldnames = ['timestamp', 'image_file', 'green_pixel_count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': timestamp, 
            'image_file': IMAGE_PATH, 
            'green_pixel_count': green_pixel_count
        })

    print("--- 分析結果 ---")
    print(f"画像ファイル: {IMAGE_PATH}")
    print(f"緑色のピクセル数: {green_pixel_count}")
    print(f"結果を'{CSV_PATH}'に保存しました。")
    print(f"マスク画像を'{MASK_OUTPUT_PATH}'に保存しました。") # ← 確認メッセージを追加