from flask_app_1 import db, app

with app.app_context():
    db.create_all()
