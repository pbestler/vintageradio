# Raspberry Pi Power Button and LED Control

This project provides a systemd service and Python script to manage a power button and control the LEDs on a Raspberry Pi. It allows you to safely shut down the Raspberry Pi using a GPIO-connected button and control the state of the PWR and ACT LEDs.

## Features

- **Power Button Listener**: Monitors a GPIO pin for button presses to trigger a safe shutdown.
- **LED Control**: Turns the PWR and ACT LEDs on or off programmatically.
- **Systemd Integration**: Automatically starts the service on boot and restarts it if it crashes.

## Project Structure

## Requirements

- Raspberry Pi with GPIO support
- Python 3
- `RPi.GPIO` library
- Root privileges for installation and execution

## Installation

1. Clone this repository to your Raspberry Pi.
2. Navigate to the `systemd/power-button` directory:
   ```bash
   cd systemd/power-button
   ```
3. Run the installation script as root:
    ```bash
    sudo ./install.sh
    ```

## Customization
GPIO Pin: The default GPIO pin for the power button is 7. You can change this by modifying the gpio_id parameter in the wait_for_powerbutton function in listen-power-button.py.
LED Names: The default LEDs are PWR and ACT. You can change these by modifying the led_name parameter in the change_led function.

## License
This project is licensed under the MIT License. See the LICENSE file for details.