class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}

        for i,j in edges:
            if i in self.graph_dict:
                self.graph_dict[i].append(j)
            else:
                self.graph_dict[i] = [j]

        print(self.graph_dict)

    
    def get_path(self,start,end,path=[]):

        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node,end,path)
            
                for k in new_path:
                    paths.append(k)

        return paths


if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]


k = Graph(routes)
print(k.get_path("Mumbai","Bangaluru"))
