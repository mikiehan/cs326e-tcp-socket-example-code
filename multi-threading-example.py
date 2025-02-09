import threading
import time
import sys

def greet():
    """Function that prints Hello, sleeps for 3 seconds, and prints Goodbye."""
    print("Hello")
    time.sleep(3)
    print("Goodbye")

def main():
    """Main function that listens for input and starts threads."""
    print("Press any key and Enter to start a new thread. Press Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to exit.")

    try:
        while True:
            user_input = sys.stdin.readline()  # Read one line of input
            if not user_input:  # Detect EOF (End of File) Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) 
                print("\nEOF detected. Exiting program...")
                break

            # Start a new thread for each key press
            thread = threading.Thread(target=greet)
            thread.start()

    except KeyboardInterrupt: #Ctrl+C 
        print("\nInterrupted by user. Exiting...")

if __name__ == "__main__":
    main()
