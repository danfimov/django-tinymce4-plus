from django.contrib import admin

from .models import TestChildModel, TestModel


class ChildInline(admin.StackedInline):
    model = TestChildModel
    extra = 1


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    inlines = [ChildInline]
