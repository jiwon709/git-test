from selenium import webdriver

import unittest


class FunctionalTest(unittest.TestCase):
    def setUp(self) :
        path = './chromedriver'
        # Django 8000 포트, html title Django 포함되어
        self.driver = webdriver.Chrome(path)

    def tearDown(self) :
        self.driver.quit()
        #알아서 창 닫아줌

    def test_has_worked_in_title(self):
        self.driver.get('http://localhost:8000')
        self.assertIn("worked", self.driver.title)


    def test_has_install_in_title(self):
        self.driver.get('http://localhost:8000')
        self.assertIn("install", self.driver.title)