class PlantLogsController < ApplicationController
  def new
    @plant_log = PlantLog.new
  end

  def create
    @plant_log = PlantLog.new(plant_log_params)
    if @plant_log.save
      redirect_to plant_logs_path, notice: "生育記録を登録しました。"
    else
      render :new, status: :unprocessable_entity
    end
  end

  def index
    @plant_logs = PlantLog.all.order(created_at: :desc)
  end

  private

  def plant_log_params
    params.require(:plant_log).permit(:comment, :image)
  end
end