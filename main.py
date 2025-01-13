from flask import Flask, request,make_response, redirect,render_template,session,url_for,flash
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)


@app.route('/')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect('/home'))
    
    session['user_ip'] = user_ip_information
    return response

@app.route("/home")
def home():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    context = {
            "user_ip": user_ip,
            "username":username,
            }
    return render_template('home.html',**context)

@app.route('/projects')
def projects():
    user_ip = request.cookies.get("user_ip_information")
    username = session.get("username")
    context = {
            "user_ip": user_ip,
            "username":username,
            }
    return render_template('projects.html',**context)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)
