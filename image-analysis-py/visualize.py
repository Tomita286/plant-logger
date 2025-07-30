import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "growth_log.csv"
CHART_OUTPUT_PATH = "growth_chart.png"

try:
    # CSVファイルを読み込む
    df = pd.read_csv(CSV_PATH)

    # タイムスタンプを日時の形式に変換
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # グラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['green_pixel_count'], marker='o', linestyle='-')
    
    # グラフの装飾
    plt.title('Green Pixel Count Over Time')
    plt.xlabel('Date and Time')
    plt.ylabel('Green Pixel Count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # グラフを画像として保存
    plt.savefig(CHART_OUTPUT_PATH)
    print(f"グラフを '{CHART_OUTPUT_PATH}' に保存しました。")

except FileNotFoundError:
    print(f"エラー: CSVファイル '{CSV_PATH}' が見つかりません。")
except Exception as e:
    print(f"エラーが発生しました: {e}")