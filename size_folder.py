import os
import argparse
#from progressbar import ProgressBar

def size_file(file_path):
    return os.path.getsize(file_path)/1000000

def size_folder(folder):
    total_size = 0
    for root, dirs, files in os.walk(folder):
        for f in files:
            file_path = os.path.join(root, f)
            if not os.path.islink(file_path):
                total_size += size_file(file_path)
    return total_size


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
    
    #pb = ProgressBar(len(subdirs))
    result = []
    for d in subdirs:
        #pb.next()
        sf = size_folder(d)
        total += sf
        result.append((d, sf))
        #print('{0} \t\t\t {1:.2f} Mb'.format(d, sf))
    
    for f in os.listdir(root):
        file_path = os.path.join(root, f)
        if os.path.isfile(file_path):
            sf = size_file(file_path)
            total += sf
            result.append((file_path, sf))
            
    result.sort(key=lambda x: x[1], reverse=True)

    for r in result:
        print('{0} \t\t\t {1:.2f} Mb'.format(r[0], r[1]))

    print('Total: {0:.2f} Mb'.format(total))