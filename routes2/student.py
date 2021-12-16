from fastapi import APIRouter

from model2.student import Student
from config2.db import conn
from schemas2.student import userEntity, usersEntity
from bson import ObjectId
student = APIRouter()

@student.get('/')
async def find_all_students():
    return usersEntity(conn.local.student.find())

@student.get('/{id}')
def find_one_student(id):
    return userEntity(conn.local.student.find_one({"_id":ObjectId(id)}))

@student.post('/')
async def create_student(student: Student):
    conn.local.student.insert_one(dict(student))
    return usersEntity(conn.local.student.find())

@student.put('/{id}')
async def update_student(id,student: Student):
    conn.local.student.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(student)})
    return userEntity(conn.local.student.find_one({"_id":ObjectId(id)}))
  
@student.delete('/{id}')
async def delete_student(id):
    return userEntity(conn.local.student.find_one_and_delete({"_id":ObjectId(id)}))   