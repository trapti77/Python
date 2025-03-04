import json
#-----------------------------YOUTUBE VIDEO MANAGER PROJECT IN PYTHON------------------------
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)#convert data json to string
            print(type(test))#list type
            return test
    except FileNotFoundError:
       return []
   
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
       json.dump(videos,file)

def list_all_videos(videos):
   print('\n')
   print('*' * 70)
   for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']},Duration:{video['time']}")
    
   print('\n')
   print('*' * 70)
def add_video(videos):
  name=input("enter video name: ")
  time= input("enter video time: ")
  videos.append({'name':name,'time':time})
  save_data_helper(videos)

def update_video(video):
   list_all_videos(video)
   index=int(input("enter video number to update"))
   if 1<= index <=len(video):
        name=input("enter video name: ")
        time=input("enter video time: ")
        video[index-1]={'name':name, 'time':time}
        save_data_helper(video)
   else:
       print("invalid index selected")
       
def delete_video(video):
    list_all_videos(video)
    index=int(input("enter video number to update : "))
    if 1<=index<=len(video):
        del video[index-1]
        save_data_helper(video)
    else:
       print("invalid index selected")
       
def main():
 videos=load_data()
 while True:
    print("\nYOUTUBE MANAGER")
    print("1. List all youtube video : ")
    print("2. Add a youtube video : ")
    print("3. Update a youtube video details : ")
    print("4. Delete a youtube video : ")
    print("5. Exit the app : ")
    choice=input("Enter your choice : ")
    print(videos)
    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)  
        case '5':
            break
        case _:
            print("invalid choice")
            
if __name__=="__main__":
    main()