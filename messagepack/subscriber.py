import asyncio

import msgpack
import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    message = msgpack.unpackb(msg.data)
    print(f"Received MessagePack message: {message}")


async def main() -> None:
    # Connect the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to subject
    await nc.subscribe("msgpack_demo", cb=message_handler)

    # Keep the subscription open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
