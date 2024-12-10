from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"
mongo = PyMongo(app)
posts_collection = mongo.db.posts

@app.route('/')
def index():
    # Fetch posts and format timestamps
    posts = posts_collection.find()
    formatted_posts = []
    for post in posts:
        post["created_at"] = post["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        formatted_posts.append(post)
    return render_template('index.html', posts=formatted_posts)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {
            "title": title,
            "content": content,
            "created_at": datetime.utcnow()  # Store as UTC
        }
        posts_collection.insert_one(post)
        return redirect(url_for('index'))
    return render_template('add_post.html')

@app.route('/post/<id>')
def post_detail(id):
    post = posts_collection.find_one({"_id": ObjectId(id)})
    # Format timestamp for display
    post["created_at"] = post["created_at"].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('post_detail.html', post=post)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    post = posts_collection.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        updated_data = {
            "title": request.form['title'],
            "content": request.form['content'],
            "created_at": post['created_at']  # Keep original timestamp
        }
        posts_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('index'))
    post["created_at"] = post["created_at"].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('edit_post.html', post=post)

@app.route('/delete/<id>')
def delete_post(id):
    posts_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
