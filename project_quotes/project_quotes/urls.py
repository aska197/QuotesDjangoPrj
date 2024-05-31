from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import signup, profile  # Change user_page to profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('users/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', success_url='/user_page/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),  # Change user_page to profile
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
