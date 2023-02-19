class FileRW:
    def __init__(self, file_name):
        self._file_name = file_name

    # Check whether the name is already in the file
    def check_name(self, name) -> bool:
        name_found = False
        names = self.get_names()
        for line in names:
            if line[0] == name:
                name_found = True
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

    def update_wins(self, name, wins):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                line[1] = wins  # Updating the score of the player
        self.store_names(names)

    def store_names(self, names):
        with open(self._file_name, "w") as wf:
            for name in names:
                wf.write(name[0] + "," + name[1] + "\n")

    def get_wins(self, name):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                return line[1]
