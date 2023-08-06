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
from ..tokens import TOKENS
# fmt: off
from ..modules.math import (
    addition, subtraction,
    multiplication, division,
    exponentiation
)
# fmt: on
from ..boxes.integer import IntegerBox
from typing import Any

from rply import ParserGenerator

# fmt: off
generator = ParserGenerator(list(TOKENS), precedence=[
    ("left", ["ADDITION", "SUBTRACTION"]),
    ("right", ["MULTIPLICATION", "DIVISION", "EXPONENTIATION"])
])
# fmt: on


@generator.production("main : expression")
def main(pieces: list[Any]):
    return pieces[0]


@generator.production("main : PRINT OPEN_PAR expression CLOSE_PAR SEMICOLON")
def expression_print(pieces: list[Any]) -> None:
    print(str(pieces[2].value))


@generator.production("expression : INTEGER")
def expression_integer(pieces: list[Any]):
    return IntegerBox(int(pieces[0].value))


@generator.production("expression : expression ADDITION expression")
@generator.production("expression : expression SUBTRACTION expression")
@generator.production("expression : expression MULTIPLICATION expression")
@generator.production("expression : expression DIVISION expression")
@generator.production("expression : expression EXPONENTIATION expression")
def expression_operators(pieces: list[Any]) -> IntegerBox:
    left_expression = pieces[0].value
    right_expression = pieces[2].value
    operator = pieces[1].gettokentype()

    # fmt: off
    callbacks = {
        "ADDITION": addition,
        "SUBTRACTION": subtraction,
        "MULTIPLICATION": multiplication,
        "DIVISION": division,
        "EXPONENTIATION": exponentiation
    }
    value = callbacks[operator](
        left_expression,
        right_expression
    )
    # fmt: on

    return IntegerBox(value)


parser = generator.build()
