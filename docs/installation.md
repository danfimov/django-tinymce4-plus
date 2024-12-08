# Installation

## Basic installation and configuration

Install `django-tinymce4-plus` from PyPI:

```bash
pip install django-tinymce4-plus
```

Add `tinymce` to `INSTALLED_APPS` in `settings.py` for your Django project:

```python
INSTALLED_APPS = (
    ...
    'tinymce',
)
```

Add `tinymce.urls` to `urls.py` for your project:

```python
urlpatterns = [
    ...
    path('tinymce/', include('tinymce.urls')),
    ...
]
```

Or with old-style regex `url`:

```python
urlpatterns = [
    ...
    url(r'^tinymce/', include('tinymce.urls')),
    ...
]
```

## Plugins

If you want to use [django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli) file manager, install this package. Refer to [django-filebrowser documentation](https://github.com/sehmaschine/django-filebrowser) to learn how to install and configure the filebrowser application.

For TinyMCE spellchecker plugin, you need to install the [pyenchant](https://pythonhosted.org/pyenchant/) extra package:

```bash
pip install django-tinymce4-plus[enchant]
```

or just 

```bash
pip install pyenchant
```

On some Linux systems, you may also need to install binary `enchant` libraries prior to installing `pyenchant`. For example, on Debian/Ubuntu use the following command:

```bash
sudo apt-get install enchant
```

Also, you need to add the necessary spelling dictionaries if they are missing from `pyenchant` default installation on your system.

Read the [Language Configuration](configuration.md#language-configuration) subsection about configuring the `tinymce4-plus` spellchecker.

## Upgrade

It is strongly recommended to upgrade `tinymce4-plus` by specifying the exact application version you want to upgrade to:

```bash
pip install django-tinymce4-plus==X.Y.Z
```

Unless you are loading TinyMCE 4 from a CDN, after upgrading you need to run Django's `collectstatic` command to update TinyMCE 4 static files in your folder where your project's static files are served from:

```bash
python3 manage.py collectstatic
```
