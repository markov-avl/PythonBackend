from flask import Blueprint, request, session, redirect, render_template, url_for, flash

from final.controller.flash_category import FlashCategory
from final.controller.method import Method
from final.controller.security.login_form import LoginForm
from final.controller.security.register_form import RegisterForm
from final.model import UserService
from final.model.entity import User
from final.model.role import Role

blueprint = Blueprint('security', __name__)
user_service = UserService()


@blueprint.route('/login', methods=[Method.GET, Method.POST])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        if user := user_service.get_by_identifier_and_password(form.identifier.data, form.password.data):
            save_session(user)
            return redirect(request.values.get('redirect', url_for('index.index')))
        flash('Неверный логин или пароль', FlashCategory.WARNING)

    return render_template('page/login.jinja2', form=form)


@blueprint.route('/register', methods=[Method.GET, Method.POST])
def register():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        try:
            user = user_service.create(
                form.login.data,
                form.password.data,
                form.phone.data,
                form.name.data,
                form.surname.data,
                form.patronymic.data
            )
            save_session(user)
            return redirect(request.values.get('redirect', url_for('index.index')))
        except ValueError as e:
            flash(str(e), FlashCategory.WARNING)

    return render_template('page/register.jinja2', form=form)


@blueprint.route('/logout', methods=[Method.GET])
def logout():
    delete_session()
    return redirect(request.values.get('redirect', url_for('index.index')))


def save_session(user: User) -> None:
    session['id'] = user.id
    session['login'] = user.login
    session['full_name'] = user.full_name
    session['is_admin'] = user.role is Role.ADMIN


def delete_session() -> None:
    session.pop('id', None)
    session.pop('login', None)
    session.pop('full_name', None)
    session.pop('is_admin', None)
