# from django.conf.urls import url
# from django.urls import path

# from . import views


# app_name="account"
# urlpatterns = [
#     path("", views.TopView.as_view(), name="top"),
#     path("home/", views.HomeView.as_view(), name="home"),
#     path("login/", views.LoginView.as_view(), name="login"),
#     path("logout/", views.LogoutView.as_view(), name="logout"),
#     path('your-url-pattern/', views.your_view_function, name='your-url-name'),
# ]

from django.urls import path
from .views import(
    TopView, HomeView, LoginView, LogoutView, SignUpView,
    CalendarView, ShopListView, search_view, get_event_data, add_event# get_event_data をインポートする
)

app_name="account"

from . import views

urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('shop_list/', views.ShopListView.as_view(), name='shop_list'),
    path('search/', views.search_view, name='search'),  # search の URL パターンを追加
    path('get-event-data/<date>/', views.get_event_data, name='get_event_data'),
    path('add-event/', views.add_event, name='add_event'),
       # ...他にも必要なURLパターンがあれば追加...
]  


