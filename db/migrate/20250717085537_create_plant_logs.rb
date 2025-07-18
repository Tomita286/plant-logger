class CreatePlantLogs < ActiveRecord::Migration[8.0]
  def change
    create_table :plant_logs do |t|
      t.text :comment

      t.timestamps
    end
  end
end
