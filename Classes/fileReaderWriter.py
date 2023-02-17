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

    # Store the players name in a text file
    def store_name(self, name):
        if not self.check_name(name):
            with open(self._file_name, 'a') as wf:
                wf.write(name + "\n")

    # Retrieving names from the text file
    def get_names(self):
        names = []
        more_enteries = True
        with open(self._file_name, 'r') as rf:
            while more_enteries:
                line = rf.readline().rstrip('\n')
                if line != '':
                    names.append(line)
                else:
                    more_enteries = False
        return names
