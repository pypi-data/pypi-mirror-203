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
"""olallieberry Token"""


class Token:
    """Lexical Token"""

    def __init__(
        self,
        # fmt: off
        __name: str,
        __idx: int,
        __line: int,
        __column: int,
        __value: str
        # fmt: on
    ) -> None:
        """
        __name (str): token name
        __idx (int): token identifier
        __line (int): token line 
        __column (int): token column
        __value (str): token value
        """
        self.name = __name
        self.idx = __idx
        self.line = __line
        self.column = __column
        self.value = __value

    def __repr__(self) -> str:
        """"""
        return "Token({name}, {idx}, {line}, {column}, {value})".format(
            name=f"name={self.name}",
            idx=f"idx={self.idx}",
            line=f"line={self.line}",
            column=f"column={self.column}",
            value=f"value={self.value}",
        )
