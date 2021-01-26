# -*- coding:utf-8 -*-
# @Time : 2021/1/21 14:24
# @Author : huruwo
# @File : main
# @Function : 后台主页
import queue

from sanic import Sanic
from sanic.response import text

from data_save import MySqlUtils

app = Sanic(name='main_app')
sql_util = MySqlUtils()

task_queue = queue.Queue(maxsize=400000)


@app.route('/goods', methods=['POST'])
async def index(request):
    """
    商品数据提交接口
    :param request:
    :return:
    """
    data = request.json
    # name,price,address,describe,other
    name = data.get('name')
    price = data.get('price')
    address = data.get('address')
    describe = data.get('describe')
    other = data.get('other')
    sql_util.insert_data(name, price, address, describe, other)
    return text('提交成功')


@app.route('/task', methods=['POST'])
async def index(request):
    """
    提交任务
    :param request:
    :return:
    """
    data = request.json
    task_queue.put(data.get('task'))
    return text('提交成功')


@app.route('/task', methods=['GET'])
async def index(request):
    """
    提取任务
    :param request:
    :return:
    """
    return task_queue.get()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
