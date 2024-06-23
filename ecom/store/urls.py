from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('about/', views.about, name="about" ),
    path('login/',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerUser, name="register"),
    path('update-user/',views.updateUser, name="updateUser"),
    path('update-info/',views.updateInfo, name="updateInfo"),
    path('update-password/',views.updatePassword, name="updatePassword"),
    path('product/<int:pk>',views.product, name="product"),
    path('category/<str:categorySearch>',views.category, name="category"),
    path('category-summary/',views.categorySummary, name="categorySummary"),
    path('search/',views.search, name="search"),
]