from flask_testing import TestCase
from flask import current_app,url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLE"] = False
        return app
    
    def test_app_exists_web(self):
        self.assertIsNotNone(current_app)

    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_show_information_get(self):
        response = self.client.get(url_for('home'))
        self.assert_200(response)

    def test_home_post(self):
        response = self.client.post(url_for('home'))
        self.assert405(response)
    def test_auth_blueprint_exist_module(self):
        self.assertIn("auth",self.app.blueprints)

    def test_auth_blueprint_login_get(self):
        response = self.client.get(url_for("auth.login"))
        self.assert200(response)

    def test_auth_blueprint_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_blueprint_login_post(self):
        test_form_fake = {
                "username":"test",
                "password":"123",
                }
        response = self.client.post(url_for("auth.login"),data=test_form_fake)
