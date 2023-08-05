from unittest.mock import patch, AsyncMock

from .event_loop import loop


@patch("bovine.BovineClient")
async def test_loop_no_loop(mock_client):
    mock_client.return_value = mock_client

    source = AsyncMock()
    mock_client.__aenter__ = AsyncMock()
    mock_client.__aenter__.return_value = mock_client

    mock_client.event_source = AsyncMock()
    mock_client.event_source.return_value = source
    source.sequence = []

    await loop({}, [])

    mock_client.__aenter__.assert_awaited_once()
    mock_client.event_source.assert_awaited_once()
