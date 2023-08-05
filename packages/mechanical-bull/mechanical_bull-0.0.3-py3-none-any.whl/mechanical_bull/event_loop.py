import bovine
import json

import logging

logger = logging.getLogger(__name__)


async def loop(client_config, handlers):
    async with bovine.BovineClient(client_config) as client:
        event_source = await client.event_source()
        async for event in event_source:
            if event.data:
                data = json.loads(event.data)
                logger.debug(event.data)

                for handler in handlers:
                    await handler(client, data)
