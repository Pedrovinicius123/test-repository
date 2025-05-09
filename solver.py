import networkx as nx
import copy, time # for debugging

def check_empty(CNF:list):
    for clause in CNF:
        if not any(clause):
            return True

    return False

def check_contradiction(CNF:list):
    for clause in CNF:
        if len(clause) == 1 and [-clause[0]] in CNF:
            return True

    return False            

class NodeGen:
    def __init__(self, max_var):
        self.max_var = max_var
        self.i = 0
        self.G = self.generate_graph()

    def generate_graph(self, G=nx.DiGraph()):
        if self.i >= self.max_var:
            return G

        G.add_edge(self.i, -self.i - 1)
        G.add_edge(self.i, self.i + 1)
        G.add_edge(-self.i, -self.i - 1)
        G.add_edge(-self.i, self.i + 1)

        self.i += 1
        return self.generate_graph(G)

    def solve(self, CNF:list, initial=0, visited=[]):
        for neighbor in self.G.neighbors(initial):
            if neighbor not in visited:
                CNF_copy = copy.deepcopy(CNF)

                for clause in CNF_copy:
                    if neighbor in clause:
                        CNF_copy.remove(clause)

                    elif -neighbor in clause:
                        clause.remove(-neighbor)

                print(CNF_copy, visited)
                time.sleep(1)
                
                if not any(CNF_copy):
                    return visited + [neighbor]
                
                
                elif not (check_contradiction(CNF_copy) or check_empty(CNF_copy)):
                    result = self.solve(CNF_copy, initial=neighbor, visited=visited + [neighbor])
                    if result:
                        return result