# Example project

The **tinymce4-plus** sources include **test_tinymce** project that can be used to run automated tests or to try a live TinyMCE 4 editor widget. The test project can also serve as a basic example of **tinymce4-plus** usage.

To use the test project, first you need to install the necessary dependencies:

```bash
uv install --all-extras
```

Then you need to create the test database:

```bash
python manage.py migrate
```

If you want to try TinyMCE in Django Admin, create a superuser to access the Admin interface:

```bash
python manage.py createsuperuser
```

To run automated tests, enter in the console:

```bash
pytest
```

Tests require web-browsers: Firefox on Windows and Chrome on other platforms. You also need to download respective Selenium drivers for your platform: [Gecko driver](https://github.com/mozilla/geckodriver/releases) or [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/). Set the necessary permissions for a driver executable and add the directory where it resides to your system `PATH` environment variable.

To open TinyMCE 4 editor, run the test server:

```bssh
python manage.py runserver
```

Then open the project's start page in your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000). The browser will open a webpage with a TinyMCE 4 editor.

//// note
The commands described in this section need to be run from the **tinymce4-plus** sources root directory.
////

The test project is very simple. It allows you to try rich text editing in TinyMCE 4 and then save the text and see how it looks on a web page.
