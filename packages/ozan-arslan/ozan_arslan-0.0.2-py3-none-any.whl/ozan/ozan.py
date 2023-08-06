import os
import time

class OzanArslan:
    text = "OZAN ARSLAN IS A GAY"

    def __init__(self):
        self.x = 0

    def run(self):
        while True:
            # Clear the console screen
            os.system("cls" if os.name == "nt" else "clear")

            # Print the text at the current position
            print(" " * self.x + OzanArslan.text)

            # Wait for a short period
            time.sleep(0.1)

            # Move the text to the right by one character
            self.x += 1

            # Wrap the text back to the beginning of the screen if it reaches the end
            if self.x >= os.get_terminal_size().columns:
                self.x = 0


