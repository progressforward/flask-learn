import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS=[
    {'name':'Yahoo', 'url': 'https://me.yahoo.com'}
]

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'gainforward@163.com'
MAIL_PASSWORD = 'hfs123'
FLASKY_MAIL_SUBJECT_PREFIX = '163.com'
FLASKY_MAIL_SENDER = 'gainforward@163.com'
ADMINS = ['progressforward@163.com']
