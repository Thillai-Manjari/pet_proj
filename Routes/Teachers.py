from fastapi import FastAPI
from fastapi.routing import APIRouter
from Models.Teachers import Teacher
from Schemas.Teachers import serializeDict,serializeList
from Config.database import conn
from bson import ObjectId

teacher=APIRouter()

@teacher.get('/')
def all_faculty_details():
    return serializeList(conn.local.teacher.find())

@teacher.get('/{id}')
def See_your_profile(id):
    return serializeDict(conn.local.teacher.find_one({"_id":ObjectId(id)}))

@teacher.post('/')
def create_your_profiles(teacher: Teacher):
    conn.local.teacher.insert_one(dict(teacher))
    return serializeList(conn.local.teacher.find())

@teacher.put('/{id}')
def Manage_profile(id,teacher:Teacher):
    conn.local.teacher.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(teacher)})
    return serializeDict(conn.local.teacher.find_one({"_id":ObjectId(id)}))

@teacher.delete('/{id}')
def Delete_profile(id):
    conn.local.teacher.find_one_and_delete({"_id":ObjectId(id)})
    return "Deleted Successfully"