class Questionnaire:
    global filename

    def __init__(self):
        self.filename = "1001_reasons.txt"
        self.append_to_file()

    def append_to_file(self):
        while True:
            print("Please, enter 'exit' if you want to quit the program")
            answer = input("Why do you like to program? : ")
            if answer.strip().lower() == 'exit':
                break
            if len(answer) <= 5:
                continue
                
            with open(self.filename, "a") as file_object:
                try:
                    file_object.write("\n" + answer)
                except UnicodeEncodeError:
                    print("Please, use Latin characters only")

    def read_from_file(self):
        print(f"Reading from file {self.filename}...")
        res = []
        with open(self.filename) as file_object:
            res += file_object.readlines()
        return res


# test task 10.05
qn = Questionnaire()
print(*qn.read_from_file())
