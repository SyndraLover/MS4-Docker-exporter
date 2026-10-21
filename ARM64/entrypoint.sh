Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
export MS4_VERSION="MuseScore-Studio-4.7.5.260831071-aarch64.AppImage"

sleep 2

cd /app 
/usr/bin/python3 main.py
