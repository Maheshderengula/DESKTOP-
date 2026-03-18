import pymongo
try:
    #establish db connection
    client=pymongo.MongoClient('mongodb://localhost:27017/') 
    #get db instance
    db=client['mb']
    #get collection instance
    emp_col=db['employees']
    emp_col.insert_one({'eid':102,'ename':'Sonia','esal':55000})
    print("Document inserted successfully")

except Exception as e:
    print(e)