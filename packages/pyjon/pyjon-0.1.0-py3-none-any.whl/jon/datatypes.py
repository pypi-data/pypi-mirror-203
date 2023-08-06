r"""
    jon.datatypes
    ~~~~~~~~~~~~~

    JON types declaration

    :copyright: (c) 2023, Justin Béra (@just1not2) <me@just1not2.org>
    :license: Apache License 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0.txt
"""
from __future__ import annotations
__all__ = [
    "JONData",
    "JONDict",
    "JONDocument",
    "JONKey",
    "JONList",
    "JONNumber",
    "JONQuotedString",
    "JONString",
    "JONStringifiedData",
]

from typing import List, Optional, Tuple, Union


JONStringifiedData = Union[
    str,
    int,
    List["JONStringifiedData"],
    List[Tuple[str, "JONStringifiedData"]],
]


class JONData:
    """JON generic data class"""

    def attach(self, child: JONData) -> None:
        """Attach child JON data to the object"""

    def replace(self, child: JONData) -> None:
        """Replace last data with new child data"""

    def json(self) -> None:
        """Return a JSON version of the object"""

    def add_char(self, char: str) -> bool:  # pylint: disable=unused-argument
        """
        Try to add a character to the data content and indicate if the data can accept any other
        characters
        """

        return True

    def to_dict(self) -> Optional[JONDict]:
        """Try to return a JONDict version of the data"""


class JONString(JONData):
    """JON string class"""

    def __init__(self, string: str = "") -> None:
        self.content = string

    def json(self) -> str:
        return self.content

    def add_char(self, char: str) -> bool:
        self.content += char
        return True


class JONKey(JONString):
    """JON dictionary key class"""


class JONQuotedString(JONString):
    """JON quoted string class"""

    def json(self) -> str:
        return f"\"{self.content}\""


class JONNumber(JONData):
    """JON number key class"""

    def __init__(self, string: str = "0") -> None:
        self.content = int(string)
        self._decimal: Optional[int] = None

    def json(self) -> int:
        return self.content

    def add_char(self, char: str) -> bool:
        if char == ".":
            if self._decimal is not None:
                return False
            self._decimal = 0.1
        elif self._decimal is not None:
            self.content += self._decimal * int(char)
            self._decimal *= 0.1
        else:
            self.content = 10 * self.content + int(char)
        return True


class JONList(JONData):
    """JON list class"""

    def __init__(self) -> None:
        self.content: List[JONData] = []

    def attach(self, child: JONData) -> None:
        self.content.append(child)

    def replace(self, child: JONData) -> None:
        if self.content:
            self.content[-1] = child

    def json(self) -> List[JONStringifiedData]:
        return [child.json() for child in self.content]

    def to_dict(self) -> JONDict:
        dict_object =  JONDict()

        # Add the first element of the list as a dict key
        if self.content and isinstance(self.content[0], JONString):
            key = JONKey(string=self.content[0].content)
            dict_object.attach(child=key)

        return dict_object


class JONDict(JONData):
    """JON dictionary class"""

    def __init__(self) -> None:
        self.content: List[Tuple[JONKey, Optional[JONData]]] = []

    def attach(self, child: JONData) -> None:
        if isinstance(child, JONKey):
            self.content.append((child, None))
        else:
            self.content[-1] = (self.content[-1][0], child)

    def replace(self, child: JONData) -> None:
        if self.content:
            self.content[-1] = (self.content[-1][0], child)

    def json(self) -> List[Tuple[str, JONStringifiedData]]:
        json = []

        for couple in self.content:
            json.append((couple[0].json(), couple[1].json() if couple[1] is not None else ""))

        return json


class JONDocument(JONDict):
    """JON document class"""
