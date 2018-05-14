# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash, redirect, url_for, make_response, request
from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    user = wtforms.StringField(u'用户名', validators=[DataRequired('用户名不能为空')])
    password = wtforms.PasswordField(u'密码', validators=[DataRequired()])
    submit = wtforms.SubmitField(u'提交')


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.cookies.get('user'):
        return redirect(url_for('user_page'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.user.data == 'zqy' and form.password.data == 'zqy':
            res = make_response(redirect(url_for('user_page')))
            res.set_cookie('user', form.user.data)
            return res
        else:
            flash('用户名或密码错误', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='登录')


@app.route('/user_page')
def user_page():
    user = request.cookies.get('user')
    if not user:
        flash('请先登录', 'danger')
        return redirect(url_for('login'))
    return render_template('user_page.html', title='欢迎回来', user=request.cookies.get('user'))


@app.route('/logout')
def logout():
    res = make_response(redirect(url_for('login')))
    res.set_cookie('user', '')
    return res


if __name__ == '__main__':
    app.run(debug=True)
