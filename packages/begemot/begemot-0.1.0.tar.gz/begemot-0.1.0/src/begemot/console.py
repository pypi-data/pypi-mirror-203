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
from sys import argv
from .analysers.lexer import lexer
from .analysers.parser import parser


def run(path: str) -> None:
    with open(path) as stream:
        lines = stream.read().split("\n")

        for line in lines:
            parser.parse(lexer.lex(line))


def handle(__argv: list[str]) -> None:
    command = __argv[1]
    argument = __argv[2]

    commands = {"run": run}
    commands[command](argument)


def main() -> None:
    handle(argv)
