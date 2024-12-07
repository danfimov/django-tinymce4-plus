from django import VERSION


if VERSION < (4, 0):
    from django.conf.urls import url
else:
    from django.urls import re_path as url

from tinymce.views import css, filebrowser, spell_check, spell_check_callback


urlpatterns = [
    url(r'^spellchecker/$', spell_check, name='tinymce-spellchecker'),
    url(r'^filebrowser/$', filebrowser, name='tinymce-filebrowser'),
    url(r'^tinymce4.css', css, name='tinymce-css'),
    url(r'^spellcheck-callback.js', spell_check_callback, name='tinymce-spellcheck-callback')
]
