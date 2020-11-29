import asyncio
import datetime
import pytz
from suntime import Sun
from wled import WLED
import time
import config


async def led_on():
    async with WLED(config.LED_IP_ADDRESS) as led:
        device = await led.update()
        if not device.state.on:
            prev_brightness = device.state.brightness
            # Turn strip on, with previous brightness
            print("LEDs turned on")
            await led.master(on=True, brightness=prev_brightness)
            # You can customise how it turns on here
            # await led.segment(segment_id=0, effect="Palette", speed=10)


async def led_off():
    async with WLED(config.LED_IP_ADDRESS) as led:
        device = await led.update()

        # Turn strip off if currently on
        if device.state.on:
            print("LEDs turned off")
            await led.master(on=False)


def convert_to_unix(datetime_given):
    return (datetime_given - datetime.datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()


def pause_until(datetime_given):
    end = datetime_given

    while datetime.datetime.now(tz=pytz.utc) < end:
        time.sleep(config.SLEEP_DELAY)


def main():
    loop = asyncio.get_event_loop()
    local_sun = Sun(config.LATITUDE, config.LONGITUDE)

    today_datetime = datetime.datetime.now(tz=pytz.utc)

    sunrise_datetime = local_sun.get_sunrise_time(today_datetime.date())
    sunset_datetime = local_sun.get_sunset_time(today_datetime.date())

    while True:

        # If sunrise has already passed, get the next sunrise
        if sunrise_datetime < today_datetime:
            sunrise_datetime = local_sun.get_sunrise_time(today_datetime.date() + datetime.timedelta(1))

        # If sunset is sooner than the sunrise
        if sunset_datetime < sunrise_datetime:
            print("Sunset is soonest, pausing")
            pause_until(sunset_datetime)
            # pause.until(sunset_datetime)
            loop.run_until_complete(led_on())
            sunset_datetime = local_sun.get_sunset_time(today_datetime.date() + datetime.timedelta(1))
            # Launch wallpaper monitor here
        if sunrise_datetime < sunset_datetime:
            print("Sunrise is soonest, pausing")
            pause_until(sunrise_datetime)
            # pause.until(sunrise_datetime)
            loop.run_until_complete(led_off())
            sunrise_datetime = local_sun.get_sunset_time(today_datetime.date() + datetime.timedelta(1))


if __name__ == "__main__":
    main()
