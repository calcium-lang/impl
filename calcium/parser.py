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

from typing import cast, TYPE_CHECKING

from alchemist.front.lexer import CompilerEOIError
from alchemist.front.parser import Paths, GraphNode, Production, Parser, CompilerSyntaxError, CompilerNoPathError

from .lexicon import (
    Identifier,
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

if TYPE_CHECKING:
    from alchemist.front.lexer import Terminal

# [[[cog
# __name__ = "calcium.parser"
#
# import cog
#
# from .syntax import (CompilationUnit, PackageDeclaration, ImportDeclarations, TopLevelTypeDeclaration, ImportDeclaration, DeclarationEncapsulation,
#                      TypeDeclaration, ImportNames, FromName, PackageName, ImportName, PackageOrTypeName, TypedefDeclaration, EnumDeclaration,
#                      UnionDeclaration, StructDeclaration, Version, BaseType, TypedefBody, EnumLayout, EnumBody, UnionBody,
#                      DeclarationExtensibility, StructSeal, StructLayout, StructBody, BodyDeclarations, EnumConstants, UnionTypes, TypeNames,
#                      BodyDeclaration, EnumConstant, StaticInitializer, MemberDeclaration, VariableInitializer, SymbolNaming, MemberStaticity,
#                      FieldDeclaration, MethodDeclaration, MethodOverride, MethodHeader, MethodBody, MethodDeclarator, Parameters, FixedParameters,
#                      VariableArityParameter, FixedParameter, Type, PrimitiveType, PointerOrArraySuffix, TypeName, VoidPointerType, FunctionType,
#                      PointerNullity, TypeAtomicity, NumericType, PointerSuffix, ArrayDim, TypeStrictness, ParameterTypes, TypeBareness,
#                      FunctionStrictness, FunctionPurity, Result, IntegralType, FloatingPointType, ValueMutability, ValueVolatility, PointerWidth,
#                      ReferenceAliasability, ThisParameter, FixedParameterTypes, VariableArityParameterType, FixedParameterType,
#                      VariableArityParameterLayout, Block, BlockStatements, ArrayInitializer, StructInitializer, VariableInitializers,
#                      FieldInitializers, FieldInitializer)
# ]]]
# [[[end]]]

# Packages


# [[[cog
# cog.out(CompilationUnit.generate())
# ]]]
class CompilationUnit(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, PackageDeclaration)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ImportDeclarations)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, TopLevelTypeDeclaration)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(PackageDeclaration.generate())
# ]]]
class PackageDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Package)
        paths0 = self._process_paths(paths0, PackageName)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Semicolon)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ImportDeclarations.generate())
# ]]]
class ImportDeclarations(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, ImportDeclaration)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, ImportDeclaration)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TopLevelTypeDeclaration.generate())
# ]]]
class TopLevelTypeDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, DeclarationEncapsulation)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, TypeDeclaration)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(ImportDeclaration.generate())
# ]]]
class ImportDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Import)
        paths0 = self._process_paths(paths0, ImportNames)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FromName)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Semicolon)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(DeclarationEncapsulation.generate())
# ]]]
class DeclarationEncapsulation(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Public)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Protected)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, Private)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TypeDeclaration.generate())
# ]]]
class TypeDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, TypedefDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, EnumDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, UnionDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 4
            paths2 = paths0
            paths2 = self._process_paths(paths2, StructDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(ImportNames.generate())
# ]]]
class ImportNames(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, ImportName)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, ImportName)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FromName.generate())
# ]]]
class FromName(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, From)
        paths0 = self._process_paths(paths0, PackageOrTypeName)
        self.output_paths = paths0
# [[[end]]]

# Names


# [[[cog
# cog.out(PackageName.generate())
# ]]]
class PackageName(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Identifier)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, FullStop)
                paths1 = self._process_paths(paths1, Identifier)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ImportName.generate())
# ]]]
class ImportName(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, As)
            paths1 = self._process_paths(paths1, Identifier)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(PackageOrTypeName.generate())
# ]]]
class PackageOrTypeName(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, FullStop)
                paths1 = self._process_paths(paths1, Identifier)

                try:  # optional
                    paths2 = paths1
                    paths2 = self._process_paths(paths2, Version)
                    GraphNode.merge_paths(paths1, paths2)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]

# Typedefs, Enums, Unions and Structs


# [[[cog
# cog.out(TypedefDeclaration.generate())
# ]]]
class TypedefDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Typedef)
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, BaseType)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, TypedefBody)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(EnumDeclaration.generate())
# ]]]
class EnumDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, EnumLayout)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Enum)
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, BaseType)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, EnumBody)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(UnionDeclaration.generate())
# ]]]
class UnionDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Union)
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, UnionBody)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(StructDeclaration.generate())
# ]]]
class StructDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, DeclarationExtensibility)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, StructSeal)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, StructLayout)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Struct)
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, BaseType)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, StructBody)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(Version.generate())
# ]]]
class Version(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, At)
        paths0 = self._process_paths(paths0, Integer)
        paths0 = self._process_paths(paths0, FullStop)
        paths0 = self._process_paths(paths0, Integer)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(BaseType.generate())
# ]]]
class BaseType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Colon)
        paths0 = self._process_paths(paths0, Type)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TypedefBody.generate())
# ]]]
class TypedefBody(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, LeftCurlyBracket)
            paths2 = self._process_paths(paths2, BodyDeclarations)
            paths2 = self._process_paths(paths2, RightCurlyBracket)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Semicolon)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(EnumLayout.generate())
# ]]]
class EnumLayout(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Strict)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Unsafe)
            paths2 = self._process_paths(paths2, C)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(EnumBody.generate())
# ]]]
class EnumBody(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftCurlyBracket)
        paths0 = self._process_paths(paths0, EnumConstants)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Semicolon)
            paths1 = self._process_paths(paths1, BodyDeclarations)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightCurlyBracket)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(UnionBody.generate())
# ]]]
class UnionBody(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftCurlyBracket)
        paths0 = self._process_paths(paths0, UnionTypes)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Semicolon)
            paths1 = self._process_paths(paths1, BodyDeclarations)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightCurlyBracket)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(DeclarationExtensibility.generate())
# ]]]
class DeclarationExtensibility(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Final)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Abstract)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(StructSeal.generate())
# ]]]
class StructSeal(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Sealed)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, LeftParenthesis)
            paths1 = self._process_paths(paths1, TypeNames)
            paths1 = self._process_paths(paths1, RightParenthesis)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(StructLayout.generate())
# ]]]
class StructLayout(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Strict)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, C)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, Packed)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(StructBody.generate())
# ]]]
class StructBody(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftCurlyBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, BodyDeclarations)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightCurlyBracket)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(BodyDeclarations.generate())
# ]]]
class BodyDeclarations(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, BodyDeclaration)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, BodyDeclaration)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(EnumConstants.generate())
# ]]]
class EnumConstants(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, EnumConstant)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, EnumConstant)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(UnionTypes.generate())
# ]]]
class UnionTypes(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, TypeDeclaration)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, TypeDeclaration)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]

# The semicolon in TypedefBody must never be found in TypedefDeclaration.


# [[[cog
# cog.out(TypeNames.generate())
# ]]]
class TypeNames(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, TypeName)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, TypeName)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(BodyDeclaration.generate())
# ]]]
class BodyDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, StaticInitializer)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, DeclarationEncapsulation)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            # begin oneof
            paths3: Paths = {}

            try:  # option 1
                paths4 = paths2
                paths4 = self._process_paths(paths4, MemberDeclaration)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths4 = paths2
                paths4 = self._process_paths(paths4, TypeDeclaration)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths3) == 0:
                raise CompilerNoPathError(self)

            paths2 = paths3
            # end oneof

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

# TypedefBody must always be found in TypedefDeclaration.


# [[[cog
# cog.out(EnumConstant.generate())
# ]]]
class EnumConstant(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FullStop)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0

            # begin oneof
            paths2: Paths = {}

            try:  # option 1
                paths3 = paths1
                paths3 = self._process_paths(paths3, Equals)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths3 = paths1
                paths3 = self._process_paths(paths3, Colon)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths2) == 0:
                raise CompilerNoPathError(self)

            paths1 = paths2
            # end oneof

            paths1 = self._process_paths(paths1, VariableInitializer)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(StaticInitializer.generate())
# ]]]
class StaticInitializer(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, SymbolNaming)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Static)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, StringIdentifier)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Block)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(MemberDeclaration.generate())
# ]]]
class MemberDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, MemberStaticity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, FieldDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, MethodDeclaration)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(VariableInitializer.generate())
# ]]]
class VariableInitializer(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Expression)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, ArrayInitializer)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, StructInitializer)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(SymbolNaming.generate())
# ]]]
class SymbolNaming(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Strict)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Plain)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(MemberStaticity.generate())
# ]]]
class MemberStaticity(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Static)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FieldDeclaration.generate())
# ]]]
class FieldDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, ValueMutability)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ValueVolatility)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, SymbolNaming)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, StringIdentifier)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Colon)
        paths0 = self._process_paths(paths0, Type)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Equals)
            paths1 = self._process_paths(paths1, VariableInitializer)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Semicolon)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(MethodDeclaration.generate())
# ]]]
class MethodDeclaration(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, DeclarationExtensibility)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, MethodOverride)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FunctionStrictness)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FunctionPurity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Func)
        paths0 = self._process_paths(paths0, MethodHeader)
        paths0 = self._process_paths(paths0, MethodBody)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(MethodOverride.generate())
# ]]]
class MethodOverride(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Override)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(MethodHeader.generate())
# ]]]
class MethodHeader(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, MethodDeclarator)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, HyphenGreaterThan)
            paths1 = self._process_paths(paths1, Result)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(MethodBody.generate())
# ]]]
class MethodBody(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Block)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Semicolon)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(MethodDeclarator.generate())
# ]]]
class MethodDeclarator(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, SymbolNaming)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, StringIdentifier)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Colon)
            paths1 = self._process_paths(paths1, TypeName)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, LeftParenthesis)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Parameters)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightParenthesis)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(Parameters.generate())
# ]]]
class Parameters(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, ThisParameter)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, FixedParameters)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, VariableArityParameter)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, FixedParameters)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, VariableArityParameter)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, VariableArityParameter)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(FixedParameters.generate())
# ]]]
class FixedParameters(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, FixedParameter)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, FixedParameter)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(VariableArityParameter.generate())
# ]]]
class VariableArityParameter(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, TripleFullStop)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, VariableArityParameterLayout)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Colon)
            paths1 = self._process_paths(paths1, Type)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(FixedParameter.generate())
# ]]]
class FixedParameter(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Colon)
            paths1 = self._process_paths(paths1, Type)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]

# Types


# [[[cog
# cog.out(Type.generate())
# ]]]
class Type(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            # begin oneof
            paths3: Paths = {}

            try:  # option 1
                paths4 = paths2
                paths4 = self._process_paths(paths4, PrimitiveType)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths4 = paths2
                paths4 = self._process_paths(paths4, TypeName)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 3
                paths4 = paths2
                paths4 = self._process_paths(paths4, VoidPointerType)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths3) == 0:
                raise CompilerNoPathError(self)

            paths2 = paths3
            # end oneof

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, PointerOrArraySuffix)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, FunctionType)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, LeftParenthesis)
            paths2 = self._process_paths(paths2, FunctionType)
            paths2 = self._process_paths(paths2, RightParenthesis)

            # begin oneof
            paths3: Paths = {}

            try:  # option 1
                paths4 = paths2
                paths4 = self._process_paths(paths4, PointerNullity)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths4 = paths2
                paths4 = self._process_paths(paths4, PointerOrArraySuffix)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths3) == 0:
                raise CompilerNoPathError(self)

            paths2 = paths3
            # end oneof

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(PrimitiveType.generate())
# ]]]
class PrimitiveType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, TypeAtomicity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, NumericType)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Bool)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, _Char)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(PointerOrArraySuffix.generate())
# ]]]
class PointerOrArraySuffix(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, PointerSuffix)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, ArrayDim)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, PointerOrArraySuffix)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TypeName.generate())
# ]]]
class TypeName(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0

            # begin oneof
            paths2: Paths = {}

            try:  # option 1
                paths3 = paths1
                paths3 = self._process_paths(paths3, TypeStrictness)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths3 = paths1
                paths3 = self._process_paths(paths3, TypeBareness)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths2) == 0:
                raise CompilerNoPathError(self)

            paths1 = paths2
            # end oneof

            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Version)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, FullStop)
                paths1 = self._process_paths(paths1, Identifier)

                try:  # optional
                    paths2 = paths1
                    paths2 = self._process_paths(paths2, Version)
                    GraphNode.merge_paths(paths1, paths2)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, LeftParenthesis)

            try:  # optional
                paths2 = paths1
                paths2 = self._process_paths(paths2, ParameterTypes)
                GraphNode.merge_paths(paths1, paths2)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths1 = self._process_paths(paths1, RightParenthesis)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(VoidPointerType.generate())
# ]]]
class VoidPointerType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Unsafe)
        paths0 = self._process_paths(paths0, Void)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ValueMutability)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ValueVolatility)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Ampersand)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, TypeAtomicity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ReferenceAliasability)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, PointerNullity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FunctionType.generate())
# ]]]
class FunctionType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, TypeAtomicity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FunctionStrictness)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FunctionPurity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Func)
        paths0 = self._process_paths(paths0, LeftParenthesis)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ParameterTypes)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightParenthesis)
        paths0 = self._process_paths(paths0, HyphenGreaterThan)
        paths0 = self._process_paths(paths0, Result)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(PointerNullity.generate())
# ]]]
class PointerNullity(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Local)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Question)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(TypeAtomicity.generate())
# ]]]
class TypeAtomicity(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Atomic)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(NumericType.generate())
# ]]]
class NumericType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, IntegralType)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, FloatingPointType)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(PointerSuffix.generate())
# ]]]
class PointerSuffix(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ValueMutability)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ValueVolatility)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Ampersand)

        try:  # optional
            paths1 = paths0

            # begin oneof
            paths2: Paths = {}

            try:  # option 1
                paths3 = paths1
                paths3 = self._process_paths(paths3, PointerWidth)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths3 = paths1
                paths3 = self._process_paths(paths3, TypeAtomicity)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths2) == 0:
                raise CompilerNoPathError(self)

            paths1 = paths2
            # end oneof

            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, ReferenceAliasability)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, PointerNullity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ArrayDim.generate())
# ]]]
class ArrayDim(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftSquareBracket)

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, TypeStrictness)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Expression)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, TypeBareness)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        paths0 = self._process_paths(paths0, RightSquareBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, PointerNullity)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TypeStrictness.generate())
# ]]]
class TypeStrictness(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Strict)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ParameterTypes.generate())
# ]]]
class ParameterTypes(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, ThisParameter)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, FixedParameterTypes)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, VariableArityParameterType)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, FixedParameterTypes)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Comma)
                paths3 = self._process_paths(paths3, VariableArityParameterType)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, VariableArityParameterType)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(TypeBareness.generate())
# ]]]
class TypeBareness(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Unsafe)
        paths0 = self._process_paths(paths0, Bare)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FunctionStrictness.generate())
# ]]]
class FunctionStrictness(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Strict)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FunctionPurity.generate())
# ]]]
class FunctionPurity(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Local)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Const)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Pure)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(Result.generate())
# ]]]
class Result(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Noreturn)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Void)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, Type)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(IntegralType.generate())
# ]]]
class IntegralType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            # begin oneof
            paths3: Paths = {}

            try:  # option 1
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Ubyte)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Byte)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 3
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Ushort)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 4
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Short)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 5
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Uint)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths3) == 0:
                raise CompilerNoPathError(self)

            paths2 = paths3
            # end oneof

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, _Int)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0

            # begin oneof
            paths3: Paths = {}

            try:  # option 1
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Ulong)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # option 2
                paths4 = paths2
                paths4 = self._process_paths(paths4, _Long)
                GraphNode.merge_paths(paths3, paths4)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            if len(paths3) == 0:
                raise CompilerNoPathError(self)

            paths2 = paths3
            # end oneof

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FloatingPointType.generate())
# ]]]
class FloatingPointType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, _Float)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, _Double)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ValueMutability.generate())
# ]]]
class ValueMutability(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Unsafe)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Var)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Local)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Const)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ValueVolatility.generate())
# ]]]
class ValueVolatility(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Local)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Volatile)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Unsafe)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Stable)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(PointerWidth.generate())
# ]]]
class PointerWidth(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            try:  # optional
                paths3 = paths2

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, Unsafe)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                paths3 = self._process_paths(paths3, Unused)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, TypeStrictness)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Wide)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, TypeBareness)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ReferenceAliasability.generate())
# ]]]
class ReferenceAliasability(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Local)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Aliasable)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Unsafe)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            paths2 = self._process_paths(paths2, Restrict)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(ThisParameter.generate())
# ]]]
class ThisParameter(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, This)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Colon)
                paths3 = self._process_paths(paths3, TypeName)

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, ValueMutability)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, ValueVolatility)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, Ampersand)

                    try:  # optional
                        paths5 = paths4
                        paths5 = self._process_paths(paths5, PointerWidth)
                        GraphNode.merge_paths(paths4, paths5)
                    except (CompilerSyntaxError, CompilerEOIError):
                        pass

                    try:  # optional
                        paths5 = paths4
                        paths5 = self._process_paths(paths5, ReferenceAliasability)
                        GraphNode.merge_paths(paths4, paths5)
                    except (CompilerSyntaxError, CompilerEOIError):
                        pass

                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, This)
            paths2 = self._process_paths(paths2, Colon)
            paths2 = self._process_paths(paths2, ValueMutability)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, ValueVolatility)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Ampersand)

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, PointerWidth)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, ReferenceAliasability)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 3
            paths2 = paths0
            paths2 = self._process_paths(paths2, This)
            paths2 = self._process_paths(paths2, Colon)
            paths2 = self._process_paths(paths2, ValueVolatility)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, Ampersand)

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, PointerWidth)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                try:  # optional
                    paths4 = paths3
                    paths4 = self._process_paths(paths4, ReferenceAliasability)
                    GraphNode.merge_paths(paths3, paths4)
                except (CompilerSyntaxError, CompilerEOIError):
                    pass

                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 4
            paths2 = paths0
            paths2 = self._process_paths(paths2, This)
            paths2 = self._process_paths(paths2, Colon)
            paths2 = self._process_paths(paths2, Ampersand)

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, PointerWidth)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            try:  # optional
                paths3 = paths2
                paths3 = self._process_paths(paths3, ReferenceAliasability)
                GraphNode.merge_paths(paths2, paths3)
            except (CompilerSyntaxError, CompilerEOIError):
                pass

            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FixedParameterTypes.generate())
# ]]]
class FixedParameterTypes(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, FixedParameterType)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, FixedParameterType)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(VariableArityParameterType.generate())
# ]]]
class VariableArityParameterType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, TripleFullStop)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, VariableArityParameterLayout)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Colon)
        paths0 = self._process_paths(paths0, Type)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(FixedParameterType.generate())
# ]]]
class FixedParameterType(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, Colon)
        paths0 = self._process_paths(paths0, Type)
        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(VariableArityParameterLayout.generate())
# ]]]
class VariableArityParameterLayout(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Strict)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Unsafe)
            paths2 = self._process_paths(paths2, C)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        self.output_paths = paths0
# [[[end]]]

# Blocks and Statements


# [[[cog
# cog.out(Block.generate())
# ]]]
class Block(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftCurlyBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, BlockStatements)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightCurlyBracket)
        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(BlockStatements.generate())
# ]]]
class BlockStatements(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, BlockStatement)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, BlockStatement)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]

# Expressions

# Array and Struct Initializers


# [[[cog
# cog.out(ArrayInitializer.generate())
# ]]]
class ArrayInitializer(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftSquareBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, VariableInitializers)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightSquareBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Colon)
            paths1 = self._process_paths(paths1, Type)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(StructInitializer.generate())
# ]]]
class StructInitializer(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, LeftCurlyBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FieldInitializers)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, RightCurlyBracket)

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, Colon)
            paths1 = self._process_paths(paths1, TypeName)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(VariableInitializers.generate())
# ]]]
class VariableInitializers(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, VariableInitializer)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, VariableInitializer)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]


# [[[cog
# cog.out(FieldInitializers.generate())
# ]]]
class FieldInitializers(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}
        paths0 = self._process_paths(paths0, FieldInitializer)

        paths1 = paths0

        while True:  # repeat
            try:
                paths1 = self._process_paths(paths1, Comma)
                paths1 = self._process_paths(paths1, FieldInitializer)
                GraphNode.merge_paths(paths0, paths1)
            except (CompilerSyntaxError, CompilerEOIError):
                break

        self.output_paths = paths0
# [[[end]]]

###


# [[[cog
# cog.out(FieldInitializer.generate())
# ]]]
class FieldInitializer(Production):
    def _derive(self) -> None:
        input_path = cast(GraphNode, self.input_path)
        paths0: Paths = {cast("Terminal", input_path.path): {input_path}}

        try:  # optional
            paths1 = paths0
            paths1 = self._process_paths(paths1, FullStop)
            GraphNode.merge_paths(paths0, paths1)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        paths0 = self._process_paths(paths0, Identifier)

        # begin oneof
        paths1: Paths = {}

        try:  # option 1
            paths2 = paths0
            paths2 = self._process_paths(paths2, Equals)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        try:  # option 2
            paths2 = paths0
            paths2 = self._process_paths(paths2, Colon)
            GraphNode.merge_paths(paths1, paths2)
        except (CompilerSyntaxError, CompilerEOIError):
            pass

        if len(paths1) == 0:
            raise CompilerNoPathError(self)

        paths0 = paths1
        # end oneof

        paths0 = self._process_paths(paths0, VariableInitializer)
        self.output_paths = paths0
# [[[end]]]


class CalciumParser(Parser):
    _start = CompilationUnit
