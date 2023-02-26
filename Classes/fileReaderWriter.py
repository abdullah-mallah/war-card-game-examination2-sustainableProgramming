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
    def store_name(self, name, wins, times_played, percentage):
        if not self.check_name(name):
            with open(self._file_name, 'a') as wf:
                wf.write(name + "," + wins + "," + times_played + "," +
                         percentage + "\n")

    # Retrieving names and score from the text file
    def get_names(self):
        names = []
        # This list consists of name and score, in the future
        # it will consist of name, score, how many times the
        # player played, percentage of winning.
        name_list = []
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

    def get_name(self, name):
        names = self.get_names()
        name_details = []
        for line in names:
            if line[0] == name:
                name_details = line.rstrip('\n').split(',')
        return name_details

    def update_wins(self, name, wins, times_played, percentage):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                line[1] = (str)(wins)  # Updating the score of the player
                line[2] = (str)(times_played)
                percentage = (wins / times_played) * 100
                line[3] = (str)(percentage)
        self.store_names(names)

    def store_names(self, names):
        with open(self._file_name, "w") as wf:
            for name in names:
                wf.write(name[0] + "," + name[1] +
                         "," + name[2] + "," + name[3] + "\n")

    def uppdate_name(self, old_name, new_name):
        names = self.get_names()
        for line in names:
            if line[0] == old_name:
                line[0] = new_name
        self.store_names(names)

    def get_wins(self, name):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                return line[1]

    def get_times_played(self, name):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                return line[2]

    def get_percentage(self, name):
        names = self.get_names()
        for line in names:
            if line[0] == name:
                return line[3]
