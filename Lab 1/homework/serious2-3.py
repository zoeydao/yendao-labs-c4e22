from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#Connect to database
client = MongoClient(uri)
db = client.get_default_database()

#Collection
posts = db['posts'] #insert_one (C), find (R)

#Document
#Create a document
post = {
    'title':'C4E22',
    'content':'''Đi học code nói chung là rất vui và useful, tuy cũng có lúc hơi buồn ngủ vì học lúc 2h chiều chủ nhật là nap time của mình huhu
    nên thầy cứ cho mấy bài tập khó hack não vào nhé :))
    Cho thử link vào xem có click vào được không :-? https://i.pinimg.com/originals/ff/89/1c/ff891c36d10cededa0411a9100f3befe.jpg
    
    btw, làm thế nào để format được content của post này nhỉ? hay là phụ thuộc vào FE của web? hmm...''',
    'author':'Zoey'
}

#Insert created document
posts.insert_one(post)    