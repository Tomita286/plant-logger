import cv2
import numpy as np
import sys # sysライブラリを追加

# --- 設定 ---
# IMAGE_PATHはコマンドライン引数から受け取るので、ここは削除します
LOWER_GREEN = np.array([35, 40, 40])
UPPER_GREEN = np.array([85, 255, 255])
# --- 設定ここまで ---

# コマンドライン引数から画像ファイルのパスを取得
if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    print("エラー: 画像ファイルのパスが指定されていません。")
    sys.exit(1)

# 画像を読み込む
image = cv2.imread(image_path)

if image is None:
    # Rails側でエラーを検知できるよう、標準エラー出力にメッセージを出す
    sys.stderr.write(f"エラー: 画像ファイル '{image_path}' が見つかりません。\n")
    sys.exit(1)

# 画像から緑色のピクセル数を計算
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_image, LOWER_GREEN, UPPER_GREEN)
green_pixel_count = np.count_nonzero(mask)

# 【重要】Railsが受け取れるように、計算結果の数値だけを出力する
print(green_pixel_count)