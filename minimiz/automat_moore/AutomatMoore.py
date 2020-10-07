from minimization_automat import MinimizationAutomat
from visualization import GraphView


class AutomatMoore:
    def __init__(self, automat_name, output_file_name, input_size, state_count, output_characters, state):
        """ Constructor"""
        self.output_file_name = output_file_name
        self.input_size = input_size
        self.graph_file_name = 'graph.dot'
        self.state_count = int(state_count)
        self.output_characters = output_characters
        self.state = state
        self.automat_name = automat_name
        self.m_transition = []
        self.vertex_index = []
        self.edge_weight = []

        self.output_state_moore = []
        self.output_character_moore = []
        self.output_state_size = []

    def graph_view(self):
        graph_view = GraphView(self.output_state_moore, self.output_state_size, self.automat_name)
        graph_view.graph_view()
        graph_view.configure_graph_file()
        # graph_view.convert_graphfile_to_png()

    def minimization_automat(self):
        minimization = MinimizationAutomat(
            self.automat_name,
            self.input_size,
            self.state_count,
            self.state,
            self.output_characters
        )
        self.output_state_moore = minimization.minimization_moore()
        self.output_character_moore = minimization.output_character_moore
        self.output_state_size = len(minimization.group_previous)

    def print_info(self):
        line = ''
        with open(f'{self.output_file_name}', 'w') as file:
            for item in self.output_character_moore:
                line += 'y' + str(item) + ' '

            for i, item in enumerate(self.output_state_moore):
                if i % self.output_state_size == 0:
                    line += '\n'
                line += 'z' + str(item) + ' '
            file.write(line)







