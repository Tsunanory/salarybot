import pytest
from telegram_bot.bot import start, handle_message


class MockMessage:
    def __init__(self, text):
        self.text = text

    async def reply_text(self, text):
        print(text)


class MockUpdate:
    def __init__(self, message):
        self.message = message


class MockContext:
    pass


@pytest.mark.asyncio
async def test_start():
    update = MockUpdate(MockMessage("/start"))
    context = MockContext()
    await start(update, context)


@pytest.mark.asyncio
async def test_handle_message():
    update = MockUpdate(MockMessage('{"dt_from": "2022-01-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'))
    context = MockContext()
    await handle_message(update, context)


@pytest.mark.asyncio
async def test_handle_message_invalid_json():
    update = MockUpdate(MockMessage('invalid json'))
    context = MockContext()
    await handle_message(update, context)
