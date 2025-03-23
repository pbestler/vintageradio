#!/bin/bash

# Set the script and service name
SCRIPT_NAME="listen-powerbutton.py"
SERVICE_NAME="power.button.service"
INSTALL_DIR="/usr/local/bin"
SERVICE_DIR="/etc/systemd/system"

# Check if running as root (required for installation)
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

echo "Installing Python script..."
cp $SCRIPT_NAME $INSTALL_DIR/

echo "Installing ${SERVICE_NAME}"
cp $SERVICE_NAME $SERVICE_DIR/

# Reload systemd daemon to recognize the new service
echo "Reloading systemd..."
systemctl daemon-reload

# Enable and start the service
echo "Enabling and starting the service..."
systemctl enable $SERVICE_NAME
systemctl start $SERVICE_NAME

# Check status of the service
echo "Service status:"
systemctl status $SERVICE_NAME

echo "Installation complete!"