from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from flask_blog import db
from flask_blog.models import Post
from flask_blog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has ben created', category='success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form= form, legend='New Post' )


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if(post.author != current_user):
        abort(403)
    else:
        form = PostForm()
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            db.session.commit()
            flash('Post has beed updated', 'success')
            return redirect(url_for('posts.post', post_id= post.id))
        elif(request.method == 'GET'):
            form.title.data = post.title
            form.content.data = post.content
    
    return render_template('create_post.html', title='Update Post', form= form, legend='Update Post' )
       
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if(post.author != current_user):
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', category='success')
    return redirect(url_for('main.home'))


@posts.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    
    return render_template('user_posts.html', posts=posts, user=user )
