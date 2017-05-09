class StateReturn:
    def __init__(self, storage_updates={}, next_state=None):
        self.storage_updates = storage_updates
        self.next_state = next_state