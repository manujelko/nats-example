import asyncio

import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Publish a message to the 'updates' subject
    await nc.publish("this.is.cool", b"Hello, NATS!")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
