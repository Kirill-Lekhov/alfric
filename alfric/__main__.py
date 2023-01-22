from .tracker import ClipboardTracker
from .listeners import clean_clipboard


if __name__ == '__main__':
    tracker = ClipboardTracker()
    tracker.register(clean_clipboard)
    tracker.track()
