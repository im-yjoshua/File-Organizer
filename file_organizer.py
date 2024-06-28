# # File Organizer
# # Write a script that organizes files in a directory into subdirectories based on their file types (e.g., documents, images, videos).

import os
import shutil

# # Function to organize files into subdirectories based on their file types.


def fileOrganizer():
    listOfFiles = os.listdir()

    # # ========================================

    # # Python File section
    # pythonFile = [file for file in listOfFiles if file.endswith('.py')]
    # checkPath = './Python Files'
    # if not os.path.exists(checkPath):
    #     os.mkdir('Python Files')
    #     for i, file in enumerate(pythonFile):
    #         try:
    #             shutil.move(pythonFile[i], checkPath)
    #             print(f"File '{pythonFile[i]}' moved to '{checkPath.strip('./')}' successfully.")
    #         except FileNotFoundError:
    #             print(f"The file '{pythonFile[i]}' does not exist.")
    #         except PermissionError:
    #             print("Permission denied.")
    #         except Exception as e:
    #             print(f"Error occurred: {e}")
    # else:
    #     print("Directory already exists.")

    # # ========================================

    # # C++ File section
    CPPfiles = [file for file in listOfFiles if file.endswith('.cpp')]
    checkPath = './C++ Files'
    if not os.path.exists(checkPath):
        os.mkdir('C++ Files')
        for i, file in enumerate(CPPfiles):
            try:
                shutil.move(CPPfiles[i], checkPath)
                print(f"File '{CPPfiles[i]}' moved to '{checkPath.strip('./')}' successfully.")
            except FileNotFoundError:
                print(f"The file '{CPPfiles[i]}' does not exist.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Directory already exists.")

    # # ========================================

    # # Images File section
    ImageFiles = [file for file in listOfFiles if (
        file.endswith('.jpg') or file.endswith('.png'))]
    checkPath = './Images'
    if not os.path.exists(checkPath):
        os.mkdir('Images')
        for i, file in enumerate(ImageFiles):
            try:
                shutil.move(ImageFiles[i], checkPath)
                print(f"File '{ImageFiles[i]}' moved to '{checkPath.strip('./')}' successfully.")
            except FileNotFoundError:
                print(f"The file '{ImageFiles[i]}' does not exist.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Directory already exists.")

    # # ========================================

    # # Audio File section
    AudioFiles = [file for file in listOfFiles if file.endswith('.mp3')]
    checkPath = './Audio Files'
    if not os.path.exists(checkPath):
        os.mkdir('Audio Files')
        for i, file in enumerate(AudioFiles):
            try:
                shutil.move(AudioFiles[i], checkPath)
                print(f"File '{AudioFiles[i]}' moved to '{checkPath.strip('./')}' successfully.")
            except FileNotFoundError:
                print(f"The file '{AudioFiles[i]}' does not exist.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Directory already exists.")

    # # ========================================

    # # Video File section
    VideoFiles = [file for file in listOfFiles if (
        file.endswith('.mp4') or file.endswith('.m4a'))]
    checkPath = './Videos'
    if not os.path.exists(checkPath):
        os.mkdir('Videos')
        for i, file in enumerate(VideoFiles):
            try:
                shutil.move(VideoFiles[i], checkPath)
                print(f"File '{VideoFiles[i]}' moved to '{checkPath.strip('./')}' successfully.")
            except FileNotFoundError:
                print(f"The file '{VideoFiles[i]}' does not exist.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Directory already exists.")

    # # ========================================

    # # Text File section
    TextFiles = [file for file in listOfFiles if file.endswith('.txt')]
    checkPath = './Text Files'
    if not os.path.exists(checkPath):
        os.mkdir('Text Files')
        for i, file in enumerate(TextFiles):
            try:
                shutil.move(TextFiles[i], checkPath)
                print(f"File '{TextFiles[i]}' moved to '{checkPath.strip('./')}' successfully.")
            except FileNotFoundError:
                print(f"The file '{TextFiles[i]}' does not exist.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Directory already exists.")


# # ========================================


if __name__ == "__main__":
    fileOrganizer()
