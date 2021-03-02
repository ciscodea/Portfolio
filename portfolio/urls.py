from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from portfolio import views as portfolio_views
from projects import views as projects_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', portfolio_views.index, name="home"),
    path('about/', portfolio_views.about, name="about-me"),
    path('contact/', portfolio_views.contact, name="contact"),
    path('projects/', projects_views.show_projects, name="projects"),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
