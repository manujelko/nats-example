import asyncio

import msgpack
import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Create a message
    message = {
        "type": "greeting",
        "content": "Hello, NATS!",
        "timestamp": 123456789,
    }

    message_bytes = msgpack.packb(message)

    # Serialize the message using MessagePack
    await nc.publish("msgpack_demo", message_bytes)
    print("Published MessagePack message")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
