# SPDX-FileCopyrightText: Copyright (C) Arduino s.r.l.
# SPDX-License-Identifier: MPL-2.0

from arduino.app_utils import *
import time

def loop():
    # Keep the bridge alive while C++ handles the hardware
    time.sleep(1)

# Start the application loop
App.run(user_loop=loop)
