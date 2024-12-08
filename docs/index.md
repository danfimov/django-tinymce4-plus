# General

`django-tinymce4-plus` is a reworked fork of [django-tinymce4](https://github.com/dani0805/django-tinymce4). It provides a [TinyMCE 4](https://www.tinymce.com/) editor widget that can be used in Django forms and models.

![TinyMCE 4 in Django Admin](_static/screenshot.png)

*TinyMCE 4 editor in Django Admin interface*

In this fork, all legacy and broken code has been cleaned in order to provide a simple but full-featured TinyMCE 4 experience in Django projects.

`django-tinymce4-plus` can use [django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli) as a file manager for TinyMCE 4 to insert images and file links into edited text.

//// note
Currently `django-filebrowser` (grapelli-based) is not compatible with `django-tinymce4-plus` because it lacks support for TinyMCE 4. See this [pull request](https://github.com/sehmaschine/django-filebrowser/pull/255) for more details.
////

The application also includes a spellchecker service for the TinyMCE 4 spellchecker plugin.

## Compatibility

- **Python**: 3.8 - 3.11
- **Django**: all LTS versions (1.11.29, 2.2.28, 3.2.25, 4.2.17)


## Naming Conventions

In this documentation `django-tinymce4-plus` or `tinymce4-plus` (all lowercase) refers to this Python/Django application, and **TinyMCE 4** or **TinyMCE** (CamelCase) refers to a JavaScript [TinyMCE](https://www.tinymce.com/) editor widget. If a version number is omitted, TinyMCE v.4.x.x is assumed.

## License

- `django-tinymce4-plus` software: [MIT license](https://en.wikipedia.org/wiki/MIT_License).
- This documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).