import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-secret-key-for-test'
    # or configure under Flask Object: app.config['SECRET_KEY'] = 'you-will-never-guess'
    # for use of WTForms