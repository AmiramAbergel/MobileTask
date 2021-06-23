def index_router(app):
    @app.route('/')
    def hello_world() -> str:
        return 'hello'
