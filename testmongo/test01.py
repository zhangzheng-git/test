import pymongo as mg
import json
dbname = 'test'
collname = 'student'
client = mg.MongoClient('127.0.0.1:27017')
# dblist = client.list_database_names()
# newdb=client[dbname]  #创建数据库
# newset = newdb['student'] #创建集合（表）c
# if dbname in dblist:
#     print("数据库已存在")
# else:
#     print('数据库不存在')
#     data = newset.insert_one({"name":'zhaowei','age':17}) #插入记录
#     col = newdb.list_collection_names()
#     if 'student' in col:
#         print('集合已存在')
#     else:
#         print('集合不存在')
db = client.get_database(dbname)
collec = db.get_collection(collname)
nRecord = collec.find().count()
print(nRecord)
for i in collec.find():
    print(i)

ret = collec.find_one({'isNonProfit':True},{'_id':0,'detail.mark':1})
# print(ret)
# ret = collec.find({'isNonProfit':True},{'_id':0,'name':1,'detail.mark':1,'detail.name':1})
ret = collec.find({'isNonProfit':True},{'_id':0})
jsonstr={}
for item in ret:
    # print('item',type(item))
    print("python字典对象:{}".format(item))
    print("+++++++++",item['address']['street'])
    print("----------",item['detail'][1]['mark'])
    jsonstr = json.dumps(item)
    # print('jsonstr',type(jsonstr))
    # print("json对象:{}".format(jsonstr))








# # coding:utf-8
"""
mongo操作工具
"""

# from pymongo import MongoClient
#
# MONGO_HOST, MONGO_PORT, MONGO_DB, MONGO_TABLE = '127.0.0.1', 27017, 'test', 'student'
#
#
# class MongoUtils:
#     """
#     链接mongoDB，进行各种操作
#     """
#
#     def __init__(self, host=MONGO_HOST, port=MONGO_PORT, db_name=MONGO_DB):
#         """
#         初始化对象，链接数据库
#         :param host: mongo数据库所在服务器地址
#         :param port: mongo数据库端口
#         :param db_name: 数据库的名称
#         :return: 无返回值
#         """
#         try:
#             self.client = None
#             self.client = MongoClient(host, port)
#             self.database = self.client.get_database(db_name)
#             self.collection = None
#         except Exception as e:
#             self.close_conn()
#             print('init mongo bar failed:{}'.format(e))
#
#     def change_collection(self, table_name=MONGO_TABLE):
#         """切换表"""
#         self.collection = self.database.get_collection(table_name)
#
#     def count_info(self, table_name=MONGO_TABLE, filter_dict=None):
#         """
#         查找表记录条数，默认返回0
#         :param table_name: str 表名
#         :param filter_dict: dict 过滤条件
#         :return: int 表记录条数
#         """
#         tab_size = 0
#         try:
#             self.collection = self.database.get_collection(table_name)
#             tab_size = self.collection.find(filter_dict).count()
#             return tab_size
#         except Exception as e:
#             print('get table size failed:{}'.format(e))
#         finally:
#             return tab_size
#
#     def update_info(self, filter_dict, update_dict, insert=False, multi=False):
#         """
#         更新表记录，默认返回false
#         :param filter_dict: dict 过滤条件，如{'campaignId':{'$in':[1,2,3]}}
#         :param update_dict: dict 更新的字段，如{'$set':{status_key:0，'campaign.status':1},{'$unset':'campaign.name':'test_camp'}}
#         :param insert: bool 如果需要更新的记录不存在是否插入
#         :param multi: bool 是否更新所有符合条件的记录， False则只更新一条，True则更新所有
#         :return: bool 是否更新成功
#         """
#         result = False
#         try:
#             self.collection.update(filter_dict, update_dict, insert, multi)
#             result = True
#             print("[INFO] update success!")
#         except Exception as e:
#             print('update failed:{}'.format(e))
#         finally:
#             return result
#
#     def insert_info(self, insert_date):
#         """
#         更新表记录，默认返回false
#         :param insert_date: dict 插入的数据，如{'campaignId':{'$in':[1,2,3]}}
#         :return: bool 是否更新成功
#         """
#         result = False
#         try:
#             self.collection.insert(insert_date)
#             result = True
#             print("insert success!")
#         except Exception as e:
#             print('insert failed:{}'.format(e))
#         finally:
#             return result
#
#     def delete_info(self, filter_date):
#         """
#         更新表记录，默认返回false
#         :param filter_date: dict 删除数据的条件，如{'campaignId':{'$in':[1,2,3]}}
#         :return: bool 是否更新成功
#         """
#         result = False
#         try:
#             self.collection.remove(filter_date)
#             result = True
#             print("remove success!")
#         except Exception as e:
#             print('remove failed:{}'.format(e))
#         finally:
#             return result
#
#     def find_one_info(self, filter_dict, return_dict):
#         """
#         查找一条表记录，默认返回空字典
#         :param filter_dict: dict 过滤条件如{'campaignId':123}
#         :param return_dict: dict 返回的字段如{'campaign.status':1,'updated':1,'_id':0}
#         :return: dict 查找到的数据
#         """
#         result = {}
#         try:
#             result = self.collection.find_one(filter_dict, return_dict)
#         except Exception as e:
#             print('find data failed:{}'.format(e))
#         finally:
#             return result
#
#     def find_multi_info(self, filter_dict, return_dict, limit_size=0, skip_index=0):
#         """
#         查找多条表记录，默认返回空数组
#         :param filter_dict: dict filter_dict: 过滤条件如{'campaignId':123}
#         :param return_dict: dict 返回的字段如{'campaign.status':1,'updated':1,'_id':0}
#         :param limit_size: int 限定返回的数据条数
#         :param skip_index: int 游标位移
#         :return: list 查询到的记录组成的列表，每个元素是一个字典
#         """
#         result = []
#         try:
#             if not limit_size:  #可以理解 如果 not后面的为假FALSE就执行
#                 if not skip_index:
#                     result = self.collection.find(filter_dict, return_dict)
#                 else:
#                     result = self.collection.find(filter_dict, return_dict).skip(skip_index)
#             else:
#                 if not skip_index:
#                     result = self.collection.find(filter_dict, return_dict).limit(limit_size)
#                 else:
#                     result = self.collection.find(filter_dict, return_dict).skip(skip_index).limit(limit_size)
#         except Exception as e:
#             print('find data failed:{}'.format(e))
#         finally:
#             return result
#
#     def close_conn(self):
#         """
#         关闭数据库链接
#         :return: 无返回值
#         """
#         if self.client:
#             self.client.close()
#
# if __name__ == '__main__':
#     MgDB = MongoUtils('127.0.0.1',27017,'test')
#     MgDB.change_collection('student')
#     # nSize = MgDB.count_info('student')
#     # print(nSize)
#
#     # MgDB.insert_info({
#     # "name": "河北交通局",
#     # "url": "http://www.bejson.com",
#     # "page": 92,
#     # "isNonProfit": True,
#     # "address": {
#     #     "street": "北京路.",
#     #     "city": "河北唐山",
#     #     "country": "中国"
#     # },
#     # "detail": [
#     #     {
#     #         "name": "Google",
#     #         "mark": 79
#     #     },
#     #     {
#     #         "name": "Baidu",
#     #         "mark": 64
#     #     },
#     #     {
#     #         "name": "SoSo",
#     #         "mark": 45
#     #     }
#     # ]
#     # })
#     nSize = MgDB.count_info('student')
#     print(nSize)
#     Re = MgDB.find_one_info({"isNonProfit": True}, {"_id": False,'name':1,'detail.mark':True})
#     for item in Re:print(item)
