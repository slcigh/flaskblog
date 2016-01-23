#encoding=utf-8
from flask import Blueprint

main = Blueprint("main", __name__) #它会给函数名加上由 Blueprint 的构造函数中给出的蓝图的名称作为前缀 


from . import views, errors