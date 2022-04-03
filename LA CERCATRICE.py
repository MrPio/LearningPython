import os


def pdf_search(directory=os.getcwd()):
    count = 0
    for path, folder, file_list in os.walk(directory):
        for file in file_list:
            if file.split('.')[-1] == "pdf":
                full_path = os.path.join(path, file)
                count += 1
                print(f"count --> {count} [{full_path}]")
                os.system(f"explorer.exe {full_path}")


pdf_search(directory="C:\\")
