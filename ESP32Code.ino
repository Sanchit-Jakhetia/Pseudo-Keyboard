#include <BleKeyboard.h>

BleKeyboard bleKeyboard("Keyboard");  // Set a name for the Bluetooth keyboard

void setup() {
  Serial.begin(115200);  // Start serial communication with the specified baud rate
  bleKeyboard.begin(); // Initialize BLE keyboard
  
  while (!bleKeyboard.isConnected()) {
    delay(500);  // Wait until BLE is connected
    Serial.println("Waiting for Bluetooth connection...");
  }
}

void loop() {
  // Check if BLE is connected and if there’s incoming data from serial
  if (bleKeyboard.isConnected() && Serial.available()) {
    String text = Serial.readStringUntil('\n');  // Read a line from serial

    if (text.length() > 0) {
      bleKeyboard.print(text);  // Send text as a keyboard input
      Serial.print("Typed: ");
      Serial.println(text);  // Print to serial monitor for debugging
    }
  }
}
