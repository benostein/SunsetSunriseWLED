# Sunset Sunrise WLED

Simple Python scripts to turn a WLED device on/off with sunset/sunrise.

There are two scripts in the project:
* ``sunset_sunrise_startup.py``
    * Designed to run when you turn your computer on.
    * Uses date, longitude and latitude to calculate sunset and sunrise times (thanks to [Suntime](https://github.com/SatAgro/suntime)).
    * Turns on LEDs when sun has set.
    * Turns off LEDs when sun has risen.
* ``sunset_sunrise_shutdown.py``
    * Designed to run when you turn your computer off.
    * Turns off LEDs (if already on).

These scripts will ensure that the LEDs will only be on when your computer is turned on and when it is dark outside.

A similar effect can be achieved with [Home Assistant](https://www.home-assistant.io/) and [Alexa routines](https://www.amazon.com/gp/help/customer/display.html?nodeId=202200080) but I prefer this solution as there is no need for another IoT device to be constantly running.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To get the script running, all you will need to have is:

* Python (3.3+)
* Windows 10
* Device running WLED on your network

### Installation

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
    This can be verified by using the command `which python` and checking it is using the Python interpreter in the `env` folder.
4. Install the Python libraries

    ```sh
    pip install -r requirements.txt
    ```
5. Edit `config.py`

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
6. Run `generate_bat_files.py`

    ```sh
    py generate_bat_files.py
    ```
    This will generate two ``.bat`` files that will launch the Python scripts.
7. Run gpedit.msc (Local Policies)
8. Computer Configuration -> Windows Settings -> Scripts -> Startup -> Properties -> Add -> (select path of ``led_startup.bat``)
9. Computer Configuration -> Windows Settings -> Scripts -> Shutdown -> Properties -> Add -> (select path of ``led_shutdown.bat``)

These scripts will now run automatically, so you should not have to worry about turning your LEDs on or off again.

## Projects Used

* [WLED](https://github.com/Aircoookie/WLED) - ESP8266/ESP32 webserver to control LEDs.
* [Python-WLED](https://github.com/frenck/python-wled) - Asynchronous Python client for WLED.
* [Suntime](https://github.com/SatAgro/suntime) - Used to calculate sunrise/sunset times.

## Contributing
Pull requests are more than welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
