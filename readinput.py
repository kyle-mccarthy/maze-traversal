class ReadInput():
    def __init__(self):
        self.filename = None
        self.matrix = []

    def get_file_name(self):
        self.filename = raw_input("filename: ")
        #self.filename = "input.txt"

    def read_file(self):
        if self.filename is None:
            print "error: no file name"
            return
        try:
            f = open(self.filename, "r")
        except IOError:
            print "Invalid file."
            return
        else:
            ## parse the file to a 2D array
            for line in f.readlines():
                l = []
                for item in line:
                    l.append(item)
                self.matrix.append(l)

    def set_path(self, shortest):
        for v in shortest:
            self.matrix[v.row][v.col] = '.'

    def print_file_matrix(self):
        for r in self.matrix:
            for c in r:
                print c,




