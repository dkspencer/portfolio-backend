from django.http import HttpResponse
from django.utils.decorators import method_decorator
from drf_spectacular.utils import OpenApiResponse as OpenAPI
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .models import CustomUser, Education, Experience, Skill
from .serializers import (EducationSerializer, ExperienceSerializer,
                          SkillSerializer, UserSerializer)
from portfolio.code.utils.exceptions import ExceptionSerializer


@method_decorator(
    name='list',
    decorator=extend_schema(
        operation_id='List Users',
        tags=['User'],
        responses={'200': OpenAPI(response=UserSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
@method_decorator(
    name='retrieve',
    decorator=extend_schema(
        operation_id='Retrieve User',
        tags=['User'],
        responses={'200': OpenAPI(response=UserSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
class UserViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self) -> HttpResponse:
        return CustomUser.objects.filter(id=self.request.user.id)


@method_decorator(
    name='list',
    decorator=extend_schema(
        operation_id='List Education',
        tags=['Education'],
        responses={'200': OpenAPI(response=EducationSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
@method_decorator(
    name='retrieve',
    decorator=extend_schema(
        operation_id='Retrieve Education',
        tags=['Education'],
        responses={'200': OpenAPI(response=EducationSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
class EducationViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    serializer_class = EducationSerializer
    http_method_names = ['get']

    def get_queryset(self) -> HttpResponse:
        return Education.objects.filter(user=self.request.user.id).order_by('-start_date')


@method_decorator(
    name='list',
    decorator=extend_schema(
        operation_id='List Experience',
        tags=['Experience'],
        responses={'200': OpenAPI(response=ExperienceSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
@method_decorator(
    name='retrieve',
    decorator=extend_schema(
        operation_id='Retrieve Experience',
        tags=['Experience'],
        responses={'200': OpenAPI(response=ExperienceSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
class ExperienceViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    serializer_class = ExperienceSerializer
    http_method_names = ['get']

    def get_queryset(self) -> HttpResponse:
        return Experience.objects.filter(user=self.request.user.id).order_by('-start_date')


@method_decorator(
    name='list',
    decorator=extend_schema(
        operation_id='List Skills',
        tags=['Skill'],
        responses={'200': OpenAPI(response=SkillSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
@method_decorator(
    name='retrieve',
    decorator=extend_schema(
        operation_id='Retrieve Skills',
        tags=['Skill'],
        responses={'200': OpenAPI(response=SkillSerializer,
                                  description='Request successful'),
                   '401': OpenAPI(response=ExceptionSerializer,
                                  description='Unauthorized access, invalid '
                                  'api key provided')}))
class SkillViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    serializer_class = SkillSerializer
    http_method_names = ['get']

    def get_queryset(self) -> HttpResponse:
        return Skill.objects.filter(user=self.request.user.id).order_by('id')
