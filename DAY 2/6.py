#dictionary

person = {
    "Fname":"Dp",
    "Mname":"Yp",
    "lname":"P",
    "parents":{
        "father":{
            "name":"yyy"
        },
        "mother":{
            "name":"AAA"
    
        },

        "qua":["SSC","HSC","BCA"],
        "isAlive":True
    },

}

print(person)
print(person["isAlive"])

person["isAlive"]=False
print(person["isAlive"])

print(type(person))