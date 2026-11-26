#!/bin/bash
if pgrep -f "autoclicker.py" > /dev/null; then
    echo '{"text":"󰍽 ON","class":"running","tooltip":"Autoclicker script is running (click to stop)"}'
else
    echo '{"text":"󰍽 OFF","class":"stopped","tooltip":"Autoclicker script is stopped (click to start)"}'
fi
