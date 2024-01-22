import asyncio

import message_pb2
import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Create a Protobuf message
    greeting = message_pb2.Greeting()
    greeting.type = "greeeting"
    greeting.content = "Hello, NATS!"
    greeting.timestamp = 123456789

    # Serialize the message to Protobuf format
    message_bytes = greeting.SerializeToString()

    # Publish the Protobuf message
    await nc.publish("protobuf_demo", message_bytes)
    print("Published Protobuf message")

    # Gracefully close the connection
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
