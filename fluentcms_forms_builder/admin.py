# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.forms import ModelForm, SlugField

from forms_builder.forms.admin import (
    FieldAdmin as AbstractFieldAdmin, FormAdmin as AbstractFormAdmin)

from .models import Form, FormEntry, Field, FieldEntry


if 'forms_builder.forms' in settings.INSTALLED_APPS:
    from forms_builder.forms import models as forms

    try:
        admin.site.unregister(forms.Form)
    except NotRegistered:
        pass


class FieldInlineForm(ModelForm):
    slug = SlugField(required=True)

    class Meta:
        model = Field
        fields = '__all__'


class FieldAdmin(admin.TabularInline):
    model = Field
    form = FieldInlineForm


class FormAdmin(AbstractFormAdmin):
    formentry_model = FormEntry
    fieldentry_model = FieldEntry
    inlines = (FieldAdmin,)
    view_on_site = False

    fieldsets = [
        (None, {
            "fields": (
                "title", "intro", "button_text", "response", "redirect_url",
            ),
        })] + AbstractFormAdmin.fieldsets[1:]

admin.site.register(Form, FormAdmin)
