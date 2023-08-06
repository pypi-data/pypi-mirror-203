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
"""olallieberry Lexer"""

from re import match
from .rule import Rule
from .token import Token


class Lexer:
    """Lexical analysis"""

    def __init__(self, __rules: list[Rule]) -> None:
        """
        __rules (list[Rule]): list of rules
        """
        self.rules = __rules

    def analyze(self, __source: list[str]) -> list[Token]:
        """Analyze a list of strings"""
        tokens = list()

        for string__ in __source:
            __line = __source.index(string__)

            for character in string__:
                __column = string__.index(character)

                for rule in self.rules:
                    result = match(rule.pattern, character)

                    if result is not None:
                        __name = rule.name
                        __idx = len(tokens) + 1
                        __value = character

                        # fmt: off
                        tokens.append(Token(
                            __name,
                            __idx,
                            __line,
                            __column,
                            __value
                        ))
                        # fmt: on

        return tokens

    def analyse(self, __source: list[str]) -> list[Token]:
        """Analyse a list of strings"""
        return self.analyze(__source)