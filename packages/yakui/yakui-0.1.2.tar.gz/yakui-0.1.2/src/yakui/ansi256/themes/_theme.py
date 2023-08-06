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
"""yakui ansi256 themes theme"""

from .._typehintings import _Color


class Theme:
    """
    Represents a yakui Theme

    Attributes:
        `_logger_name` (Color | Effect | str) Color or Effect for name of the logger\n
        `_timestamp` (Color | Effect | str) Color or Effect for timestamp\n
        `_level_info` (Color | Effect | str) Color or Effect for level INFO\n
        `_level_warn` (Color | Effect | str) Color or Effect for level WARN\n
        `_level_debug` (Color | Effect | str) Color or Effect for level DEBUG\n
        `_level_error` (Color | Effect | str) Color or Effect for level ERROR\n
        `_level_fatal` (Color | Effect | str) Color or Effect for level FATAL\n
        `_caller_parent_name` (Color | Effect | str) Color or Effect for
        caller parent name\n
        `_caller_name` (Color | Effect | str) Color or Effect for caller name\n
        `_message` (Color | Effect | str) Color or Effect for message\n
    """

    def __init__(
        self,
        _logger_name: _Color | str,
        _timestamp: _Color | str,
        _level_info: _Color | str,
        _level_warn: _Color | str,
        _level_debug: _Color | str,
        _level_error: _Color | str,
        _level_fatal: _Color | str,
        _caller_parent_name: _Color | str,
        _caller_name: _Color | str,
        _message: _Color | str,
    ) -> None:
        self._logger_name = _logger_name
        self._timestamp = _timestamp
        self._level_info = _level_info
        self._level_warn = _level_warn
        self._level_debug = _level_debug
        self._level_error = _level_error
        self._level_fatal = _level_fatal
        self._caller_parent_name = _caller_parent_name
        self._caller_name = _caller_name
        self._message = _message
