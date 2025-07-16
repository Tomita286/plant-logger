class DashboardController < ApplicationController
  def index
    @sensor_readings = SensorReading.all
  end
end
