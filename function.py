from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 创建模型使用


def get_db(DATABASE):
    user = DATABASE.get('USER')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, name)


def init_ext(app):
    db.init_app(app=app)
