import sqlite3
# agregar redirect
from flask import Flask, render_template, abort, request, url_for, redirect
from db import get_db_connection

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

# se comenta /home
# @app.route('/home', methods=['GET'])
# def home():
#     return render_template('home.html')

@app.route('/post', methods=['GET'])
def get_all_post():
    conn = get_db_connection()
    # cambiar fetchone() por fetchall()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('post/posts.html', posts=posts)

@app.route('/post/<int:post_id>', methods=['GET'])
def get_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    # verificar si post es None
    if post is None:
        abort(404)
    return render_template('post/post.html', post=post)

# agregar los methods=['GET', 'POST']
@app.route('/post/create', methods=['GET', 'POST'])
def create_one_post():
    if request.method == 'POST':
        title = request.form['title']
        # cambiar contend por content
        contend = request.form['content']
        conn = get_db_connection()
        # error ! por ?
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, contend))
        conn.commit()
        conn.close()
        # cambiar return redirect(url_for('get_all_post')) por redirect(url_for('get_all_post'))
        return redirect(url_for('get_all_post'))
    # agregar elif para request.method == "GET":
    elif request.method == "GET":
        return render_template('post/create.html')

@app.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit_one_post(id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    conn.close()
    # verificar si post es None
    if post is None:
        abort(404)
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_post'))
    elif request.method == 'GET':
        return render_template('post/edit.html', post=post)

# cambiar <str:post_id> por <string:post_id>
@app.route('/post/delete/<string:post_id>', methods=['POST'])
def delete_one_post(post_id):
    conn = get_db_connection()
    # cambiar (post_id) por (post_id,)
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_all_post'))

# modificar el puerto y completar el host
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
