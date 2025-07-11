class Api::SensorReadingsController < ApplicationController
  # APIでは不要な、Railsのセキュリティ機能を無効化します
  skip_before_action :verify_authenticity_token

  def create
    # 受け取ったデータを使って、新しいSensorReadingオブジェクトを作成
    @sensor_reading = SensorReading.new(sensor_reading_params)

    # データベースへの保存を試みる
    if @sensor_reading.save
      # 保存が成功した場合
      render json: { status: 'success', data: @sensor_reading }, status: :created
    else
      # 保存が失敗した場合
      render json: { status: 'error', errors: @sensor_reading.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  # 受け取るパラメータを安全に設定するためのメソッド
  def sensor_reading_params
    params.require(:sensor_reading).permit(
      :temperature,
      :humidity,
      :pressure,
      :water_temperature,
      :flow_rate,
      :tds,
      :light_intensity
    )
  end
end