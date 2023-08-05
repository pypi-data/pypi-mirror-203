import bovine
import json


async def loop(client_config, handlers):
    async with bovine.BovineClient(client_config) as client:
        event_source = await client.event_source()
        async for event in event_source:
            if event.data:
                data = json.loads(event.data)

                for handler in handlers:
                    await handler(client, data)
