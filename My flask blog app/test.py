from learn import app 
from learn import db  
from learn.models import User, Post
app_ctx = app.app_context()
app_ctx.push()

''' with app.app_context():
   #user_1=User(username='Corey',email='C@demo.com',password='password')
    #user_2=User(username='John Doe',email='jd@demo.com',password='password')
    #db.session.add(user_1)
    #db.session.add(user_2)
    #db.session.commit() 

print(User.query.all())
print(User.query.first())
user=User.query.filter_by(username='Corey').first()
print(user.id)
user = User.query.get(1)
print(user)
print(user.posts)
with app.app_context():
    post_1=Post(title='Blog_1', content='First Post content!', user_id=user.id)
    post_2=Post(title='Blog_2', content='Second Post content!', user_id=user.id)
    db.session.add(post_1)
    db.session.add(post_2)
    db.session.commit()

print(user.posts)
for post in user.posts:
    print(post.title)

post=Post.query.first()
print(post.user_id)
print(post.author)
db.drop_all()'''
user=User.query.all()
print(user)

app_ctx.pop() 

from itsdangerous import URLSafeTimedSerializer as Serializer
S=Serializer('secret', 30)