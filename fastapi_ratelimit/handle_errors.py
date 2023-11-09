class EngineException(Exception):
    def __init__(self, expression, message):
        self.message = message
        self.expression = expression
