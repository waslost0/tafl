from minimization_automat import MinimizationAutomat
from visualization import GraphView


class AutomatMealy:
    def __init__(self, automat_name, output_file_name, input_size, state_count, input_edges):
        """ Constructor"""
        self.output_file_name = output_file_name
        self.input_size = input_size
        self.graph_file_name = 'graph.dot'
        self.state_count = int(state_count)
        self.input_edges = input_edges
        self.automat_name = automat_name
        self.m_transition = []
        self.vertex_index = []
        self.edge_weight = []

        self.output_state_mealy = []
        self.output_character_mealy = []
        self.output_state_size = 0

    def graph_view(self):
        graph_view = GraphView(self.output_state_mealy, self.output_state_size, self.automat_name)
        graph_view.graph_view()
        graph_view.configure_graph_file()

    def minimization_automat(self):
        minimization = MinimizationAutomat(
            self.automat_name,
            self.input_size,
            self.state_count,
            self.input_edges
        )
        self.output_state_mealy = minimization.minimization_mealy()
        self.output_state_size = len(minimization.group_previous)

    def print_info(self):
        line = ''

        with open(f'{self.output_file_name}', 'w') as file:
            for i, item in enumerate(self.output_state_mealy):
                if i % self.output_state_size == 0 and i != 0:
                    line += '\n'
                line += 'q' + str(item[0]) + '/' + str(item[1]) + ' '
            file.write(line)
