class Node:
    def __init__(self, state, parent='', action=''):
        self.state = state
        self.parent = parent
        self.action = action


class Search:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number

    def succ(self, state):
        x = state[0]
        y = state[1]
        angle = state[2]
        angles = {0: 'UP', 90: 'RIGHT', 270: 'LEFT', 180: 'DOWN'}
        match(angles[angle]):
            case 'UP':
                possible = [['left', x, y, 270], ['right', x, y, 90]]
                if y != 0: possible.append(['move', x, y - self.cell_size, 0])
                return possible
            case 'RIGHT':
                possible = [['left', x, y, 0], ['right', x, y, 180]]
                if x != self.cell_size*(self.cell_number-1): possible.append(['move', x + self.cell_size, y, 90])
                return possible
            case 'DOWN':
                possible = [['left', x, y, 90], ['right', x, y, 270]]
                if y != self.cell_size*(self.cell_number-1): possible.append(['move', x, y + self.cell_size, 180])
                return possible
            case 'LEFT':
                possible = [['left', x, y, 180], ['right', x, y, 0]]
                if x != 0: possible.append(['move', x - self.cell_size, y, 270])
                return possible

    def graphsearch(self, istate, goaltest):
        x = istate[0]
        y = istate[1]
        angle = istate[2]

        fringe = [Node([x, y, angle])]  # queue (moves/states to check)
        fringe_state = [fringe[0].state]
        explored = []

        while True:
            if len(fringe) == 0:
                return False

            elem = fringe.pop(0)
            fringe_state.pop(0)

            # if goal_test(elem.state):
            #     return
            # print(elem.state[0], elem.state[1], elem.state[2])
            if elem.state[0] == goaltest[0] and elem.state[1] == goaltest[1]:  # checks if we reached the given point
                steps = []
                while elem.parent != '':
                    steps.append([elem.action, elem.state[0], elem.state[1]])  # should return only elem.action in prod
                    elem = elem.parent

                steps.reverse()
                print(steps)  # only for dev
                return steps

            explored.append(elem.state)

            for (action, state_x, state_y, state_angle) in self.succ(elem.state):
                if [state_x, state_y, state_angle] not in fringe_state and \
                        [state_x, state_y, state_angle] not in explored:
                    x = Node([state_x, state_y, state_angle])
                    x.parent = elem
                    x.action = action
                    fringe.append(x)
                    fringe_state.append(x.state)
