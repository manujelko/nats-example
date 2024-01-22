import asyncio

import nats


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Publish messages to 'tasks' subject
    for i in range(10):
        dots = "." * i
        msg = f"Task {i}{dots}"
        await nc.publish("tasks", msg.encode())
        print(f"Published: {msg}")

    # Gracefully close the connection


if __name__ == "__main__":
    asyncio.run(main())
