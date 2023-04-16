class Node:
    def __init__(self, state, parent='', action=''):
        self.state = state
        self.parent = parent
        self.action = action


class Search:
    def __init__(self, cell_size):
        self.cell_size = cell_size

    # WARNING! IT EXCEEDS THE PLANE!!!
    def succ(self, state):  # successor function
        x = state[0]
        y = state[1]
        angle = state[2]
        if angle == 0:
            return [['move', x, y - self.cell_size, 0], ['left', x, y, 270], ['right', x, y, 90]]
        if angle == 90:
            return [['move', x + self.cell_size, y, 90], ['left', x, y, 0], ['right', x, y, 180]]
        if angle == 180:
            return [['move', x, y + self.cell_size, 180], ['left', x, y, 90], ['right', x, y, 270]]
        if angle == 270:
            return [['move', x - self.cell_size, y, 270], ['left', x, y, 180], ['right', x, y, 0]]

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
                if state_x < 0 or state_y < 0:  # check if any of the values are negative
                    continue
                if [state_x, state_y, state_angle] not in fringe_state and \
                        [state_x, state_y, state_angle] not in explored:
                    x = Node([state_x, state_y, state_angle])
                    x.parent = elem
                    x.action = action
                    fringe.append(x)
                    fringe_state.append(x.state)


se = Search(50)
se.graphsearch(istate=[50, 50, 0], goaltest=[150, 250])