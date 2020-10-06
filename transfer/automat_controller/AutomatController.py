from automat_mealy.AutomatMealy import AutomatMealy
from automat_moore.AutomatMoore import AutomatMoore

from base_logger import logger
import re


class AutomatController:
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.file_output = file_output
        self.automat_info = {
                'input_size': '',
                'output_size': '',
                'state_count': '',
                'name_automat': ''
            }

    def process_command(self):
        input_data = self.read_data_from_file()

        if not input_data:
            return

        self.get_automat_config(input_data)
        logger.debug(self.automat_info)

        if self.automat_info['name_automat'] == 'moore':
            output_character = []
            moore_data = []
            output_character = self.fill_output_state(self.automat_info['state_count'], input_data)
            moore_data = self.fill_data_moore(input_data)
            logger.debug(moore_data)
            logger.debug(output_character)

            automat_moore = AutomatMoore(
                self.file_output,
                self.automat_info['state_count'],
                output_character,
                moore_data
                )
            automat_moore.transfer_automat()
            automat_moore.write_result_to_file()
            automat_moore.graph_view()
            automat_moore.configure_graph_file()
            automat_moore.convert_graphfile_to_png(automat_moore.graph_file_name)
        elif self.automat_info['name_automat'] == 'mealy':
            input_edges = self.fill_data_mealy(input_data)
            print(input_edges)

            automat_mealy = AutomatMealy(
                self.file_output,
                self.automat_info['input_size'],
                self.automat_info['state_count'],
                input_edges
                )
            automat_mealy.transfer_automat()
            automat_mealy.write_result_to_file()
            automat_mealy.graph_view()
            automat_mealy.configure_graph_file()
            automat_mealy.convert_graphfile_to_png(automat_mealy.graph_file_name)

    def fill_data_mealy(self, input_data):
        input_edge = []
        imput_string = ' '.join(line for line in input_data)

        for line in imput_string.split():
            input_edge.append(list(int(item) for item in re.findall(r'\d+', line)))
        return input_edge

    def fill_data_moore(self, input_data):
        moore_data = []
        try:
            for line in input_data:
                moore_data.append([int(value) for value in line.replace('q', '').split()])
        except ValueError as error:
            logger.error(error)
            raise error
        else:
            return moore_data

    def read_data_from_file(self) -> list:
        try:
            with open(self.file_input) as input_file:
                input_data = input_file.read().splitlines()
        except FileNotFoundError as error:
            logger.error(error)
            raise error
        else:
            return input_data

    def fill_output_state(self, state_count, input_data):
        output_characters = []
        try:
            output_characters = [int(value) for value in input_data.pop(0).replace('y', '').split()]
        except (IndexError, ValueError) as error:
            logger.error(error)
            raise error
        else:
            return output_characters

    def get_automat_config(self, input_data) -> list:
        try:
            for i, key in enumerate(self.automat_info):
                self.automat_info[key] = input_data.pop(0)
        except IndexError as error:
            logger.error(error)
            raise error
