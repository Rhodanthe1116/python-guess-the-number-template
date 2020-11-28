from flask import Flask, render_template, request, redirect, url_for
from replit import db
from datetime import datetime, timezone, timedelta
import random

tz = timezone(timedelta(hours=+8))

web_site = Flask(__name__)



# Guess The number.
ans = random.randint(1, 10000)
print(ans)
@web_site.route('/', defaults={'num': 0})
def index(num):
    global ans
    num = request.args.get('num')
    result = ''
    if not num:
        num = 0

    num = int(num)
    
    # -----------------Start of your code---------------------
    # Start your code here. There are some useful variables for you.
    # - ans: a number. 
    # - num: a number that users input.
    # - result: your output string.
    
    # This is an example.
    if 1 == 1:
        result = '1 is 1'
    

    # 
    # -----------------End of your code---------------------
    comments =  db["comments"] if "comments" in db.keys() else [] 
    print(comments)
    return render_template('index.html', 
        num=num,
        result=result,
        comments=comments
    )

@web_site.route('/comments', methods=['GET', 'POST', 'DELETE'], defaults={'num': 0})
def comments(num):
    if request.method == "GET":
        del db['comments']
        return redirect('/')

    author = request.form.get('author')
    content = request.form.get('content')

    newComment = {
        'author': author, 
        'content': content, 
        'create_time': datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    }
    oldComments = db["comments"] if "comments" in db.keys() else []
    comments = [newComment] + oldComments
    db["comments"] = comments

    return redirect('/')

web_site.run(host='0.0.0.0', port=8080)
