import json
import sys
import time
from contextlib import contextmanager
from unittest import mock

import pytest
from selenium.webdriver import Chrome, ChromeOptions, Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse


try:
    from enchant import Broker
    enchant_imported = True
except ImportError:
    enchant_imported = False


@contextmanager
def log_browser_errors(browser):
    """
    Log errors caught by browser engine

    :param browser: Selenium browser
    """
    try:
        yield
    except Exception:
        print('*** Start browser log ***')
        print(browser.get_log('browser'))
        print('**** End browser log ****')
        raise


class TestSelenium(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSelenium, cls).setUpClass()
        print('Initializing browser engine...')
        if sys.platform == 'win32':
            # Chrome hangs up on Windows
            capabilities = DesiredCapabilities.FIREFOX
            capabilities['loggingPrefs'] = {'browser': 'ALL'}
            cls.browser = Firefox(capabilities=capabilities)
        else:
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            cls.browser = Chrome(options=options)
        print('Browser engine initialized.')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(TestSelenium, cls).tearDownClass()

    def tearDown(self):
        self.browser.delete_all_cookies()
        super(TestSelenium, self).tearDown()


@pytest.mark.skip('Selenium tests are not working')
class TestRenderTinyMceWidget(TestSelenium):
    def test_rendering_tinymce4_widget(self):
        # Test if TinyMCE 4 widget is actually rendered by JavaScript
        self.browser.get(self.live_server_url + reverse('create'))
        with log_browser_errors(self.browser):
            self.browser.find_element(By.ID, 'mceu_16')

    def test_rendering_in_different_languages(self):
        with self.settings(LANGUAGE_CODE='fr-fr'):
            self.browser.get(self.live_server_url + reverse('create'))
            with log_browser_errors(self.browser):
                self.browser.find_element(By.ID, 'mceu_16')
                self.assertTrue('Appuyer sur ALT-F9 pour le menu.' in self.browser.page_source)
        with self.settings(LANGUAGE_CODE='uk'):
            self.browser.refresh()
            with log_browser_errors(self.browser):
                self.browser.find_element(By.ID, 'mceu_16')
                self.assertTrue('Параграф' in self.browser.page_source)


@pytest.mark.skip('Selenium tests are not working')
class TestRenderTinyMceAdminWidget(TestSelenium):
    def setUp(self):
        User.objects.create_superuser('test', 'test@test.com', 'test')
        self.browser.get(self.live_server_url + '/admin')
        self.browser.find_element(By.ID, 'id_username').send_keys('test')
        self.browser.find_element(By.ID, 'id_password').send_keys('test')
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        time.sleep(0.2)
        super(TestRenderTinyMceAdminWidget, self).setUp()

    def test_rendering_tinymce4_admin_widget(self):
        self.browser.get(self.live_server_url + '/admin/test_tinymce/testmodel/add/')
        time.sleep(0.2)
        with log_browser_errors(self.browser):
            editors = self.browser.find_elements_by_class_name('mce-tinymce')
            self.assertEqual(len(editors), 2)

    def test_adding_tinymce_widget_in_admin_inline(self):
        self.browser.get(self.live_server_url + '/admin/test_tinymce/testmodel/add/')
        time.sleep(0.2)
        with log_browser_errors(self.browser):
            self.browser.find_element(By.CSS_SELECTOR, 'div.add-row a').click()
            editors = self.browser.find_elements(By.CLASS_NAME, 'mce-tinymce')
            self.assertEqual(len(editors), 3)
            self.browser.find_element(By.CSS_SELECTOR, 'a.inline-deletelink').click()
            editors = self.browser.find_elements(By.CLASS_NAME, 'mce-tinymce')
            self.assertEqual(len(editors), 2)
            self.browser.find_element(By.CSS_SELECTOR, 'div.add-row a').click()
            editors = self.browser.find_elements(By.CLASS_NAME, 'mce-tinymce')
            self.assertEqual(len(editors), 3)


class TestSpellCheckView(TestCase):
    @pytest.mark.skipif(not enchant_imported, reason='Enchant package is not installed')
    def test_spell_check(self):
        broker = Broker()
        languages = broker.list_languages()
        lang = 'en_US'
        if lang not in languages:
            lang = lang[:2]
            if lang not in languages:
                raise LookupError('Enchant package does not have English spellckecker dictionary!')
        text = 'The quick brown fox jumps over the lazy dog.'
        data = {'id': '0', 'params': {'lang': lang, 'text': text}}
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertTrue('result' in json.loads(response.content.decode('utf-8')))
        text = 'The quik brown fox jumps ower the lazy dog.'
        data['params']['text'] = text
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        result = json.loads(response.content.decode('utf-8'))['result']
        self.assertEqual(len(result), 2)

    def test_missing_dictionary(self):
        data = {'id': '0', 'params': {'lang': 'fo_BA', 'text': 'text'}}
        response = self.client.post(reverse('tinymce-spellchecker'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertTrue('error' in json.loads(response.content.decode('utf-8')))


class SpellCheckCallBackTestCase(TestCase):
    def test_spell_check_callback(self):
        response = self.client.get(reverse('tinymce-spellcheck-callback'))
        self.assertContains(response, reverse('tinymce-spellchecker'))
        self.assertIn('charset=utf-8', str(response.serialize_headers()))


class CssViewTestCase(TestCase):
    def test_css_view(self):
        response = self.client.get(reverse('tinymce-css'))
        self.assertContains(response, 'margin-left')
        self.assertIn('charset=utf-8', str(response.serialize_headers()))


class FileBrowserViewTestCase(TestCase):
    @mock.patch('tinymce.views.reverse')
    def test_filebrowser_view(self, mock_reverse):
        mock_reverse.return_value = '/filebrowser'
        response = self.client.get(reverse('tinymce-filebrowser'))
        self.assertContains(response, '/filebrowser')
        self.assertIn('charset=utf-8', str(response.serialize_headers()))
