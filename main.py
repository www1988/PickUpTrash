# -*- coding:utf-8 -*-
# @Time : 2021/1/21 14:24
# @Author : huruwo
# @File : main
# @Function : 后台主页
from sanic import Sanic
from sanic.response import text

app = Sanic(name='main_app')


@app.route('/goods', methods=['POST'])
async def index(request):
    """
    商品数据提交接口
    :param request:
    :return:
    """
    print(request.json)
    return text('提交成功')
