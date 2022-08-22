from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('kakao/login/', views.KakaoLoginView.as_view(), name="kakaologin"),
    path('kakao/signup/',views.login_api, name="signup"),
    path('kakao/login/callback/', views.KakaoCallbackView.as_view()),
]