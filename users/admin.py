from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Education, Experience, Profile, Skill, Project, Link
from rest_framework.authtoken.models import Token

admin.site.unregister(Group)


class TokenInline(admin.StackedInline):
    model = Token
    can_delete = False
    verbose_name_plural = 'Token'
    fk_name = 'user'
    extra = 0


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    extra = 0


class LinkInline(admin.StackedInline):
    model = Link
    can_delete = True
    verbose_name_plural = 'Link'
    fk_name = 'user'
    extra = 0


class CustomUserAdmin(UserAdmin):

    inlines = (ProfileInline, TokenInline, LinkInline)

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')

    list_filter = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company',
                    'country', 'start_date', 'end_date')

    list_filter = ['title', 'company']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'confidence')

    list_filter = ['name', 'confidence']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'university',
                    'country', 'start_date', 'end_date')

    list_filter = ['degree', 'university']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

    list_filter = ['description']


admin.site.register(CustomUser, CustomUserAdmin)
