#!/bin/bash
SCRIPT="$HOME/.config/waybar/scripts/autoclicker.py"

if pgrep -f "autoclicker.py" > /dev/null; then
    pkill -f "autoclicker.py"
else
    setsid nohup python "$SCRIPT" > /dev/null 2>&1 &
fi
