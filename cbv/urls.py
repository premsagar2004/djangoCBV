from django.urls import path
from . import views
from .views import GeeksUpdateView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',views.blog,name='blog'),
    path('<pk>/update/',GeeksUpdateView.as_view()),
]
