class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        # Clear forward history
        self.history = self.history[:self.current_index + 1]
        # Add new URL to history
        self.history.append(url)
        # Update current index
        self.current_index += 1

    def back(self, steps: int) -> str:
        # Calculate the number of steps to move back
        steps = min(steps, self.current_index)
        self.current_index -= steps
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        # Calculate the number of steps to move forward
        steps = min(steps, len(self.history) - 1 - self.current_index)
        self.current_index += steps
        return self.history[self.current_index]
