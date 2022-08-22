from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsageError(Exception):

    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.errorhandler(InvalidAPIUsageError)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code
