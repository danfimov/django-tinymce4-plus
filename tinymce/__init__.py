"""
django-tinymce4-plus
--------------------

This application provides a rich-text WYSIWYG `TinyMCE 4`_ widget
for Django forms and models.

.. _TinyMCE 4: https://www.tinymce.com/
"""

from __future__ import absolute_import

from tinymce.models import HTMLField
from tinymce.widgets import AdminTinyMCE, TinyMCE


__all__ = ['HTMLField', 'TinyMCE', 'AdminTinyMCE']
