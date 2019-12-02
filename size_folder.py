import os
import argparse

def size_folder(folder):
    total_size = 0
    for root, dirs, files in os.walk(folder):
        for f in files:
            file_path = os.path.join(root, f)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size/1000000


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shows the size of subfolders in a folder')
    parser.add_argument('folder', metavar='path', type=str, help='The folder path')
    args = parser.parse_args()

    PATH = args.folder
    subdirs = []
    total = 0

    for root, dirs, files in os.walk(PATH):    
        for d in dirs:
            subdirs.append(os.path.join(root, d))
        break

    for d in subdirs:
        sf = size_folder(d)
        total += sf
        print('{0} \t\t\t {1:.2f} Mb'.format(d, sf))
    
    print('Total: {0:.2f} Mb'.format(total))