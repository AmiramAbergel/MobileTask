

def router(app):
    @app.route('/login/', methods=['GET', 'POST'])
    def login() -> None:
        return

    @app.route('/doctors/', methods=['GET', 'POST'])
    def get_all_doctors() -> None:
        return

    @app.route('/doctors/available', methods=['GET', 'POST'])
    def get_available_doctors() -> None:
        return

    @app.route('/appointments/add', methods=['GET', 'POST'])
    def add_appointment() -> None:
        return

