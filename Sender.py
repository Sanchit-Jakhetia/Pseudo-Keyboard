import tkinter as tk
import serial
import time

# Configure the serial port
esp32_port = 'COM8'  # Replace with your ESP32's COM port
baud_rate = 115200
serial_connection = None

# Set rate control parameters (150 characters per minute -> 1 character every 0.4 seconds)
character_rate = 1  # Time interval between characters in seconds

def open_serial_connection():
    global serial_connection
    try:
        # Establish a serial connection
        serial_connection = serial.Serial(esp32_port, baud_rate)
        time.sleep(2)  # Give time to establish connection
        print(f"Connected to {esp32_port} at {baud_rate} baud.")
    except serial.SerialException as e:
        print(f"Error: {e}")
        serial_connection = None

def send_to_esp32(char_to_send):
    global serial_connection
    if serial_connection and serial_connection.is_open:
        serial_connection.write(char_to_send.encode())  # Send only the character to ESP32
        print(f"Sent to ESP32: {char_to_send}")
    else:
        print("Serial connection is not open.")

def send_code_block():
    """Send the block of code one character at a time."""
    code_block = text_area.get("1.0", tk.END).strip()  # Get the entire block of text
    for char in code_block:
        send_to_esp32(char)  # Send regular characters without checking for Enter
        time.sleep(character_rate)  # Wait before sending the next character

# Create the main window
root = tk.Tk()
root.title("Notepad GUI")

# Set the window size
root.geometry("700x600")

# Dark mode colors
bg_color = "#2e2e2e"  # Dark gray background
fg_color = "#ffffff"  # White text
button_bg = "#444444"  # Dark button background
button_fg = "#ffffff"  # White text on buttons

# Configure the window appearance
root.configure(bg=bg_color)

# Create a text widget to input text
text_area = tk.Text(root, wrap='word', font=("Arial", 12), bg=bg_color, fg=fg_color, insertbackground='white')
text_area.pack(expand="true", fill="both", padx=10, pady=10)

# Create a button to manually send text to ESP32
send_button = tk.Button(root, text="Send Code to ESP32", command=send_code_block, bg=button_bg, fg=button_fg)
send_button.pack(pady=10)  # Ensure the button is placed below the text area

# Open serial connection when the application starts
open_serial_connection()

# Start the GUI event loop
root.mainloop()

# Close the serial connection when exiting the program
if serial_connection and serial_connection.is_open:
    serial_connection.close()
    print("Serial connection closed.")
