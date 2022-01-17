from django.contrib import admin
from .models import *


# Home
admin.site.register(Home)


# About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]


# Skills
class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine,
    ]


# Portfolio
admin.site.register(Portfolio)
