# Sunset Sunrise WLED

Simple Python scripts that turns on a WLED device connected to your local network, when the sun sets (and off when the sun rises).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To get the script running, all you will need to have installed is:

* Python (3.3+)
* Windows 7+

### Installation

A step by step series of examples that tell you how to get a development env running

1. Clone the repo and enter the folder
   ```sh
   git clone https://github.com/benostein/SunsetSunriseWLED.git
   cd SunsetSunriseWLED
   ```
2. Create virtual environment
   ```sh
   py -m venv env
   ```
3. Activate virtual environment
   ```sh
   .\env\Scripts\activate
   ```
   This can be verified by using the command ``which python`` and checking it is using the Python interpreter in the ``env`` folder.
4. Install the Python libraries
   ```sh
   pip install -r requirements.txt
   ```
5. Edit ``config.py``
   ```python
   # Your latitude here
   LATITUDE = 51.5074
   # Your longitude here
   LONGITUDE = 0.1278
   # Your WLED IP address here
   LED_IP_ADDRESS = "192.168.0.57"
   # Config sleep delay here (optional)
   SLEEP_DELAY = 2
   ```
6. Run ``generate_bat_files.py``
   ```sh
   py generate_bat_files.py
   ```
   This will generate two ``.bat`` files that will launch the Python scripts.
7. Run gpedit.msc (Local Policies)
8. Computer Configuration -> Windows Settings -> Scripts -> Startup -> Properties -> Add -> (select path of ``led_startup.bat``)
9. Computer Configuration -> Windows Settings -> Scripts -> Shutdown -> Properties -> Add -> (select path of ``led_shutdown.bat``)