from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('kakao/login/', views.KakaoLoginView.as_view(), name="kakaologin"),
    path('kakao/signup/',views.login_api, name="signup"),
    path('kakao/login/callback/', views.KakaoCallbackloginView.as_view()),
]