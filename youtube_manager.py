import json
youtube = 'youtube.txt'

def Load_data():
    try:
        with open(youtube, 'r') as file:
            test = json.load(file)
            # print(test)
            return test  # return the loaded data
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)



def List_all_videos(videos):
    print("\n")
    print("-"*60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("-"*60)
def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, "time":time})
    save_data_helper(videos)
    print("New video is added successfully!")

def Update_videos(videos):
    List_all_videos(videos)
    index = int(input("Enter video number to update: "))
    if 1 <= index <= len(videos):
       name = input("enter the new video number ")
       time = input("enter the new video time ")
       videos[index-1] = {'name': name, "time": time}
       save_data_helper(videos)
    else:
        print("invalid selection !")
def Delete_videos(videos):
    List_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid selection !")


def main():
    
    videos = Load_data()
    while True:
        print("\n Youtube manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update youtube videos ")
        print("4. Delete a youtube videos ")
        print("5. Exit App ")

        choice = input(" \n Enter your choice  ")
        # print(videos)

        match choice:
            case "1":
                List_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                Update_videos(videos)
            case "4":
                Delete_videos(videos)
            case "5":
                print("Goodbye!")
                break
            case _:  # default/miss match
                print("Invalid choice. Please try again.") 

if __name__ == "__main__":
    main()