import asyncio
import json

import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    json_str = msg.data.decode()
    json_message = json.loads(json_str)
    print(f"Received JSON message: {json_message}")


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to subject
    await nc.subscribe("json_demo", cb=message_handler)

    # Keep the subscription open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
