"""
This script is used to deal with the text file.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""


class FileRW:
    """This class stores and retrieves players'information from text file."""

    def __init__(self, file_name):
        """Store file name."""
        self._file_name = file_name

    def check_name(self, name) -> bool:
        """
        Take a string as parameter.

        If name is found in text file return True else return False.
        """
        if self._file_name == "score.txt":
            name_found = False
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    name_found = True
            return name_found
        else:
            raise FileNotFoundError

    def store_name(self, name, wins, times_played, percentage):
        """
        Take 4 strings as parameter.

        Store them in one line in text file.
        """
        if self._file_name == "score.txt":
            if not self.check_name(name):
                with open(self._file_name, 'a') as wf:
                    wf.write(name + "," + wins + "," + times_played + "," +
                             percentage + "\n")
        else:
            raise FileNotFoundError

    def get_names(self):
        """Return the names of players from a text file as list."""
        if self._file_name == "score.txt":
            names = []
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
        """Take a string as parameter and return it from a text file."""
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
        """
        Take 4 strings as parameter.

        Update a name's information in text file.
        """
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    line[1] = (str)(wins)
                    line[2] = (str)(times_played)
                    percentage = (wins / times_played) * 100
                    line[3] = (str)(percentage)
            self.store_names(names)
        else:
            raise FileNotFoundError

    def store_names(self, names):
        """Take a list as parameter and store it in text file."""
        if self._file_name == "score.txt":
            with open(self._file_name, "w") as wf:
                for name in names:
                    wf.write(name[0] + "," + name[1] +
                             "," + name[2] + "," + name[3] + "\n")
        else:
            raise FileNotFoundError

    def uppdate_name(self, old_name, new_name):
        """
        Take 2 strings as parameter.

        Update a name in text file.
        """
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == old_name:
                    line[0] = new_name
            self.store_names(names)
        else:
            raise FileNotFoundError

    def get_wins(self, name):
        """
        Take 1 string as parameter.

        Retrieve the wins of a name from text file.
        """
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[1]
        else:
            raise FileNotFoundError

    def get_times_played(self, name):
        """
        Take 1 string as parameter.

        Retrieve times played of a name from text file.
        """
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[2]
        else:
            raise FileNotFoundError

    def get_percentage(self, name):
        """
        Take 1 string as parameter.

        Retrieve percentage of wins of a name from text file.
        """
        if self._file_name == "score.txt":
            names = self.get_names()
            for line in names:
                if line[0] == name:
                    return line[3]
        else:
            raise FileNotFoundError

    def get_file_name(self):
        """Return _file_name variable."""
        return self._file_name

    def set_file_name(self, file_name):
        """
        Take a string.

        Set variable _file_name to the string parameter.
        """
        self._file_name = file_name
