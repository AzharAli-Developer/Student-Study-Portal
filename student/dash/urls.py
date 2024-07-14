from django.urls import path
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_view
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='dash/login.html',
                                                         authentication_form=AuthenticationForm), name='login'),
    path('book', views.book,name='book'),
    path('conversion', views.conversion,name='conversion'),
    path('dictionary', views.dictionary,name='dictionary'),
    path('homework', views.homework,name='homework'),
    path('update_work/<int:pk>', views.update_work,name='update_work'),
    path('delete_work/<int:pk>', views.delete_work,name='delete_work'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('notes', views.notes,name='notes'),
    path('notesdetails/<int:pk>', views.notes_details,name='notesdetails'),
    path('notesdelete/<int:pk>', views.notes_delete,name='notesdelete'),
    path('profile/', views.profile,name='profile'),
    path('register', views.register,name='register'),
    path('todo', views.todo,name='todo'),
    path('tododelete/<int:pk>', views.todo_delete,name='tododelete'),
    path('update_todo/<int:pk>', views.update_todo,name='update_todo'),
    path('wiki', views.wiki,name='wiki'),
    path('youtube', views.youtube,name='youtube'),


]