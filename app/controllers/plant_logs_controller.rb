class PlantLogsController < ApplicationController
  # edit, update, destroy アクションの前に @plant_log をセットする
  before_action :set_plant_log, only: [:edit, :update, :destroy]

  def index
    @plant_logs = PlantLog.all.order(created_at: :desc)
  end

  def new
    @plant_log = PlantLog.new
  end

  def create
    @plant_log = PlantLog.new(plant_log_params)
    if @plant_log.save
      # ↓↓↓↓ ここから画像分析の処理を追加 ↓↓↓↓

      # 1. アップロードされた画像を一時ファイルとして保存
      image_path = ActiveStorage::Blob.service.path_for(@plant_log.image.key)

      # 2. Pythonスクリプトを呼び出すコマンドを組み立てる
      # NOTE: Pythonの仮想環境を直接指定するのが確実
      python_executable = Rails.root.join('image-analysis-py', 'venv', 'bin', 'python')
      script_path = Rails.root.join('image-analysis-py', 'analyze.py')
      command = "#{python_executable} #{script_path} #{image_path}"

      # 3. コマンドを実行し、結果（ピクセル数）を取得する
      pixel_count_str = `#{command}`

      # 4. 結果をデータベースに保存する
      # stripで改行などを除去し、to_iで整数に変換
      @plant_log.update(green_pixel_count: pixel_count_str.strip.to_i)

      # ↑↑↑↑ ここまで追加 ↑↑↑↑

      redirect_to plant_logs_path, notice: "生育記録を登録し、画像分析を実行しました。" # ← 正しいメッセージ
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
    # before_actionで@plant_logがセットされるので、この中は空でOK
  end

  def update
    if @plant_log.update(plant_log_params)
      redirect_to plant_logs_path, notice: "生育記録を更新しました。"
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @plant_log.destroy
    redirect_to plant_logs_path, notice: "生育記録を削除しました。", status: :see_other
  end

  private

  def set_plant_log
    @plant_log = PlantLog.find(params[:id])
  end

  def plant_log_params
    params.require(:plant_log).permit(:comment, :image)
  end
end