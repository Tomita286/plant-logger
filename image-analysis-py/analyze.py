import cv2
import numpy as np
import csv
from datetime import datetime
import os

# --- 設定 ---
IMAGE_PATH = "retasunogazou.jpg" 
CSV_PATH = "growth_log.csv"
LOWER_GREEN = np.array([35, 40, 40])
UPPER_GREEN = np.array([85, 255, 255])
# --- 設定ここまで ---

# 画像を読み込む
image = cv2.imread(IMAGE_PATH)

if image is None:
    print(f"エラー: 画像ファイル '{IMAGE_PATH}' が見つかりません。")
else:
    # 画像をBGRからHSV色空間に変換
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 指定した緑色の範囲に収まる部分を抽出するマスクを作成
    mask = cv2.inRange(hsv_image, LOWER_GREEN, UPPER_GREEN)
    
    # マスクの白色のピクセル（＝緑色の領域）の数を数える
    green_pixel_count = np.count_nonzero(mask)

    # 現在の日時を取得
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CSVファイルに追記
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