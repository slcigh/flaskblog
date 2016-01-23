# encoding=utf-8
# coding=utf-8
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import current_user

from . import main
from .forms import PostForm, SearchForm
from .. import db
from ..models import User, Post, Category, Tag
from sqlalchemy import func


def get_tags():
    tags = dict(db.session.query(Tag.name, db.func.count(Post.id)).join(Post.tags).group_by(Tag.id))
    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    return sorted_tags


@main.route('/')
@main.route('/<int:page>')
def index(page=1):
    posts = Post.query.order_by(Post.id.desc()).paginate(page, per_page=5, error_out=False)
    categories = Category.query.all()
    # tags = dict(db.session.query(Tag.name, db.func.count(Post.id)).join(Post.tags).group_by(Tag.id))
    # tags = {}
    # for (k,v) in tags_t.items():
    # tags[k] = int(v*10/sum(i for i in tags_t.values()))
    # sorted_tags = sorted(tags.items(), key=lambda x:x[1], reverse=True)
    return render_template("asdf.html", posts=posts, categories=categories, tags=get_tags())


@main.route("/post/<int:id>")
def post(id):
    posts = Post.query.filter_by(id=id).first_or_404()
    categories = Category.query.all()
    return render_template("xpost.html", posts=posts, categories=categories, tags=get_tags())


@main.route("/true")
@main.route('/true/<int:page>')
def true(page=1):
    posts = Post.query.order_by(Post.id.desc()).paginate(page, per_page=10, error_out=False)
    categories = Category.query.all()
    return render_template("true.html", posts=posts, categories=categories, tags=get_tags())


#@main.route("/<name>")
@main.route("/<name>/<int:page>")
def view_posts_in_category(name, page=1):
    posts = Post.query.join(Category).filter_by(name=name).order_by(Post.id.desc()).paginate(page,
                                                                                             per_page=5,
                                                                                             error_out=False)
    categories = Category.query.all()
    return render_template("xcat.html", name=name, posts=posts, categories=categories, tags=get_tags())


# @main.route("/tags/<name>")
# def view_posts_in_tags(name):
#     tag = Tag.query.filter_by(name=name).first_or_404()
#     categories = Category.query.all()
#     return render_template("xtags.html", name=name, posts=tag.posts, categories=categories, tags=get_tags())
#@main.route("/tags/<name>")
@main.route("/tags/<name>/<int:page>")
def view_posts_in_tags(name, page=1):
    posts = Post.query.join(Post.tags).filter_by(name=name).order_by(Post.id.desc()).paginate(page,
                                                                                              per_page=5,
                                                                                              error_out=False)
    categories = Category.query.all()
    return render_template("xcat.html", name=name, posts=posts, categories=categories, tags=get_tags())


@main.route('/search', methods=['POST'])
def search():
    query = SearchForm().search.data
    results = Post.query.whoosh_search(query).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)


# TODO add flask-moment