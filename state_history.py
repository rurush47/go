import copy


class StateHistory:
    def __init__(self):
        self.states = []

    def add_state(self, state):
        new_state = copy.deepcopy(state)
        self.states.append(new_state)

    def is_already_in_history(self, state):
        if state in self.states:
            return True
        else:
            return False
