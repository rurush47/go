class StateHistory:
    def __init__(self):
        self.states = []

    def add_state(self, state):
        self.states.append(state)
        if len(self.states) > 2:
            self.states.pop(0)

    def is_already_in_history(self, state):
        if state in self.states:
            return True
        else:
            return False

    def get_last_state(self):
        return self.states[-1]

    def get_state_list(self):
        return self.states
