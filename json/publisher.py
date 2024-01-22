import asyncio
import json

import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Create a JSON message
    json_message = {
        "type": "greeting",
        "content": "Hello, NATS!",
        "timestamp": 123456789,
    }

    # Serialize the JSON message and encode it to bytes
    message = json.dumps(json_message).encode()

    # Publish the message
    await nc.publish("json_demo", message)
    print("Published JSON message")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
