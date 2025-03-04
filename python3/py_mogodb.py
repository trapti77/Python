from pymongo import MongoClient
from bson import ObjectId
client=MongoClient("mongodb+srv://trapti45:trapti77@#@tcoding.esensl4.mongodb.net/?retryWrites=true&w=majority&appName=Tcoding",  tlsAllowInvalidCertificates=True)
#not a good idea to include id and pass in code files
#not a good way to handle

db=client["Tcoding"]
video_collection=db["videos"]
print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID : {video['_id']},name : {video['name']}, time :{video['time']}")

def add_videos(name,time):
  video_collection.insert_one({"name":name,"time":time})

def update_videos(vid_id,name,time):
    video_collection.update_one(#update one value
        {'_od':vid_id},
        {'$set':{"name":name,"time": time}}#it is a operator  used to set value
    )

def delete_videos(vid_id):
    video_collection.delete_one({"_id":vid_id})
    #debug this video_id problem

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. exit app")
        choice=input("enter your choice : ")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("enter the video name : ")
            time=input("enter the time : ")
            add_videos(name,time)
        elif choice=='3':
            vid_id=input("enter the video id to update : ")
            name=input("enter the video name : ")
            time=input("enter the time : ")
            update_videos(vid_id,name,time)
        elif choice=='4':
            vid_id=input("enter the video id to delete : ")
            delete_videos(vid_id)
        elif choice=='5':
            break
        else:
            print("enter invalid choice")
        

if __name__=="__main__":
    main()