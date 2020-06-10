import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  #need to be set in bashrc
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  #need to be set in bashrc
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  #need to be set in bashrc
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')  #need to be set in bashrc

#after setting in bashrc, you might need to restart your terminal/system for bshrc to run again or you can run it again manually or you can export these variables in shell manually
