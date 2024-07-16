#!/usr/bin/python3

'''function definition '''


def read_file(filename=""):
    '''function to read file '''

    with open(filename, 'r', encoding='utf-8') as fp:
        # opening a file with read access mode

        print(fp.read())

