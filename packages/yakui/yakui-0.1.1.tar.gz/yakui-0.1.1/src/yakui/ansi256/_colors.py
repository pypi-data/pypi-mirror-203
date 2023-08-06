# -*- coding: utf-8 -*-
# Copyright 2023 mmlvgx
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""yakui ansi256 colors"""

from ._typehintings import _Color
from ._constants import CSI


class _ColorConverters:
    """Represents a yakui Colors Converters"""

    def __init__(self, mode: int | str) -> None:
        self.__mode = mode

    def from_rgb(
        self,
        # fmt: off
        red: int | str,
        green: int | str,
        blue: int | str
        # fmt: on
    ) -> _Color | str:
        """
        New Color from rgb

        Parameters:
            `red` (int | str): Red component of Color
            `green` (int | str): Green component of Color
            `blue` (int | str): Blue component of Color
        """
        return f"{CSI}{self.__mode};2;{red};{green};{blue}m"

    def from_hex(self, code: str) -> _Color | str:
        """
        New color from hex

        Parameters:
            `code` (str): Hex code of Color
        """
        code = code.lstrip("#")

        red, green, blue = tuple(int(code[i : i + 2], 16) for i in (0, 2, 4))
        return self.from_rgb(red, green, blue)


class _ColorDefaults:
    """Represents a Defaults yakui Colors"""

    def __init__(self, mode: int | str) -> None:
        self.__mode = mode
        # fmt: off
        self._color_converters = _ColorConverters(
            self.__mode
        )
        # fmt: on
        self.WHITE: _Color | str = self._color_converters.from_rgb(255, 255, 255)
        self.BLACK: _Color | str = self._color_converters.from_rgb(0, 0, 0)
        self.RED: _Color | str = self._color_converters.from_rgb(255, 0, 0)
        self.GREEN: _Color | str = self._color_converters.from_rgb(0, 255, 0)
        self.BLUE: _Color | str = self._color_converters.from_rgb(0, 0, 255)


class Color:
    """
    Represents a yakui Color

    Attributes:
        `Converters` (instance): yakui Colors Converters
        `Defaults` (instance): Defaults yakui Colors
    """

    def __init__(self, mode: int | str) -> None:
        self.Converters = _ColorConverters(mode)
        self.Defaults = _ColorDefaults(mode)
