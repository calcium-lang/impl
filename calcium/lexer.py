# This file is part of the Calcium language implementation
# Copyright (C) 2023  Natan Junges <natanajunges@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from alchemist.front.lexer import Lexer

from .lexicon import (
    WHITESPACES,
    SINGLELINE_COMMENT,
    MULTILINE_COMMENT,
    Identifier,
    StringLiteral,
    StringIdentifier,
    Abstract,
    Aliasable,
    As,
    Atomic,
    Bare,
    Bool,
    C,
    Const,
    Enum,
    Final,
    From,
    Func,
    Import,
    Local,
    Noreturn,
    Override,
    Package,
    Packed,
    Plain,
    Private,
    Protected,
    Public,
    Pure,
    Restrict,
    Sealed,
    Stable,
    Static,
    Strict,
    Struct,
    This,
    Typedef,
    Union,
    Unsafe,
    Unused,
    Var,
    Void,
    Volatile,
    Wide,
    _Byte,
    _Char,
    _Double,
    _Float,
    _Int,
    _Long,
    _Short,
    _Ubyte,
    _Uint,
    _Ulong,
    _Ushort,
    BlockStatement,
    Expression,
    Integer,
    LeftSquareBracket,
    RightSquareBracket,
    LeftParenthesis,
    RightParenthesis,
    LeftCurlyBracket,
    RightCurlyBracket,
    FullStop,
    HyphenGreaterThan,
    Ampersand,
    Question,
    Colon,
    Semicolon,
    TripleFullStop,
    Equals,
    Comma,
    At
)


class CalciumLexer(Lexer):
    _terminals = Lexer.sort([
        (
            Identifier,
            Lexer.sort([
                Abstract,
                Aliasable,
                As,
                Atomic,
                Bare,
                Bool,
                C,
                Const,
                Enum,
                Final,
                From,
                Func,
                Import,
                Local,
                Noreturn,
                Override,
                Package,
                Packed,
                Plain,
                Private,
                Protected,
                Public,
                Pure,
                Restrict,
                Sealed,
                Stable,
                Static,
                Strict,
                Struct,
                This,
                Typedef,
                Union,
                Unsafe,
                Unused,
                Var,
                Void,
                Volatile,
                Wide,
                _Byte,
                _Char,
                _Double,
                _Float,
                _Int,
                _Long,
                _Short,
                _Ubyte,
                _Uint,
                _Ulong,
                _Ushort,
                BlockStatement,
                Expression
            ])
        ),
        (StringLiteral, [StringIdentifier]),
        Integer,
        LeftSquareBracket,
        RightSquareBracket,
        LeftParenthesis,
        RightParenthesis,
        LeftCurlyBracket,
        RightCurlyBracket,
        FullStop,
        HyphenGreaterThan,
        Ampersand,
        Question,
        Colon,
        Semicolon,
        TripleFullStop,
        Equals,
        Comma,
        At
    ])
    _ignored = [WHITESPACES, SINGLELINE_COMMENT, MULTILINE_COMMENT]
