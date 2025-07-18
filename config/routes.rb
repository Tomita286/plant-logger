Rails.application.routes.draw do
  get "plant_logs/new"
  get "plant_logs/create"
  get "plant_logs/index"
  get "dashboard/index"
    # ↓↓↓↓ この一行を追加します ↓↓↓↓
  resources :plant_logs, only: [:index, :new, :create]
  # ↑↑↑↑ この一行を追加します ↑↑↑↑

  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Render dynamic PWA files from app/views/pwa/* (remember to link manifest in application.html.erb)
  # get "manifest" => "rails/pwa#manifest", as: :pwa_manifest
  # get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker

  # Defines the root path route ("/")
  # root "posts#index"
  # ↓↓↓↓ ここから追記 ↓↓↓↓
  namespace :api do
    resources :sensor_readings, only: [:create]
  end
end
