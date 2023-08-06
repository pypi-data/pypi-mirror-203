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
"""yakui levels"""


class Level:
    """
    Represents a yakui Level

    Attributes:
        `name` (str): Name of the Level
        `value` (int): Value of the Level
    """

    def __init__(self, name: str, value: int) -> None:
        self._name = name
        self._value = value


class Levels:
    """
    Represents a yakui Levels
    """

    INFO = Level("info", 10)
    WARN = Level("warn", 15)
    DEBUG = Level("debug", 20)
    ERROR = Level("error", 25)
    FATAL = Level("fatal", 30)
