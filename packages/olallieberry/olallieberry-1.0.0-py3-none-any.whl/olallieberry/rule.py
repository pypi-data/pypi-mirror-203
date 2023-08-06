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
"""olallieberry Rule"""

from re import Pattern


class Rule:
    """
    Lexical Rule

    Attributes:
        __name (str): rule name
        __pattern (str | Pattern[str]): rule pattern
    """

    def __init__(self, name: str, pattern: str | Pattern[str]) -> None:
        self.name = name
        self.pattern = pattern

    def __repr__(self) -> str:
        return f"Rule(name={self.name}, pattern={self.pattern})"
