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
    """
    Lexical analysis

    Attributes:
        rules (list[Rule]): list of rules
    """

    def __init__(self, rules: list[Rule]) -> None:
        self.rules = rules

    def analyze(self, source: list[str]) -> list[Token]:
        """
        Analyze a list of strings

        Parameters:
            source (list[str]): list of strings
        """
        tokens = list()

        for string in source:
            line = source.index(string)

            for character in string:
                column = string.index(character)

                for rule in self.rules:
                    result = match(rule.pattern, character)

                    if result is not None:
                        name = rule.name
                        idx = len(tokens) + 1
                        value = character

                        # fmt: off
                        tokens.append(Token(
                            name,
                            idx,
                            line,
                            column,
                            value
                        ))
                        # fmt: on

        return tokens

    def analyse(self, source: list[str]) -> list[Token]:
        """
        Analyse a list of strings

        Parameters:
            source (list[str]): list of strings
        """
        return self.analyze(source)