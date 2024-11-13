# Text Transfer Using ESP32 with Python GUI

This repository provides a Python GUI-based notepad for transferring text data between two laptops via an ESP32 microcontroller. The application is designed to allow typing text in a notepad interface and then sending each character at a controlled rate to an ESP32, which can pass the data to a connected device over Bluetooth.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Configuration](#configuration)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project uses a Python application to create a notepad-style interface, which connects to an ESP32 over a serial connection (COM port). Characters typed or pasted in the notepad are automatically sent one by one to the ESP32 at a predefined rate. The ESP32 then sends each character to a paired device via Bluetooth, simulating typing on that device.

## Features

- **Python GUI Notepad**: A simple, dark-mode notepad interface for entering text.
- **Automatic Character Transmission**: Characters are transmitted one at a time to the ESP32.
- **Rate Control**: Adjustable character send rate (default: 150 characters per minute).
- **Line Break Support**: Converts line breaks for compatibility with Bluetooth typing simulation.

## Usage

1. Type or paste a block of text in the notepad interface.
2. The text is automatically sent one character at a time to the ESP32 at the configured rate.
3. The ESP32 transmits the text to the connected device, simulating a typing effect on the target laptop.

## Installation

### Prerequisites
- **Python 3.x**
- **Tkinter** (for GUI)
- **pyserial** (for serial communication)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/esp32-text-transfer-notepad.git
   ```
2. Install the required libraries:
   ```bash
   pip install pyserial
   ```
3. Upload the BLE Keyboard code to your ESP32. Use the [ESP32 BLE Keyboard library](https://github.com/T-vK/ESP32-BLE-Keyboard) to enable Bluetooth typing simulation.

## Configuration

1. Update the `esp32_port` variable in the Python script with the correct COM port for your ESP32 (e.g., `COM8`).
2. Set the desired **baud rate** (default: 115200) and **character send rate** in the script.

## Code Overview

- **Python Notepad GUI**: Provides an interface for typing text and sends each character to the ESP32 via a serial connection.
- **ESP32 BLE Keyboard Integration**: The ESP32 receives characters from the serial input and uses BLE to type them on the connected device.

## Limitations

- **Enter Key**: The enter key functionality is mapped to Bluetooth’s return key simulation.
- **Connection Stability**: Ensure that the ESP32 is paired with the target device for smooth operation.
- **Character Rate**: Adjustments may be needed for larger text blocks or faster typing speeds.

## Contributing

Contributions to improve this tool are welcome! Please open a pull request for any feature updates or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
