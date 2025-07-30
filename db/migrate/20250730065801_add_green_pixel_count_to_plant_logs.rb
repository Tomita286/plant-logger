class AddGreenPixelCountToPlantLogs < ActiveRecord::Migration[8.0]
  def change
    add_column :plant_logs, :green_pixel_count, :integer
  end
end
