from typing import Callable, List, Union
from time import sleep

import pyperclip


Number = Union[int, float]


class ClipboardTracker:
    _listeners: List[Callable]
    _tracking: bool
    _pooling_interval: Number

    def __init__(self, pooling_interval=0.2) -> None:
        self._listeners = []
        self._pooling_interval = pooling_interval

    def register(self, listener: Callable) -> None:
        self._listeners.append(listener)

    def unregiste(self, listener: Callable) -> None:
        self._listeners.remove(listener)

    def track(self) -> None:
        last_clipboard_value = None

        while True:
            clipboard_value = pyperclip.paste()

            if clipboard_value:
                if last_clipboard_value != clipboard_value:
                    for listener in self._listeners:
                        listener(clipboard_value)

                    last_clipboard_value = clipboard_value

            sleep(self._pooling_interval)
