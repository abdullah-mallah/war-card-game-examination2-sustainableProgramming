class FileRW:
    def __init__(self, file_name):
        self._file_name = file_name

    # Check whether the name is already in the file
    def check_name(self, name) -> bool:
        if self._file_name == "score.txt":
            name_found = False
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    name_found = True
            return name_found
        else:
            raise FileNotFoundError

    # Store the players name and score in a text file
    def store_name(self, name, wins, times_played, percentage):
        if self._file_name == "score.txt":
            if not self.check_name(name):
                with open(self._file_name, 'a') as wf:
                    wf.write(name + "," + wins + "," + times_played + "," +
                             percentage + "\n")
        else:
            raise FileNotFoundError

    # Retrieving names and score from the text file
    def get_names(self):
        if self._file_name == "score.txt":
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
        else:
            raise FileNotFoundError

    def get_name(self, name):
        if self._file_name == "score.txt":
            names = self.get_names()
            name_details = []
            for line in names:
                if line[0] == name:
                    name_details = line.rstrip('\n').split(',')
            return name_details
        else:
            raise FileNotFoundError

    def update_wins(self, name, wins, times_played, percentage):
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    line[1] = (str)(wins)  # Updating the score of the player
                    line[2] = (str)(times_played)
                    percentage = (wins / times_played) * 100
                    line[3] = (str)(percentage)
            self.store_names(names)
        else:
            raise FileNotFoundError

    def store_names(self, names):
        if self._file_name == "score.txt":
            with open(self._file_name, "w") as wf:
                for name in names:
                    wf.write(name[0] + "," + name[1] +
                             "," + name[2] + "," + name[3] + "\n")
        else:
            raise FileNotFoundError

    def uppdate_name(self, old_name, new_name):
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == old_name:
                    line[0] = new_name
            self.store_names(names)
        else:
            raise FileNotFoundError

    def get_wins(self, name):
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[1]
        else:
            raise FileNotFoundError

    def get_times_played(self, name):
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[2]
        else:
            raise FileNotFoundError

    def get_percentage(self, name):
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[3]
        else:
            raise FileNotFoundError
