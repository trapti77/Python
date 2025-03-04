import sqlite3

conn=sqlite3.connect('youtube.db')#create connection with file

cursor=conn.cursor()

cursor.execute('''
              CREATE TABLE IF NOT EXISTS videos(
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  time TEXT NOT NULL
                )
            ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
   cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
   conn.commit()

def update_videos(vid_id,name,time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,vid_id))
    conn.commit()

def delete_videos(vid_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(vid_id))
    conn.commit()

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
    
    conn.close()
    
    
if __name__=="__main__":
    main()
