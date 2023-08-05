from unittest.mock import AsyncMock, MagicMock

from bovine.activitystreams.activity_factory import Activity
from .handle_follow_request import handle


async def test_does_nothing_on_random_activity():
    data = {"type": "Note"}

    client = AsyncMock()

    await handle(client, data)

    client.send_to_outbox.assert_not_awaited()


async def test_replies_to_follow_with_accept():
    data = Activity(type="Follow", actor="actor").build()
    client = AsyncMock()
    client.activity_factory.accept = MagicMock()

    await handle(client, data)

    client.send_to_outbox.assert_awaited_once()
