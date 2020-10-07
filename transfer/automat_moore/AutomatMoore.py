
import os
DOT_PATH = 'C:/Users/Zver/Desktop/TAaFL-master/lw1/TransformationAutomat/TransformationAutomat/Graphviz/bin/'


class AutomatMoore:
    def __init__(self, output_file_name, state_count, output_characters, moore_data):
        """ Constructor"""
        self.output_file_name = output_file_name
        self.graph_file_name = 'graph.dot'
        self.state_count = int(state_count)
        self.output_characters = output_characters
        self.moore_data = moore_data
        self.m_transition = []
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
        for i, line in enumerate(self.m_transition):
            if i % self.state_count == 0 and i != 0:
                x += 1
                index = 0

            self.edge_weight.append(f'x{str(x)}y{str(line[1])}')
            self.vertex_index.append([index, line[0]])
            index += 1

    def transfer_automat(self):
        for i, _ in enumerate(self.moore_data):
            for j, _ in enumerate(self.output_characters):
                current_state = self.moore_data[i][j]
                self.m_transition.append([current_state, self.output_characters[current_state]])

    def write_result_to_file(self):
        line = ''
        with open(f'{self.output_file_name}', 'w') as file:
            for i, node in enumerate(self.m_transition):
                if i % self.state_count == 0 and i != 0:
                    line += '\n'
                line += 'q' + str(node[0]) + 'y' + str(node[1]) + ' '
            file.write(line)
