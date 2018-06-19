import os


CWD = os.getcwd()


def clear():
    for the_file in os.listdir(CWD):
        file_path = os.path.join(CWD, the_file)
        if (os.path.isfile(file_path) and
                not the_file == 'clear.py' and
                (the_file[-4:] == '.txt' or the_file == 'tmp_msg.bin')):
            os.unlink(file_path)


if __name__ == '__main__':
    clear()
    print 'directory cleared successfully!'

