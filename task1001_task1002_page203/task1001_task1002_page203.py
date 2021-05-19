class MyFileReader:
    """Reading data from a text file"""
    textfile = "learning_python.txt"

    def __init__(self):
        global textfile

    def read_from_file1(self):
        # 'with' keyword is being used to close/clean up some resource/file even if exceptions will be thrown
        with open(self.textfile) as file_object:
            f_content = file_object.read()
        return f_content

    def read_from_file2(self):
        with open(self.textfile) as file_object:
            for line in file_object:
                print(line.rstrip()[::-1])  # rstrip() removes newline character

    def read_from_file3(self):
        with open(self.textfile) as file_object:
            lines = file_object.readlines()
        some_var = ''
        for line in lines:
            some_var += line[::3]
        return some_var

    def read_from_file4(self):
        strings = []
        with open(self.textfile) as file_object:
            for line in file_object:
                strings.append(line)
        return strings


# test task 10.01
fr = MyFileReader()
print(fr.read_from_file1())
print('-----')
fr.read_from_file2()
print('-----')
print(fr.read_from_file3())
print('-----')
print(fr.read_from_file4())
print('-----')

# test task 10.02
fr_new = MyFileReader()
text = fr_new.read_from_file4()
for strng in text:
    print(strng.rstrip().replace('Python', 'Ruby'))
