class Machine:
    def __init__(self, initialState):
        self.state = initialState
        self.events = {}
        self.callbacks = {}

    def when(self, event, transitions):
        self.events[event] = transitions

    def on(self, state, fn):
        self.callbacks[state] = fn

    def trigger(self, event):
        if event not in self.events:
            return False

        transitions = self.events[event]

        if self.state not in transitions:
            return False

        self.state = transitions[self.state]

        for state in [self.state, "any"]:
            if state in self.callbacks:
                self.callbacks[state]()

        return True
