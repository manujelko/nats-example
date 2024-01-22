import asyncio

import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Send a request and wait for the response
    response = await nc.request("requests", b"Hello, can you hear me?")
    print(f"Received response: {response.data.decode()}")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
