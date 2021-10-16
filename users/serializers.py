from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Education, Experience, Profile, Project, Skill, CustomUser, Link

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        exclude = []
        ref_name = None


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        exclude = ['user']
        ref_name = None


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        exclude = ['user']
        ref_name = None


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        exclude = []
        ref_name = None


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        exclude = ['id', 'user']
        ref_name = None


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        ref_name = None


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(help_text='User personal information')
    links = LinkSerializer(many=True, help_text='User links')

    class Meta:
        model = CustomUser
        fields = ['profile', 'id', 'links']
        ref_name = None
