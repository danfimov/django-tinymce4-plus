# Configuration

## Application Configuration

The following options can be defined for `tinymce4-plus` in your Django project's `settings.py` file.

### `TINYMCE_DEFAULT_CONFIG`

TinyMCE 4 widget configuration. `tinymce4-plus` provides a reasonable default configuration with essential editing capabilities, so you need to use this option only if you want to create your own custom TinyMCE configuration.

//// note
In `tinymce4-plus` the TinyMCE configuration is defined as a Python `dict`. The `dict` configuration is then translated to JSON configuration according to `json.JSONEncoder` rules.
////

See [TinyMCE documentation](https://www.tinymce.com/docs/) for available configuration options.

Default configuration:

```python
DEFAULT = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code lists',
    'toolbar1': 'formatselect | bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'width': 'auto',
    'height': 360,
}
```

### `TINYMCE_SPELLCHECKER`

Enables spellchecker function for TinyMCE. For the default configuration, it also adds a spellcheck button to the TinyMCE toolbar. Default: `False`.

//// note
If you are using a custom TinyMCE configuration, don't forget to add the [spellchecker](https://www.tinymce.com/docs/plugins/spellchecker/) plugin to your configuration, and add the necessary menu item/toolbar button. Also read the [Language Configuration](#language-configuration) subsection about how to configure the spellchecker.
////

### `TINYMCE_FILEBROWSER`

Enables file browser support in TinyMCE image and link dialogs. `tinymce4-plus` supports [django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli) file browser. Default: `True` if `'filebrowser'` is added to [INSTALLED_APPS](https://docs.djangoproject.com/en/2.0/ref/settings/#installed-apps), else `False`.

### `TINYMCE_JS_URL`

A path to the TinyMCE JavaScript library. Default: `{your_static_url}/tinymce/js/tinymce/tinymce.min.js`. The following example shows how to load the TinyMCE library from a CDN:

```python
TINYMCE_JS_URL = '//cdn.tinymce.com/4/tinymce.min.js'
```

### `TINYMCE_ADDITIONAL_JS_URLS`

A `list` of URLs for additional JavaScript files to be used with the TinyMCE widget, for example, custom TinyMCE plugins. Default: `None`.

### `TINYMCE_CSS_URL`

A path to a CSS file with additional styles for TinyMCE. Unlike `content_style` and `content_css` TinyMCE settings (see [Applying custom CSS](advanced.md#applying-custom-css)), this CSS is applied to the TinyMCE widget itself, for example, to correct the widget position on a page. Default: `None`.

### `TINYMCE_CALLBACKS`

Allows defining custom TinyMCE callbacks, for example, `file_browser_callback` or `spellchecker_callback`. This is a Python `dict` where keys are the names of callbacks and values are JavaScript objects as Python strings. Default: `{}` (an empty `dict`). Read [TinyMCE documentation](https://www.tinymce.com/docs/) to learn about available callbacks.

> **Note:** Custom `file_browser_callback` and `spellchecker_callback` options defined in `TINYMCE_CALLBACKS` override `tinymce4-plus` built-in callbacks.

## Language Configuration

By default, `tinymce4-plus` sets TinyMCE interface language and writing directionality depending on the current Django language. However, to correctly select a TinyMCE 4 translation file, the Django language code must match the name of the TinyMCE translation file. Supported combinations:

- `ll` (Django) => `ll.js` (TinyMCE)
- `ll-cc` (Django) => `ll_CC.js` (TinyMCE)
- `ll-cc` (Django) => `ll.js` (TinyMCE)

The `ll` (Django) => `ll_CC.js` (TinyMCE) is not supported because TinyMCE may have several country-specific variants of translation files. In this case, you can manually rename the necessary TinyMCE translation file to match your Django language code.

The `LANGUAGES` option defines the list of available spellchecker languages. The first language in this list is used as the default one. The list of spellchecker languages also depends on available **pyenchant** dictionaries. For example, on Windows, the default **pyenchant** installation includes only English, German, and French spellchecker dictionaries. You can view the list of available spellchecker dictionaries by running the `enchant.list_languages()` function in a console from your working Python environment. For example:

```python
>>> import enchant
>>> enchant.list_languages()
['de_DE', 'en_AU', 'en_GB', 'en_US', 'fr_FR']
```

On Linux, you can install [Hunspell](http://hunspell.github.io) dictionaries for your languages that will be automatically used by **pyenchant**. E.g. for the Ukrainian spelling dictionary on Ubuntu/Debian:

```bash
sudo apt install hunspell-uk
```

On Windows, you need to add the necessary dictionaries manually to the **enchant** package in the `site-packages` directory of your working Python environment. Additional spellchecker dictionaries can be downloaded from [this page](http://www.softmaker.com/en/download/dictionaries). Unpack a `.sox` file using an archive manager, for example, [7zip](http://www.7-zip.org/), and copy `.dic` and `.aff` for your language to `enchant/share/enchant/myspell/` directory inside the **enchant** package.

//// note
Django language codes in `LANGUAGES` must match dictionary filenames. For example, `'en-us'` in `LANGUAGES` (with a country code) corresponds to `en_US.dic`/`en_US.aff` dictionary files, and `'uk'` (no country code) corresponds to `uk.dic`/`uk.aff` dictionary files.
////

Also, you can completely override TinyMCE automatic language configuration by defining the necessary language options in `TINYMCE_DEFAULT_CONFIG`.
