import pymongo
from pprint import pprint


# 데이터베이스와 컬렉션을 생성하는 코드입니다.
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

# 새로 들어온 책들입니다. 리스트로 묶어 선언하세요.
new_book1 = {"title": "Alice\'s Adventures in Wonderland", "author": "Lewis Carroll", "publisher": "Macmillan", "date_received": "2015-11-26"}
new_book2 = {"title": "The Old Man and the Sea", "author": "Ernest Miller Hemingway","publisher": "Charles Scribner\'s Sons" ,"date_received": "2014-11-02"}
new_book3 = {"title": "The Great Gatsby", "author": "Francis Scott Key Fitzgerald", "date_received": "2019-01-12"}


# 데이터를 만들고 삽입하세요.
result = col.insert_many([new_book1, new_book2, new_book3])

# 삽입된 데이터 id들을 출력하세요.
pprint(result.inserted_ids)
