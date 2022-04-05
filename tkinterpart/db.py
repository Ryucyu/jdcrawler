import json
from csv import DictReader
from pymongo import MongoClient
import pandas as pd

class GetData:
    def __init__(self):
        client = MongoClient()
        collection = client['jdcrawler']['jdphone']
        self.data = [i for i in collection.find()]

    def all(self):
        return self.data

db = GetData()

if __name__ == '__main__':
    data = GetData()
    info = data.all()
    print(info)





#     def insert(self,student):
#         self.studnets.append(student)
#         with open("students.json", "w") as fp:
#             fp.write(json.dumps(self.studnets, ensure_ascii=False))
#
#     def delete_by_id(self,id):
#         for student in self.studnets:
#             if student['id'] == id:
#                 self.studnets.remove(student)
#                 with open("students.json", "w") as fp:
#                     fp.write(json.dumps(self.studnets, ensure_ascii=False))
#                 return True,f"用户id{id}删除成功"
#         return False,f'用户id:{id}不存在'
#
#     def search_by_username(self,id):
#         for student in self.studnets:
#             if student['id'] == str(id):
#                 return True,student
#         return False,f'用户id:{id}不存在'
#
#     def update(self,stu):
#         for student in self.studnets:
#             if student['id'] == stu['id']:
#                 student.update(stu)
#                 with open("students.json", "w") as fp:
#                     fp.write(json.dumps(self.studnets, ensure_ascii=False))
#                 return True,f'{stu["id"]}修改成功'
#         return False,f'用户id:{stu["id"]}不存在'
#
#     def delete_by_class(self, classes):
#         new_students= self.studnets[:]
#         flag = 0
#         for student in new_students:
#             if student['class'] == classes:
#                 self.studnets.remove(student)
#                 flag = 1
#         if flag:
#             with open("students.json", "w") as fp:
#                 fp.write(json.dumps(self.studnets, ensure_ascii=False))
#             return True, f"班级{classes}删除成功"
#         return False, f'班级{classes}不存在'
#
















