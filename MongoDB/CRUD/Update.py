import pymongo

# 데이터베이스와 컬렉션을 생성하는 코드입니다.
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

# 잘못 입력된 책 작가를 수정하기 위한 딕셔너리를 만드세요.
update = ({"$set": {"author" : "Joanne Kathleen Rowling"}})
query = { "title": { "$regex": "^Harry Potter" } }

# 잘못 입력된 책 작가를 수정하세요.
# myquery = { "필드명": { "$regex": "^찾고자 하는 내용" } }
update_book = col.update_many(query, update)

# 몇 권의 책이 수정되었는지 확인하세요.
print(update_book.modified_count)

# 책이 잘 수정되었는지 확인하는 코드입니다. 수정하지 마세요!
for x in col.find(query):
    print(x)
