from readinput import ReadInput
from graph import Graph

# read the input from the file
readinput = ReadInput()
readinput.get_file_name()
readinput.read_file()

# build the graph
graph = Graph()
graph.read_matrix_to_graph(readinput.matrix)
graph.find_adjacent()
# check input
if graph.start is None or graph.end is None:
    print "Invalid input.  Missing start or end."
else:
    #graph.bfs()
    graph.dfs(graph.start)  # use DFS instead of BFS
    graph.calc_shortest_path(graph.end)  # get the path from DFS
    # see if a path exists
    if len(graph.shortest_path) == 0:
        print "Could not find path."
    else:
        readinput.set_path(graph.shortest_path)
        readinput.print_file_matrix()
        graph.print_shortest_path()