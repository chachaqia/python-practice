# COMP9021 22T3
# Assignment 2 *** Due Monday Week 11 @ 10.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# IMPORT ANY REQUIRED MODULE
import sys
from copy import deepcopy


class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze:
    map = []
    map_grid = []
    map_grid_upgrade = []
    map_grid_upgrade_x_dim = 0
    map_grid_upgrade_y_dim = 0
    map_grid_upgrade_gate = []
    gate_count_result = 0
    map_grid_upgrade_duplicate = []
    wall_count = []
    pointer = 0
    wall_count_result = 0
    map_grid_upgrade_area = []
    accessible_area_result = 0
    map_grid_upgrade_accessible_area = []
    inaccessible_area_point_result = 0
    map_grid_upgrade_inaccessible_area = []
    map_grid_upgrade_accessible_culdesacs = []
    culdesacs_nodes = []
    culdesacs_sets_result = 0
    entry_exit_path_result = 0
    map_grid_upgrade_entry_exit_area = []
    entry_exit_path_node = []
    entry_exit_path_color_map = []

    def __init__(self, filename):
        self.filename = filename
        file = open(self.filename)
        while True:
            text = file.readline()
            if not text:
                break
            text = text.replace(' ', '')
            text = text.replace('\n', '')
            self.map.append(text)
        file.close()

        n = 0
        for i in self.map:
            if i == "":
                continue
            self.map_grid.append([])
            for j in i:
                self.map_grid[n].append(int(j))
            n += 1

        length = len(self.map_grid[0])
        for i in self.map_grid:
            if len(i) != length:
                raise MazeError('Incorrect input.')
            for j in i:
                if j not in [0, 1, 2, 3]:
                    raise MazeError('Incorrect input.')

        if len(self.map_grid) < 2 or len(self.map_grid) > 41:
            raise MazeError('Incorrect input.')
        if length < 2 or length > 31:
            raise MazeError('Incorrect input.')

        for i in self.map_grid[len(self.map_grid) - 1]:
            if i == 2 or i == 3:
                raise MazeError('Input does not represent a maze.')

        for i in range(len(self.map_grid)):
            if self.map_grid[i][length - 1] == 1 or self.map_grid[i][length - 1] == 3:
                raise MazeError('Input does not represent a maze.')

        for i in range(len(self.map_grid) * 2):
            self.map_grid_upgrade.append([])

        y = 0
        for i in self.map_grid:
            for j in i:
                if j == 0:
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y].append(1)
                    self.map_grid_upgrade[y + 1].append(1)
                    self.map_grid_upgrade[y + 1].append(1)
                elif j == 1:
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y + 1].append(1)
                    self.map_grid_upgrade[y + 1].append(1)
                elif j == 2:
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y].append(1)
                    self.map_grid_upgrade[y + 1].append(0)
                    self.map_grid_upgrade[y + 1].append(1)
                elif j == 3:
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y].append(0)
                    self.map_grid_upgrade[y + 1].append(0)
                    self.map_grid_upgrade[y + 1].append(1)
            y += 2

    def find_wall(self, y, x):
        if self.map_grid_upgrade_duplicate[y][x] == 1:
            return
        else:
            self.wall_count[self.pointer].append([y, x])
            self.map_grid_upgrade_duplicate[y][x] = 1
        # top find
        if y - 1 >= 0:
            self.find_wall(y - 1, x)
        # bottom find
        if y + 1 <= self.map_grid_upgrade_y_dim - 1:
            self.find_wall(y + 1, x)
        # left find
        if x - 1 >= 0:
            self.find_wall(y, x - 1)
        # right find
        if x + 1 <= self.map_grid_upgrade_x_dim - 1:
            self.find_wall(y, x + 1)
        return

    def find_area(self, y, x):
        if self.map_grid_upgrade_duplicate[y][x] != 1:
            return
        else:
            self.map_grid_upgrade_area[self.pointer].append([y, x])
            self.map_grid_upgrade_duplicate[y][x] = 2
        # top find
        if y - 1 >= 0:
            self.find_area(y - 1, x)
        # bottom find
        if y + 1 <= self.map_grid_upgrade_y_dim - 2:
            self.find_area(y + 1, x)
        # left find
        if x - 1 >= 0:
            self.find_area(y, x - 1)
        # right find
        if x + 1 <= self.map_grid_upgrade_x_dim - 2:
            self.find_area(y, x + 1)
        return

    def colour_culdesacs(self, current_node, arrived_area_set):
        if current_node not in arrived_area_set or self.map_grid_upgrade_duplicate[current_node[0]][
            current_node[1]] == 2:
            return
        count = 0
        if self.map_grid_upgrade_duplicate[current_node[0]][current_node[1] + 1] == 0:
            count += 1
        if self.map_grid_upgrade_duplicate[current_node[0]][current_node[1] - 1] == 0:
            count += 1
        if self.map_grid_upgrade_duplicate[current_node[0] + 1][current_node[1]] == 0:
            count += 1
        if self.map_grid_upgrade_duplicate[current_node[0] - 1][current_node[1]] == 0:
            count += 1
        if count == 3:
            self.map_grid_upgrade_duplicate[current_node[0]][current_node[1]] = 2
            self.map_grid_upgrade_duplicate[current_node[0]][current_node[1] + 1] = 0
            self.map_grid_upgrade_duplicate[current_node[0]][current_node[1] - 1] = 0
            self.map_grid_upgrade_duplicate[current_node[0] + 1][current_node[1]] = 0
            self.map_grid_upgrade_duplicate[current_node[0] - 1][current_node[1]] = 0

            if current_node[0] + 2 <= self.map_grid_upgrade_y_dim - 1:
                self.colour_culdesacs([current_node[0] + 2, current_node[1]], arrived_area_set)
            if current_node[1] + 2 <= self.map_grid_upgrade_x_dim - 1:
                self.colour_culdesacs([current_node[0], current_node[1] + 2], arrived_area_set)
            if current_node[1] - 2 >= 1:
                self.colour_culdesacs([current_node[0], current_node[1] - 2], arrived_area_set)
            if current_node[0] - 2 >= 1:
                self.colour_culdesacs([current_node[0] - 2, current_node[1]], arrived_area_set)
            return
        else:
            return

            # POSSIBLY DEFINE OTHER METHODS

    def find_culdesacs(self, curent_node):
        if curent_node not in self.culdesacs_nodes:
            return
        if self.map_grid_upgrade_duplicate[curent_node[0]][curent_node[1]] == 3:
            return
        else:
            self.map_grid_upgrade_accessible_culdesacs[self.pointer].append(curent_node)
            self.map_grid_upgrade_duplicate[curent_node[0]][curent_node[1]] = 3
            if curent_node[0] - 2 >= 1:
                if self.map_grid_upgrade_duplicate[curent_node[0] - 1][curent_node[1]] == 1:
                    self.find_culdesacs([curent_node[0] - 2, curent_node[1]])
            if curent_node[0] + 2 <= self.map_grid_upgrade_y_dim - 1:
                if self.map_grid_upgrade_duplicate[curent_node[0] + 1][curent_node[1]] == 1:
                    self.find_culdesacs([curent_node[0] + 2, curent_node[1]])
            if curent_node[1] - 2 >= 1:
                if self.map_grid_upgrade_duplicate[curent_node[0]][curent_node[1] - 1] == 1:
                    self.find_culdesacs([curent_node[0], curent_node[1] - 2])
            if curent_node[1] + 2 <= self.map_grid_upgrade_x_dim - 1:
                if self.map_grid_upgrade_duplicate[curent_node[0]][curent_node[1] + 1] == 1:
                    self.find_culdesacs([curent_node[0], curent_node[1] + 2])
            return

    def analyse(self):
        self.map_grid_upgrade_y_dim = len(self.map_grid_upgrade)
        self.map_grid_upgrade_x_dim = len(self.map_grid_upgrade[0])
        # find number of gates
        for i in range(self.map_grid_upgrade_x_dim - 1):
            if self.map_grid_upgrade[0][i] == 1:
                self.gate_count_result += 1
                self.map_grid_upgrade_gate.append([0, i])
        for i in range(self.map_grid_upgrade_x_dim - 1):
            if self.map_grid_upgrade[self.map_grid_upgrade_y_dim - 2][i] == 1:
                self.gate_count_result += 1
                self.map_grid_upgrade_gate.append([self.map_grid_upgrade_y_dim - 2, i])
        for i in range(1, self.map_grid_upgrade_y_dim - 1):
            if self.map_grid_upgrade[i][0] == 1:
                self.gate_count_result += 1
                self.map_grid_upgrade_gate.append([i, 0])
            if self.map_grid_upgrade[i][self.map_grid_upgrade_x_dim - 2] == 1:
                self.gate_count_result += 1
                self.map_grid_upgrade_gate.append([i, self.map_grid_upgrade_x_dim - 2])
        if self.gate_count_result == 0:
            print("The maze has no gate.")
        elif self.gate_count_result == 1:
            print("The maze has a single gate.")
        else:
            print("The maze has %d gates." % self.gate_count_result)

        # find number of wall
        self.map_grid_upgrade_duplicate = deepcopy(self.map_grid_upgrade)
        for y in range(self.map_grid_upgrade_y_dim - 1):
            for x in range(self.map_grid_upgrade_x_dim - 1):
                if self.map_grid_upgrade_duplicate[y][x] == 0:
                    self.wall_count.append([])
                    self.find_wall(y, x)
                    self.pointer += 1
        for i in self.wall_count:
            if len(i) != 1:
                self.wall_count_result += 1
        if self.wall_count_result == 0:
            print("The maze has no wall.")
        elif self.wall_count_result == 1:
            print("The maze has walls that are all connected.")
        else:
            print("The maze has %d sets of walls that are all connected." % self.wall_count_result)

        # find all areas:
        self.map_grid_upgrade_duplicate = deepcopy(self.map_grid_upgrade)
        self.pointer = 0
        for y in range(self.map_grid_upgrade_y_dim - 1):
            for x in range(self.map_grid_upgrade_x_dim - 1):
                if self.map_grid_upgrade[y][x] == 1:
                    self.map_grid_upgrade_area.append([])
                    self.find_area(y, x)
                    self.pointer += 1

        # find accessible areas and inaccessible inner pointers:
        for i in self.map_grid_upgrade_area:
            judge = 0
            for j in i:
                if j in self.map_grid_upgrade_gate:
                    self.map_grid_upgrade_accessible_area.append(i)
                    self.accessible_area_result += 1
                    judge = 1
                    break
            if judge == 0:
                self.map_grid_upgrade_inaccessible_area.append(i)

        for i in self.map_grid_upgrade_inaccessible_area:
            for j in i:
                if j[0] % 2 == 1 and j[1] % 2 == 1:
                    self.inaccessible_area_point_result += 1

        if self.inaccessible_area_point_result == 0:
            print("The maze has no inaccessible inner point.")
        elif self.inaccessible_area_point_result == 1:
            print("The maze has a unique inaccessible inner point.")
        else:
            print("The maze has %d inaccessible inner points." % self.inaccessible_area_point_result)

        if self.accessible_area_result == 0:
            print("The maze has no accessible area.")
        elif self.accessible_area_result == 1:
            print("The maze has a unique accessible area.")
        else:
            print("The maze has %d accessible areas." % self.accessible_area_result)

        # find the number of accessible cul-de-sacs
        self.map_grid_upgrade_duplicate = deepcopy(self.map_grid_upgrade)

        for i in self.map_grid_upgrade_accessible_area:
            for j in i:
                count = 0
                if self.map_grid_upgrade_duplicate[j[0]][j[1] + 1] == 0:
                    count += 1
                if self.map_grid_upgrade_duplicate[j[0]][j[1] - 1] == 0:
                    count += 1
                if self.map_grid_upgrade_duplicate[j[0] + 1][j[1]] == 0:
                    count += 1
                if self.map_grid_upgrade_duplicate[j[0] - 1][j[1]] == 0:
                    count += 1
                if count == 3 and j[0] % 2 == 1 and j[1] % 2 == 1 and self.map_grid_upgrade_duplicate[j[0]][j[1]] != 2:
                    self.map_grid_upgrade_duplicate[j[0]][j[1] + 1] = 0
                    self.map_grid_upgrade_duplicate[j[0]][j[1] - 1] = 0
                    self.map_grid_upgrade_duplicate[j[0] + 1][j[1]] = 0
                    self.map_grid_upgrade_duplicate[j[0] - 1][j[1]] = 0
                    self.map_grid_upgrade_duplicate[j[0]][j[1]] = 2

                    if j[0] + 2 <= self.map_grid_upgrade_y_dim - 1:
                        self.colour_culdesacs([j[0] + 2, j[1]], i)
                    if j[1] + 2 <= self.map_grid_upgrade_x_dim - 1:
                        self.colour_culdesacs([j[0], j[1] + 2], i)
                    if j[1] - 2 >= 1:
                        self.colour_culdesacs([j[0], j[1] - 2], i)
                    if j[0] - 2 >= 1:
                        self.colour_culdesacs([j[0] - 2, j[1]], i)

        for y in range(self.map_grid_upgrade_y_dim - 1):
            for x in range(self.map_grid_upgrade_x_dim - 1):
                if self.map_grid_upgrade_duplicate[y][x] == 2:
                    self.culdesacs_nodes.append([y, x])

        self.entry_exit_path_color_map = deepcopy(self.map_grid_upgrade_duplicate)
        self.map_grid_upgrade_duplicate = deepcopy(self.map_grid_upgrade)
        for i in self.culdesacs_nodes:
            self.map_grid_upgrade_duplicate[i[0]][i[1]] = 2

        self.pointer = 0
        for i in self.culdesacs_nodes:
            count = 0
            if self.map_grid_upgrade_duplicate[i[0]][i[1] + 1] == 0:
                count += 1
            if self.map_grid_upgrade_duplicate[i[0]][i[1] - 1] == 0:
                count += 1
            if self.map_grid_upgrade_duplicate[i[0] + 1][i[1]] == 0:
                count += 1
            if self.map_grid_upgrade_duplicate[i[0] - 1][i[1]] == 0:
                count += 1
            if count == 3 and self.map_grid_upgrade_duplicate[i[0]][i[1]] != 3:
                self.map_grid_upgrade_duplicate[i[0]][i[1]] = 3
                self.map_grid_upgrade_accessible_culdesacs.append([])
                self.map_grid_upgrade_accessible_culdesacs[self.pointer].append(i)
                if i[0] - 2 >= 1 and self.map_grid_upgrade_duplicate[i[0] - 1][i[1]] == 1:
                    self.find_culdesacs([i[0] - 2, i[1]])
                if i[0] + 2 <= self.map_grid_upgrade_y_dim - 1 and self.map_grid_upgrade_duplicate[i[0] + 1][i[1]] == 1:
                    self.find_culdesacs([i[0] + 2, i[1]])
                if i[1] - 2 >= 1 and self.map_grid_upgrade_duplicate[i[0]][i[1] - 1] == 1:
                    self.find_culdesacs([i[0], i[1] - 2])
                if i[1] + 2 <= self.map_grid_upgrade_x_dim - 1 and self.map_grid_upgrade_duplicate[i[0]][i[1] + 1] == 1:
                    self.find_culdesacs([i[0], i[1] + 2])
                self.pointer += 1

        self.culdesacs_sets_result = len(self.map_grid_upgrade_accessible_culdesacs)
        if self.culdesacs_sets_result == 0:
            print("The maze has no accessible cul-de-sac.")
        elif self.culdesacs_sets_result == 1:
            print("The maze has accessible cul-de-sacs that are all connected.")
        else:
            print("The maze has %d sets of accessible cul-de-sacs that are all connected." % self.culdesacs_sets_result)

        # find entry-exit path
        for i in self.map_grid_upgrade_accessible_area:
            count = 0
            for j in i:
                if j in self.map_grid_upgrade_gate:
                    count += 1
            if count == 2:
                self.entry_exit_path_result += 1
                self.map_grid_upgrade_entry_exit_area.append(i)

        for i in self.map_grid_upgrade_entry_exit_area:
            for j in self.culdesacs_nodes:
                if j in i:
                    i.remove(j)

        for i in self.map_grid_upgrade_entry_exit_area:
            for j in i:
                count = 0
                if j[0] % 2 == 1 and j[1] % 2 == 1:
                    if self.entry_exit_path_color_map[j[0]][j[1] + 1] == 1:
                        count += 1
                    if self.entry_exit_path_color_map[j[0]][j[1] - 1] == 1:
                        count += 1
                    if self.entry_exit_path_color_map[j[0] + 1][j[1]] == 1:
                        count += 1
                    if self.entry_exit_path_color_map[j[0] - 1][j[1]] == 1:
                        count += 1
                if count > 2:
                    self.map_grid_upgrade_entry_exit_area.remove(i)
                    self.entry_exit_path_result -= 1
                    break

        if self.entry_exit_path_result == 0:
            print("The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif self.entry_exit_path_result == 1:
            print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        else:
            print(
                "The maze has %d entry-exit paths with no intersections not to cul-de-sacs." % self.entry_exit_path_result)

    def display(self):
        somefile = self.filename[0: -4]
        with open('%s.tex' % somefile, 'w') as file:
            file.write('\\documentclass[10pt]{article}\n')
            file.write('\\usepackage{tikz}\n')
            file.write('\\usetikzlibrary{shapes.misc}\n')
            file.write('\\usepackage[margin=0cm]{geometry}\n')
            file.write('\\pagestyle{empty}\n')
            file.write('\\tikzstyle{every node}=[cross out, draw, red]\n\n')
            file.write('\\begin{document}\n\n')
            file.write('\\vspace*{\\fill}\n')
            file.write('\\begin{center}\n')
            file.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n% Walls\n')
            # draw wall
            y1, y2 = 0, 1
            x1, x2 = 0, 1
            while y1 < self.map_grid_upgrade_y_dim:
                while x2 < self.map_grid_upgrade_x_dim:
                    if self.map_grid_upgrade[y1][x1] == 0 and self.map_grid_upgrade[y1][x2] == 0:
                        start = x1 / 2
                        while 1:
                            x1 += 2
                            x2 += 2
                            if self.map_grid_upgrade[y1][x1] != 0 or \
                                    self.map_grid_upgrade[y1][x2] != 0:
                                break
                        end = x1 / 2
                        file.write('    \\draw (%d,%d) -- (%d,%d);\n' % (start, y1 / 2, end, y1 / 2))
                    x1 += 2
                    x2 += 2
                y1 += 2
                x1, x2 = 0, 1

            y1, y2 = 0, 1
            x1, x2 = 0, 1
            while x1 < self.map_grid_upgrade_x_dim:
                while y2 < self.map_grid_upgrade_y_dim:
                    if self.map_grid_upgrade[y1][x1] == 0 and self.map_grid_upgrade[y2][x1] == 0:
                        start = y1 / 2
                        while 1:
                            y2 += 2
                            y1 += 2
                            if self.map_grid_upgrade[y1][x1] != 0 or \
                                    self.map_grid_upgrade[y2][x1] != 0:
                                break
                        end = y1 / 2
                        file.write('    \\draw (%d,%d) -- (%d,%d);\n' % (x1 / 2, start, x1 / 2, end))
                    y1 += 2
                    y2 += 2
                x1 += 2
                y1, y2 = 0, 1

            # draw pillar
            file.write('% Pillars\n')
            y = 0
            while y < self.map_grid_upgrade_y_dim - 1:
                x = 0
                while x < self.map_grid_upgrade_x_dim - 1:
                    if x == 0 and y == 0:
                        if self.map_grid_upgrade[y + 1][x] == 1 \
                                and self.map_grid_upgrade[y][x + 1] == 1:
                            file.write('    \\fill[green] (%d,%d) circle(0.2);\n' % (x / 2, y / 2))

                    elif x == 0 and y != 0:
                        if self.map_grid_upgrade[y + 1][x] == 1 \
                                and self.map_grid_upgrade[y - 1][x] == 1 \
                                and self.map_grid_upgrade[y][x + 1] == 1:
                            file.write('    \\fill[green] (%d,%d) circle(0.2);\n' % (x / 2, y / 2))

                    elif x != 0 and y == 0:
                        if self.map_grid_upgrade[y + 1][x] == 1 \
                                and self.map_grid_upgrade[y][x + 1] == 1 \
                                and self.map_grid_upgrade[y][x - 1] == 1:
                            file.write('    \\fill[green] (%d,%d) circle(0.2);\n' % (x / 2, y / 2))

                    else:
                        if self.map_grid_upgrade[y + 1][x] == 1 \
                                and self.map_grid_upgrade[y][x + 1] == 1 \
                                and self.map_grid_upgrade[y - 1][x] == 1 \
                                and self.map_grid_upgrade[y][x - 1] == 1:
                            file.write('    \\fill[green] (%d,%d) circle(0.2);\n' % (x / 2, y / 2))
                    x += 2
                y += 2

            # draw accessible cul-de-sacs
            file.write('% Inner points in accessible cul-de-sacs\n')
            for i in self.culdesacs_nodes:
                file.write('    \\node at (%.01f,%.01f) {};\n' % (i[1] / 2, i[0] / 2))

            # draw Entry-exit paths without intersections
            file.write('% Entry-exit paths without intersections\n')

            for i in self.map_grid_upgrade_entry_exit_area:
                for j in i:
                    self.entry_exit_path_node.append(j)

            for i in range(self.map_grid_upgrade_y_dim - 1):
                if self.entry_exit_path_color_map[i][self.map_grid_upgrade_x_dim - 2] == 1:
                    self.entry_exit_path_node.append([i, self.map_grid_upgrade_x_dim - 1])
            for i in range(self.map_grid_upgrade_x_dim - 1):
                if self.entry_exit_path_color_map[self.map_grid_upgrade_y_dim - 2][i] == 1:
                    self.entry_exit_path_node.append([self.map_grid_upgrade_y_dim - 1, i])

            y1, y2 = 0, 1
            x1, x2 = 0, 1
            while y2 < self.map_grid_upgrade_y_dim:
                while x2 < self.map_grid_upgrade_x_dim:
                    if self.entry_exit_path_color_map[y2][x1] == 1 and self.entry_exit_path_color_map[y2][x2] == 1 \
                            and [y2, x1] in self.entry_exit_path_node and [y2, x2] in self.entry_exit_path_node:
                        start = (x1 - 1) / 2
                        while x2 < self.map_grid_upgrade_x_dim:
                            x1 += 2
                            x2 += 2
                            if x2 >= self.map_grid_upgrade_x_dim:
                                break
                            if self.entry_exit_path_color_map[y2][x1] != 1 or self.entry_exit_path_color_map[y2][
                                x2] != 1 \
                                    or [y2, x1] not in self.entry_exit_path_node \
                                    or [y2, x2] not in self.entry_exit_path_node:
                                break
                        end = (x1 - 1) / 2
                        file.write('    \\draw[dashed, yellow] (%0.1f,%0.1f) -- (%0.1f,%0.1f);\n' % (
                        start, y2 / 2, end, y2 / 2))
                    x1 += 2
                    x2 += 2
                y2 += 2
                x1, x2 = 0, 1

            y1, y2 = 0, 1
            x1, x2 = 0, 1
            while x2 < self.map_grid_upgrade_x_dim:
                while y1 < self.map_grid_upgrade_y_dim:
                    if self.entry_exit_path_color_map[y1][x2] == 1 and self.entry_exit_path_color_map[y2][x2] == 1 \
                            and [y1, x2] in self.entry_exit_path_node and [y2, x2] in self.entry_exit_path_node:
                        start = (y1 - 1) / 2
                        while y2 < self.map_grid_upgrade_y_dim:
                            y2 += 2
                            y1 += 2
                            if y2 >= self.map_grid_upgrade_y_dim:
                                break
                            if self.entry_exit_path_color_map[y1][x2] != 1 or self.entry_exit_path_color_map[y2][
                                x2] != 1 \
                                    or [y1, x2] not in self.entry_exit_path_node \
                                    or [y2, x2] not in self.entry_exit_path_node:
                                break
                        end = (y1 - 1) / 2
                        file.write('    \\draw[dashed, yellow] (%0.1f,%0.1f) -- (%0.1f,%0.1f);\n' % (
                        x2 / 2, start, x2 / 2, end))
                    y1 += 2
                    y2 += 2
                x2 += 2
                y1, y2 = 0, 1

            file.write('\\end{tikzpicture}\n')
            file.write('\\end{center}\n')
            file.write('\\vspace*{\\fill}\n\n')
            file.write('\\end{document}')


if __name__ == '__main__':
    maze = Maze('maze_1.txt')
    maze.analyse()
    maze.display()
