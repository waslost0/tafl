import os
DOT_PATH = 'C:/Users/Zver/Desktop/TAaFL-master/lw1/TransformationAutomat/TransformationAutomat/Graphviz/bin/'

class GraphView:
    def __init__(self, output_data, size, automat_name):
        self.output_data = output_data
        self.size = size
        self.automat_name = automat_name
        self.graph_file_name = 'graph.dot'

        self.edge = []
        self.weights = []

    def graph_view(self):
        x = 0
        index = 0
        for i, line in enumerate(self.output_data):
            if i % self.size == 0 and i != 0:
                x += 1
                index = 0

            if self.automat_name == 'mealy':
                self.weights.append(f'x{str(x)}y{str(line[1])}')
                self.edge.append([index, line[0]])
            else:
                self.weights.append(f'x{str(x)}')
                self.edge.append([index, line])
            index += 1

    def configure_graph_file(self):
        sorted_zip = sorted(zip(self.edge, self.weights), key=lambda x: x[0][0])
        out_line = 'digraph {\n'
        for edge, weight in sorted_zip:
            out_line += f'\t{edge[0]} -> {edge[1]}[label={weight}];\n'
        out_line += '}'
        with open(f'{self.graph_file_name}', 'w') as file:
            file.write(out_line)

    def convert_graphfile_to_png(self):
        os.system(f'{DOT_PATH}dot -Tpng -o graph.png {self.graph_file_name}')