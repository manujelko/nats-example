import asyncio

import nats
from nats.errors import NoRespondersError, TimeoutError


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Send a request and wait for the response
    try:
        response = await nc.request("requests", b"Hello, can you hear me?", timeout=1)
        print(f"Received response: {response.data.decode()}")
    except NoRespondersError:
        print("No responders")
    except TimeoutError:
        print("Request timed out")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
