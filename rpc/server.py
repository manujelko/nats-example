import asyncio

import nats
from nats.aio.msg import Msg


async def request_handler(msg: Msg) -> None:
    print(f"Received a request: {msg.data.decode()}")
    await msg.respond(b"I got your message!")


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to a subject to handle requests
    await nc.subscribe("requests", cb=request_handler)

    # Keep the connection open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
