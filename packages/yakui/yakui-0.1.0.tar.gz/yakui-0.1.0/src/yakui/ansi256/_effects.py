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
"""yakui ansi256 effects"""

from ._typehintings import _Effect
from ._constants import CSI


class _EffectConverters:
    """yakui Effects Converters"""

    def __init__(self) -> None:
        ...

    def from_value(self, value: int) -> _Effect | str:
        """
        New Effect from value

        Parameters:
            `value` (int): Ansi code value for Effect
        """
        return f"{CSI}{value}m"


class _EffectDefaults:
    """Defaults yakui Effects"""

    def __init__(self) -> None:
        self._effect_converters = _EffectConverters()

        self.RESET: _Effect | str = self._effect_converters.from_value(0)
        self.BOLD: _Effect | str = self._effect_converters.from_value(1)
        self.FAINT: _Effect | str = self._effect_converters.from_value(2)
        self.ITALIC: _Effect | str = self._effect_converters.from_value(3)
        self.UNDERLINE: _Effect | str = self._effect_converters.from_value(4)

        self.NORMAL = self.RESET


class Effect:
    """
    Represents a yakui Effect

    Attributes:
        `Converters` (instance): yakui Effects Converters
        `Defaults` (instance): Defaults yakui Effects
    """
    Converters = _EffectConverters()
    Defaults = _EffectDefaults()

