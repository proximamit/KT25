import time

def blink_text(text, duration=10, interval=0.5):
    """
    Prints blinking text in the terminal.
    \033[5m is the ANSI escape code for blink.
    \033[0m is the ANSI escape code for reset.
    """
    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            # Print blinking text
            print(f"\033[5m{text}\033[0m", end="\r")
            time.sleep(interval)
            # Print space to create 'off' state
            print(" " * len(text), end="\r")
            time.sleep(interval)
    except KeyboardInterrupt:
        # Clear line on exit
        print("\033[2K", end="\r")

# Run the blink
blink_text("Happy New Year!!", duration=10)
print("\nGood Bye 2025.")
