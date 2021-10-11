from django.urls import path
from . import views

app_name = 'managementapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInpView.as_view(), name='signin'),
    path('signout/', views.SignOut, name='signout'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.UpdateTodoView.as_view(), name='update'),
    path('todo/create/', views.CreateView.as_view(), name='createtodo'),
    path('<int:pk>/delete/', views.Delete, name='delete'),
    path('<int:pk>/checked/', views.Checked, name='checked'),
    path('<int:pk>/done/', views.Done, name='done'),
    path('<int:pk>/undone/', views.UnDone, name='undone'),
]