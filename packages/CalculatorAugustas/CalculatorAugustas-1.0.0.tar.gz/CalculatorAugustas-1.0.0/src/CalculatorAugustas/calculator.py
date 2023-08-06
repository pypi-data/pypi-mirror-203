class Calculator:
    memory: float

    def __init__(self, variable: float = 0) -> float:
        """The initial value for the calculator's memory is set."""
        self.memory = variable

    def add(self, variable: float) -> float:
        """Calculator adds an entered number to an in-memory value."""
        self.memory += variable
        return self.memory

    def subtract(self, variable: float) -> float:
        """Calculator subtracts an entered number from an in-memory value."""
        self.memory -= variable
        return self.memory

    def multiply(self, variable: float) -> float:
        """Calculator multiplies an entered number by an in-memory value."""
        self.memory *= variable
        return self.memory

    def divide(self, variable: float) -> float:
        """Calculator divides an entered number by an in-memory value."""
        if variable == 0:
            raise ValueError(f"Division by {variable} is not possible")
        else:
            self.memory /= variable
        return self.memory

    def root(self, variable: float) -> float:
        """Calculator takes a root of a memory value by an entered number"""
        if self.memory < 0:
            raise ValueError(f"Root calculation is not valid, {self.memory} is a negative number")
        elif variable <= 0:
            raise ValueError(f"Selected degree value {variable} is not valid")
        else:
            self.memory = self.memory ** (1 / variable)
        return self.memory

    def reset(self) -> None:
        """Calculator memory is set to 0."""
        self.memory = 0
