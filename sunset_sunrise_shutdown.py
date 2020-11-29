import asyncio
import config
from wled import WLED


async def led_off():
    async with WLED(config.LED_IP_ADDRESS) as led:
        device = await led.update()
        print(device.info.version)

        # Turn strip off
        if device.state.on:
            await led.master(on=False)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(led_off())
