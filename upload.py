import shutil

source_folder = './firmware'
destination_disk = '/Volumes/KEYBOARD_'

if __name__ == '__main__':
    side = sys.argv[1]
    if side == 'left':
        shutil.copytree(source_folder, destination_disk + 'L')
    elif side == 'right':
        shutil.copytree(source_folder, destination_disk + 'R')
    else:
        print('Invalid side')
        sys.exit(1)


