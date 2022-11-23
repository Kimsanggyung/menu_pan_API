from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MenuList, MenuDetail
from .views import SignupAPI, LoginAPI, LogoutAPI

urlpatterns = [
  path('menu/', MenuList.as_view()),
  path('menu/<int:pk>', MenuDetail.as_view()),
  path('signup/', SignupAPI.as_view()),
  path('login/', LoginAPI.as_view()),
  path('logout/', LogoutAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)