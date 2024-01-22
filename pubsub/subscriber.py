import asyncio

import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    print(f"Received a message on '{msg.subject}': {msg.data.decode()}")


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to subject
    await nc.subscribe("this.is.cool", cb=message_handler)
    await nc.subscribe("this.>", cb=message_handler)
    await nc.subscribe("this.*.cool", cb=message_handler)
    await nc.subscribe("this.is.*", cb=message_handler)
    await nc.subscribe("update", cb=message_handler)
    await nc.subscribe("this.*", cb=message_handler)

    # Keep the subscription open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
