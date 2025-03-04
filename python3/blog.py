import json

def load_data():
    try:
        with open('blogs.txt','r') as file:
            data=json.load(file)
            return data
    except FileNotFoundError:
        return [] 
def save_data(blogs):
        with open('blogs.txt','w') as file:
         json.dump(blogs,file)
         
def show_blogs(blogs):
     print('\n')
     print('*'*100)
     for index ,blog in enumerate(blogs,start=1):
         print(f"{index}.{blog['title']},description:{blog['desc']}")
         
     print('\n')
     print('*'*100)
     
def create_blogs(blogs):
    title=input("enter title name")
    desc=input("enter description ")
    blogs.append({'title':title,'desc':desc})
    save_data(blogs)

def update_blogs(blogs):
    show_blogs(blogs)
    index=int(input('enter index to update'))
    if 1<=index<=len(blogs):
     title=input("enter title name")
     desc=input("enter description ")
     blogs[index-1]={'title':title,'desc':desc}
     save_data(blogs)
    else:
        print("invalid number")
        
def delete_blogs(blogs):
      show_blogs(blogs)
      index=int(input('enter index to update'))
      if 1<=index<=len(blogs):
          del blogs[index-1]
          save_data(blogs)
      else:
          print('invalide number') 
          

def main():
    blogs=load_data()
    
    while True:
        print('\n')
        print('*************************blogs manager app*********************')
        print('1. show all blogs')
        print('2. create blogs')
        print('3. update blogs')
        print('4. delete blogs')
        print('5. exist from the app')
        
        choice=input('enter your choice:')
        match choice:
            case '1':
                show_blogs(blogs)
            case '2':
                create_blogs(blogs)
            case '3':
                update_blogs(blogs)
            case '4':
                delete_blogs(blogs)
            case '5':
                break
            case _:
                print("invalid choice entered")
        
if __name__=='__main__':
 main()