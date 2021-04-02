# *_* coding: utf-8 *_*
# time:2021-04-0211:13
# tools:PyCharm
# file_name：db_test.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
# import os
import django

# os.environ.setdefault('DJANGO_SETTING_MODULE', 'MyDjango.settings')
django.setup()

from boards.models import Board
"""添加数据的两种方法"""
# 方法一：
# board=Board(name="Django",description='This is a board about Django.')
# 需要调用save()方法来保存
# board.save()
# 方法二：不需调用save()方法，直接创建
# board=Board.objects.create(name="Python",description='General discussion about Python.')

# 获取所有数据（对象）
# print(Board.objects.all())

# 获取数据信息
# board=Board.objects.get(id=1)
# print(board.id)
# print(board.name)
# print(board.description)
# 修改信息
# p.description='Django discussion board.'
# p.save()

borards_list=Board.objects.all()
for board in borards_list:
    print(board.description)
