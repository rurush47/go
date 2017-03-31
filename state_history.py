import copy


class StateHistory:
    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.append(state)

    def is_already_in_history(self, state):
        if state in self.states:
            return True
        else:
            return False

    def get_last_state(self):
        return self.states[-1]
