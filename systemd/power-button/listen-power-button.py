#!/usr/bin/env python3

import RPi.GPIO as GPIO
import logging


def change_led(led_name="PWR", state="on"):
    """Turns the Raspberry Pi LED ON or OFF based on the given state.
    Args:
        led_name (str): The name of the LED PWR or ACT (default: "PWR" for Raspberry Pi).
        state (str): "on" to turn the LED on, "off" to turn it off.
    """
    trigger_path = f"/sys/class/leds/{led_name}/trigger"
    brightness_path = f"/sys/class/leds/{led_name}/brightness"

    try:
        if state.lower() == "on":
            with open(trigger_path, "w") as f:
                f.write("none")  # Disable automatic control
            with open(brightness_path, "w") as f:
                f.write("1")  # Turn LED ON
            print("ACT LED turned ON.")
        elif state.lower() == "off":
            with open(trigger_path, "w") as f:
                f.write("none")  # Disable automatic control
            with open(brightness_path, "w") as f:
                f.write("0")  # Turn LED OFF
            print("ACT LED turned OFF.")
        else:
            print("Invalid argument! Use 'on' or 'off'.")

    except PermissionError:
        print("Permission denied! Try running with sudo.")
    except FileNotFoundError:
        print(f"LED {led_name} not found. Check available LEDs in /sys/class/leds/")
    except Exception as e:
        print(f"Error: {e}")


def wait_for_powerbutton(gpio_id=3):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print(f"Registered GPIO{gpioid} as shutdown button. Waiting. ")
    try:
        GPIO.wait_for_edge(gpio_id, GPIO.FALLING)
        print(f"Shutdown triggered by GPIO{gpio_id} -> Shutting down.")
        subprocess.call(["shutdown", "-h", "now"], shell=False)
    except Exception as e:
        print(f"Error during shutdown.")
    finally:
        GPIO.cleanup()


change_led("PWR", "OFF")
change_led("ACT", "ON")

wait_for_powerbutton()
