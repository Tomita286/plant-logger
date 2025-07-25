import cv2
import numpy as np

# --- 設定 ---
# 1. ここに、分析したい画像ファイルの名前を入力します
IMAGE_PATH = "retasunogazou.jpg" 

# 2. 抽出したい緑色の範囲を指定します (HSV色空間)
# この値は、画像によって調整が必要な場合があります
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

    # 結果を表示
    print(f"画像ファイル: {IMAGE_PATH}")
    print(f"緑色のピクセル数: {green_pixel_count}")