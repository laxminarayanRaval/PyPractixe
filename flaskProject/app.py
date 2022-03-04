from flask import Flask, render_template, request, redirect, url_for
from utils.posts_model import PostsModel

postmodel = PostsModel('PostsAppDB')

app = Flask(__name__)


def get_posts():
    return postmodel.get_all_posts_data()


def get_post_by_id(id):
    return postmodel.get_post_data(id)


def get_posts_cnt():
    return postmodel.get_post_count()[0][0]

"""posts = {
    0: {
        'id': 0,
        'title': 'Hello, World!',
        'author': 'Mr. Lx',
        'content': 'This is my First blog Post!',
        'date': 'Today'
    },
    1: {
        'id': 1,
        'title': 'Want to How to be a Billionaire.',
        'author': 'Mr. Lx',
        'content': 'Work Smart & Learn Hard.\r\nThe only Guru-Mantra you need to find a way to be a Billionaire.',
        'date': 'Today'
    },
    2: {
        'id': 2,
        'title': 'How to make a Diamond.',
        'author': 'Mr. Lx',
        'content': "You must have born in China to get such question's answers.",
        'date': 'Today'
    },
    3: {
        'id': 3,
        'title': 'Who is the Murderer?',
        'author': 'Mr. Lx',
        'content': 'The One who Killed Victim is a Murder. Definition of murderer\r\n: one who murders ; especially : one who commits the crime of murder.',
        'date': 'Today'
    }
}"""


@app.route('/')
def home():
    posts = get_posts()
    # print(posts)
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = get_post_by_id(post_id)[0]
    # print(post_id, post)
    # return f"<h1>Post: {post['title']}</h1>\n<h3>content:\n\n{post['content']}</h3>"
    if not post:
        return render_template('404.jinja2', message=f'A post with #{post_id} not available right Now.')
    return render_template('posts.jinja2', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        pdate = request.form.get('pdate')
        post_id = get_posts_cnt() + 1
        # posts[post_id] = {'id': post_id, 'title': title, 'author': author, 'content': content, 'date': pdate}
        postmodel.new_post(post_id, title, author, content, pdate)
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
