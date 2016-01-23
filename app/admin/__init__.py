# encoding=utf-8
# coding:utf-8
from flask.ext.admin import Admin
from app.admin.views import AdminUserView, AdminPostView, AdminCategoryView, AdminTagView, MyAdminIndexView


def create_admin(app=None, db=None):
    admin = Admin(app, 'Admin', index_view=MyAdminIndexView(), base_template='my_master.html',
                  template_mode='bootstrap3')
    admin.add_view(AdminUserView(User, db.session))
    admin.add_view(AdminPostView(Post, db.session))
    admin.add_view(AdminCategoryView(Category, db.session))
    admin.add_view(AdminTagView(Tag, db.session))


from app.models import User, Post, Category, Tag
