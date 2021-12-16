def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "age":item["age"],
        "gender":item["gender"],
        "department":item["department"],
        "credit_score":item["credit_score"],
        "blood_group":item["blood_group"],
        "email":item["email"],
        "roll_no":item["roll_no"],
        "year":item["year"]
    }

def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]