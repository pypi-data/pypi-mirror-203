from typing import ClassVar

import lief.Android # type: ignore

class ANDROID_VERSIONS:
    __members__: ClassVar[dict] = ...  # read-only
    UNKNOWN: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_601: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_700: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_710: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_712: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_800: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_810: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_900: ClassVar[ANDROID_VERSIONS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def code_name(version: lief.Android.ANDROID_VERSIONS) -> str: ...
def version_string(version: lief.Android.ANDROID_VERSIONS) -> str: ...
