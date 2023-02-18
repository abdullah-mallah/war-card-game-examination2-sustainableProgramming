class FileRW:
    def __init__(self, file_name):
        self._file_name = file_name

    # Check whether the name is already in the file
    def check_name(self, name) -> bool:
        name_found = False
        more_enteries = True
        with open(self._file_name, 'r') as rf:
            while more_enteries:
                line = rf.readline().rstrip('\n')
                if line != '':
                    if line == name:
                        name_found = True
                        more_enteries = False
                else:
                    more_enteries = False
        return name_found

    # Store the players name and score in a text file
    def store_name(self, name, score):
        if not self.check_name(name):
            with open(self._file_name, 'a') as wf:
                wf.write(name + "," + score + "\n")

    # Retrieving names and score from the text file
    def get_names(self):
        names = []
        name_list = []  # This list consists of name and score, in the future it will consist of name, score, how many times the player played, percentage of winning.
        more_enteries = True
        with open(self._file_name, 'r') as rf:
            while more_enteries:
                line = rf.readline().rstrip('\n')
                if line != '':
                    name_list = line.split(',')
                    names.append(name_list)
                else:
                    more_enteries = False
        return names
