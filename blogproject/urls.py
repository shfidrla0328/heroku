from django.urls import path, include
from django.contrib import admin
import blogapp.urls
import blogapp.views
import portfolio.views
import accounts.urls
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('portfolio/portfolio', portfolio.views.portfolio, name="portfolio"),
    path('blogapp/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)