import sys
import os
from typing import List


def split_text(text: str, sep: str) -> List[str]:
    i = text.find(sep)
    if i == -1:
        return [text.strip()]

    return [text[0:i].strip(), text[i + len(sep):].strip()]


def charsi_dir():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)

    return os.getcwd()
