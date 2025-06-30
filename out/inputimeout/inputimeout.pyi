from _typeshed import Incomplete

DEFAULT_TIMEOUT: float
INTERVAL: float
SP: str
CR: str
LF: str
CRLF: Incomplete

class TimeoutOccurred(Exception): ...

def echo(string) -> None: ...
def posix_inputimeout(prompt: str = '', timeout=...) -> str: ...
def win_inputimeout(prompt: str = '', timeout=...) -> str: ...
inputimeout = posix_inputimeout
inputimeout = win_inputimeout
