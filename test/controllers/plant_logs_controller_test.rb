require "test_helper"

class PlantLogsControllerTest < ActionDispatch::IntegrationTest
  test "should get new" do
    get plant_logs_new_url
    assert_response :success
  end

  test "should get create" do
    get plant_logs_create_url
    assert_response :success
  end

  test "should get index" do
    get plant_logs_index_url
    assert_response :success
  end
end
