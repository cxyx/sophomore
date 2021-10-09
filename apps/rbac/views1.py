from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers.jwt_serializers import MyTokenObtainPairSerializer
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from icecream import ic
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f'MyCustomBackend')
        ic(kwargs)
        try:
            # 用户名 & 邮件 & 手机号验证
            user = User.objects.get(Q(username=username) |
                                    Q(email=kwargs.get('email', None)) |
                                    Q(email=kwargs.get('mobile', None)))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
