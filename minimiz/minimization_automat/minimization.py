
class MinimizationAutomat:
    def __init__(self, automat_name, input_size, state_count, automat_data, output_characters=''):
        """ Constructor"""
        self.automat_name = automat_name
        self.input_size = int(input_size)
        self.state_count = int(state_count)
        self.output_characters = output_characters
        self.input_edge = automat_data
        self.output_state_moore = []

        self.output_character_moore = []
        self.output_character_mealy = []

        self.group_vector = []
        self.group_previous = []
        self.output_state = []

    def minimization_moore(self):
        group_edge = self.getting_group_moore()
        group_previous_edge = self.getting_group_previous_edge(group_edge)
        output_state_moore = self.fillout_moore(group_previous_edge)
        return output_state_moore

    def minimization_mealy(self):
        group_vector = self.getting_group(self.input_edge)
        group_edge = self.getting_group_edge(group_vector)
        group_previous_edge = self.getting_group_previous_edge(group_edge)

        output_state_mealy = self.fillout_mealy(group_previous_edge)
        return output_state_mealy

    def get_output_state_size(self):
        pass

    def get_output_character_moore(self):
        pass

    def fillout_mealy(self, group_previous_edge):
        size = len(self.group_previous)
        self.output_state_moore = [[None, None] for _ in range(0, size * self.input_size)]

        for i in range(0, size):
            index_insert = i
            index_row = 0
            index_column = self.group_previous[i][0]
            self.output_character_moore.append(self.output_characters[index_column])
            for j in range(0, self.input_size):
                unit = self.input_edge[index_row][index_column]
                it = [item for item in group_previous_edge if item[1] == unit]
                if it:
                    self.output_state_moore[index_insert] = it[0][0]
                if j < self.input_size - 1:
                    index_row += 1
                    index_insert += size

        return self.output_state_moore

    def fillout_moore(self, group_previous_edge):
        size = len(self.group_previous)
        self.output_state_moore = [[None] for _ in range(0, size * self.input_size)]

        for i in range(0, size):
            index_insert = i
            index_row = 0
            index_column = self.group_previous[i][0]
            self.output_character_moore.append(self.output_characters[index_column])
            for j in range(0, self.input_size):
                unit = self.input_edge[index_row][index_column]
                it = [item for item in group_previous_edge if item[1] == unit]
                if it:
                    self.output_state_moore[index_insert] = it[0][0]
                if j < self.input_size - 1:
                    index_row += 1
                    index_insert += size

        return self.output_state_moore

    def getting_group_moore(self):
        unique = list(set(self.output_characters))
        group_edge = [[None, None] for _ in range(0, len(self.output_characters))]
        self.group_vector = [[] * i for i in range(0, len(unique))]
        for i, unicum in enumerate(unique):
            for j, out_char in enumerate(self.output_characters):
                if unicum == out_char:
                    group_edge[j] = [i, j]
                    self.group_vector[i].append(j)

        return group_edge

    def getting_group(self, input_edge):
        output = [None] * self.state_count
        for i, item in enumerate(output):
            output[i] = [None] * self.input_size

        for i in range(0, self.state_count):
            temporary = []
            index = i
            for j in range(0, self.input_size):
                temporary.append(input_edge[index][1])
                index += self.state_count
            output[i] = temporary
        return output       

    def getting_group_next(self):
        group = self.getting_group(self.output_state)
        unique = []

        for it in self.group_previous:
            setUnique = []
            for it2 in it:
                gr_temp = group[it2]
                if gr_temp not in setUnique:
                    setUnique.append(group[it2])

            for item in reversed(setUnique):
                 unique.append(item)

        group_edge = [[0, 0] for _ in range(0, self.state_count)]
        group_vector = [[] for _ in range(0, len(unique))]


        sum_ = 0
        index = 0
        for i in range(0, len(unique)):
            for j in range(0, len(self.group_previous)):

                size = len(self.group_previous[index])
                for k in range(0, size):
                    unit = self.group_previous[index][k]
                    
                    if unique[i] == group[unit]:
                        group_edge[unit] = [i, unit]
                        group_vector[i].append(unit)

                sum_ += len(group_vector[i])
                if sum_ == size:
                    sum_ = 0
                else:
                    index -= 1
                break
            index += 1
        group_vector = sorted(group_vector)

        return group_vector, group_edge

    def getting_group_previous_edge(self, group_edge):
        group_previous_edge = []
        self.output_state = [[0, 0] for _ in range(0, self.state_count * self.input_size)]

        for i in range(0, len(self.output_state)):
            group_next_edge = []
            group_next_vector = []

            if i != 0:
                group_next_vector, group_next_edge,  = self.getting_group_next()

            group_result_edge = group_edge if i == 0 else group_next_edge
    
            if self.automat_name == 'mealy':
                for j in range(0, self.state_count):
                    index_edge = j
                    unit = self.input_edge[index_edge][0]
                    for k in range(0, self.input_size):
                        it = [item for item in group_result_edge if item[1] == unit]
                        if it:
                            self.output_state[index_edge] = [0, it[0][0]]

                        if k < self.input_size - 1:
                            index_edge += 1
                            unit = self.input_edge[index_edge][0]

            else:
                for j in range(0, len(self.output_characters)):
                    index_column = 0
                    index_row = 0
                    index_column = j
                    unit = self.input_edge[index_row][index_column]
                    for k in range(0, self.input_size):
                        it = [item for item in group_result_edge if item[1] == unit]
                        #if it[0] != group_result_edge[-1]:
                        if it:
                            self.output_state[index_column] = [0, it[0][0]]

                        if k < self.input_size - 1:
                            index_row += 1
                            unit = self.input_edge[index_row][j]
                            index_column += self.state_count

            if group_previous_edge == group_result_edge:
                break
            group_previous_edge = group_result_edge

            if i == 0:
                self.group_previous = self.group_vector
            else:
                self.group_previous = group_next_vector

            a = 1
            print()
        return group_previous_edge


    def getting_group_edge(self, group):
        unique = []

        for item in group:
            print(item)
            if item not in unique:
                unique.append(item)
        unique = sorted(unique)

        group_edge = [[None, None] for _ in range(0, self.state_count)]
        self.group_vector = [[] * i for i in range(0, len(unique))]

        for i, unicum in enumerate(unique):
            for j, out_char in enumerate(group):
                if unicum == out_char:
                    group_edge[j] = [i, j]
                    self.group_vector[i].append(j)

        return group_edge
