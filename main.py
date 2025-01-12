from flask import Flask, request,make_response, redirect,render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']= 'nox'

items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']


class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario",validators=[DataRequired()])
    password = PasswordField("Contraseña",validators=[DataRequired()])
    submit = SubmitField("Enviar datos",validators=[DataRequired()])

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html',error=error)


@app.route('/')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect('/home'))
    
    session['user_ip'] = user_ip_information
    return response

@app.route("/home",methods=["GET","POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    login_form = LoginForm()
    context = {
            "user_ip": user_ip,
            "items":items,
            "login_form":login_form,
            "username":username,
            }
    if login_form.validate_on_submit():
        username=login_form.username.data
        session["username"] = username
        flash('Nombre de usuario registrado correctamente')
        return redirect(url_for('index'))
    return render_template("home.html", **context)

@app.route('/projects')
def projects():
    user_ip = request.cookies.get("user_ip_information")
    context = {
            "user_ip": user_ip,
            }
    return render_template('projects.html',**context)
app.run(host='0.0.0.0',port=3000,debug=True)
