from flask import Flask, render_template

app = Flask(__name__)

posts = {
    0: {
        'title': 'Hello, World!',
        'content': 'This is my First blog Post!'
    }
}


@app.route('/')
def home():
    return 'Hello, World'


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    # return f"<h1>Post: {post['title']}</h1>\n<h3>content:\n\n{post['content']}</h3>"
    if not post:
        return render_template('404.html', message=f'A post with #{post_id} not available right Now.')
    return render_template('posts.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
