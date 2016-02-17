# encoding=utf-8
# coding=utf-8

from flask import render_template
from . import main
from .forms import SearchForm
from .. import db
from ..models import Post, Category, Tag


def get_tags():
    tags = dict(db.session.query(Tag.name, db.func.count(Post.id)).join(Post.tags).group_by(Tag.id))
    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    return sorted_tags


@main.route('/')
@main.route('/<int:page>')
def index(page=1):
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    categories = Category.query.all()
    return render_template("index.html", posts=posts, categories=categories, tags=get_tags())


@main.route("/post/<int:id>")
def post(id):
    posts = Post.query.filter_by(id=id).first_or_404()
    categories = Category.query.all()
    return render_template("posts.html", posts=posts, categories=categories, tags=get_tags())


@main.route("/tags/<name>/<int:page>")
def view_posts_in_tags(name, page=1):
    posts = Post.query.join(Post.tags).filter_by(name=name).order_by(Post.id.desc()).paginate(page,
                                                                                              per_page=5,
                                                                                              error_out=False)
    categories = Category.query.all()
    return render_template("tags.html", name=name, posts=posts, categories=categories, tags=get_tags())


@main.route("/<name>/<int:page>")
def view_posts_in_category(name, page=1):
    posts = Post.query.join(Category).filter_by(name=name).order_by(Post.id.desc()).paginate(page,
                                                                                             per_page=5,
                                                                                             error_out=False)
    categories = Category.query.all()
    return render_template("categories.html", name=name, posts=posts, categories=categories, tags=get_tags())


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/search', methods=['POST'])
def search():
    query = SearchForm().search.data
    results = Post.query.whoosh_search(query).all()
    return render_template('search.html',
                           query=query,
                           results=results)

