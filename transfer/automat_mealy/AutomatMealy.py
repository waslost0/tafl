import os
import itertools
DOT_PATH = 'C:/Users/Zver/Desktop/TAaFL-master/lw1/TransformationAutomat/TransformationAutomat/Graphviz/bin/'


class AutomatMealy:
    def __init__(self, output_file_name, input_size, state_count, input_edge):
        """ Constructor"""
        self.output_file_name = output_file_name
        self.graph_file_name = 'graph.dot'
        self.state_count = int(state_count)
        self.input_edge = input_edge
        self.input_size = int(input_size)
        self.output_state = []
        self.unique_edges = []
        self.vertex_index = []
        self.edge_weight = []

    @staticmethod
    def convert_graphfile_to_png(graph_file_name):
        os.system(f'{DOT_PATH}dot -Tpng -o graph.png {graph_file_name}')

    def configure_graph_file(self):
        sorted_zip = sorted(zip(self.vertex_index, self.edge_weight), key=lambda x: x[0][0])
        out_line = 'digraph {\n'
        for edge, weight in sorted_zip:
            out_line += f'\t{edge[0]} -> {edge[1]}[label={weight}];\n'
        out_line += '}'
        with open(f'{self.graph_file_name}', 'w') as file:
            file.write(out_line)

    def graph_view(self):
        x = 0
        index = 0
        for i, line in enumerate(self.output_state):
            if i % len(self.unique_edges) == 0 and i != 0:
                x += 1
                index = 0

            self.edge_weight.append(f'x{str(x)}')
            self.vertex_index.append([index, line])
            index += 1

    def transfer_automat(self):
        sorted_edges = sorted(self.input_edge)
        self.unique_edges = list(sorted_edges for sorted_edges, _ in itertools.groupby(sorted_edges))
        self.output_state = [0] * (len(self.unique_edges) * self.input_size)

        for i in range(0, len(self.unique_edges)):
            index_edge = i
            search_index = self.unique_edges[i][0]
            for j in range(0, self.input_size):
                it = self.input_edge[search_index]
                self.output_state[index_edge] = self.unique_edges.index(it)
                if j < self.input_size - 1:
                    index_edge += len(self.unique_edges)
                    search_index += self.state_count

    def write_result_to_file(self):
        line = ''
        with open(f'{self.output_file_name}', 'w') as file:
            for i, item in enumerate(self.output_state):
                if i % len(self.unique_edges) == 0 and i != 0:
                    line += '\n'
                line += 'z' + str(item) + ' '
            file.write(line)
