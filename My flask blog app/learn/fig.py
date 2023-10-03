from per import secret
class Config():
     SECRET_KEY='abddb3bc3ba8144ceb167070e023166b'
     SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
     MAIL_SERVER= 'smtp.googlemail.com'
     MAIL_PORT= 587
     MAIL_USE_TLS = True 
     MAIL_USERNAME= 'michael.n.ezeana@gmail.com'
     MAIL_PASSWORD= secret


     