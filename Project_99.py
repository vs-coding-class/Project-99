import os
import shutil

path = input('Please enter the path of the folder that you would like to clean up... ')
days = input('Please enter the number of days you would like to organize your folder by... ')

nanoseconds = int(days) * 24 * 3600000000000
print(nanoseconds)
os.mkdir('C:/Users/vinay/Desktop/Older_than_'+days+'_days')

for (root, dirs, files) in os.walk(path, topdown = True):
    for name in files:
        file_name = os.path.join(root, name)
        print(file_name)
        ctime_file = os.stat(file_name).st_ctime
        print(ctime_file)
        if(ctime_file > nanoseconds):
            os.remove(file_name)

    for name in dirs:
        dir_name = os.path.join(root, name)
        print(dir_name)
        ctime_dir = os.stat(dir_name).st_ctime
        print(ctime_dir)
        if(ctime_dir > nanoseconds):
            shutil.rmtree(dir_name)