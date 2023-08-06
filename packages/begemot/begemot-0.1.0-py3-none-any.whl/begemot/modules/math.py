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
from ..constants import COMPONENTS
from ctypes import c_int
from ctypes import cdll


library = cdll.LoadLibrary(f"{COMPONENTS}/math.so")


def addition(a: int, b: int) -> int:
    # fmt: off
    return int(library.addition(
        c_int(a), c_int(b)
    ))
    # fmt: on

def subtraction(a: int, b: int) -> int:
    # fmt: off
    return int(library.subtraction(
        c_int(a), c_int(b)
    ))
    # fmt: on

def multiplication(a: int, b: int) -> int:
    # fmt: off
    return int(library.multiplication(
        c_int(a), c_int(b)
    ))
    # fmt: on

def division(a: int, b: int) -> int:
    # fmt: off
    return int(library.division(
        c_int(a), c_int(b)
    ))
    # fmt: on

def exponentiation(a: int, b: int) -> int:
    return int(library.exponentiation(
        c_int(a), c_int(b)
    ))