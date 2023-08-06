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

# Add
TOKENS = {
    "INTEGER": r"\d+",

    "ADDITION": r"lisamine",
    "SUBTRACTION": r"lahutamine",
    "MULTIPLICATION": r"korrutamine",
    "DIVISION": r"jaotus",
    "EXPONENTIATION": r"alkendamine",

    "OPEN_PAR": r"\(",
    "CLOSE_PAR": r"\)",
    "SEMICOLON": r"\;",

    "PRINT": r"printida",
}

# Ignore
WHITESPACE = r"\s+"
