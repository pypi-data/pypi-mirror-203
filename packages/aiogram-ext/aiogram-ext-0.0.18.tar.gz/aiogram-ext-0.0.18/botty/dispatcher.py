import asyncio
from typing import TypeVar

import aiogram
from aiogram.utils.executor import Executor
from aiohttp.web import Application
from .buttons import CallbackButton
from .deps import State
from .filters import (
    CallbackQueryButton,
    InlineQueryButton,
    MessageButton,
    StorageDataFilter,
)

T = TypeVar("T")


class Dispatcher(aiogram.Dispatcher):
    @staticmethod
    def _gen_payload(
            locals_: dict, exclude: list[str] = None, default_exclude=("self", "cls")
    ):
        kwargs = locals_.pop("kwargs", {})
        locals_.update(kwargs)

        if exclude is None:
            exclude = []
        return {
            key: value
            for key, value in locals_.items()
            if key not in exclude + list(default_exclude)
               and value is not None
               and not key.startswith("_")
        }

    def _setup_filters(self):
        filters_factory = self.filters_factory
        filters_factory.bind(
            StorageDataFilter,
            exclude_event_handlers=[
                self.errors_handlers,
                self.poll_handlers,
                self.poll_answer_handlers,
            ],
        )
        filters_factory.bind(
            CallbackQueryButton, event_handlers=[self.callback_query_handlers]
        )
        filters_factory.bind(
            InlineQueryButton, event_handlers=[self.inline_query_handlers]
        )
        filters_factory.bind(
            MessageButton,
            event_handlers=[
                self.message_handlers,
                self.edited_message_handlers,
            ],
        )

        super()._setup_filters()

    def command(self, command: str, state: str = None):
        return self.message_handler(commands=command, state=state)

    def start(self, state: str | None = "*"):
        return self.command("start", state)

    def button(self, button: CallbackButton):
        return self.callback_query_handler(button=button)

    def text(self, text: str = None, state: str | State = None):
        return self.message_handler(button=text, state=state)

    def contact(self, state: str | State = None):
        return self.message_handler(content_types="contact", state=state)

    def document(self, state: str | State = None):
        return self.message_handler(content_types="document", state=state)

    def photo(self, state: str | State = None):
        return self.message_handler(content_types="photo", state=state)

    def run(self):
        Executor(self).start_polling()

    def run_server(self, base_url: str, app: Application = None, path: str = "/"):
        executor = Executor(self)
        executor.set_webhook(path, web_app=app)
        self._set_webhook(base_url + path)
        executor.run_app(port=80)

    def _set_webhook(self, url: str):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.bot.set_webhook(url))
