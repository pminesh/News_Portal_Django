from django.urls import path,include
from DailyNews import views
from django.contrib.auth import views as auth_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register('news',views.news_list)

urlpatterns = [
    path('',views.index,name='index'),

    #restframework
    path('rest/',include(router.urls)),

    #dailynews
    path('contact/',views.contact,name='contact'),
    path('comment/<int:id>/',views.comment,name='comment'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('allnews/',views.allnews,name='allnews'),
    path('user_login/',views.login,name='login'),   
    path('logoutform/',views.logoutform,name='logoutform'),    
    path('user_register/',views.register,name='register'), 
    path('contactus/',views.contactus,name='contactus'), 
    path('category_news/<int:id>/',views.category_news,name='category_news'),
    path('view_more/<int:id>/',views.view_more,name='view_more'),

    #Password Reset
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]