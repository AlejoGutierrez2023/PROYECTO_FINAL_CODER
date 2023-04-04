from django.urls import path
from App_Accounts import views
from django.contrib.auth.views import LogoutView
urlpatterns = [


path('', views.base, name='base'),
path('signup/', views.signup, name='signup'),
path('login/', views.user_login, name='login'),
path('logout/', LogoutView.as_view(template_name='App_Accounts/logout.html'), name='logout'),
path('profile/', views.profile_view, name='profile'),
path('profile/edit/<int:pk>/', views.edit_profile_view, name='profile_edit'),
path('profile/delete/<int:pk>/', views.delete_profile_view, name='profile_delete')
]



