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
"""yakui ansi256 beautify"""

from ._effects import Effect
from ._typehintings import _Color, _Effect


def beautify(
    text: str,
    color: _Color | str,
    effect: _Effect | str = Effect.Defaults.NORMAL,
) -> str:
    """Beautify text with given Color and Effect"""

    return effect + color + text + Effect.Defaults.RESET