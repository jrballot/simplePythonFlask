

from flask import redirect , render_template, request, session, flash, url_for, Blueprint
from .forms import LoginForm, RegisterForm

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route('/', methods=('GET','POST'))
def login():
    error = None
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form['name'])
            print(request.form['password'])

            if request.form['name'] == "julio" and request.form['password'] == 'qwe123qwe':
                flash('Bem vindo ao Painel de Cursos!!!')
                return redirect(url_for('courses.courses'))
            else:
                error = "Usuário ou senha errada!!!"

    return render_template('login.html', form=form, error=error)