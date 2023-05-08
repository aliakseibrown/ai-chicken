class Node:
    def __init__(self, state, parent='', action='', distance=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.distance = distance

class Search:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number

    def succ(self, state):
        x = state[0]
        y = state[1]
        angle = state[2]
        match(angle):
            case 'UP':
                possible = [['left', x, y, 'LEFT'], ['right', x, y, 'RIGHT']]
                if y != 0: possible.append(['move', x, y - self.cell_size, 'UP'])
                return possible
            case 'RIGHT':
                possible = [['left', x, y, 'UP'], ['right', x, y, 'DOWN']]
                if x != self.cell_size*(self.cell_number-1): possible.append(['move', x + self.cell_size, y, 'RIGHT'])
                return possible
            case 'DOWN':
                possible = [['left', x, y, 'RIGHT'], ['right', x, y, 'LEFT']]
                if y != self.cell_size*(self.cell_number-1): possible.append(['move', x, y + self.cell_size, 'DOWN'])
                return possible
            case 'LEFT':
                possible = [['left', x, y, 'DOWN'], ['right', x, y, 'UP']]
                if x != 0: possible.append(['move', x - self.cell_size, y, 'LEFT'])
                return possible

    def cost(self, node, stones, goal, flowers):
        # cost = node.distance
        cost = 0
        # cost += 10 if stones[node.state[0], node.state[1]] == 1 else 1
        cost += 1000 if (node.state[0], node.state[1]) in stones else 1
        cost += 30 if ((node.state[0]), (node.state[1])) in flowers else 1

        if node.parent:
            node = node.parent
            cost += node.distance  # should return only elem.action in prod
        return cost

    def heuristic(self, node, goal):
        return abs(node.state[0] - goal[0]) + abs(node.state[1] - goal[1])

    #bandaid to know about stones
    def astarsearch(self, istate, goaltest, stones, flowers):
        
        #to be expanded
        def cost_old(x, y):
            if (x, y) in stones:
                return 10
            else:
                return 1

        
        x = istate[0]
        y = istate[1]
        angle = istate[2]

        # fringe = [(Node([x, y, angle]), cost_old(x, y))]  # queue (moves/states to check)
        fringe = [(Node([x, y, angle]))]  # queue (moves/states to check)
        fringe[0].distance = self.cost(fringe[0], stones, goaltest, flowers)
        fringe.append((Node([x, y, angle]), self.cost(fringe[0], stones, goaltest, flowers)))
        fringe.pop(0)

        explored = []

        while True:
            if len(fringe) == 0:
                return False

            fringe.sort(key=lambda x: x[1])
            elem = fringe.pop(0)[0]

            # if goal_test(elem.state):
            #     return
            # print(elem.state[0], elem.state[1], elem.state[2])
            if elem.state[0] == goaltest[0] and elem.state[1] == goaltest[1]:  # checks if we reached the given point
                steps = []
                while elem.parent: 
                    steps.append([elem.action, elem.state[0], elem.state[1]])  # should return only elem.action in prod
                    elem = elem.parent

                steps.reverse()
                print(steps)  # only for dev
                return steps

            explored.append(elem.state)

            for (action, state_x, state_y, state_angle) in self.succ(elem.state):
                x = Node([state_x, state_y, state_angle], elem, action)
                x.parent = elem

                priority = self.cost(elem, stones, goaltest, flowers) + self.heuristic(elem, goaltest)
                elem.distance = priority
                # priority = cost_old(x, y) + self.heuristic(elem, goaltest)
                fringe_states = [node.state for (node, p) in fringe]

                if x.state not in fringe_states and x.state not in explored:
                    fringe.append((x, priority))
                elif x.state in fringe_states:
                    for i in range(len(fringe)):
                        if fringe[i][0].state == x.state:
                            if fringe[i][1] > priority:
                                fringe[i] = (x, priority)
