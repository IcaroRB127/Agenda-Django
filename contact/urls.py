from django.urls import path
from contact import views

app_name= 'contact'

urlpatterns = [
    path('search/', views.contact_views.search, name='search'),
    path('', views.contact_views.index, name='index'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact_views.contact, name='contact'),
    path('contact/<int:contact_id>/update', views.contact_forms.update, name='update'),
    path('contact/<int:contact_id>/delete', views.contact_forms.delete, name='delete'),
    path('contact/create/', views.contact_forms.create, name='create'),

# user
    path('user/create/', views.user_forms.register, name='register'),
    path('user/login/', views.user_forms.login_view, name='login'),
    path('user/logout/', views.user_forms.logout_view, name='logout'),
    path('user/update/', views.user_forms.user_update, name='user_update'),
]