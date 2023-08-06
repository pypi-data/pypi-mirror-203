class BahaCalculator:
    """
    A class representing a basic calculator.

    Attributes:
        memory (float): The current value in the calculator's memory.
    """

    def __init__(self):
        """
        Initialize a new Calculator object with memory value of 0.
        """
        self.memory = 0.0

    def add(self, value):
        """
        Add a value to the current memory.

        Input:
            value (float): The value to add to the current memory.

        Returns:
            float: The new value of the calculator's memory.
        """
        self.memory += value
        return self.memory

    def subtract(self, value):
        """
        Subtract a value from the current memory.

        Input:
            value (float): The value to subtract from the current memory.

        Returns:
            float: The new value of the calculator's memory.
        """
        self.memory -= value
        return self.memory

    def multiply(self, value):
        """
        Multiply the current memory by a value.

        Input:
            value (float): The value to multiply the current memory by.

        Returns:
            float: The new value of the calculator's memory.
        """
        self.memory *= value
        return self.memory

    def divide(self, value):
        """
        Divide the current memory by a value.

        Input:
            value (float): The value to divide the current memory by.

        Returns:
            float: The new value of the calculator's memory.
        """
        if value == 0:
            raise ValueError("Cannot divide by zero")
        self.memory /= value
        return self.memory

    def root(self, n):
        """
        Take the nth root of the current memory.

        Input:
            n (int): The root to take of the current memory.

        Returns:
            float: The new value of the calculator's memory.
        """
        if n == 0:
            return 'Cant take the 0th root' #check for zero division
        self.memory **= (1/n)
        return self.memory

    def reset(self):
        """
        Reset the memory to 0.

        Returns:
            float: The new value of the calculator's memory (0.0).
        """
        self.memory = 0.0
        return self.memory  
c = BahaCalculator()
print(c.add(2))
print(c.multiply(4))
print(c.reset())