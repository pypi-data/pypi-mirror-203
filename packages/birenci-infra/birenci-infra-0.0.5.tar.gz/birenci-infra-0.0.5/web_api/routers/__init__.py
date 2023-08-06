from flask import Flask

from . import build, perf, component, pull_request, pull_request_job, test_case


def register_router(app: Flask):
    app.register_blueprint(perf.router)
    app.register_blueprint(build.router)
    app.register_blueprint(pull_request.router)
    app.register_blueprint(pull_request_job.router)
    app.register_blueprint(component.router)
    app.register_blueprint(test_case.router)
