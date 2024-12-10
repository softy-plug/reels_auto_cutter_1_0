import os

os.system("pip install python-ffmpeg")
os.system("pip3 install ffprobe")

input("Нажмите Enter для запуска программы")

#from ffprobe import FFProbe

def list_bat_files():
    # Get a list of all .bat files in the current directory
    return [f for f in os.listdir() if f.endswith('.bat')]

def open_bat_file(file_name):
    # Open the selected .bat file
    os.startfile(file_name)

def main():
    bat_files = list_bat_files()
    
    if not bat_files:
        print("No .bat files found in the current directory.")
        return

    print("Select a .bat file to open:")
    for index, file in enumerate(bat_files):
        print(f"{index + 1}: {file}")

    choice = input("Enter the number of the file you want to open: ")

    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(bat_files):
            open_bat_file(bat_files[choice_index])
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
 
input("Нажмите Enter для закрытия окна")

#softy_plug