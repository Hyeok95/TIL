import pymongo

# 데이터베이스를 생성하는 코드입니다. 수정하지 마세요!
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")

# 컬렉션을 생성하세요.
col = db.get_collection('books')

# 데이터를 삽입하는 코드: 컬렉션이 잘 생성되었는지 확인하기 위해서는 반드시 아래 주석을 해제하세요.
data = col.insert_one({ "title": "Harry Potter and the Deathly Hallows", "author": "Joanne Kathleen Rowling","publisher": "Bloomsbury Publishing" ,"date_received": "2017-07-21"})

# 컬렉션 목록을 reuslt 리스트에 저장하세요.
result = db.list_collection_names()

# 값을 잘 저장하였는지 확인하기 위한 코드입니다. 수정하지 마세요!
print(result)
