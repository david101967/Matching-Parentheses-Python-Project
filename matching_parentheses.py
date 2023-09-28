class Stack:
    def __init__(self):
        # Initialize a stack using a list to store elements.
        self.stack = []

    def push(self, item):
        # Add an item to the top of the stack.
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item from the stack, if not empty.
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        # Check if the stack is empty.
        return len(self.stack) == 0


class BalancedParenthesesChecker:
    @staticmethod
    def check_with_stack(expression):
        # Check balanced parentheses using a stack.

        # Create an instance of the Stack class.
        stack = Stack()

        for char in expression:
            if char == '(':
                # If an opening parenthesis is encountered, push it onto the stack.
                stack.push(char)
            elif char == ')':
                # If a closing parenthesis is encountered, check if the stack is empty or the top element is not an opening parenthesis.
                # If either condition is true, the expression is not balanced.
                if stack.is_empty() or stack.pop() != '(':
                    return False

        # Check if the stack is empty after processing all characters.
        return stack.is_empty()

    @staticmethod
    def check_with_queues(expression):
        # Check balanced parentheses using a queue.

        # Create lists to simulate queues for left and right parentheses.
        left_queue = []
        right_queue = []

        for char in expression:
            if char == '(':
                # Enqueue left parentheses.
                left_queue.append(char)
            elif char == ')':
                # Enqueue right parentheses.
                right_queue.append(char)

        # Match and dequeue paired parentheses.
        while left_queue and right_queue:
            left_queue.pop(0)
            right_queue.pop(0)

        # Check if both queues are empty, indicating balanced parentheses.
        return len(left_queue) == 0 and len(right_queue) == 0


def main():
    while True:
        user_input = input("Enter a string with parentheses (or type 'exit' to quit the program): ")

        if user_input.lower() == 'exit':
            break

        # Check balanced parentheses using the stack-based approach.
        if BalancedParenthesesChecker.check_with_stack(user_input):
            print("The string has balanced parentheses (using a stack).")
        else:
            print("The string does not have balanced parentheses (using a stack).")

        # Check balanced parentheses using the queue-based approach.
        if BalancedParenthesesChecker.check_with_queues(user_input):
            print("The string has balanced parentheses (using queues).")
        else:
            print("The string does not have balanced parentheses (using queues).")


if __name__ == "__main__":
    main()
