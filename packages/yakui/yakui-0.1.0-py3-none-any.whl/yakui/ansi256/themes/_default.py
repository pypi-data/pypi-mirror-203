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
"""yakui ansi256 themes default"""

from ._theme import Theme
from .._colors import Color
from .._effects import Effect
from .._constants import FOREGROUND


tango = Theme(
    Color(FOREGROUND).Converters.from_hex("#555753"),
    Color(FOREGROUND).Converters.from_hex("#4E9A06"),

    Color(FOREGROUND).Converters.from_hex("#729FCF") +
    Effect.Defaults.BOLD, # Info
    Color(FOREGROUND).Converters.from_hex("#AD7FA8") +
    Effect.Defaults.BOLD, # Warn
    Color(FOREGROUND).Converters.from_hex("#34E2E2") +
    Effect.Defaults.BOLD, # Debug
    Color(FOREGROUND).Converters.from_hex("#EF2929") +
    Effect.Defaults.BOLD, # Error
    Color(FOREGROUND).Converters.from_hex("#CC0000") +
    Effect.Defaults.BOLD, # Fatal

    Color(FOREGROUND).Converters.from_hex("#555753"),
    Color(FOREGROUND).Converters.from_hex("#4E9A06") + 
    Effect.Defaults.BOLD,
    Color(FOREGROUND).Converters.from_hex("#4E9A06") +
    Effect.Defaults.ITALIC
)
