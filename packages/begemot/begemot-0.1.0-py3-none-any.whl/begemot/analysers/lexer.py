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
from ..tokens import TOKENS, WHITESPACE
from rply import LexerGenerator


generator = LexerGenerator()


for token in TOKENS.items():
    name, pattern = token
    generator.add(name, pattern)

generator.ignore(WHITESPACE)


lexer = generator.build()
