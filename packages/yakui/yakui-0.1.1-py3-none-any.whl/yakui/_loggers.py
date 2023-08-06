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
"""yakui loggers"""

from sys import stdout
# fmt: off
from ._levels import Level, Levels
# fmt: on
from ._constants import W
from ._callers import caller
from ._timestamps import timestamp

from .ansi256._beautify import beautify
from .ansi256.themes._theme import Theme
from .ansi256.themes._default import tango


class Logger:
    """
    Represents a yakui Logger

    Attributes:
        `name` (str): Name of the logger
        `ansi` (bool): Whether to use ansi
        `theme` (Theme): Theme for the logger
        `indent` (int): Indent for the logger
    """

    def __init__(
        self,
        name: str = "yakui",
        *,
        ansi: bool = False,
        theme: Theme = tango,
        indent: int = 4,
        filename: str = None,
    ) -> None:
        self.__name = name
        self.__ansi = ansi
        self.__theme = theme
        self.__indent = indent
        self.__filename = filename

        # fmt: off
        levels = [
            Levels.INFO,
            Levels.WARN,
            Levels.DEBUG,
            Levels.ERROR,
            Levels.FATAL
        ]
        # fmt: on
        self.__levels = {level._value: level._name for level in levels}

    @property
    def name(self) -> str:
        """Name of the logger"""
        return self.__name

    @name.setter
    def name(self, new: str) -> None:
        """Set new name of the logger"""
        self.__name = new

    @property
    def ansi(self) -> bool:
        """Whether to use ansi"""
        return self.__ansi

    @ansi.setter
    def ansi(self, new: bool) -> None:
        """Set whether to use ansi"""
        self.__ansi = new

    @property
    def theme(self) -> Theme:
        """Theme for the logger"""
        return self.__theme

    @theme.setter
    def theme(self, new: Theme) -> None:
        """Set new theme for the logger"""
        self.__theme = new

    @property
    def indent(self) -> int:
        """Indent for the logger"""
        return self.__indent

    @indent.setter
    def indent(self, new: int) -> None:
        """Set new indent for the logger"""
        self.__indent = new

    def log(self, level: Level, message: str) -> None:
        """
        Log message to the standart output

        Parameters:
            `level` (Level): Level of logging
            `message` (str): A message to log
        """
        logger_name = self.__name

        level_name = level.name
        level_value = level.value
        level_text = level_name.upper()

        assert level_value in self.__levels

        _timestamp = timestamp()
        _caller = caller()

        caller_name = _caller.name
        caller_parent_name = _caller.parent.name

        if self.__ansi:
            logger_name = beautify(logger_name, self.__theme._logger_name)
            _timestamp = beautify(_timestamp, self.__theme._timestamp)
            level_text = beautify(
                level_text, self.__theme.__getattribute__(f"_level_{level_name}")
            )
            caller_parent_name = beautify(
                caller_parent_name, self.__theme._caller_parent_name
            )
            caller_name = beautify(caller_name, self.__theme._caller_name)
            message = beautify(message, self.__theme._message)

        # fmt: off
        log = \
        (
            f"{logger_name}{W * self.__indent}"
            f"[{_timestamp} {level_text}]{W * self.__indent}"
            f"({caller_parent_name}/{caller_name}){W * self.__indent}{message}\n"
        )
        # fmt: on
        if self.__filename is not None:
            with open(self.__filename) as stream:
                stream.write(log)

        stdout.write(log)

    def info(self, message: str) -> None:
        """
        Confirmation that things are working as expected

        Parameters:
            `message` (str): A message to info
        """
        self.log(Levels.INFO, message)

    def warn(self, message: str) -> None:
        """
        An indication that something unexpected happened,
        or indicative of some problem in the near future.
        The software is still working as expected.

        Parameters:
            `message` (str): A message to warn
        """
        self.log(Levels.WARN, message)

    def debug(self, message: str) -> None:
        """
        Detailed information, typically of
        interest only when diagnosing problems

        Parameters:
            `message` (str): A message to debug
        """
        self.log(Levels.DEBUG, message)

    def error(self, message: str) -> None:
        """
        Due to a more serious problem,
        the software has not been able to perform some function.

        Parameters:
            `message` (str): A message to error
        """
        self.log(Levels.ERROR, message)

    def fatal(self, message: str) -> None:
        """
        A serious error, indicating that the program
        itself may be unable to continue running.

        Parameters:
            `message` (str): A message to fatal
        """
        self.log(Levels.FATAL, message)
