class CreateSensorReadings < ActiveRecord::Migration[8.0]
  def change
    create_table :sensor_readings do |t|
      t.float :temperature
      t.float :humidity
      t.float :pressure
      t.float :water_temperature
      t.float :flow_rate
      t.float :tds
      t.integer :light_intensity

      t.timestamps
    end
  end
end
