#!/bin/bash

# Set the script and service name
SCRIPT_NAME="listen-power-button.py"
SERVICE_NAME="power-button.service"
INSTALL_DIR="/usr/local/bin"
SERVICE_DIR="/etc/systemd/system"

# Check if running as root (required for uninstallation)
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# Stop and disable the systemd service
echo "Stopping and disabling the service..."
systemctl stop $SERVICE_NAME
systemctl disable $SERVICE_NAME

# Remove the systemd service
echo "Removing systemd service..."
rm -f $SERVICE_DIR/$SERVICE_NAME

# Reload systemd daemon to recognize changes
systemctl daemon-reload

# Remove the Python script
echo "Removing Python script..."
rm -f $INSTALL_DIR/$SCRIPT_NAME

echo "Uninstallation complete!"