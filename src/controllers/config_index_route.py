from flask import request, redirect, url_for, render_template


def index_router(app):
    @app.route('/')
    def hello_world() -> str:
        return 'Hello World!'

    @app.route('/login/', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('home'))
        return render_template('login.html', error=error)

