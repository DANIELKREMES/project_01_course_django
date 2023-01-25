from recipes.views import home, about , exit_ , user
from django.urls import path

urlpatterns = [
    # path('about/', my_views),
    # path('home/', my_client),
    # path("logout/", exit),
    path('', home),
    path("about/", about),
    path("exit/", exit_),
    path("user/", user),
]

