from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet, EducationViewSet, ExperienceViewSet, SkillViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'user', UserViewSet, 'User')
router.register(r'education', EducationViewSet, 'Education')
router.register(r'experience', ExperienceViewSet, 'Experience')
router.register(r'skill', SkillViewSet, 'Skill')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('documentation', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]
