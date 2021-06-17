

def router(app):
    @app.route('/login/', methods=['GET', 'POST'])
    def login() -> str:
        return