class Plant:
    def __init__(self, id, name, state, image_zero, image_one, x, y, empty):
        self.id = id
        self.name = name
        self.state = state
        self.image_state_zero = image_zero
        self.image_state_one = image_one
        self.xy = [x, y]
        self.empty = empty
        