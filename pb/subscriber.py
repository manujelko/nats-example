import asyncio

import message_pb2
import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    greeting = message_pb2.Greeting()
    greeting.ParseFromString(msg.data)
    print(f"Received Protobuf message: {greeting}")


async def main() -> None:
    # Connect the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to subject
    await nc.subscribe("protobuf_demo", cb=message_handler)

    # Keep the subscription open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
