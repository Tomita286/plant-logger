Rails.application.routes.draw do
  # /dashboard/index というURLでグラフページを表示
  get "dashboard/index"

  # 生育記録用のページ
  resources :plant_logs, only: [:index, :new, :create]

  # トップページ('/')にアクセスしたら、生育記録一覧を表示
  root "plant_logs#index"

  # API用の設定
  namespace :api do
    resources :sensor_readings, only: [:create]
  end
end
