"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
