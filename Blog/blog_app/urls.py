from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.register,name='signup'),
    path('captcha/', include("captcha.urls")),
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('usersearch/',views.usersearch,name="usersearch"),
    path('blog/postComment', views.postComment, name="postComment"),
    path('blogPost/<int:sno>', views.blogPost, name="blogPost"),
    path('logout/',views.logout,name="logout")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

