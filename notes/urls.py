from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import NoteViewSet, MyLoginView, MyLogoutView

router = SimpleRouter()
router.register(r'note', NoteViewSet)

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls
