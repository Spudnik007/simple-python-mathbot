import math

class MathBot:
    def __init__(self):
        self.history = []

    def run(self):
        print("Welcome to MathBot!")
        print("Enter mathematical expressions to calculate, or type 'quit' to exit.")
        print("You can use +, -, *, /, ** (for power), and parentheses.")
        while True:
            user_input = input(">> ").strip().lower()
            if user_input == "quit":
                print("Goodbye!")
                break
            elif user_input == "history":
                self.display_history()
            else:
                self.calculate_expression(user_input)

    def display_history(self):
        if not self.history:
            print("No history available.")
        else:
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")

    def calculate_expression(self, expression):
        try:
            # Replace '^' with '**' for power operations
            expression = expression.replace("^", "**")
            result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": math.pow})
            print(f"Result: {result}")
            self.history.append(f"{expression} = {result}")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    MathBot().run()
