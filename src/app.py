import logging
from controllers.config_routes import router
from controllers.config_index_route import index_router
from dal.init_data import InitData


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask
        # Create app
        app = Flask(__name__)
        """
        Routes
        """
        index_router(app)
        router(app)
        """
        Initialize DB
        """
        InitData().init_patients_data()
        InitData().init_doctors_data()

        return app
    except Exception:
        logger.exception(f"Error starting flask App")
        raise
