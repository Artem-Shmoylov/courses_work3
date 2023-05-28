class Operation:
    def __init__(self, id, state, date, operationAmount, description, sender, to):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.sender = sender
        self.to = to

    def __repr__(self):
        return f"Operation(id={self.id}, state={self.state}, date={self.date}, operationAmount={self.operationAmount}, description={self.description}, sender={self.sender}, to={self.to})"
