import pyperclip


def clean_clipboard(val: str) -> None:
    pyperclip.copy(val.replace('\n', ' ').replace('\r', ' '))
