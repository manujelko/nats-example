import asyncio
import sys

import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    name = sys.argv[1]
    content = msg.data.decode()
    print(f"Worker {name} received a message on '{msg.subject}': {content}")
    print("Doing work...")
    work_time = content.count(".")
    await asyncio.sleep(work_time)
    print("Work done!")


async def main() -> None:
    # Connect to the NATS server
    nc = await nats.connect("nats://localhost:4222")

    # Subscribe to subject with queue group
    await nc.subscribe("tasks", queue="worker-group", cb=message_handler)

    # Keep the subscription open
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
