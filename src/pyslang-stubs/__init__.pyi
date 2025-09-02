"""
Python bindings for slang, the SystemVerilog compiler library
"""

from __future__ import annotations

import os
import typing
from typing import Any, ClassVar, Final

from typing_extensions import Self

try:
    from pybind11_builtins import pybind11_type as _metaclass  # type: ignore
except ImportError:
    _metaclass = type  # type: ignore

class ASTFlags(metaclass=_metaclass):
    AllowClockingBlock: ClassVar[ASTFlags]
    """Value = 131072"""
    AllowCoverageSampleFormal: ClassVar[ASTFlags]
    """Value = 33554432"""
    AllowCoverpoint: ClassVar[ASTFlags]
    """Value = 67108864"""
    AllowDataType: ClassVar[ASTFlags]
    """Value = 4"""
    AllowInterconnect: ClassVar[ASTFlags]
    """Value = 536870912"""
    AllowNetType: ClassVar[ASTFlags]
    """Value = 134217728"""
    AllowTypeReferences: ClassVar[ASTFlags]
    """Value = 32768"""
    AllowUnboundedLiteral: ClassVar[ASTFlags]
    """Value = 512"""
    AllowUnboundedLiteralArithmetic: ClassVar[ASTFlags]
    """Value = 1024"""
    AssertionDefaultArg: ClassVar[ASTFlags]
    """Value = 17179869184"""
    AssertionDelayOrRepetition: ClassVar[ASTFlags]
    """Value = 524288"""
    AssertionExpr: ClassVar[ASTFlags]
    """Value = 65536"""
    AssertionInstanceArgCheck: ClassVar[ASTFlags]
    """Value = 262144"""
    AssignmentAllowed: ClassVar[ASTFlags]
    """Value = 8"""
    AssignmentDisallowed: ClassVar[ASTFlags]
    """Value = 16"""
    BindInstantiation: ClassVar[ASTFlags]
    """Value = 2199023255552"""
    ConcurrentAssertActionBlock: ClassVar[ASTFlags]
    """Value = 16777216"""
    ConfigParam: ClassVar[ASTFlags]
    """Value = 137438953472"""
    DPIArg: ClassVar[ASTFlags]
    """Value = 8589934592"""
    DisallowUDNT: ClassVar[ASTFlags]
    """Value = 1099511627776"""
    EventExpression: ClassVar[ASTFlags]
    """Value = 16384"""
    Final: ClassVar[ASTFlags]
    """Value = 4096"""
    ForkJoinAnyNone: ClassVar[ASTFlags]
    """Value = 549755813888"""
    Function: ClassVar[ASTFlags]
    """Value = 2048"""
    InsideConcatenation: ClassVar[ASTFlags]
    """Value = 1"""
    LAndRValue: ClassVar[ASTFlags]
    """Value = 34359738368"""
    LValue: ClassVar[ASTFlags]
    """Value = 1048576"""
    NoReference: ClassVar[ASTFlags]
    """Value = 68719476736"""
    NonBlockingTimingControl: ClassVar[ASTFlags]
    """Value = 8192"""
    NonProcedural: ClassVar[ASTFlags]
    """Value = 32"""
    None_: ClassVar[ASTFlags]
    """Value = 0"""
    OutputArg: ClassVar[ASTFlags]
    """Value = 268435456"""
    PropertyNegation: ClassVar[ASTFlags]
    """Value = 2097152"""
    PropertyTimeAdvance: ClassVar[ASTFlags]
    """Value = 4194304"""
    RecursivePropertyArg: ClassVar[ASTFlags]
    """Value = 8388608"""
    SpecifyBlock: ClassVar[ASTFlags]
    """Value = 2147483648"""
    SpecparamInitializer: ClassVar[ASTFlags]
    """Value = 4294967296"""
    StaticInitializer: ClassVar[ASTFlags]
    """Value = 64"""
    StreamingAllowed: ClassVar[ASTFlags]
    """Value = 128"""
    StreamingWithRange: ClassVar[ASTFlags]
    """Value = 1073741824"""
    TopLevelStatement: ClassVar[ASTFlags]
    """Value = 256"""
    TypeOperator: ClassVar[ASTFlags]
    """Value = 274877906944"""
    UnevaluatedBranch: ClassVar[ASTFlags]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class EvalFlags(metaclass=_metaclass):
    None_: ClassVar[EvalFlags]
    """Value = 0"""
    IsScript: ClassVar[EvalFlags]
    """Value = 1"""
    CacheResults: ClassVar[EvalFlags]
    """Value = 2"""
    SpecparamsAllowed: ClassVar[EvalFlags]
    """Value = 4"""
    CovergroupExpr: ClassVar[EvalFlags]
    """Value = 8"""
    AllowUnboundedPlaceholder: ClassVar[EvalFlags]
    """Value = 16"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ASTContext(metaclass=_metaclass):
    """Contains required context for binding syntax nodes with symbols to form an AST."""

    def __init__(
        self, scope: Scope, lookupLocation: LookupLocation, flags: ASTFlags = ASTFlags.None_
    ) -> None: ...
    def addAssertionBacktrace(self, diag: Diagnostic) -> None:
        """If this context is within an assertion instance, report a backtrace of how that
        instance was expanded to the given diagnostic; otherwise, do nothing.
        """

    def addDiag(self, code: DiagCode, location: SourceLocation | SourceRange) -> Diagnostic:
        """Issues a new diagnostic."""

    def eval(self, expr: Expression, extraFlags: EvalFlags = EvalFlags.None_) -> ConstantValue:
        """Evaluates the provided expression as a constant expression."""

    def evalDimension(
        self, syntax: VariableDimensionSyntax, requireRange: bool, isPacked: bool
    ) -> EvaluatedDimension:
        """Evaluates the given dimension syntax to determine its compile-time bounds and
        other properties.

        Args:
            syntax (VariableDimensionSyntax): The dimension syntax node to evaluate
            requireRange (bool): If true, the dimension syntax must represent a range,
                                 as opposed to a single index or other kind of dimension
            isPacked (bool): If true, this dimension should be treated as a packed dimension

        Returns:
            EvaluatedDimension: Details about the evaluated dimension
        """
    @typing.overload
    def evalInteger(self, syntax: Any, extraFlags: ASTFlags = ...) -> int | None: ...
    @typing.overload
    def evalInteger(self, expr: Any, extraFlags: EvalFlags = ...) -> int | None: ...
    def evalPackedDimension(self, syntax: Any) -> EvaluatedDimension: ...
    def evalUnpackedDimension(self, syntax: Any) -> EvaluatedDimension: ...
    def getRandMode(self, symbol: Any) -> RandMode: ...
    def requireBooleanConvertible(self, expr: Any) -> bool: ...
    def requireGtZero(self, value: int | None, range: Any) -> bool: ...
    @typing.overload
    def requireIntegral(self, expr: Any) -> bool: ...
    @typing.overload
    def requireIntegral(self, cv: Any, range: Any) -> bool: ...
    def requireNoUnknowns(self, value: Any, range: Any) -> bool: ...
    def requirePositive(self, value: Any, range: Any) -> bool: ...
    @typing.overload
    def requireSimpleExpr(self, expr: Any) -> ExpressionSyntax: ...
    @typing.overload
    def requireSimpleExpr(self, expr: Any, code: Any) -> ExpressionSyntax: ...
    @typing.overload
    def requireValidBitWidth(self, width: int, range: Any) -> bool: ...
    @typing.overload
    def requireValidBitWidth(self, value: Any, range: Any) -> int | None: ...
    def resetFlags(self, addedFlags: ASTFlags) -> ASTContext: ...
    def tryEval(self, expr: Any) -> ConstantValue: ...
    @property
    def flags(self) -> ASTFlags: ...
    @property
    def getCompilation(self) -> Compilation: ...
    @property
    def getInstance(self) -> InstanceSymbolBase: ...
    @property
    def getLocation(self) -> LookupLocation: ...
    @property
    def getProceduralBlock(self) -> ProceduralBlockSymbol: ...
    @property
    def inAlwaysCombLatch(self) -> bool: ...
    @property
    def inUnevaluatedBranch(self) -> bool: ...
    @property
    def lookupIndex(self) -> Any: ...
    @property
    def scope(self) -> Scope: ...

class AbortAssertionExpr(AssertionExpr):
    class Action(metaclass=_metaclass):
        Accept: ClassVar[Self]
        """Value: 0"""
        Reject: ClassVar[Self]
        """Value: 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Accept: Final = Action.Accept
    Reject: Final = Action.Reject

    @property
    def action(self) -> Action: ...
    @property
    def condition(self) -> Expression: ...
    @property
    def expr(self) -> AssertionExpr: ...
    @property
    def isSync(self) -> bool: ...

class AcceptOnPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    expr: PropertyExprSyntax
    keyword: Token
    openParen: Token

class ActionBlockSyntax(SyntaxNode):
    elseClause: ElseClauseSyntax
    statement: StatementSyntax

class AnalysisFlags(metaclass=_metaclass):
    AllowDupInitialDrivers: ClassVar[AnalysisFlags]
    """Value = 16"""
    AllowMultiDrivenLocals: ClassVar[AnalysisFlags]
    """Value = 8"""
    CheckUnused: ClassVar[AnalysisFlags]
    """Value = 1"""
    FullCaseFourState: ClassVar[AnalysisFlags]
    """Value = 4"""
    FullCaseUniquePriority: ClassVar[AnalysisFlags]
    """Value = 2"""
    # TODO: File issue on slang repo about 'None' namming
    # None: ClassVar[AnalysisFlags]
    # Value = 0

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class AnalysisManager(metaclass=_metaclass):
    def __init__(self, options: AnalysisOptions = ...) -> None: ...
    def analyze(self, compilation: Any) -> AnalyzedDesign: ...
    def analyzeScopeBlocking(self, scope: Any, parentProcedure: Any = None) -> AnalyzedScope: ...
    def getAnalyzedScope(self, scope: Any) -> AnalyzedScope: ...
    def getAnalyzedSubroutine(self, symbol: Any) -> Any: ...
    def getDiagnostics(self, sourceManager: Any) -> Any: ...
    def getDrivers(self, symbol: Any) -> list[tuple[ValueDriver, tuple[int, int]]]: ...
    @property
    def options(self) -> AnalysisOptions: ...

class AnalysisOptions(metaclass=_metaclass):
    flags: AnalysisFlags
    maxCaseAnalysisSteps: int
    maxLoopAnalysisSteps: int
    numThreads: int
    def __init__(self) -> None: ...

class AnalyzedDesign(metaclass=_metaclass):
    @property
    def compilation(self) -> Any: ...
    @property
    def compilationUnits(self) -> list[AnalyzedScope]: ...
    @property
    def packages(self) -> list[AnalyzedScope]: ...
    @property
    def topInstances(self) -> list[PendingAnalysis]: ...

class AnalyzedProcedure(metaclass=_metaclass):
    @property
    def analyzedSymbol(self) -> Any: ...
    @property
    def assertions(self) -> list[Any]: ...
    @property
    def callExpressions(self) -> list[Any]: ...
    @property
    def drivers(self) -> list[tuple[Any, list[tuple[ValueDriver, tuple[int, int]]]]]: ...
    @property
    def inferredClock(self) -> Any: ...
    @property
    def parentProcedure(self) -> AnalyzedProcedure: ...

class AnalyzedScope(metaclass=_metaclass):
    @property
    def childScopes(self) -> list[Any]: ...
    @property
    def procedures(self) -> list[Any]: ...
    @property
    def scope(self) -> Any: ...

class AnonymousProgramSymbol(Symbol, Scope):
    pass

class AnonymousProgramSyntax(MemberSyntax):
    endkeyword: Token
    keyword: Token
    members: Any
    semi: Token

class AnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: Any

class AnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: Any
    semi: Token

class ArbitrarySymbolExpression(Expression):
    @property
    def symbol(self) -> Any: ...

class ArgumentDirection(metaclass=_metaclass):
    In: ClassVar[ArgumentDirection]
    """Value = 0"""
    InOut: ClassVar[ArgumentDirection]
    """Value = 2"""
    Out: ClassVar[ArgumentDirection]
    """Value = 1"""
    Ref: ClassVar[ArgumentDirection]
    """Value = 3"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ArgumentListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    parameters: Any

class ArgumentSyntax(SyntaxNode):
    pass

class ArrayOrRandomizeMethodExpressionSyntax(ExpressionSyntax):
    args: ParenExpressionListSyntax
    constraints: ConstraintBlockSyntax
    method: ExpressionSyntax
    with_: Token

class AssertionExpr(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> AssertionExprKind: ...
    @property
    def syntax(self) -> Any: ...

class AssertionExprKind(metaclass=_metaclass):
    Abort: ClassVar[AssertionExprKind]
    """Value = 9"""
    Binary: ClassVar[AssertionExprKind]
    """Value = 5"""
    Case: ClassVar[AssertionExprKind]
    """Value = 11"""
    Clocking: ClassVar[AssertionExprKind]
    """Value = 7"""
    Conditional: ClassVar[AssertionExprKind]
    """Value = 10"""
    DisableIff: ClassVar[AssertionExprKind]
    """Value = 12"""
    FirstMatch: ClassVar[AssertionExprKind]
    """Value = 6"""
    Invalid: ClassVar[AssertionExprKind]
    """Value = 0"""
    SequenceConcat: ClassVar[AssertionExprKind]
    """Value = 2"""
    SequenceWithMatch: ClassVar[AssertionExprKind]
    """Value = 3"""
    Simple: ClassVar[AssertionExprKind]
    """Value = 1"""
    StrongWeak: ClassVar[AssertionExprKind]
    """Value = 8"""
    Unary: ClassVar[AssertionExprKind]
    """Value = 4"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class AssertionInstanceExpression(Expression):
    @property
    def arguments(self) -> list[tuple[Any, Expression | AssertionExpr | TimingControl]]: ...
    @property
    def body(self) -> AssertionExpr: ...
    @property
    def isRecursiveProperty(self) -> bool: ...
    @property
    def localVars(self) -> list[Any]: ...
    @property
    def symbol(self) -> Any: ...

class AssertionItemPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: Any

class AssertionItemPortSyntax(SyntaxNode):
    attributes: Any
    defaultValue: EqualsAssertionArgClauseSyntax
    dimensions: Any
    direction: Token
    local: Token
    name: Token
    type: DataTypeSyntax

class AssertionKind(metaclass=_metaclass):
    Assert: ClassVar[AssertionKind]
    """Value = 0"""
    Assume: ClassVar[AssertionKind]
    """Value = 1"""
    CoverProperty: ClassVar[AssertionKind]
    """Value = 2"""
    CoverSequence: ClassVar[AssertionKind]
    """Value = 3"""
    Expect: ClassVar[AssertionKind]
    """Value = 5"""
    Restrict: ClassVar[AssertionKind]
    """Value = 4"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class AssertionPortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection | None: ...
    @property
    def isLocalVar(self) -> bool: ...
    @property
    def type(self) -> Any: ...

class AssignmentExpression(Expression):
    @property
    def isCompound(self) -> bool: ...
    @property
    def isLValueArg(self) -> bool: ...
    @property
    def isNonBlocking(self) -> bool: ...
    @property
    def left(self) -> Expression: ...
    @property
    def op(self) -> BinaryOperator | None: ...
    @property
    def right(self) -> Expression: ...
    @property
    def timingControl(self) -> TimingControl: ...

class AssignmentPatternExpressionBase(Expression):
    @property
    def elements(self) -> list[Expression]: ...

class AssignmentPatternExpressionSyntax(PrimaryExpressionSyntax):
    pattern: AssignmentPatternSyntax
    type: DataTypeSyntax

class AssignmentPatternItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    key: ExpressionSyntax

class AssignmentPatternSyntax(SyntaxNode):
    pass

class AssociativeArrayType(Type):
    @property
    def elementType(self) -> Type: ...
    @property
    def indexType(self) -> Type: ...

class AttributeInstanceSyntax(SyntaxNode):
    closeParen: Token
    closeStar: Token
    openParen: Token
    openStar: Token
    specs: Any

class AttributeSpecSyntax(SyntaxNode):
    name: Token
    value: EqualsValueClauseSyntax

class AttributeSymbol(Symbol):
    @property
    def value(self) -> ConstantValue: ...

class BadExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax

class Bag(metaclass=_metaclass):
    compilationOptions: CompilationOptions
    lexerOptions: Any
    parserOptions: Any
    preprocessorOptions: Any
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, list: list) -> None: ...

class BeginKeywordsDirectiveSyntax(DirectiveSyntax):
    versionSpecifier: Token

class BinSelectWithFilterExpr(BinsSelectExpr):
    @property
    def expr(self) -> BinsSelectExpr: ...
    @property
    def filter(self) -> Any: ...
    @property
    def matchesExpr(self) -> Any: ...

class BinSelectWithFilterExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    filter: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
    openParen: Token
    with_: Token

class BinaryAssertionExpr(AssertionExpr):
    @property
    def left(self) -> AssertionExpr: ...
    @property
    def op(self) -> BinaryAssertionOperator: ...
    @property
    def right(self) -> AssertionExpr: ...

class BinaryAssertionOperator(metaclass=_metaclass):
    And: ClassVar[BinaryAssertionOperator]
    """Value = 0"""
    Iff: ClassVar[BinaryAssertionOperator]
    """Value = 5"""
    Implies: ClassVar[BinaryAssertionOperator]
    """Value = 10"""
    Intersect: ClassVar[BinaryAssertionOperator]
    """Value = 2"""
    NonOverlappedFollowedBy: ClassVar[BinaryAssertionOperator]
    """Value = 14"""
    NonOverlappedImplication: ClassVar[BinaryAssertionOperator]
    """Value = 12"""
    Or: ClassVar[BinaryAssertionOperator]
    """Value = 1"""
    OverlappedFollowedBy: ClassVar[BinaryAssertionOperator]
    """Value = 13"""
    OverlappedImplication: ClassVar[BinaryAssertionOperator]
    """Value = 11"""
    SUntil: ClassVar[BinaryAssertionOperator]
    """Value = 7"""
    SUntilWith: ClassVar[BinaryAssertionOperator]
    """Value = 9"""
    Throughout: ClassVar[BinaryAssertionOperator]
    """Value = 3"""
    Until: ClassVar[BinaryAssertionOperator]
    """Value = 6"""
    UntilWith: ClassVar[BinaryAssertionOperator]
    """Value = 8"""
    Within: ClassVar[BinaryAssertionOperator]
    """Value = 4"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class BinaryBinsSelectExpr(BinsSelectExpr):
    class Op(metaclass=_metaclass):
        And: ClassVar[Self]
        """Value = 0"""
        Or: ClassVar[Self]
        """Value = 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    And: Final = Op.And
    Or: Final = Op.Or

    @property
    def left(self) -> BinsSelectExpr: ...
    @property
    def op(self) -> Any: ...
    @property
    def right(self) -> BinsSelectExpr: ...

class BinaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    left: BinsSelectExpressionSyntax
    op: Token
    right: BinsSelectExpressionSyntax

class BinaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    left: BlockEventExpressionSyntax
    orKeyword: Token
    right: BlockEventExpressionSyntax

class BinaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    left: ConditionalDirectiveExpressionSyntax
    op: Token
    right: ConditionalDirectiveExpressionSyntax

class BinaryEventExpressionSyntax(EventExpressionSyntax):
    left: EventExpressionSyntax
    operatorToken: Token
    right: EventExpressionSyntax

class BinaryExpression(Expression):
    @property
    def left(self) -> Expression: ...
    @property
    def op(self) -> BinaryOperator: ...
    @property
    def right(self) -> Expression: ...

class BinaryExpressionSyntax(ExpressionSyntax):
    attributes: Any
    left: ExpressionSyntax
    operatorToken: Token
    right: ExpressionSyntax

class BinaryOperator(metaclass=_metaclass):
    Add: ClassVar[BinaryOperator]
    """Value = 0"""
    ArithmeticShiftLeft: ClassVar[BinaryOperator]
    """Value = 25"""
    ArithmeticShiftRight: ClassVar[BinaryOperator]
    """Value = 26"""
    BinaryAnd: ClassVar[BinaryOperator]
    """Value = 5"""
    BinaryOr: ClassVar[BinaryOperator]
    """Value = 6"""
    BinaryXnor: ClassVar[BinaryOperator]
    """Value = 8"""
    BinaryXor: ClassVar[BinaryOperator]
    """Value = 7"""
    CaseEquality: ClassVar[BinaryOperator]
    """Value = 11"""
    CaseInequality: ClassVar[BinaryOperator]
    """Value = 12"""
    Divide: ClassVar[BinaryOperator]
    """Value = 3"""
    Equality: ClassVar[BinaryOperator]
    """Value = 9"""
    GreaterThan: ClassVar[BinaryOperator]
    """Value = 14"""
    GreaterThanEqual: ClassVar[BinaryOperator]
    """Value = 13"""
    Inequality: ClassVar[BinaryOperator]
    """Value = 10"""
    LessThan: ClassVar[BinaryOperator]
    """Value = 16"""
    LessThanEqual: ClassVar[BinaryOperator]
    """Value = 15"""
    LogicalAnd: ClassVar[BinaryOperator]
    """Value = 19"""
    LogicalEquivalence: ClassVar[BinaryOperator]
    """Value = 22"""
    LogicalImplication: ClassVar[BinaryOperator]
    """Value = 21"""
    LogicalOr: ClassVar[BinaryOperator]
    """Value = 20"""
    LogicalShiftLeft: ClassVar[BinaryOperator]
    """Value = 23"""
    LogicalShiftRight: ClassVar[BinaryOperator]
    """Value = 24"""
    Mod: ClassVar[BinaryOperator]
    """Value = 4"""
    Multiply: ClassVar[BinaryOperator]
    """Value = 2"""
    Power: ClassVar[BinaryOperator]
    """Value = 27"""
    Subtract: ClassVar[BinaryOperator]
    """Value = 1"""
    WildcardEquality: ClassVar[BinaryOperator]
    """Value = 17"""
    WildcardInequality: ClassVar[BinaryOperator]
    """Value = 18"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class BinaryPropertyExprSyntax(PropertyExprSyntax):
    left: PropertyExprSyntax
    op: Token
    right: PropertyExprSyntax

class BinarySequenceExprSyntax(SequenceExprSyntax):
    left: SequenceExprSyntax
    op: Token
    right: SequenceExprSyntax

class BindDirectiveSyntax(MemberSyntax):
    bind: Token
    instantiation: MemberSyntax
    target: NameSyntax
    targetInstances: BindTargetListSyntax

class BindTargetListSyntax(SyntaxNode):
    colon: Token
    targets: Any

class BinsSelectConditionExprSyntax(BinsSelectExpressionSyntax):
    binsof: Token
    closeParen: Token
    intersects: IntersectClauseSyntax
    name: NameSyntax
    openParen: Token

class BinsSelectExpr(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> BinsSelectExprKind: ...
    @property
    def syntax(self) -> Any: ...

class BinsSelectExprKind(metaclass=_metaclass):
    Binary: ClassVar[BinsSelectExprKind]
    """Value = 3"""
    Condition: ClassVar[BinsSelectExprKind]
    """Value = 1"""
    CrossId: ClassVar[BinsSelectExprKind]
    """Value = 6"""
    Invalid: ClassVar[BinsSelectExprKind]
    """Value = 0"""
    SetExpr: ClassVar[BinsSelectExprKind]
    """Value = 4"""
    Unary: ClassVar[BinsSelectExprKind]
    """Value = 2"""
    WithFilter: ClassVar[BinsSelectExprKind]
    """Value = 5"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class BinsSelectExpressionSyntax(SyntaxNode):
    pass

class BinsSelectionSyntax(MemberSyntax):
    equals: Token
    expr: BinsSelectExpressionSyntax
    iff: CoverageIffClauseSyntax
    keyword: Token
    name: Token
    semi: Token

class BitSelectSyntax(SelectorSyntax):
    expr: ExpressionSyntax

class BlockCoverageEventSyntax(SyntaxNode):
    atat: Token
    closeParen: Token
    expr: BlockEventExpressionSyntax
    openParen: Token

class BlockEventExpressionSyntax(SyntaxNode):
    pass

class BlockEventListControl(TimingControl):
    class Event(metaclass=_metaclass):
        @property
        def isBegin(self) -> bool: ...
        @property
        def target(self) -> Any: ...

    @property
    def events(self) -> list[Any]: ...

class BlockStatement(Statement):
    @property
    def blockKind(self) -> StatementBlockKind: ...
    @property
    def blockSymbol(self) -> Any: ...
    @property
    def body(self) -> Statement: ...

class BlockStatementSyntax(StatementSyntax):
    begin: Token
    blockName: NamedBlockClauseSyntax
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: Any

class BreakStatement(Statement):
    pass

class BufferID(metaclass=_metaclass):
    placeholder: typing.ClassVar[BufferID]  # value = BufferID(4294967295)
    @staticmethod
    def getPlaceholder() -> BufferID: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __ge__(self, arg0: BufferID) -> bool: ...
    def __gt__(self, arg0: BufferID) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self) -> None: ...
    def __le__(self, arg0: BufferID) -> bool: ...
    def __lt__(self, arg0: BufferID) -> bool: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    @property
    def id(self) -> int: ...

class BumpAllocator(metaclass=_metaclass):
    def __init__(self) -> None: ...

class CHandleType(Type):
    pass

class CallExpression(Expression):
    class IteratorCallInfo(metaclass=_metaclass):
        @property
        def iterExpr(self) -> Expression: ...
        @property
        def iterVar(self) -> Any: ...

    class RandomizeCallInfo(metaclass=_metaclass):
        @property
        def constraintRestrictions(self) -> list[str]: ...
        @property
        def inlineConstraints(self) -> Constraint: ...

    class SystemCallInfo(metaclass=_metaclass):
        @property
        def extraInfo(
            self,
        ) -> None | CallExpression.IteratorCallInfo | CallExpression.RandomizeCallInfo: ...
        @property
        def scope(self) -> Any: ...
        @property
        def subroutine(self) -> SystemSubroutine: ...

    @property
    def arguments(self) -> list[Expression]: ...
    @property
    def isSystemCall(self) -> bool: ...
    @property
    def subroutine(self) -> Any: ...
    @property
    def subroutineKind(self) -> SubroutineKind: ...
    @property
    def subroutineName(self) -> str: ...
    @property
    def thisClass(self) -> Expression: ...

class CaseAssertionExpr(AssertionExpr):
    class ItemGroup(metaclass=_metaclass):
        @property
        def body(self) -> AssertionExpr: ...
        @property
        def expressions(self) -> list[Any]: ...

    @property
    def defaultCase(self) -> AssertionExpr: ...
    @property
    def expr(self) -> Any: ...
    @property
    def items(self) -> list[Any]: ...

class CaseGenerateSyntax(MemberSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    endCase: Token
    items: Any
    keyword: Token
    openParen: Token

class CaseItemSyntax(SyntaxNode):
    pass

class CasePropertyExprSyntax(PropertyExprSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: Any
    openParen: Token

class CaseStatement(Statement):
    class ItemGroup(metaclass=_metaclass):
        @property
        def expressions(self) -> list[Expression]: ...
        @property
        def stmt(self) -> Statement: ...

    @property
    def check(self) -> UniquePriorityCheck: ...
    @property
    def condition(self) -> CaseStatementCondition: ...
    @property
    def defaultCase(self) -> Statement: ...
    @property
    def expr(self) -> Expression: ...
    @property
    def items(self) -> list[Any]: ...

class CaseStatementCondition(metaclass=_metaclass):
    Inside: ClassVar[CaseStatementCondition]
    """Value = 3"""
    Normal: ClassVar[CaseStatementCondition]
    """Value = 0"""
    WildcardJustZ: ClassVar[CaseStatementCondition]
    """Value = 2"""
    WildcardXOrZ: ClassVar[CaseStatementCondition]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class CaseStatementSyntax(StatementSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: Any
    matchesOrInside: Token
    openParen: Token
    uniqueOrPriority: Token

class CastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    left: ExpressionSyntax
    right: ParenthesizedExpressionSyntax

class CellConfigRuleSyntax(ConfigRuleSyntax):
    cell: Token
    name: ConfigCellIdentifierSyntax
    ruleClause: ConfigRuleClauseSyntax
    semi: Token

class ChargeStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token

class CheckerDataDeclarationSyntax(MemberSyntax):
    data: DataDeclarationSyntax
    rand: Token

class CheckerDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    members: Any
    name: Token
    portList: AssertionItemPortListSyntax
    semi: Token

class CheckerInstanceBodySymbol(Symbol, Scope):
    @property
    def checker(self) -> Any: ...
    @property
    def parentInstance(self) -> CheckerInstanceSymbol: ...

class CheckerInstanceStatementSyntax(StatementSyntax):
    instance: CheckerInstantiationSyntax

class CheckerInstanceSymbol(InstanceSymbolBase):
    class Connection(metaclass=_metaclass):
        @property
        def actual(self) -> Expression | AssertionExpr | TimingControl: ...
        @property
        def attributes(self) -> list[AttributeSymbol]: ...
        @property
        def formal(self) -> Symbol: ...
        @property
        def outputInitialExpr(self) -> Expression: ...

    @property
    def body(self) -> Any: ...
    @property
    def portConnections(self) -> list[Any]: ...

class CheckerInstantiationSyntax(MemberSyntax):
    instances: Any
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: NameSyntax

class CheckerSymbol(Symbol, Scope):
    @property
    def ports(self) -> list[AssertionPortSymbol]: ...

class ClassDeclarationSyntax(MemberSyntax):
    classKeyword: Token
    endBlockName: NamedBlockClauseSyntax
    endClass: Token
    extendsClause: ExtendsClauseSyntax
    finalSpecifier: ClassSpecifierSyntax
    implementsClause: ImplementsClauseSyntax
    items: Any
    name: Token
    parameters: ParameterPortListSyntax
    semi: Token
    virtualOrInterface: Token

class ClassMethodDeclarationSyntax(MemberSyntax):
    declaration: FunctionDeclarationSyntax
    qualifiers: Any

class ClassMethodPrototypeSyntax(MemberSyntax):
    prototype: FunctionPrototypeSyntax
    qualifiers: Any
    semi: Token

class ClassNameSyntax(NameSyntax):
    identifier: Token
    parameters: ParameterValueAssignmentSyntax

class ClassPropertyDeclarationSyntax(MemberSyntax):
    declaration: MemberSyntax
    qualifiers: Any

class ClassPropertySymbol(VariableSymbol):
    @property
    def randMode(self) -> RandMode: ...
    @property
    def visibility(self) -> Visibility: ...

class ClassSpecifierSyntax(SyntaxNode):
    colon: Token
    keyword: Token

class ClassType(Type, Scope):
    @property
    def baseClass(self) -> Type: ...
    @property
    def baseConstructorCall(self) -> Expression: ...
    @property
    def constructor(self) -> SubroutineSymbol: ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol: ...
    @property
    def genericClass(self) -> Any: ...
    @property
    def implementedInterfaces(self) -> list[Type]: ...
    @property
    def isAbstract(self) -> bool: ...
    @property
    def isFinal(self) -> bool: ...
    @property
    def isInterface(self) -> bool: ...

class ClockVarSymbol(VariableSymbol):
    @property
    def direction(self) -> ArgumentDirection: ...
    @property
    def inputSkew(self) -> ClockingSkew: ...
    @property
    def outputSkew(self) -> ClockingSkew: ...

class ClockingAssertionExpr(AssertionExpr):
    @property
    def clocking(self) -> TimingControl: ...
    @property
    def expr(self) -> AssertionExpr: ...

class ClockingBlockSymbol(Symbol, Scope):
    @property
    def defaultInputSkew(self) -> ClockingSkew: ...
    @property
    def defaultOutputSkew(self) -> ClockingSkew: ...
    @property
    def event(self) -> TimingControl: ...

class ClockingDeclarationSyntax(MemberSyntax):
    at: Token
    blockName: Token
    clocking: Token
    endBlockName: NamedBlockClauseSyntax
    endClocking: Token
    event: EventExpressionSyntax
    globalOrDefault: Token
    items: Any
    semi: Token

class ClockingDirectionSyntax(SyntaxNode):
    input: Token
    inputSkew: ClockingSkewSyntax
    output: Token
    outputSkew: ClockingSkewSyntax

class ClockingEventExpression(Expression):
    @property
    def timingControl(self) -> TimingControl: ...

class ClockingItemSyntax(MemberSyntax):
    decls: Any
    direction: ClockingDirectionSyntax
    semi: Token

class ClockingPropertyExprSyntax(PropertyExprSyntax):
    event: TimingControlSyntax
    expr: PropertyExprSyntax

class ClockingSequenceExprSyntax(SequenceExprSyntax):
    event: TimingControlSyntax
    expr: SequenceExprSyntax

class ClockingSkew(metaclass=_metaclass):
    @property
    def delay(self) -> TimingControl: ...
    @property
    def edge(self) -> EdgeKind: ...
    @property
    def hasValue(self) -> bool: ...

class ClockingSkewSyntax(SyntaxNode):
    delay: TimingControlSyntax
    edge: Token

class ColonExpressionClauseSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax

class CommandLineOptions(metaclass=_metaclass):
    expandEnvVars: bool
    ignoreDuplicates: bool
    ignoreProgramName: bool
    supportsComments: bool
    def __init__(self) -> None: ...

class Compilation(metaclass=_metaclass):
    class DefinitionLookupResult(metaclass=_metaclass):
        configRoot: Any
        configRule: Any
        definition: Any
        def __init__(self) -> None: ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, options: Any) -> None: ...
    def addDiagnostics(self, diagnostics: Any) -> None: ...
    def addSyntaxTree(self, tree: Any) -> None: ...
    def addSystemMethod(self, typeKind: Any, method: Any) -> None: ...
    def addSystemSubroutine(self, subroutine: Any) -> None: ...
    def createScriptScope(self) -> Any: ...
    def getAllDiagnostics(self) -> Any: ...
    @typing.overload
    def getAttributes(self, symbol: Any) -> list[Any]: ...
    @typing.overload
    def getAttributes(self, stmt: Any) -> list[Any]: ...
    @typing.overload
    def getAttributes(self, expr: Any) -> list[Any]: ...
    @typing.overload
    def getAttributes(self, conn: Any) -> list[Any]: ...
    def getCompilationUnit(self, syntax: Any) -> Any: ...
    def getCompilationUnits(self) -> list[Any]: ...
    def getDefinitions(self) -> list[Any]: ...
    def getGateType(self, name: str) -> Any: ...
    def getNetType(self, kind: Any) -> Any: ...
    def getPackage(self, name: str) -> Any: ...
    def getPackages(self) -> list[Any]: ...
    def getParseDiagnostics(self) -> Any: ...
    def getRoot(self) -> Any: ...
    def getSemanticDiagnostics(self) -> Any: ...
    def getSourceLibrary(self, name: str) -> Any: ...
    def getStdPackage(self) -> Any: ...
    def getSyntaxTrees(self) -> list[Any]: ...
    def getSystemMethod(self, typeKind: Any, name: str) -> Any: ...
    def getSystemSubroutine(self, name: str) -> Any: ...
    def getType(self, kind: Any) -> Any: ...
    def parseName(self, name: str) -> Any: ...
    def tryGetDefinition(self, name: str, scope: Any) -> Any: ...
    def tryParseName(self, name: str, diags: Any) -> Any: ...
    @property
    def bitType(self) -> Any: ...
    @property
    def byteType(self) -> Any: ...
    @property
    def defaultLibrary(self) -> Any: ...
    @property
    def defaultTimeScale(self) -> Any | None: ...
    @property
    def errorType(self) -> Any: ...
    @property
    def hasFatalErrors(self) -> bool: ...
    @property
    def hasIssuedErrors(self) -> bool: ...
    @property
    def intType(self) -> Any: ...
    @property
    def integerType(self) -> Any: ...
    @property
    def isElaborated(self) -> bool: ...
    @property
    def isFinalized(self) -> bool: ...
    @property
    def logicType(self) -> Any: ...
    @property
    def nullType(self) -> Any: ...
    @property
    def options(self) -> CompilationOptions: ...
    @property
    def realType(self) -> Any: ...
    @property
    def shortRealType(self) -> Any: ...
    @property
    def sourceManager(self) -> Any: ...
    @property
    def stringType(self) -> Any: ...
    @property
    def typeRefType(self) -> Any: ...
    @property
    def unboundedType(self) -> Any: ...
    @property
    def unsignedIntType(self) -> Any: ...
    @property
    def voidType(self) -> Any: ...
    @property
    def wireNetType(self) -> Any: ...

class CompilationFlags(metaclass=_metaclass):
    AllowBareValParamAssignment: ClassVar[CompilationFlags]
    """Value = 256"""
    AllowHierarchicalConst: ClassVar[CompilationFlags]
    """Value = 1"""
    AllowMergingAnsiPorts: ClassVar[CompilationFlags]
    """Value = 1024"""
    AllowRecursiveImplicitCall: ClassVar[CompilationFlags]
    """Value = 128"""
    AllowSelfDeterminedStreamConcat: ClassVar[CompilationFlags]
    """Value = 512"""
    AllowTopLevelIfacePorts: ClassVar[CompilationFlags]
    """Value = 8"""
    AllowUseBeforeDeclare: ClassVar[CompilationFlags]
    """Value = 4"""
    DisableInstanceCaching: ClassVar[CompilationFlags]
    """Value = 2048"""
    DisallowRefsToUnknownInstances: ClassVar[CompilationFlags]
    """Value = 4096"""
    IgnoreUnknownModules: ClassVar[CompilationFlags]
    """Value = 32"""
    LintMode: ClassVar[CompilationFlags]
    """Value = 16"""
    None_: ClassVar[CompilationFlags]
    """Value = 0"""
    RelaxEnumConversions: ClassVar[CompilationFlags]
    """Value = 2"""
    RelaxStringConversions: ClassVar[CompilationFlags]
    """Value = 64"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class CompilationOptions(metaclass=_metaclass):
    defaultLiblist: list[str]
    defaultTimeScale: Any | None
    errorLimit: int
    flags: CompilationFlags
    languageVersion: Any
    maxConstexprBacktrace: int
    maxConstexprDepth: int
    maxConstexprSteps: int
    maxDefParamSteps: int
    maxGenerateSteps: int
    maxInstanceArray: int
    maxInstanceDepth: int
    minTypMax: MinTypMax
    paramOverrides: list[str]
    topModules: set[str]
    typoCorrectionLimit: int
    def __init__(self) -> None: ...

class CompilationUnitSymbol(Symbol, Scope):
    @property
    def timeScale(self) -> TimeScale | None: ...

class CompilationUnitSyntax(SyntaxNode):
    endOfFile: Token
    members: Any

class ConcatenationExpression(Expression):
    @property
    def operands(self) -> list[Expression]: ...

class ConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: Any
    openBrace: Token

class ConcurrentAssertionMemberSyntax(MemberSyntax):
    statement: ConcurrentAssertionStatementSyntax

class ConcurrentAssertionStatement(Statement):
    @property
    def assertionKind(self) -> AssertionKind: ...
    @property
    def ifFalse(self) -> Statement: ...
    @property
    def ifTrue(self) -> Statement: ...
    @property
    def propertySpec(self) -> AssertionExpr: ...

class ConcurrentAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    keyword: Token
    openParen: Token
    propertyOrSequence: Token
    propertySpec: PropertySpecSyntax

class ConditionBinsSelectExpr(BinsSelectExpr):
    @property
    def intersects(self) -> list[Any]: ...
    @property
    def target(self) -> Any: ...

class ConditionalAssertionExpr(AssertionExpr):
    @property
    def condition(self) -> Any: ...
    @property
    def elseExpr(self) -> AssertionExpr: ...
    @property
    def ifExpr(self) -> AssertionExpr: ...

class ConditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: Any
    expr: ConditionalDirectiveExpressionSyntax

class ConditionalConstraint(Constraint):
    @property
    def elseBody(self) -> Constraint: ...
    @property
    def ifBody(self) -> Constraint: ...
    @property
    def predicate(self) -> Any: ...

class ConditionalConstraintSyntax(ConstraintItemSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    constraints: ConstraintItemSyntax
    elseClause: ElseConstraintClauseSyntax
    ifKeyword: Token
    openParen: Token

class ConditionalDirectiveExpressionSyntax(SyntaxNode):
    pass

class ConditionalExpression(Expression):
    class Condition(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def pattern(self) -> Pattern: ...

    @property
    def conditions(self) -> list[Any]: ...
    @property
    def left(self) -> Expression: ...
    @property
    def right(self) -> Expression: ...

class ConditionalExpressionSyntax(ExpressionSyntax):
    attributes: Any
    colon: Token
    left: ExpressionSyntax
    predicate: ConditionalPredicateSyntax
    question: Token
    right: ExpressionSyntax

class ConditionalPathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    keyword: Token
    openParen: Token
    path: PathDeclarationSyntax
    predicate: ExpressionSyntax

class ConditionalPatternSyntax(SyntaxNode):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax

class ConditionalPredicateSyntax(SyntaxNode):
    conditions: Any

class ConditionalPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElsePropertyClauseSyntax
    expr: PropertyExprSyntax
    ifKeyword: Token
    openParen: Token

class ConditionalStatement(Statement):
    class Condition(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def pattern(self) -> Pattern: ...

    @property
    def check(self) -> UniquePriorityCheck: ...
    @property
    def conditions(self) -> list[Any]: ...
    @property
    def ifFalse(self) -> Statement: ...
    @property
    def ifTrue(self) -> Statement: ...

class ConditionalStatementSyntax(StatementSyntax):
    closeParen: Token
    elseClause: ElseClauseSyntax
    ifKeyword: Token
    openParen: Token
    predicate: ConditionalPredicateSyntax
    statement: StatementSyntax
    uniqueOrPriority: Token

class ConfigBlockSymbol(Symbol, Scope):
    pass

class ConfigCellIdentifierSyntax(SyntaxNode):
    cell: Token
    dot: Token
    library: Token

class ConfigDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    config: Token
    design: Token
    endconfig: Token
    localparams: Any
    name: Token
    rules: Any
    semi1: Token
    semi2: Token
    topCells: Any

class ConfigInstanceIdentifierSyntax(SyntaxNode):
    dot: Token
    name: Token

class ConfigLiblistSyntax(ConfigRuleClauseSyntax):
    liblist: Token
    libraries: Any

class ConfigRuleClauseSyntax(SyntaxNode):
    pass

class ConfigRuleSyntax(SyntaxNode):
    pass

class ConfigUseClauseSyntax(ConfigRuleClauseSyntax):
    colon: Token
    config: Token
    name: ConfigCellIdentifierSyntax
    paramAssignments: ParameterValueAssignmentSyntax
    use: Token

class ConstantPattern(Pattern):
    @property
    def expr(self) -> Any: ...

class ConstantRange(metaclass=_metaclass):
    left: int
    right: int
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, left: int, right: int) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def containsPoint(self, arg0: int) -> bool: ...
    def getIndexedRange(self, arg0: int, arg1: bool, arg2: bool) -> ConstantRange | None: ...
    def overlaps(self, arg0: ConstantRange) -> bool: ...
    def reverse(self) -> ConstantRange: ...
    def subrange(self, arg0: ConstantRange) -> ConstantRange: ...
    def translateIndex(self, arg0: int) -> int: ...
    @property
    def isLittleEndian(self) -> bool: ...
    @property
    def lower(self) -> int: ...
    @property
    def upper(self) -> int: ...
    @property
    def width(self) -> int: ...

class ConstantValue(metaclass=_metaclass):
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, integer: SVInt) -> None: ...
    @typing.overload
    def __init__(self, str: str) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: float) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def bitstreamWidth(self) -> int: ...
    def convertToByteArray(self, size: int, isSigned: bool) -> ConstantValue: ...
    def convertToByteQueue(self, isSigned: bool) -> ConstantValue: ...
    @typing.overload
    def convertToInt(self) -> ConstantValue: ...
    @typing.overload
    def convertToInt(self, width: int, isSigned: bool, isFourState: bool) -> ConstantValue: ...
    def convertToReal(self) -> ConstantValue: ...
    def convertToShortReal(self) -> ConstantValue: ...
    def convertToStr(self) -> ConstantValue: ...
    def empty(self) -> bool: ...
    def getSlice(self, upper: int, lower: int, defaultValue: ConstantValue) -> ConstantValue: ...
    def hasUnknown(self) -> bool: ...
    def isContainer(self) -> bool: ...
    def isFalse(self) -> bool: ...
    def isTrue(self) -> bool: ...
    def size(self) -> int: ...
    @property
    def value(self) -> SVInt | float | list | dict | Null | None: ...

class Constraint(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> ConstraintKind: ...
    @property
    def syntax(self) -> Any: ...

class ConstraintBlockFlags(metaclass=_metaclass):
    ExplicitExtern: ClassVar[ConstraintBlockFlags]
    """Value = 16"""
    Extends: ClassVar[ConstraintBlockFlags]
    """Value = 64"""
    Extern: ClassVar[ConstraintBlockFlags]
    """Value = 8"""
    Final: ClassVar[ConstraintBlockFlags]
    """Value = 128"""
    Initial: ClassVar[ConstraintBlockFlags]
    """Value = 32"""
    None_: ClassVar[ConstraintBlockFlags]
    """Value = 0"""
    Pure: ClassVar[ConstraintBlockFlags]
    """Value = 2"""
    Static: ClassVar[ConstraintBlockFlags]
    """Value = 4"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ConstraintBlockSymbol(Symbol, Scope):
    @property
    def constraints(self) -> Constraint: ...
    @property
    def flags(self) -> ConstraintBlockFlags: ...
    @property
    def thisVar(self) -> VariableSymbol: ...

class ConstraintBlockSyntax(ConstraintItemSyntax):
    closeBrace: Token
    items: Any
    openBrace: Token

class ConstraintDeclarationSyntax(MemberSyntax):
    block: ConstraintBlockSyntax
    keyword: Token
    name: NameSyntax
    qualifiers: Any
    specifiers: Any

class ConstraintItemSyntax(SyntaxNode):
    pass

class ConstraintKind(metaclass=_metaclass):
    Conditional: ClassVar[ConstraintKind]
    """Value = 4"""
    DisableSoft: ClassVar[ConstraintKind]
    """Value = 6"""
    Expression: ClassVar[ConstraintKind]
    """Value = 2"""
    Foreach: ClassVar[ConstraintKind]
    """Value = 8"""
    Implication: ClassVar[ConstraintKind]
    """Value = 3"""
    Invalid: ClassVar[ConstraintKind]
    """Value = 0"""
    List: ClassVar[ConstraintKind]
    """Value = 1"""
    SolveBefore: ClassVar[ConstraintKind]
    """Value = 7"""
    Uniqueness: ClassVar[ConstraintKind]
    """Value = 5"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ConstraintList(Constraint):
    @property
    def list(self) -> list[Constraint]: ...

class ConstraintPrototypeSyntax(MemberSyntax):
    keyword: Token
    name: NameSyntax
    qualifiers: Any
    semi: Token
    specifiers: Any

class ContinueStatement(Statement):
    pass

class ContinuousAssignSymbol(Symbol):
    @property
    def assignment(self) -> Expression: ...
    @property
    def delay(self) -> TimingControl: ...
    @property
    def driveStrength(self) -> tuple[Any | None, Any | None]: ...

class ContinuousAssignSyntax(MemberSyntax):
    assign: Token
    assignments: Any
    delay: TimingControlSyntax
    semi: Token
    strength: DriveStrengthSyntax

class ConversionExpression(Expression):
    @property
    def conversionKind(self) -> ConversionKind: ...
    @property
    def isImplicit(self) -> bool: ...
    @property
    def operand(self) -> Expression: ...

class ConversionKind(metaclass=_metaclass):
    BitstreamCast: ClassVar[ConversionKind]
    """Value = 4"""
    Explicit: ClassVar[ConversionKind]
    """Value = 3"""
    Implicit: ClassVar[ConversionKind]
    """Value = 0"""
    Propagated: ClassVar[ConversionKind]
    """Value = 1"""
    StreamingConcat: ClassVar[ConversionKind]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class CopyClassExpression(Expression):
    @property
    def sourceExpr(self) -> Expression: ...

class CopyClassExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    scopedNew: NameSyntax

class CoverCrossBodySymbol(Symbol, Scope):
    @property
    def crossQueueType(self) -> Any: ...

class CoverCrossSymbol(Symbol, Scope):
    @property
    def iffExpr(self) -> Expression: ...
    @property
    def options(self) -> list[CoverageOptionSetter]: ...
    @property
    def targets(self) -> list[CoverpointSymbol]: ...

class CoverCrossSyntax(MemberSyntax):
    closeBrace: Token
    cross: Token
    emptySemi: Token
    iff: CoverageIffClauseSyntax
    items: Any
    label: NamedLabelSyntax
    members: Any
    openBrace: Token

class CoverageBinInitializerSyntax(SyntaxNode):
    pass

class CoverageBinSymbol(Symbol):
    class BinKind(metaclass=_metaclass):
        Bins: ClassVar[Self]
        """Value = 0"""
        IgnoreBins: ClassVar[Self]
        """Value = 2"""
        IllegalBins: ClassVar[Self]
        """Value = 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    class TransRangeList(metaclass=_metaclass):
        class RepeatKind(metaclass=_metaclass):
            Consecutive = 1
            GoTo = 3
            Nonconsecutive = 2
            None_ = 0

            __members__: dict[str, Self]

            def __int__(self) -> int: ...
            def __index__(self, index: int) -> Self: ...
            @property
            def name(self) -> str: ...
            @property
            def value(self) -> int: ...

        Consecutive: Final = RepeatKind.Consecutive
        GoTo: Final = RepeatKind.GoTo
        Nonconsecutive: Final = RepeatKind.Nonconsecutive
        None_: Final = RepeatKind.None_

        @property
        def items(self) -> list[Expression]: ...
        @property
        def repeatFrom(self) -> Expression: ...
        @property
        def repeatKind(self) -> Any: ...
        @property
        def repeatTo(self) -> Expression: ...

    Bins: Final = BinKind.Bins
    IgnoreBins: Final = BinKind.IgnoreBins
    IllegalBins: Final = BinKind.IllegalBins

    @property
    def binsKind(self) -> Any: ...
    @property
    def crossSelectExpr(self) -> BinsSelectExpr: ...
    @property
    def iffExpr(self) -> Expression: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isDefault(self) -> bool: ...
    @property
    def isDefaultSequence(self) -> bool: ...
    @property
    def isWildcard(self) -> bool: ...
    @property
    def numberOfBinsExpr(self) -> Expression: ...
    @property
    def setCoverageExpr(self) -> Expression: ...
    @property
    def values(self) -> list[Expression]: ...
    @property
    def withExpr(self) -> Expression: ...

class CoverageBinsArraySizeSyntax(SyntaxNode):
    closeBracket: Token
    expr: ExpressionSyntax
    openBracket: Token

class CoverageBinsSyntax(MemberSyntax):
    equals: Token
    iff: CoverageIffClauseSyntax
    initializer: CoverageBinInitializerSyntax
    keyword: Token
    name: Token
    semi: Token
    size: CoverageBinsArraySizeSyntax
    wildcard: Token

class CoverageIffClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token

class CoverageOptionSetter(metaclass=_metaclass):
    @property
    def expression(self) -> Expression: ...
    @property
    def isTypeOption(self) -> bool: ...
    @property
    def name(self) -> str: ...

class CoverageOptionSyntax(MemberSyntax):
    expr: ExpressionSyntax
    semi: Token

class CovergroupBodySymbol(Symbol, Scope):
    @property
    def options(self) -> list[CoverageOptionSetter]: ...

class CovergroupDeclarationSyntax(MemberSyntax):
    covergroup: Token
    endBlockName: NamedBlockClauseSyntax
    endgroup: Token
    event: SyntaxNode
    extends: Token
    members: Any
    name: Token
    portList: FunctionPortListSyntax
    semi: Token

class CovergroupType(Type, Scope):
    @property
    def arguments(self) -> list[FormalArgumentSymbol]: ...
    @property
    def baseGroup(self) -> Type: ...
    @property
    def body(self) -> CovergroupBodySymbol: ...
    @property
    def coverageEvent(self) -> TimingControl: ...

class CoverpointSymbol(Symbol, Scope):
    @property
    def coverageExpr(self) -> Expression: ...
    @property
    def iffExpr(self) -> Expression: ...
    @property
    def options(self) -> list[CoverageOptionSetter]: ...
    @property
    def type(self) -> Any: ...

class CoverpointSyntax(MemberSyntax):
    closeBrace: Token
    coverpoint: Token
    emptySemi: Token
    expr: ExpressionSyntax
    iff: CoverageIffClauseSyntax
    label: NamedLabelSyntax
    members: Any
    openBrace: Token
    type: DataTypeSyntax

class CrossIdBinsSelectExpr(BinsSelectExpr):
    pass

class CycleDelayControl(TimingControl):
    @property
    def expr(self) -> Any: ...

class DPIExportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    functionOrTask: Token
    keyword: Token
    name: Token
    semi: Token
    specString: Token

class DPIImportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    keyword: Token
    method: FunctionPrototypeSyntax
    property: Token
    semi: Token
    specString: Token

class DPIOpenArrayType(Type):
    @property
    def elementType(self) -> Type: ...
    @property
    def isPacked(self) -> bool: ...

class DataDeclarationSyntax(MemberSyntax):
    declarators: Any
    modifiers: Any
    semi: Token
    type: DataTypeSyntax

class DataTypeExpression(Expression):
    pass

class DataTypeSyntax(ExpressionSyntax):
    pass

class DeclaratorSyntax(SyntaxNode):
    dimensions: Any
    initializer: EqualsValueClauseSyntax
    name: Token

class DeclaredType(metaclass=_metaclass):
    @property
    def initializer(self) -> Expression: ...
    @property
    def initializerLocation(self) -> SourceLocation: ...
    @property
    def initializerSyntax(self) -> ExpressionSyntax: ...
    @property
    def isEvaluating(self) -> bool: ...
    @property
    def type(self) -> Type: ...
    @property
    def typeSyntax(self) -> DataTypeSyntax: ...

class DefParamAssignmentSyntax(SyntaxNode):
    name: NameSyntax
    setter: EqualsValueClauseSyntax

class DefParamSymbol(Symbol):
    @property
    def initializer(self) -> Expression: ...
    @property
    def target(self) -> Symbol: ...
    @property
    def value(self) -> ConstantValue: ...

class DefParamSyntax(MemberSyntax):
    assignments: Any
    defparam: Token
    semi: Token

class DefaultCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    defaultKeyword: Token

class DefaultClockingReferenceSyntax(MemberSyntax):
    clocking: Token
    defaultKeyword: Token
    name: Token
    semi: Token

class DefaultConfigRuleSyntax(ConfigRuleSyntax):
    defaultKeyword: Token
    liblist: ConfigLiblistSyntax
    semi: Token

class DefaultCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    defaultKeyword: Token
    sequenceKeyword: Token

class DefaultDecayTimeDirectiveSyntax(DirectiveSyntax):
    time: Token

class DefaultDisableDeclarationSyntax(MemberSyntax):
    defaultKeyword: Token
    disableKeyword: Token
    expr: ExpressionSyntax
    iffKeyword: Token
    semi: Token

class DefaultDistItemSyntax(DistItemBaseSyntax):
    defaultKeyword: Token
    weight: DistWeightSyntax

class DefaultExtendsClauseArgSyntax(SyntaxNode):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token

class DefaultFunctionPortSyntax(FunctionPortBaseSyntax):
    keyword: Token

class DefaultNetTypeDirectiveSyntax(DirectiveSyntax):
    netType: Token

class DefaultPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    expr: PropertyExprSyntax
    semi: Token

class DefaultRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    item: RsProdItemSyntax
    semi: Token

class DefaultSkewItemSyntax(MemberSyntax):
    direction: ClockingDirectionSyntax
    keyword: Token
    semi: Token

class DefaultTriregStrengthDirectiveSyntax(DirectiveSyntax):
    strength: Token

class DeferredAssertionSyntax(SyntaxNode):
    finalKeyword: Token
    hash: Token
    zero: Token

class DefineDirectiveSyntax(DirectiveSyntax):
    body: Any
    formalArguments: MacroFormalArgumentListSyntax
    name: Token

class DefinitionKind(metaclass=_metaclass):
    Interface: ClassVar[DefinitionKind]
    """Value = 1"""
    Module: ClassVar[DefinitionKind]
    """Value = 0"""
    Program: ClassVar[DefinitionKind]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DefinitionSymbol(Symbol):
    def __repr__(self) -> str: ...
    def getArticleKindString(self) -> str: ...
    def getKindString(self) -> str: ...
    @property
    def cellDefine(self) -> bool: ...
    @property
    def defaultLifetime(self) -> VariableLifetime: ...
    @property
    def defaultNetType(self) -> Any: ...
    @property
    def definitionKind(self) -> DefinitionKind: ...
    @property
    def instanceCount(self) -> int: ...
    @property
    def timeScale(self) -> TimeScale | None: ...
    @property
    def unconnectedDrive(self) -> UnconnectedDrive: ...

class Delay3Control(TimingControl):
    @property
    def expr1(self) -> Any: ...
    @property
    def expr2(self) -> Any: ...
    @property
    def expr3(self) -> Any: ...

class Delay3Syntax(TimingControlSyntax):
    closeParen: Token
    comma1: Token
    comma2: Token
    delay1: ExpressionSyntax
    delay2: ExpressionSyntax
    delay3: ExpressionSyntax
    hash: Token
    openParen: Token

class DelayControl(TimingControl):
    @property
    def expr(self) -> Any: ...

class DelaySyntax(TimingControlSyntax):
    delayValue: ExpressionSyntax
    hash: Token

class DelayedSequenceElementSyntax(SyntaxNode):
    closeBracket: Token
    delayVal: ExpressionSyntax
    doubleHash: Token
    expr: SequenceExprSyntax
    op: Token
    openBracket: Token
    range: SelectorSyntax

class DelayedSequenceExprSyntax(SequenceExprSyntax):
    elements: Any
    first: SequenceExprSyntax

class DiagCode(metaclass=_metaclass):
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, subsystem: DiagSubsystem, code: int) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def getCode(self) -> int: ...
    def getSubsystem(self) -> DiagSubsystem: ...

class DiagGroup(metaclass=_metaclass):
    def __init__(self, name: str, diags: list[DiagCode]) -> None: ...
    def __repr__(self) -> str: ...
    def getDiags(self) -> list[DiagCode]: ...
    def getName(self) -> str: ...

class DiagSubsystem(metaclass=_metaclass):
    Analysis: ClassVar[DiagSubsystem]
    """Value = 14"""
    Compilation: ClassVar[DiagSubsystem]
    """Value = 13"""
    ConstEval: ClassVar[DiagSubsystem]
    """Value = 12"""
    Declarations: ClassVar[DiagSubsystem]
    """Value = 6"""
    Expressions: ClassVar[DiagSubsystem]
    """Value = 7"""
    General: ClassVar[DiagSubsystem]
    """Value = 1"""
    Invalid: ClassVar[DiagSubsystem]
    """Value = 0"""
    Lexer: ClassVar[DiagSubsystem]
    """Value = 2"""
    Lookup: ClassVar[DiagSubsystem]
    """Value = 10"""
    Meta: ClassVar[DiagSubsystem]
    """Value = 15"""
    Netlist: ClassVar[DiagSubsystem]
    """Value = 17"""
    Numeric: ClassVar[DiagSubsystem]
    """Value = 3"""
    Parser: ClassVar[DiagSubsystem]
    """Value = 5"""
    Preprocessor: ClassVar[DiagSubsystem]
    """Value = 4"""
    Statements: ClassVar[DiagSubsystem]
    """Value = 8"""
    SysFuncs: ClassVar[DiagSubsystem]
    """Value = 11"""
    Tidy: ClassVar[DiagSubsystem]
    """Value = 16"""
    Types: ClassVar[DiagSubsystem]
    """Value = 9"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Diagnostic(metaclass=_metaclass):
    def __eq__(self, arg0: object) -> bool: ...
    def __init__(self, code: DiagCode, location: SourceLocation) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def isError(self) -> bool: ...
    @property
    def args(self) -> list[str | int | int | str | ConstantValue | tuple[Any, Any]]: ...
    @property
    def code(self) -> DiagCode: ...
    @property
    def location(self) -> SourceLocation: ...
    @property
    def ranges(self) -> list[SourceRange]: ...
    @property
    def symbol(self) -> Any: ...

class DiagnosticClient(metaclass=_metaclass):
    def report(self, diagnostic: ReportedDiagnostic) -> None: ...
    def setEngine(self, engine: DiagnosticEngine) -> None: ...
    def showAbsPaths(self, show: bool) -> None: ...

class DiagnosticEngine(metaclass=_metaclass):
    @staticmethod
    def reportAll(sourceManager: SourceManager, diag: list[Diagnostic]) -> str: ...
    def __init__(self, sourceManager: SourceManager) -> None: ...
    def addClient(self, client: Any) -> None: ...
    def clearClients(self) -> None: ...
    def clearCounts(self) -> None: ...
    @typing.overload
    def clearMappings(self) -> None: ...
    @typing.overload
    def clearMappings(self, severity: DiagnosticSeverity) -> None: ...
    def findDiagGroup(self, name: str) -> DiagGroup: ...
    def findFromOptionName(self, optionName: str) -> list[DiagCode]: ...
    def formatMessage(self, diag: Diagnostic) -> str: ...
    def getMessage(self, code: DiagCode) -> str: ...
    def getOptionName(self, code: DiagCode) -> str: ...
    def getSeverity(self, code: DiagCode, location: SourceLocation) -> DiagnosticSeverity: ...
    def issue(self, diagnostic: Diagnostic) -> None: ...
    def setErrorLimit(self, limit: int) -> None: ...
    def setErrorsAsFatal(self, set: bool) -> None: ...
    def setFatalsAsErrors(self, set: bool) -> None: ...
    def setIgnoreAllNotes(self, set: bool) -> None: ...
    def setIgnoreAllWarnings(self, set: bool) -> None: ...
    @typing.overload
    def setMappingsFromPragmas(self) -> Diagnostics: ...
    @typing.overload
    def setMappingsFromPragmas(self, buffer: BufferID) -> Diagnostics: ...
    def setMessage(self, code: DiagCode, message: str) -> None: ...
    def setSeverity(self, code: DiagCode, severity: DiagnosticSeverity) -> None: ...
    def setWarningOptions(self, options: list[str]) -> Diagnostics: ...
    def setWarningsAsErrors(self, set: bool) -> None: ...
    @property
    def numErrors(self) -> int: ...
    @property
    def numWarnings(self) -> int: ...
    @property
    def sourceManager(self) -> SourceManager: ...

class DiagnosticSeverity(metaclass=_metaclass):
    Error: ClassVar[DiagnosticSeverity]
    """Value = 3"""
    Fatal: ClassVar[DiagnosticSeverity]
    """Value = 4"""
    Ignored: ClassVar[DiagnosticSeverity]
    """Value = 0"""
    Note: ClassVar[DiagnosticSeverity]
    """Value = 1"""
    Warning: ClassVar[DiagnosticSeverity]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Diagnostics(metaclass=_metaclass):
    def __getitem__(self, arg0: int) -> Diagnostic: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[Diagnostic]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def add(self, code: DiagCode, location: SourceLocation) -> Diagnostic: ...
    @typing.overload
    def add(self, code: DiagCode, range: SourceRange) -> Diagnostic: ...
    @typing.overload
    def add(self, source: Any, code: DiagCode, location: SourceLocation) -> Diagnostic: ...
    @typing.overload
    def add(self, source: Any, code: DiagCode, range: SourceRange) -> Diagnostic: ...
    def sort(self, sourceManager: SourceManager) -> None: ...

class Diags(metaclass=_metaclass):
    AlwaysFFEventControl: typing.ClassVar[DiagCode]
    AlwaysInChecker: typing.ClassVar[DiagCode]
    AlwaysWithoutTimingControl: typing.ClassVar[DiagCode]
    AmbiguousWildcardImport: typing.ClassVar[DiagCode]
    AnsiIfacePortDefault: typing.ClassVar[DiagCode]
    ArgCannotBeEmpty: typing.ClassVar[DiagCode]
    ArgDoesNotExist: typing.ClassVar[DiagCode]
    ArithInShift: typing.ClassVar[DiagCode]
    ArithOpMismatch: typing.ClassVar[DiagCode]
    ArrayDimTooLarge: typing.ClassVar[DiagCode]
    ArrayLocatorWithClause: typing.ClassVar[DiagCode]
    ArrayMethodComparable: typing.ClassVar[DiagCode]
    ArrayMethodIntegral: typing.ClassVar[DiagCode]
    AssertionArgNeedsRegExpr: typing.ClassVar[DiagCode]
    AssertionArgTypeMismatch: typing.ClassVar[DiagCode]
    AssertionArgTypeSequence: typing.ClassVar[DiagCode]
    AssertionDelayFormalType: typing.ClassVar[DiagCode]
    AssertionExprType: typing.ClassVar[DiagCode]
    AssertionFuncArg: typing.ClassVar[DiagCode]
    AssertionNoClock: typing.ClassVar[DiagCode]
    AssertionOutputLocalVar: typing.ClassVar[DiagCode]
    AssertionPortDirNoLocal: typing.ClassVar[DiagCode]
    AssertionPortOutputDefault: typing.ClassVar[DiagCode]
    AssertionPortPropOutput: typing.ClassVar[DiagCode]
    AssertionPortRef: typing.ClassVar[DiagCode]
    AssertionPortTypedLValue: typing.ClassVar[DiagCode]
    AssignToCHandle: typing.ClassVar[DiagCode]
    AssignToNet: typing.ClassVar[DiagCode]
    AssignedToLocalBodyParam: typing.ClassVar[DiagCode]
    AssignedToLocalPortParam: typing.ClassVar[DiagCode]
    AssignmentNotAllowed: typing.ClassVar[DiagCode]
    AssignmentPatternAssociativeType: typing.ClassVar[DiagCode]
    AssignmentPatternDynamicDefault: typing.ClassVar[DiagCode]
    AssignmentPatternDynamicType: typing.ClassVar[DiagCode]
    AssignmentPatternKeyDupDefault: typing.ClassVar[DiagCode]
    AssignmentPatternKeyDupName: typing.ClassVar[DiagCode]
    AssignmentPatternKeyDupValue: typing.ClassVar[DiagCode]
    AssignmentPatternKeyExpr: typing.ClassVar[DiagCode]
    AssignmentPatternLValueDynamic: typing.ClassVar[DiagCode]
    AssignmentPatternMissingElements: typing.ClassVar[DiagCode]
    AssignmentPatternNoContext: typing.ClassVar[DiagCode]
    AssignmentPatternNoMember: typing.ClassVar[DiagCode]
    AssignmentRequiresParens: typing.ClassVar[DiagCode]
    AssignmentToConstVar: typing.ClassVar[DiagCode]
    AssociativeWildcardNotAllowed: typing.ClassVar[DiagCode]
    AttributesNotAllowed: typing.ClassVar[DiagCode]
    AutoFromNonBlockingTiming: typing.ClassVar[DiagCode]
    AutoFromNonProcedural: typing.ClassVar[DiagCode]
    AutoFromStaticInit: typing.ClassVar[DiagCode]
    AutoVarToRefStatic: typing.ClassVar[DiagCode]
    AutoVarTraced: typing.ClassVar[DiagCode]
    AutoVariableHierarchical: typing.ClassVar[DiagCode]
    AutomaticNotAllowed: typing.ClassVar[DiagCode]
    BadAssignment: typing.ClassVar[DiagCode]
    BadAssignmentPatternType: typing.ClassVar[DiagCode]
    BadBinaryDigit: typing.ClassVar[DiagCode]
    BadBinaryExpression: typing.ClassVar[DiagCode]
    BadCastType: typing.ClassVar[DiagCode]
    BadConcatExpression: typing.ClassVar[DiagCode]
    BadConditionalExpression: typing.ClassVar[DiagCode]
    BadConversion: typing.ClassVar[DiagCode]
    BadDecimalDigit: typing.ClassVar[DiagCode]
    BadDisableSoft: typing.ClassVar[DiagCode]
    BadFinishNum: typing.ClassVar[DiagCode]
    BadForceNetType: typing.ClassVar[DiagCode]
    BadHexDigit: typing.ClassVar[DiagCode]
    BadIndexExpression: typing.ClassVar[DiagCode]
    BadInstanceArrayRange: typing.ClassVar[DiagCode]
    BadIntegerCast: typing.ClassVar[DiagCode]
    BadOctalDigit: typing.ClassVar[DiagCode]
    BadProceduralAssign: typing.ClassVar[DiagCode]
    BadProceduralForce: typing.ClassVar[DiagCode]
    BadReplicationExpression: typing.ClassVar[DiagCode]
    BadSetMembershipType: typing.ClassVar[DiagCode]
    BadSliceType: typing.ClassVar[DiagCode]
    BadSolveBefore: typing.ClassVar[DiagCode]
    BadStreamCast: typing.ClassVar[DiagCode]
    BadStreamContext: typing.ClassVar[DiagCode]
    BadStreamExprType: typing.ClassVar[DiagCode]
    BadStreamSize: typing.ClassVar[DiagCode]
    BadStreamSlice: typing.ClassVar[DiagCode]
    BadStreamSourceType: typing.ClassVar[DiagCode]
    BadStreamTargetType: typing.ClassVar[DiagCode]
    BadStreamWithOrder: typing.ClassVar[DiagCode]
    BadStreamWithType: typing.ClassVar[DiagCode]
    BadSystemSubroutineArg: typing.ClassVar[DiagCode]
    BadTypeParamExpr: typing.ClassVar[DiagCode]
    BadUnaryExpression: typing.ClassVar[DiagCode]
    BadUniquenessType: typing.ClassVar[DiagCode]
    BadValueRange: typing.ClassVar[DiagCode]
    BaseConstructorDuplicate: typing.ClassVar[DiagCode]
    BaseConstructorNotCalled: typing.ClassVar[DiagCode]
    BiDiSwitchNetTypes: typing.ClassVar[DiagCode]
    BindDirectiveInvalidName: typing.ClassVar[DiagCode]
    BindTargetPrimitive: typing.ClassVar[DiagCode]
    BindTypeParamMismatch: typing.ClassVar[DiagCode]
    BindTypeParamNotFound: typing.ClassVar[DiagCode]
    BindUnderBind: typing.ClassVar[DiagCode]
    BitwiseOpMismatch: typing.ClassVar[DiagCode]
    BitwiseOpParentheses: typing.ClassVar[DiagCode]
    BitwiseRelPrecedence: typing.ClassVar[DiagCode]
    BlockingAssignToFreeVar: typing.ClassVar[DiagCode]
    BlockingInAlwaysFF: typing.ClassVar[DiagCode]
    BodyForPure: typing.ClassVar[DiagCode]
    BodyForPureConstraint: typing.ClassVar[DiagCode]
    BodyParamNoInitializer: typing.ClassVar[DiagCode]
    CHandleInAssertion: typing.ClassVar[DiagCode]
    CannotCompareTwoInstances: typing.ClassVar[DiagCode]
    CannotDeclareType: typing.ClassVar[DiagCode]
    CannotIndexScalar: typing.ClassVar[DiagCode]
    CantDeclarePortSigned: typing.ClassVar[DiagCode]
    CantModifyConst: typing.ClassVar[DiagCode]
    CaseComplex: typing.ClassVar[DiagCode]
    CaseDefault: typing.ClassVar[DiagCode]
    CaseDup: typing.ClassVar[DiagCode]
    CaseEnum: typing.ClassVar[DiagCode]
    CaseEnumExplicit: typing.ClassVar[DiagCode]
    CaseGenerateDup: typing.ClassVar[DiagCode]
    CaseGenerateEmpty: typing.ClassVar[DiagCode]
    CaseGenerateNoBlock: typing.ClassVar[DiagCode]
    CaseIncomplete: typing.ClassVar[DiagCode]
    CaseInsideKeyword: typing.ClassVar[DiagCode]
    CaseNotWildcard: typing.ClassVar[DiagCode]
    CaseOutsideRange: typing.ClassVar[DiagCode]
    CaseOverlap: typing.ClassVar[DiagCode]
    CaseRedundantDefault: typing.ClassVar[DiagCode]
    CaseStatementEmpty: typing.ClassVar[DiagCode]
    CaseTypeMismatch: typing.ClassVar[DiagCode]
    CaseUnreachable: typing.ClassVar[DiagCode]
    CaseWildcard2State: typing.ClassVar[DiagCode]
    CaseZWithX: typing.ClassVar[DiagCode]
    ChainedMethodParens: typing.ClassVar[DiagCode]
    ChargeWithTriReg: typing.ClassVar[DiagCode]
    CheckerArgCannotBeEmpty: typing.ClassVar[DiagCode]
    CheckerBlockingAssign: typing.ClassVar[DiagCode]
    CheckerClassBadInstantiation: typing.ClassVar[DiagCode]
    CheckerForkJoinRef: typing.ClassVar[DiagCode]
    CheckerFuncArg: typing.ClassVar[DiagCode]
    CheckerFuncBadInstantiation: typing.ClassVar[DiagCode]
    CheckerHierarchical: typing.ClassVar[DiagCode]
    CheckerInCheckerProc: typing.ClassVar[DiagCode]
    CheckerInForkJoin: typing.ClassVar[DiagCode]
    CheckerNotInProc: typing.ClassVar[DiagCode]
    CheckerOutputBadType: typing.ClassVar[DiagCode]
    CheckerParameterAssign: typing.ClassVar[DiagCode]
    CheckerPortDirectionType: typing.ClassVar[DiagCode]
    CheckerPortInout: typing.ClassVar[DiagCode]
    CheckerTimingControl: typing.ClassVar[DiagCode]
    ClassInheritanceCycle: typing.ClassVar[DiagCode]
    ClassMemberInAssertion: typing.ClassVar[DiagCode]
    ClassPrivateMembersBitstream: typing.ClassVar[DiagCode]
    ClassSpecifierConflict: typing.ClassVar[DiagCode]
    ClockVarAssignConcat: typing.ClassVar[DiagCode]
    ClockVarBadTiming: typing.ClassVar[DiagCode]
    ClockVarOutputRead: typing.ClassVar[DiagCode]
    ClockVarSyncDrive: typing.ClassVar[DiagCode]
    ClockVarTargetAssign: typing.ClassVar[DiagCode]
    ClockingBlockEventEdge: typing.ClassVar[DiagCode]
    ClockingBlockEventIff: typing.ClassVar[DiagCode]
    ClockingNameEmpty: typing.ClassVar[DiagCode]
    ComparisonMismatch: typing.ClassVar[DiagCode]
    CompilationUnitFromPackage: typing.ClassVar[DiagCode]
    ConcatWithStringInt: typing.ClassVar[DiagCode]
    ConcurrentAssertActionBlock: typing.ClassVar[DiagCode]
    ConcurrentAssertNotInProc: typing.ClassVar[DiagCode]
    ConditionalPrecedence: typing.ClassVar[DiagCode]
    ConfigDupTop: typing.ClassVar[DiagCode]
    ConfigInstanceUnderOtherConfig: typing.ClassVar[DiagCode]
    ConfigInstanceWrongTop: typing.ClassVar[DiagCode]
    ConfigMissingName: typing.ClassVar[DiagCode]
    ConfigOverrideTop: typing.ClassVar[DiagCode]
    ConfigParamLiteral: typing.ClassVar[DiagCode]
    ConfigParamsForPrimitive: typing.ClassVar[DiagCode]
    ConfigParamsIgnored: typing.ClassVar[DiagCode]
    ConfigParamsOrdered: typing.ClassVar[DiagCode]
    ConfigSpecificCellLiblist: typing.ClassVar[DiagCode]
    ConsecutiveComparison: typing.ClassVar[DiagCode]
    ConstEvalAssertionFailed: typing.ClassVar[DiagCode]
    ConstEvalAssociativeElementNotFound: typing.ClassVar[DiagCode]
    ConstEvalAssociativeIndexInvalid: typing.ClassVar[DiagCode]
    ConstEvalBitstreamCastSize: typing.ClassVar[DiagCode]
    ConstEvalCaseItemsNotUnique: typing.ClassVar[DiagCode]
    ConstEvalCheckers: typing.ClassVar[DiagCode]
    ConstEvalClassType: typing.ClassVar[DiagCode]
    ConstEvalCovergroupType: typing.ClassVar[DiagCode]
    ConstEvalDPINotConstant: typing.ClassVar[DiagCode]
    ConstEvalDisableTarget: typing.ClassVar[DiagCode]
    ConstEvalDynamicArrayIndex: typing.ClassVar[DiagCode]
    ConstEvalDynamicArrayRange: typing.ClassVar[DiagCode]
    ConstEvalDynamicToFixedSize: typing.ClassVar[DiagCode]
    ConstEvalEmptyQueue: typing.ClassVar[DiagCode]
    ConstEvalExceededMaxCallDepth: typing.ClassVar[DiagCode]
    ConstEvalExceededMaxSteps: typing.ClassVar[DiagCode]
    ConstEvalFunctionArgDirection: typing.ClassVar[DiagCode]
    ConstEvalFunctionIdentifiersMustBeLocal: typing.ClassVar[DiagCode]
    ConstEvalFunctionInsideGenerate: typing.ClassVar[DiagCode]
    ConstEvalHierarchicalName: typing.ClassVar[DiagCode]
    ConstEvalIdUsedInCEBeforeDecl: typing.ClassVar[DiagCode]
    ConstEvalIfItemsNotUnique: typing.ClassVar[DiagCode]
    ConstEvalMethodNotConstant: typing.ClassVar[DiagCode]
    ConstEvalNoCaseItemsMatched: typing.ClassVar[DiagCode]
    ConstEvalNoIfItemsMatched: typing.ClassVar[DiagCode]
    ConstEvalNonConstVariable: typing.ClassVar[DiagCode]
    ConstEvalParallelBlockNotConst: typing.ClassVar[DiagCode]
    ConstEvalParamCycle: typing.ClassVar[DiagCode]
    ConstEvalProceduralAssign: typing.ClassVar[DiagCode]
    ConstEvalQueueRange: typing.ClassVar[DiagCode]
    ConstEvalRandValue: typing.ClassVar[DiagCode]
    ConstEvalReplicationCountInvalid: typing.ClassVar[DiagCode]
    ConstEvalStaticSkipped: typing.ClassVar[DiagCode]
    ConstEvalSubroutineNotConstant: typing.ClassVar[DiagCode]
    ConstEvalTaggedUnion: typing.ClassVar[DiagCode]
    ConstEvalTaskNotConstant: typing.ClassVar[DiagCode]
    ConstEvalTimedStmtNotConst: typing.ClassVar[DiagCode]
    ConstEvalVoidNotConstant: typing.ClassVar[DiagCode]
    ConstFunctionPortRequiresRef: typing.ClassVar[DiagCode]
    ConstPortNotAllowed: typing.ClassVar[DiagCode]
    ConstSysTaskIgnored: typing.ClassVar[DiagCode]
    ConstVarNoInitializer: typing.ClassVar[DiagCode]
    ConstVarToRef: typing.ClassVar[DiagCode]
    ConstantConversion: typing.ClassVar[DiagCode]
    ConstraintNotInClass: typing.ClassVar[DiagCode]
    ConstraintQualOutOfBlock: typing.ClassVar[DiagCode]
    ConstructorOutsideClass: typing.ClassVar[DiagCode]
    ConstructorReturnType: typing.ClassVar[DiagCode]
    CopyClassTarget: typing.ClassVar[DiagCode]
    CouldNotOpenIncludeFile: typing.ClassVar[DiagCode]
    CouldNotResolveHierarchicalPath: typing.ClassVar[DiagCode]
    CoverCrossItems: typing.ClassVar[DiagCode]
    CoverOptionImmutable: typing.ClassVar[DiagCode]
    CoverStmtNoFail: typing.ClassVar[DiagCode]
    CoverageBinDefSeqSize: typing.ClassVar[DiagCode]
    CoverageBinDefaultIgnore: typing.ClassVar[DiagCode]
    CoverageBinDefaultWildcard: typing.ClassVar[DiagCode]
    CoverageBinTargetName: typing.ClassVar[DiagCode]
    CoverageBinTransSize: typing.ClassVar[DiagCode]
    CoverageExprVar: typing.ClassVar[DiagCode]
    CoverageOptionDup: typing.ClassVar[DiagCode]
    CoverageSampleFormal: typing.ClassVar[DiagCode]
    CoverageSetType: typing.ClassVar[DiagCode]
    CovergroupOutArg: typing.ClassVar[DiagCode]
    CycleDelayNonClock: typing.ClassVar[DiagCode]
    DPIExportDifferentScope: typing.ClassVar[DiagCode]
    DPIExportDuplicate: typing.ClassVar[DiagCode]
    DPIExportDuplicateCId: typing.ClassVar[DiagCode]
    DPIExportImportedFunc: typing.ClassVar[DiagCode]
    DPIExportKindMismatch: typing.ClassVar[DiagCode]
    DPIPureArg: typing.ClassVar[DiagCode]
    DPIPureReturn: typing.ClassVar[DiagCode]
    DPIPureTask: typing.ClassVar[DiagCode]
    DPIRefArg: typing.ClassVar[DiagCode]
    DPISignatureMismatch: typing.ClassVar[DiagCode]
    DPISpecDisallowed: typing.ClassVar[DiagCode]
    DecimalDigitMultipleUnknown: typing.ClassVar[DiagCode]
    DeclModifierConflict: typing.ClassVar[DiagCode]
    DeclModifierOrdering: typing.ClassVar[DiagCode]
    DeclarationsAtStart: typing.ClassVar[DiagCode]
    DefParamCycle: typing.ClassVar[DiagCode]
    DefParamLocal: typing.ClassVar[DiagCode]
    DefParamTarget: typing.ClassVar[DiagCode]
    DefParamTargetChange: typing.ClassVar[DiagCode]
    DefaultArgNotAllowed: typing.ClassVar[DiagCode]
    DefaultSuperArgLocalReference: typing.ClassVar[DiagCode]
    DeferredAssertAutoRefArg: typing.ClassVar[DiagCode]
    DeferredAssertNonVoid: typing.ClassVar[DiagCode]
    DeferredAssertOutArg: typing.ClassVar[DiagCode]
    DeferredDelayMustBeZero: typing.ClassVar[DiagCode]
    DefinitionUsedAsType: typing.ClassVar[DiagCode]
    DefinitionUsedAsValue: typing.ClassVar[DiagCode]
    DefparamBadHierarchy: typing.ClassVar[DiagCode]
    Delay3NotAllowed: typing.ClassVar[DiagCode]
    Delay3OnVar: typing.ClassVar[DiagCode]
    Delay3UdpNotAllowed: typing.ClassVar[DiagCode]
    DelayNotNumeric: typing.ClassVar[DiagCode]
    DelaysNotAllowed: typing.ClassVar[DiagCode]
    DerivedCovergroupNoBase: typing.ClassVar[DiagCode]
    DerivedCovergroupNotInClass: typing.ClassVar[DiagCode]
    DifferentClockInClockingBlock: typing.ClassVar[DiagCode]
    DigitsLeadingUnderscore: typing.ClassVar[DiagCode]
    DimensionIndexInvalid: typing.ClassVar[DiagCode]
    DimensionRequiresConstRange: typing.ClassVar[DiagCode]
    DirectionOnInterfacePort: typing.ClassVar[DiagCode]
    DirectionWithInterfacePort: typing.ClassVar[DiagCode]
    DirectiveInsideDesignElement: typing.ClassVar[DiagCode]
    DisableIffLocalVar: typing.ClassVar[DiagCode]
    DisableIffMatched: typing.ClassVar[DiagCode]
    DisallowedPortDefault: typing.ClassVar[DiagCode]
    DistRealRangeWeight: typing.ClassVar[DiagCode]
    DotIntoInstArray: typing.ClassVar[DiagCode]
    DotOnType: typing.ClassVar[DiagCode]
    DriveStrengthHighZ: typing.ClassVar[DiagCode]
    DriveStrengthInvalid: typing.ClassVar[DiagCode]
    DriveStrengthNotAllowed: typing.ClassVar[DiagCode]
    DupConfigRule: typing.ClassVar[DiagCode]
    DupInterfaceExternMethod: typing.ClassVar[DiagCode]
    DupTimingPath: typing.ClassVar[DiagCode]
    DuplicateArgAssignment: typing.ClassVar[DiagCode]
    DuplicateAttribute: typing.ClassVar[DiagCode]
    DuplicateBind: typing.ClassVar[DiagCode]
    DuplicateClassSpecifier: typing.ClassVar[DiagCode]
    DuplicateDeclModifier: typing.ClassVar[DiagCode]
    DuplicateDefinition: typing.ClassVar[DiagCode]
    DuplicateDefparam: typing.ClassVar[DiagCode]
    DuplicateImport: typing.ClassVar[DiagCode]
    DuplicateParamAssignment: typing.ClassVar[DiagCode]
    DuplicatePortConnection: typing.ClassVar[DiagCode]
    DuplicateQualifier: typing.ClassVar[DiagCode]
    DuplicateWildcardPortConnection: typing.ClassVar[DiagCode]
    DynamicDimensionIndex: typing.ClassVar[DiagCode]
    DynamicFromChecker: typing.ClassVar[DiagCode]
    DynamicNotProcedural: typing.ClassVar[DiagCode]
    EdgeDescWrongKeyword: typing.ClassVar[DiagCode]
    EmbeddedNull: typing.ClassVar[DiagCode]
    EmptyArgNotAllowed: typing.ClassVar[DiagCode]
    EmptyAssignmentPattern: typing.ClassVar[DiagCode]
    EmptyBody: typing.ClassVar[DiagCode]
    EmptyConcatNotAllowed: typing.ClassVar[DiagCode]
    EmptyMember: typing.ClassVar[DiagCode]
    EmptyStatement: typing.ClassVar[DiagCode]
    EmptyUdpPort: typing.ClassVar[DiagCode]
    EndNameMismatch: typing.ClassVar[DiagCode]
    EndNameNotEmpty: typing.ClassVar[DiagCode]
    EnumIncrementUnknown: typing.ClassVar[DiagCode]
    EnumRangeLiteral: typing.ClassVar[DiagCode]
    EnumRangeMultiDimensional: typing.ClassVar[DiagCode]
    EnumValueDuplicate: typing.ClassVar[DiagCode]
    EnumValueOutOfRange: typing.ClassVar[DiagCode]
    EnumValueOverflow: typing.ClassVar[DiagCode]
    EnumValueSizeMismatch: typing.ClassVar[DiagCode]
    EnumValueUnknownBits: typing.ClassVar[DiagCode]
    ErrorTask: typing.ClassVar[DiagCode]
    EscapedWhitespace: typing.ClassVar[DiagCode]
    EventExprAssertionArg: typing.ClassVar[DiagCode]
    EventExpressionConstant: typing.ClassVar[DiagCode]
    EventExpressionFuncArg: typing.ClassVar[DiagCode]
    EventTriggerCycleDelay: typing.ClassVar[DiagCode]
    ExceededMaxIncludeDepth: typing.ClassVar[DiagCode]
    ExpectedAnsiPort: typing.ClassVar[DiagCode]
    ExpectedArgument: typing.ClassVar[DiagCode]
    ExpectedAssertionItemPort: typing.ClassVar[DiagCode]
    ExpectedAssignmentKey: typing.ClassVar[DiagCode]
    ExpectedAttribute: typing.ClassVar[DiagCode]
    ExpectedCaseItem: typing.ClassVar[DiagCode]
    ExpectedClassPropertyName: typing.ClassVar[DiagCode]
    ExpectedClassSpecifier: typing.ClassVar[DiagCode]
    ExpectedClockingSkew: typing.ClassVar[DiagCode]
    ExpectedClosingQuote: typing.ClassVar[DiagCode]
    ExpectedConditionalPattern: typing.ClassVar[DiagCode]
    ExpectedConstraintName: typing.ClassVar[DiagCode]
    ExpectedContinuousAssignment: typing.ClassVar[DiagCode]
    ExpectedDPISpecString: typing.ClassVar[DiagCode]
    ExpectedDeclarator: typing.ClassVar[DiagCode]
    ExpectedDiagPragmaArg: typing.ClassVar[DiagCode]
    ExpectedDiagPragmaLevel: typing.ClassVar[DiagCode]
    ExpectedDistItem: typing.ClassVar[DiagCode]
    ExpectedDriveStrength: typing.ClassVar[DiagCode]
    ExpectedEdgeDescriptor: typing.ClassVar[DiagCode]
    ExpectedEnumBase: typing.ClassVar[DiagCode]
    ExpectedExpression: typing.ClassVar[DiagCode]
    ExpectedForInitializer: typing.ClassVar[DiagCode]
    ExpectedFunctionPort: typing.ClassVar[DiagCode]
    ExpectedFunctionPortList: typing.ClassVar[DiagCode]
    ExpectedGenvarIterVar: typing.ClassVar[DiagCode]
    ExpectedHierarchicalInstantiation: typing.ClassVar[DiagCode]
    ExpectedIdentifier: typing.ClassVar[DiagCode]
    ExpectedIfOrCase: typing.ClassVar[DiagCode]
    ExpectedImportExport: typing.ClassVar[DiagCode]
    ExpectedIncludeFileName: typing.ClassVar[DiagCode]
    ExpectedIntegerBaseAfterSigned: typing.ClassVar[DiagCode]
    ExpectedIntegerLiteral: typing.ClassVar[DiagCode]
    ExpectedInterfaceClassName: typing.ClassVar[DiagCode]
    ExpectedIterationExpression: typing.ClassVar[DiagCode]
    ExpectedIteratorName: typing.ClassVar[DiagCode]
    ExpectedMacroArgs: typing.ClassVar[DiagCode]
    ExpectedMacroStringifyEnd: typing.ClassVar[DiagCode]
    ExpectedMember: typing.ClassVar[DiagCode]
    ExpectedModOrVarName: typing.ClassVar[DiagCode]
    ExpectedModportPort: typing.ClassVar[DiagCode]
    ExpectedModuleInstance: typing.ClassVar[DiagCode]
    ExpectedModuleName: typing.ClassVar[DiagCode]
    ExpectedNetDelay: typing.ClassVar[DiagCode]
    ExpectedNetRef: typing.ClassVar[DiagCode]
    ExpectedNetStrength: typing.ClassVar[DiagCode]
    ExpectedNetType: typing.ClassVar[DiagCode]
    ExpectedNonAnsiPort: typing.ClassVar[DiagCode]
    ExpectedPackageImport: typing.ClassVar[DiagCode]
    ExpectedParameterPort: typing.ClassVar[DiagCode]
    ExpectedPathOp: typing.ClassVar[DiagCode]
    ExpectedPattern: typing.ClassVar[DiagCode]
    ExpectedPortConnection: typing.ClassVar[DiagCode]
    ExpectedPortList: typing.ClassVar[DiagCode]
    ExpectedPragmaExpression: typing.ClassVar[DiagCode]
    ExpectedPragmaName: typing.ClassVar[DiagCode]
    ExpectedProtectArg: typing.ClassVar[DiagCode]
    ExpectedProtectKeyword: typing.ClassVar[DiagCode]
    ExpectedRsRule: typing.ClassVar[DiagCode]
    ExpectedSampleKeyword: typing.ClassVar[DiagCode]
    ExpectedScopeName: typing.ClassVar[DiagCode]
    ExpectedScopeOrAssert: typing.ClassVar[DiagCode]
    ExpectedStatement: typing.ClassVar[DiagCode]
    ExpectedStreamExpression: typing.ClassVar[DiagCode]
    ExpectedStringLiteral: typing.ClassVar[DiagCode]
    ExpectedSubroutineName: typing.ClassVar[DiagCode]
    ExpectedTimeLiteral: typing.ClassVar[DiagCode]
    ExpectedToken: typing.ClassVar[DiagCode]
    ExpectedUdpPort: typing.ClassVar[DiagCode]
    ExpectedUdpSymbol: typing.ClassVar[DiagCode]
    ExpectedValueRangeElement: typing.ClassVar[DiagCode]
    ExpectedVariableAssignment: typing.ClassVar[DiagCode]
    ExpectedVariableName: typing.ClassVar[DiagCode]
    ExpectedVectorDigits: typing.ClassVar[DiagCode]
    ExplicitClockInClockingBlock: typing.ClassVar[DiagCode]
    ExprMustBeIntegral: typing.ClassVar[DiagCode]
    ExprNotConstraint: typing.ClassVar[DiagCode]
    ExprNotStatement: typing.ClassVar[DiagCode]
    ExpressionNotAssignable: typing.ClassVar[DiagCode]
    ExpressionNotCallable: typing.ClassVar[DiagCode]
    ExtendClassFromIface: typing.ClassVar[DiagCode]
    ExtendFromFinal: typing.ClassVar[DiagCode]
    ExtendIfaceFromClass: typing.ClassVar[DiagCode]
    ExternDeclMismatchImpl: typing.ClassVar[DiagCode]
    ExternDeclMismatchPrev: typing.ClassVar[DiagCode]
    ExternFuncForkJoin: typing.ClassVar[DiagCode]
    ExternIfaceArrayMethod: typing.ClassVar[DiagCode]
    ExternWildcardPortList: typing.ClassVar[DiagCode]
    ExtraPragmaArgs: typing.ClassVar[DiagCode]
    ExtraProtectEnd: typing.ClassVar[DiagCode]
    FatalTask: typing.ClassVar[DiagCode]
    FinalSpecifierLast: typing.ClassVar[DiagCode]
    FinalWithPure: typing.ClassVar[DiagCode]
    FloatBoolConv: typing.ClassVar[DiagCode]
    FloatIntConv: typing.ClassVar[DiagCode]
    FloatNarrow: typing.ClassVar[DiagCode]
    FloatWiden: typing.ClassVar[DiagCode]
    ForeachDynamicDimAfterSkipped: typing.ClassVar[DiagCode]
    ForeachWildcardIndex: typing.ClassVar[DiagCode]
    ForkJoinAlwaysComb: typing.ClassVar[DiagCode]
    FormatEmptyArg: typing.ClassVar[DiagCode]
    FormatMismatchedType: typing.ClassVar[DiagCode]
    FormatMultibitStrength: typing.ClassVar[DiagCode]
    FormatNoArgument: typing.ClassVar[DiagCode]
    FormatRealInt: typing.ClassVar[DiagCode]
    FormatSpecifierInvalidWidth: typing.ClassVar[DiagCode]
    FormatSpecifierNotFloat: typing.ClassVar[DiagCode]
    FormatSpecifierWidthNotAllowed: typing.ClassVar[DiagCode]
    FormatTooManyArgs: typing.ClassVar[DiagCode]
    FormatUnspecifiedType: typing.ClassVar[DiagCode]
    ForwardTypedefDoesNotMatch: typing.ClassVar[DiagCode]
    ForwardTypedefVisibility: typing.ClassVar[DiagCode]
    GFSVMatchItems: typing.ClassVar[DiagCode]
    GateUDNTConn: typing.ClassVar[DiagCode]
    GenericClassScopeResolution: typing.ClassVar[DiagCode]
    GenvarDuplicate: typing.ClassVar[DiagCode]
    GenvarUnknownBits: typing.ClassVar[DiagCode]
    GlobalClockEventExpr: typing.ClassVar[DiagCode]
    GlobalClockingEmpty: typing.ClassVar[DiagCode]
    GlobalClockingGenerate: typing.ClassVar[DiagCode]
    GlobalSampledValueAssertionExpr: typing.ClassVar[DiagCode]
    GlobalSampledValueNested: typing.ClassVar[DiagCode]
    HierarchicalFromPackage: typing.ClassVar[DiagCode]
    HierarchicalRefUnknownModule: typing.ClassVar[DiagCode]
    IfNoneEdgeSensitive: typing.ClassVar[DiagCode]
    IfaceExtendIncomplete: typing.ClassVar[DiagCode]
    IfaceExtendTypeParam: typing.ClassVar[DiagCode]
    IfaceImportExportTarget: typing.ClassVar[DiagCode]
    IfaceMethodHidden: typing.ClassVar[DiagCode]
    IfaceMethodNoImpl: typing.ClassVar[DiagCode]
    IfaceMethodNotExtern: typing.ClassVar[DiagCode]
    IfaceMethodNotVirtual: typing.ClassVar[DiagCode]
    IfaceMethodPure: typing.ClassVar[DiagCode]
    IfaceNameConflict: typing.ClassVar[DiagCode]
    IfacePortInExpr: typing.ClassVar[DiagCode]
    IgnoredMacroPaste: typing.ClassVar[DiagCode]
    IgnoredSlice: typing.ClassVar[DiagCode]
    IllegalReferenceToProgramItem: typing.ClassVar[DiagCode]
    ImplementNonIface: typing.ClassVar[DiagCode]
    ImplicitConnNetInconsistent: typing.ClassVar[DiagCode]
    ImplicitConvert: typing.ClassVar[DiagCode]
    ImplicitEventInAssertion: typing.ClassVar[DiagCode]
    ImplicitNamedPortNotFound: typing.ClassVar[DiagCode]
    ImplicitNamedPortTypeMismatch: typing.ClassVar[DiagCode]
    ImplicitNetPortNoDefault: typing.ClassVar[DiagCode]
    ImplicitNotAllowed: typing.ClassVar[DiagCode]
    ImportNameCollision: typing.ClassVar[DiagCode]
    InOutDefaultSkew: typing.ClassVar[DiagCode]
    InOutPortCannotBeVariable: typing.ClassVar[DiagCode]
    InOutUWireConn: typing.ClassVar[DiagCode]
    InOutUWirePort: typing.ClassVar[DiagCode]
    InOutVarPortConn: typing.ClassVar[DiagCode]
    IncDecNotAllowed: typing.ClassVar[DiagCode]
    IncompleteReturn: typing.ClassVar[DiagCode]
    IndexOOB: typing.ClassVar[DiagCode]
    IndexValueInvalid: typing.ClassVar[DiagCode]
    InequivalentUniquenessTypes: typing.ClassVar[DiagCode]
    InferredComb: typing.ClassVar[DiagCode]
    InferredLatch: typing.ClassVar[DiagCode]
    InferredValDefArg: typing.ClassVar[DiagCode]
    InfinitelyRecursiveHierarchy: typing.ClassVar[DiagCode]
    InfoTask: typing.ClassVar[DiagCode]
    InheritFromAbstract: typing.ClassVar[DiagCode]
    InheritFromAbstractConstraint: typing.ClassVar[DiagCode]
    InitializerRequired: typing.ClassVar[DiagCode]
    InputPortAssign: typing.ClassVar[DiagCode]
    InputPortCoercion: typing.ClassVar[DiagCode]
    InstanceArrayEndianMismatch: typing.ClassVar[DiagCode]
    InstanceMissingParens: typing.ClassVar[DiagCode]
    InstanceNameRequired: typing.ClassVar[DiagCode]
    InstanceWithDelay: typing.ClassVar[DiagCode]
    InstanceWithStrength: typing.ClassVar[DiagCode]
    IntBoolConv: typing.ClassVar[DiagCode]
    IntFloatConv: typing.ClassVar[DiagCode]
    InterconnectDelaySyntax: typing.ClassVar[DiagCode]
    InterconnectInitializer: typing.ClassVar[DiagCode]
    InterconnectMultiPort: typing.ClassVar[DiagCode]
    InterconnectPortVar: typing.ClassVar[DiagCode]
    InterconnectReference: typing.ClassVar[DiagCode]
    InterconnectTypeSyntax: typing.ClassVar[DiagCode]
    InterfacePortInvalidExpression: typing.ClassVar[DiagCode]
    InterfacePortNotConnected: typing.ClassVar[DiagCode]
    InterfacePortTypeMismatch: typing.ClassVar[DiagCode]
    InvalidAccessDotColon: typing.ClassVar[DiagCode]
    InvalidArgumentExpr: typing.ClassVar[DiagCode]
    InvalidArrayElemType: typing.ClassVar[DiagCode]
    InvalidArraySize: typing.ClassVar[DiagCode]
    InvalidAssociativeIndexType: typing.ClassVar[DiagCode]
    InvalidBindTarget: typing.ClassVar[DiagCode]
    InvalidBinsMatches: typing.ClassVar[DiagCode]
    InvalidBinsTarget: typing.ClassVar[DiagCode]
    InvalidBlockEventTarget: typing.ClassVar[DiagCode]
    InvalidClassAccess: typing.ClassVar[DiagCode]
    InvalidClockingSignal: typing.ClassVar[DiagCode]
    InvalidCommaInPropExpr: typing.ClassVar[DiagCode]
    InvalidConstraintExpr: typing.ClassVar[DiagCode]
    InvalidConstraintQualifier: typing.ClassVar[DiagCode]
    InvalidConstructorAccess: typing.ClassVar[DiagCode]
    InvalidCoverageExpr: typing.ClassVar[DiagCode]
    InvalidCoverageOption: typing.ClassVar[DiagCode]
    InvalidDPIArgType: typing.ClassVar[DiagCode]
    InvalidDPICIdentifier: typing.ClassVar[DiagCode]
    InvalidDPIReturnType: typing.ClassVar[DiagCode]
    InvalidDeferredAssertAction: typing.ClassVar[DiagCode]
    InvalidDelayValue: typing.ClassVar[DiagCode]
    InvalidDimensionRange: typing.ClassVar[DiagCode]
    InvalidDisableTarget: typing.ClassVar[DiagCode]
    InvalidDistExpression: typing.ClassVar[DiagCode]
    InvalidEdgeDescriptor: typing.ClassVar[DiagCode]
    InvalidEncodingByte: typing.ClassVar[DiagCode]
    InvalidEnumBase: typing.ClassVar[DiagCode]
    InvalidEventExpression: typing.ClassVar[DiagCode]
    InvalidExtendsDefault: typing.ClassVar[DiagCode]
    InvalidForInitializer: typing.ClassVar[DiagCode]
    InvalidForStepExpression: typing.ClassVar[DiagCode]
    InvalidGenvarIterExpression: typing.ClassVar[DiagCode]
    InvalidHexEscapeCode: typing.ClassVar[DiagCode]
    InvalidHierarchicalIfacePortConn: typing.ClassVar[DiagCode]
    InvalidInferredTimeScale: typing.ClassVar[DiagCode]
    InvalidInstanceForParent: typing.ClassVar[DiagCode]
    InvalidLineDirectiveLevel: typing.ClassVar[DiagCode]
    InvalidMacroName: typing.ClassVar[DiagCode]
    InvalidMatchItem: typing.ClassVar[DiagCode]
    InvalidMemberAccess: typing.ClassVar[DiagCode]
    InvalidMethodOverride: typing.ClassVar[DiagCode]
    InvalidMethodQualifier: typing.ClassVar[DiagCode]
    InvalidModportAccess: typing.ClassVar[DiagCode]
    InvalidMulticlockedSeqOp: typing.ClassVar[DiagCode]
    InvalidNGateCount: typing.ClassVar[DiagCode]
    InvalidNetType: typing.ClassVar[DiagCode]
    InvalidPackageDecl: typing.ClassVar[DiagCode]
    InvalidParamOverrideOpt: typing.ClassVar[DiagCode]
    InvalidPortSubType: typing.ClassVar[DiagCode]
    InvalidPortType: typing.ClassVar[DiagCode]
    InvalidPragmaNumber: typing.ClassVar[DiagCode]
    InvalidPragmaViewport: typing.ClassVar[DiagCode]
    InvalidPrimInstanceForParent: typing.ClassVar[DiagCode]
    InvalidPrimitivePortConn: typing.ClassVar[DiagCode]
    InvalidPropertyIndex: typing.ClassVar[DiagCode]
    InvalidPropertyQualifier: typing.ClassVar[DiagCode]
    InvalidPropertyRange: typing.ClassVar[DiagCode]
    InvalidPullStrength: typing.ClassVar[DiagCode]
    InvalidPulseStyle: typing.ClassVar[DiagCode]
    InvalidQualifierForConstructor: typing.ClassVar[DiagCode]
    InvalidQualifierForIfaceMember: typing.ClassVar[DiagCode]
    InvalidQualifierForMember: typing.ClassVar[DiagCode]
    InvalidRandType: typing.ClassVar[DiagCode]
    InvalidRandomizeOverride: typing.ClassVar[DiagCode]
    InvalidRefArg: typing.ClassVar[DiagCode]
    InvalidRepeatRange: typing.ClassVar[DiagCode]
    InvalidScopeIndexExpression: typing.ClassVar[DiagCode]
    InvalidSelectExpression: typing.ClassVar[DiagCode]
    InvalidSignalEventInSeq: typing.ClassVar[DiagCode]
    InvalidSpecifyDest: typing.ClassVar[DiagCode]
    InvalidSpecifyPath: typing.ClassVar[DiagCode]
    InvalidSpecifySource: typing.ClassVar[DiagCode]
    InvalidSpecifyType: typing.ClassVar[DiagCode]
    InvalidStmtInChecker: typing.ClassVar[DiagCode]
    InvalidStringArg: typing.ClassVar[DiagCode]
    InvalidSuperNew: typing.ClassVar[DiagCode]
    InvalidSuperNewDefault: typing.ClassVar[DiagCode]
    InvalidSyntaxInEventExpr: typing.ClassVar[DiagCode]
    InvalidThisHandle: typing.ClassVar[DiagCode]
    InvalidTimeScalePrecision: typing.ClassVar[DiagCode]
    InvalidTimeScaleSpecifier: typing.ClassVar[DiagCode]
    InvalidTimingCheckNotifierArg: typing.ClassVar[DiagCode]
    InvalidTopModule: typing.ClassVar[DiagCode]
    InvalidUTF8Seq: typing.ClassVar[DiagCode]
    InvalidUnionMember: typing.ClassVar[DiagCode]
    InvalidUniquenessExpr: typing.ClassVar[DiagCode]
    InvalidUserDefinedNetType: typing.ClassVar[DiagCode]
    IsUnboundedParamArg: typing.ClassVar[DiagCode]
    IteratorArgsWithoutWithClause: typing.ClassVar[DiagCode]
    LabelAndName: typing.ClassVar[DiagCode]
    LetHierarchical: typing.ClassVar[DiagCode]
    LifetimeForPrototype: typing.ClassVar[DiagCode]
    LiteralSizeIsZero: typing.ClassVar[DiagCode]
    LiteralSizeTooLarge: typing.ClassVar[DiagCode]
    LocalFormalVarMultiAssign: typing.ClassVar[DiagCode]
    LocalMemberAccess: typing.ClassVar[DiagCode]
    LocalNotAllowed: typing.ClassVar[DiagCode]
    LocalParamNoInitializer: typing.ClassVar[DiagCode]
    LocalVarEventExpr: typing.ClassVar[DiagCode]
    LocalVarMatchItem: typing.ClassVar[DiagCode]
    LocalVarOutputEmptyMatch: typing.ClassVar[DiagCode]
    LocalVarTypeRequired: typing.ClassVar[DiagCode]
    LogicalNotParentheses: typing.ClassVar[DiagCode]
    LogicalOpParentheses: typing.ClassVar[DiagCode]
    LoopVarShadowsArray: typing.ClassVar[DiagCode]
    MacroOpsOutsideDefinition: typing.ClassVar[DiagCode]
    MacroTokensAfterPragmaProtect: typing.ClassVar[DiagCode]
    MatchItemsAdmitEmpty: typing.ClassVar[DiagCode]
    MaxGenerateStepsExceeded: typing.ClassVar[DiagCode]
    MaxInstanceArrayExceeded: typing.ClassVar[DiagCode]
    MaxInstanceDepthExceeded: typing.ClassVar[DiagCode]
    MemberDefinitionBeforeClass: typing.ClassVar[DiagCode]
    MethodArgCountMismatch: typing.ClassVar[DiagCode]
    MethodArgDefaultMismatch: typing.ClassVar[DiagCode]
    MethodArgDirectionMismatch: typing.ClassVar[DiagCode]
    MethodArgNameMismatch: typing.ClassVar[DiagCode]
    MethodArgNoDefault: typing.ClassVar[DiagCode]
    MethodArgTypeMismatch: typing.ClassVar[DiagCode]
    MethodKindMismatch: typing.ClassVar[DiagCode]
    MethodReturnMismatch: typing.ClassVar[DiagCode]
    MethodReturnTypeScoped: typing.ClassVar[DiagCode]
    MethodStaticLifetime: typing.ClassVar[DiagCode]
    MismatchConstraintSpecifiers: typing.ClassVar[DiagCode]
    MismatchStaticConstraint: typing.ClassVar[DiagCode]
    MismatchedEndKeywordsDirective: typing.ClassVar[DiagCode]
    MismatchedTimeScales: typing.ClassVar[DiagCode]
    MismatchedUserDefPortConn: typing.ClassVar[DiagCode]
    MismatchedUserDefPortDir: typing.ClassVar[DiagCode]
    MisplacedDirectiveChar: typing.ClassVar[DiagCode]
    MisplacedTrailingSeparator: typing.ClassVar[DiagCode]
    MissingConstraintBlock: typing.ClassVar[DiagCode]
    MissingEndIfDirective: typing.ClassVar[DiagCode]
    MissingExponentDigits: typing.ClassVar[DiagCode]
    MissingExportImpl: typing.ClassVar[DiagCode]
    MissingExternImpl: typing.ClassVar[DiagCode]
    MissingExternModuleImpl: typing.ClassVar[DiagCode]
    MissingExternWildcardPorts: typing.ClassVar[DiagCode]
    MissingFormatSpecifier: typing.ClassVar[DiagCode]
    MissingFractionalDigits: typing.ClassVar[DiagCode]
    MissingInvocationParens: typing.ClassVar[DiagCode]
    MissingModportPortDirection: typing.ClassVar[DiagCode]
    MissingPortIODeclaration: typing.ClassVar[DiagCode]
    MissingReturn: typing.ClassVar[DiagCode]
    MissingReturnValue: typing.ClassVar[DiagCode]
    MissingReturnValueProd: typing.ClassVar[DiagCode]
    MissingTimeScale: typing.ClassVar[DiagCode]
    MixedVarAssigns: typing.ClassVar[DiagCode]
    MixingOrderedAndNamedArgs: typing.ClassVar[DiagCode]
    MixingOrderedAndNamedParams: typing.ClassVar[DiagCode]
    MixingOrderedAndNamedPorts: typing.ClassVar[DiagCode]
    MixingSubroutinePortKinds: typing.ClassVar[DiagCode]
    ModportConnMismatch: typing.ClassVar[DiagCode]
    MultiBitEdge: typing.ClassVar[DiagCode]
    MulticlockedInClockingBlock: typing.ClassVar[DiagCode]
    MulticlockedSeqEmptyMatch: typing.ClassVar[DiagCode]
    MultipleAlwaysAssigns: typing.ClassVar[DiagCode]
    MultipleContAssigns: typing.ClassVar[DiagCode]
    MultipleDefaultCases: typing.ClassVar[DiagCode]
    MultipleDefaultClocking: typing.ClassVar[DiagCode]
    MultipleDefaultConstructorArg: typing.ClassVar[DiagCode]
    MultipleDefaultDisable: typing.ClassVar[DiagCode]
    MultipleDefaultDistWeight: typing.ClassVar[DiagCode]
    MultipleDefaultInputSkew: typing.ClassVar[DiagCode]
    MultipleDefaultOutputSkew: typing.ClassVar[DiagCode]
    MultipleDefaultRules: typing.ClassVar[DiagCode]
    MultipleGenerateDefaultCases: typing.ClassVar[DiagCode]
    MultipleGlobalClocking: typing.ClassVar[DiagCode]
    MultipleNetAlias: typing.ClassVar[DiagCode]
    MultiplePackedOpenArrays: typing.ClassVar[DiagCode]
    MultipleParallelTerminals: typing.ClassVar[DiagCode]
    MultipleTopDupName: typing.ClassVar[DiagCode]
    MultipleUDNTDrivers: typing.ClassVar[DiagCode]
    MultipleUWireDrivers: typing.ClassVar[DiagCode]
    NTResolveArgModify: typing.ClassVar[DiagCode]
    NTResolveClass: typing.ClassVar[DiagCode]
    NTResolveReturn: typing.ClassVar[DiagCode]
    NTResolveSingleArg: typing.ClassVar[DiagCode]
    NTResolveTask: typing.ClassVar[DiagCode]
    NTResolveUserDef: typing.ClassVar[DiagCode]
    NameListWithScopeRandomize: typing.ClassVar[DiagCode]
    NamedArgNotAllowed: typing.ClassVar[DiagCode]
    NegativeTimingLimit: typing.ClassVar[DiagCode]
    NestedBlockComment: typing.ClassVar[DiagCode]
    NestedConfigMultipleTops: typing.ClassVar[DiagCode]
    NestedDisableIff: typing.ClassVar[DiagCode]
    NestedIface: typing.ClassVar[DiagCode]
    NestedNonStaticClassMethod: typing.ClassVar[DiagCode]
    NestedNonStaticClassProperty: typing.ClassVar[DiagCode]
    NestedProtectBegin: typing.ClassVar[DiagCode]
    NetAliasCommonNetType: typing.ClassVar[DiagCode]
    NetAliasHierarchical: typing.ClassVar[DiagCode]
    NetAliasNotANet: typing.ClassVar[DiagCode]
    NetAliasSelf: typing.ClassVar[DiagCode]
    NetAliasWidthMismatch: typing.ClassVar[DiagCode]
    NetInconsistent: typing.ClassVar[DiagCode]
    NetRangeInconsistent: typing.ClassVar[DiagCode]
    NewArrayTarget: typing.ClassVar[DiagCode]
    NewClassTarget: typing.ClassVar[DiagCode]
    NewInterfaceClass: typing.ClassVar[DiagCode]
    NewKeywordQualified: typing.ClassVar[DiagCode]
    NewVirtualClass: typing.ClassVar[DiagCode]
    NoChangeEdgeRequired: typing.ClassVar[DiagCode]
    NoCommaInList: typing.ClassVar[DiagCode]
    NoCommonComparisonType: typing.ClassVar[DiagCode]
    NoConstraintBody: typing.ClassVar[DiagCode]
    NoDeclInClass: typing.ClassVar[DiagCode]
    NoDefaultClocking: typing.ClassVar[DiagCode]
    NoDefaultSpecialization: typing.ClassVar[DiagCode]
    NoGlobalClocking: typing.ClassVar[DiagCode]
    NoImplicitConversion: typing.ClassVar[DiagCode]
    NoInferredClock: typing.ClassVar[DiagCode]
    NoLabelOnSemicolon: typing.ClassVar[DiagCode]
    NoMemberImplFound: typing.ClassVar[DiagCode]
    NoTopModules: typing.ClassVar[DiagCode]
    NoUniqueClock: typing.ClassVar[DiagCode]
    NonIntegralConstraintLiteral: typing.ClassVar[DiagCode]
    NonPrintableChar: typing.ClassVar[DiagCode]
    NonProceduralFuncArg: typing.ClassVar[DiagCode]
    NonStandardGenBlock: typing.ClassVar[DiagCode]
    NonStaticClassMethod: typing.ClassVar[DiagCode]
    NonStaticClassProperty: typing.ClassVar[DiagCode]
    NonblockingAssignmentToAuto: typing.ClassVar[DiagCode]
    NonblockingDynamicAssign: typing.ClassVar[DiagCode]
    NonblockingInFinal: typing.ClassVar[DiagCode]
    NonstandardDist: typing.ClassVar[DiagCode]
    NonstandardEscapeCode: typing.ClassVar[DiagCode]
    NonstandardForeach: typing.ClassVar[DiagCode]
    NonstandardSysFunc: typing.ClassVar[DiagCode]
    NotAChecker: typing.ClassVar[DiagCode]
    NotAClass: typing.ClassVar[DiagCode]
    NotAClockingBlock: typing.ClassVar[DiagCode]
    NotAGenericClass: typing.ClassVar[DiagCode]
    NotAGenvar: typing.ClassVar[DiagCode]
    NotAHierarchicalScope: typing.ClassVar[DiagCode]
    NotAModport: typing.ClassVar[DiagCode]
    NotAProduction: typing.ClassVar[DiagCode]
    NotASubroutine: typing.ClassVar[DiagCode]
    NotAType: typing.ClassVar[DiagCode]
    NotAValue: typing.ClassVar[DiagCode]
    NotAllowedInAnonymousProgram: typing.ClassVar[DiagCode]
    NotAllowedInCU: typing.ClassVar[DiagCode]
    NotAllowedInChecker: typing.ClassVar[DiagCode]
    NotAllowedInClass: typing.ClassVar[DiagCode]
    NotAllowedInClocking: typing.ClassVar[DiagCode]
    NotAllowedInGenerate: typing.ClassVar[DiagCode]
    NotAllowedInIfaceClass: typing.ClassVar[DiagCode]
    NotAllowedInInterface: typing.ClassVar[DiagCode]
    NotAllowedInModport: typing.ClassVar[DiagCode]
    NotAllowedInModule: typing.ClassVar[DiagCode]
    NotAllowedInPackage: typing.ClassVar[DiagCode]
    NotAllowedInProgram: typing.ClassVar[DiagCode]
    NotAnArray: typing.ClassVar[DiagCode]
    NotAnEvent: typing.ClassVar[DiagCode]
    NotAnInterface: typing.ClassVar[DiagCode]
    NotAnInterfaceOrPort: typing.ClassVar[DiagCode]
    NotBooleanConvertible: typing.ClassVar[DiagCode]
    NotEnoughMacroArgs: typing.ClassVar[DiagCode]
    NoteAliasDeclaration: typing.ClassVar[DiagCode]
    NoteAliasedTo: typing.ClassVar[DiagCode]
    NoteAlwaysFalse: typing.ClassVar[DiagCode]
    NoteAssignedHere: typing.ClassVar[DiagCode]
    NoteClockHere: typing.ClassVar[DiagCode]
    NoteCommonAncestor: typing.ClassVar[DiagCode]
    NoteComparisonReduces: typing.ClassVar[DiagCode]
    NoteConditionalPrecedenceFix: typing.ClassVar[DiagCode]
    NoteConfigRule: typing.ClassVar[DiagCode]
    NoteDeclarationHere: typing.ClassVar[DiagCode]
    NoteDirectiveHere: typing.ClassVar[DiagCode]
    NoteDrivenHere: typing.ClassVar[DiagCode]
    NoteExpandedHere: typing.ClassVar[DiagCode]
    NoteFromHere2: typing.ClassVar[DiagCode]
    NoteHierarchicalRef: typing.ClassVar[DiagCode]
    NoteImportedFrom: typing.ClassVar[DiagCode]
    NoteInCallTo: typing.ClassVar[DiagCode]
    NoteLastBlockEnded: typing.ClassVar[DiagCode]
    NoteLastBlockStarted: typing.ClassVar[DiagCode]
    NoteLogicalNotFix: typing.ClassVar[DiagCode]
    NoteLogicalNotSilence: typing.ClassVar[DiagCode]
    NoteOriginalAssign: typing.ClassVar[DiagCode]
    NotePrecedenceBitwiseFirst: typing.ClassVar[DiagCode]
    NotePrecedenceSilence: typing.ClassVar[DiagCode]
    NotePreviousDefinition: typing.ClassVar[DiagCode]
    NotePreviousMatch: typing.ClassVar[DiagCode]
    NotePreviousUsage: typing.ClassVar[DiagCode]
    NoteReferencedHere: typing.ClassVar[DiagCode]
    NoteRequiredHere: typing.ClassVar[DiagCode]
    NoteSkippingFrames: typing.ClassVar[DiagCode]
    NoteToMatchThis: typing.ClassVar[DiagCode]
    NoteUdpCoverage: typing.ClassVar[DiagCode]
    NoteWhileExpanding: typing.ClassVar[DiagCode]
    NullPortExpression: typing.ClassVar[DiagCode]
    ObjectTooLarge: typing.ClassVar[DiagCode]
    OctalEscapeCodeTooBig: typing.ClassVar[DiagCode]
    OutRefFuncConstraint: typing.ClassVar[DiagCode]
    OutputPortCoercion: typing.ClassVar[DiagCode]
    OverridingExtends: typing.ClassVar[DiagCode]
    OverridingFinal: typing.ClassVar[DiagCode]
    OverridingInitial: typing.ClassVar[DiagCode]
    PackageExportSelf: typing.ClassVar[DiagCode]
    PackageImportSelf: typing.ClassVar[DiagCode]
    PackageNetInit: typing.ClassVar[DiagCode]
    PackedArrayConv: typing.ClassVar[DiagCode]
    PackedArrayNotIntegral: typing.ClassVar[DiagCode]
    PackedDimsOnPredefinedType: typing.ClassVar[DiagCode]
    PackedDimsOnUnpacked: typing.ClassVar[DiagCode]
    PackedDimsRequireFullRange: typing.ClassVar[DiagCode]
    PackedMemberHasInitializer: typing.ClassVar[DiagCode]
    PackedMemberNotIntegral: typing.ClassVar[DiagCode]
    PackedTypeTooLarge: typing.ClassVar[DiagCode]
    PackedUnionWidthMismatch: typing.ClassVar[DiagCode]
    ParallelPathWidth: typing.ClassVar[DiagCode]
    ParamHasNoValue: typing.ClassVar[DiagCode]
    ParameterDoesNotExist: typing.ClassVar[DiagCode]
    ParseTreeTooDeep: typing.ClassVar[DiagCode]
    PastNumTicksInvalid: typing.ClassVar[DiagCode]
    PathPulseInExpr: typing.ClassVar[DiagCode]
    PathPulseInvalidPathName: typing.ClassVar[DiagCode]
    PatternStructTooFew: typing.ClassVar[DiagCode]
    PatternStructTooMany: typing.ClassVar[DiagCode]
    PatternStructType: typing.ClassVar[DiagCode]
    PatternTaggedType: typing.ClassVar[DiagCode]
    PlaRangeInAscendingOrder: typing.ClassVar[DiagCode]
    PointlessVoidCast: typing.ClassVar[DiagCode]
    PortConcatInOut: typing.ClassVar[DiagCode]
    PortConcatRef: typing.ClassVar[DiagCode]
    PortConnArrayMismatch: typing.ClassVar[DiagCode]
    PortConnDimensionsMismatch: typing.ClassVar[DiagCode]
    PortDeclDimensionsMismatch: typing.ClassVar[DiagCode]
    PortDeclInANSIModule: typing.ClassVar[DiagCode]
    PortDoesNotExist: typing.ClassVar[DiagCode]
    PortTypeNotInterfaceOrData: typing.ClassVar[DiagCode]
    PortWidthExpand: typing.ClassVar[DiagCode]
    PortWidthTruncate: typing.ClassVar[DiagCode]
    PrimitiveAnsiMix: typing.ClassVar[DiagCode]
    PrimitiveDupInitial: typing.ClassVar[DiagCode]
    PrimitiveDupOutput: typing.ClassVar[DiagCode]
    PrimitiveInitVal: typing.ClassVar[DiagCode]
    PrimitiveInitialInComb: typing.ClassVar[DiagCode]
    PrimitiveOutputFirst: typing.ClassVar[DiagCode]
    PrimitivePortCountWrong: typing.ClassVar[DiagCode]
    PrimitivePortDup: typing.ClassVar[DiagCode]
    PrimitivePortMissing: typing.ClassVar[DiagCode]
    PrimitivePortUnknown: typing.ClassVar[DiagCode]
    PrimitiveRegDup: typing.ClassVar[DiagCode]
    PrimitiveRegInput: typing.ClassVar[DiagCode]
    PrimitiveTwoPorts: typing.ClassVar[DiagCode]
    PrimitiveWrongInitial: typing.ClassVar[DiagCode]
    PropAbortLocalVar: typing.ClassVar[DiagCode]
    PropAbortMatched: typing.ClassVar[DiagCode]
    PropExprInSequence: typing.ClassVar[DiagCode]
    PropInstanceRepetition: typing.ClassVar[DiagCode]
    PropertyLhsInvalid: typing.ClassVar[DiagCode]
    PropertyPortInLet: typing.ClassVar[DiagCode]
    PropertyPortInSeq: typing.ClassVar[DiagCode]
    ProtectArgList: typing.ClassVar[DiagCode]
    ProtectEncodingBytes: typing.ClassVar[DiagCode]
    ProtectedEnvelope: typing.ClassVar[DiagCode]
    ProtectedMemberAccess: typing.ClassVar[DiagCode]
    PullStrengthHighZ: typing.ClassVar[DiagCode]
    PulseControlPATHPULSE: typing.ClassVar[DiagCode]
    PulseControlSpecifyParent: typing.ClassVar[DiagCode]
    PureConstraintInAbstract: typing.ClassVar[DiagCode]
    PureInAbstract: typing.ClassVar[DiagCode]
    PureRequiresVirtual: typing.ClassVar[DiagCode]
    QualifierConflict: typing.ClassVar[DiagCode]
    QualifierNotFirst: typing.ClassVar[DiagCode]
    QualifiersOnOutOfBlock: typing.ClassVar[DiagCode]
    QueryOnAssociativeNonIntegral: typing.ClassVar[DiagCode]
    QueryOnAssociativeWildcard: typing.ClassVar[DiagCode]
    QueryOnDynamicType: typing.ClassVar[DiagCode]
    RandCInDist: typing.ClassVar[DiagCode]
    RandCInSoft: typing.ClassVar[DiagCode]
    RandCInSolveBefore: typing.ClassVar[DiagCode]
    RandCInUnique: typing.ClassVar[DiagCode]
    RandJoinNotEnough: typing.ClassVar[DiagCode]
    RandJoinNotNumeric: typing.ClassVar[DiagCode]
    RandJoinProdItem: typing.ClassVar[DiagCode]
    RandNeededInDist: typing.ClassVar[DiagCode]
    RandOnPackedMember: typing.ClassVar[DiagCode]
    RandOnUnionMember: typing.ClassVar[DiagCode]
    RangeOOB: typing.ClassVar[DiagCode]
    RangeSelectAssociative: typing.ClassVar[DiagCode]
    RangeWidthOOB: typing.ClassVar[DiagCode]
    RangeWidthOverflow: typing.ClassVar[DiagCode]
    RawProtectEOF: typing.ClassVar[DiagCode]
    RealCoverpointBins: typing.ClassVar[DiagCode]
    RealCoverpointDefaultArray: typing.ClassVar[DiagCode]
    RealCoverpointImplicit: typing.ClassVar[DiagCode]
    RealCoverpointTransBins: typing.ClassVar[DiagCode]
    RealCoverpointWildcardBins: typing.ClassVar[DiagCode]
    RealCoverpointWithExpr: typing.ClassVar[DiagCode]
    RealLiteralOverflow: typing.ClassVar[DiagCode]
    RealLiteralUnderflow: typing.ClassVar[DiagCode]
    RecursiveClassSpecialization: typing.ClassVar[DiagCode]
    RecursiveDefinition: typing.ClassVar[DiagCode]
    RecursiveLet: typing.ClassVar[DiagCode]
    RecursiveMacro: typing.ClassVar[DiagCode]
    RecursivePropArgExpr: typing.ClassVar[DiagCode]
    RecursivePropDisableIff: typing.ClassVar[DiagCode]
    RecursivePropNegation: typing.ClassVar[DiagCode]
    RecursivePropTimeAdvance: typing.ClassVar[DiagCode]
    RecursiveSequence: typing.ClassVar[DiagCode]
    RedefiningMacro: typing.ClassVar[DiagCode]
    Redefinition: typing.ClassVar[DiagCode]
    RedefinitionDifferentType: typing.ClassVar[DiagCode]
    RefArgAutomaticFunc: typing.ClassVar[DiagCode]
    RefArgForkJoin: typing.ClassVar[DiagCode]
    RefPortMustBeVariable: typing.ClassVar[DiagCode]
    RefPortUnconnected: typing.ClassVar[DiagCode]
    RefPortUnnamedUnconnected: typing.ClassVar[DiagCode]
    RefTypeMismatch: typing.ClassVar[DiagCode]
    RegAfterNettype: typing.ClassVar[DiagCode]
    RepeatControlNotEvent: typing.ClassVar[DiagCode]
    RepeatNotNumeric: typing.ClassVar[DiagCode]
    ReplicationZeroOutsideConcat: typing.ClassVar[DiagCode]
    RestrictStmtNoFail: typing.ClassVar[DiagCode]
    ReturnInParallel: typing.ClassVar[DiagCode]
    ReturnNotInSubroutine: typing.ClassVar[DiagCode]
    ReversedValueRange: typing.ClassVar[DiagCode]
    SampledValueFuncClock: typing.ClassVar[DiagCode]
    SampledValueLocalVar: typing.ClassVar[DiagCode]
    SampledValueMatched: typing.ClassVar[DiagCode]
    ScopeIncompleteTypedef: typing.ClassVar[DiagCode]
    ScopeIndexOutOfRange: typing.ClassVar[DiagCode]
    ScopeNotIndexable: typing.ClassVar[DiagCode]
    ScopedClassCopy: typing.ClassVar[DiagCode]
    SelectAfterRangeSelect: typing.ClassVar[DiagCode]
    SelectEndianDynamic: typing.ClassVar[DiagCode]
    SelectEndianMismatch: typing.ClassVar[DiagCode]
    SelectOfVectoredNet: typing.ClassVar[DiagCode]
    SeqEmptyMatch: typing.ClassVar[DiagCode]
    SeqInstanceRepetition: typing.ClassVar[DiagCode]
    SeqMethodEndClock: typing.ClassVar[DiagCode]
    SeqMethodInputLocalVar: typing.ClassVar[DiagCode]
    SeqNoMatch: typing.ClassVar[DiagCode]
    SeqOnlyEmpty: typing.ClassVar[DiagCode]
    SeqRangeMinMax: typing.ClassVar[DiagCode]
    SequenceMatchedOutsideAssertion: typing.ClassVar[DiagCode]
    SequenceMethodLocalVar: typing.ClassVar[DiagCode]
    SignCompare: typing.ClassVar[DiagCode]
    SignConversion: typing.ClassVar[DiagCode]
    SignedIntegerOverflow: typing.ClassVar[DiagCode]
    SignednessNoEffect: typing.ClassVar[DiagCode]
    SingleBitVectored: typing.ClassVar[DiagCode]
    SolveBeforeDisallowed: typing.ClassVar[DiagCode]
    SpecifiersNotAllowed: typing.ClassVar[DiagCode]
    SpecifyBlockParam: typing.ClassVar[DiagCode]
    SpecifyPathBadReference: typing.ClassVar[DiagCode]
    SpecifyPathConditionExpr: typing.ClassVar[DiagCode]
    SpecifyPathMultiDim: typing.ClassVar[DiagCode]
    SpecparamInConstant: typing.ClassVar[DiagCode]
    SplitDistWeightOp: typing.ClassVar[DiagCode]
    StatementNotInLoop: typing.ClassVar[DiagCode]
    StaticAssert: typing.ClassVar[DiagCode]
    StaticConstNoInitializer: typing.ClassVar[DiagCode]
    StaticFuncSpecifier: typing.ClassVar[DiagCode]
    StaticInitOrder: typing.ClassVar[DiagCode]
    StaticInitValue: typing.ClassVar[DiagCode]
    StaticInitializerMustBeExplicit: typing.ClassVar[DiagCode]
    SubroutineMatchAutoRefArg: typing.ClassVar[DiagCode]
    SubroutineMatchNonVoid: typing.ClassVar[DiagCode]
    SubroutineMatchOutArg: typing.ClassVar[DiagCode]
    SubroutinePortInitializer: typing.ClassVar[DiagCode]
    SubroutinePrototypeScoped: typing.ClassVar[DiagCode]
    SuperNoBase: typing.ClassVar[DiagCode]
    SuperOutsideClass: typing.ClassVar[DiagCode]
    SysFuncHierarchicalNotAllowed: typing.ClassVar[DiagCode]
    SysFuncNotConst: typing.ClassVar[DiagCode]
    TaggedStruct: typing.ClassVar[DiagCode]
    TaggedUnionMissingInit: typing.ClassVar[DiagCode]
    TaggedUnionTarget: typing.ClassVar[DiagCode]
    TaskConstructor: typing.ClassVar[DiagCode]
    TaskFromFinal: typing.ClassVar[DiagCode]
    TaskFromFunction: typing.ClassVar[DiagCode]
    TaskInConstraint: typing.ClassVar[DiagCode]
    TaskReturnType: typing.ClassVar[DiagCode]
    ThroughoutLhsInvalid: typing.ClassVar[DiagCode]
    TimeScaleFirstInScope: typing.ClassVar[DiagCode]
    TimingCheckEventEdgeRequired: typing.ClassVar[DiagCode]
    TimingCheckEventNotAllowed: typing.ClassVar[DiagCode]
    TimingControlNotAllowed: typing.ClassVar[DiagCode]
    TimingInFuncNotAllowed: typing.ClassVar[DiagCode]
    TooFewArguments: typing.ClassVar[DiagCode]
    TooManyActualMacroArgs: typing.ClassVar[DiagCode]
    TooManyArguments: typing.ClassVar[DiagCode]
    TooManyEdgeDescriptors: typing.ClassVar[DiagCode]
    TooManyErrors: typing.ClassVar[DiagCode]
    TooManyForeachVars: typing.ClassVar[DiagCode]
    TooManyLexerErrors: typing.ClassVar[DiagCode]
    TooManyParamAssignments: typing.ClassVar[DiagCode]
    TooManyPortConnections: typing.ClassVar[DiagCode]
    TopModuleIfacePort: typing.ClassVar[DiagCode]
    TopModuleRefPort: typing.ClassVar[DiagCode]
    TopModuleUnnamedRefPort: typing.ClassVar[DiagCode]
    TypeHierarchical: typing.ClassVar[DiagCode]
    TypeIsNotAClass: typing.ClassVar[DiagCode]
    TypeRefDeclVar: typing.ClassVar[DiagCode]
    TypeRefHierarchical: typing.ClassVar[DiagCode]
    TypeRefVoid: typing.ClassVar[DiagCode]
    TypeRestrictionMismatch: typing.ClassVar[DiagCode]
    TypoIdentifier: typing.ClassVar[DiagCode]
    UTF8Char: typing.ClassVar[DiagCode]
    UdpAllX: typing.ClassVar[DiagCode]
    UdpCombState: typing.ClassVar[DiagCode]
    UdpCoverage: typing.ClassVar[DiagCode]
    UdpDupDiffOutput: typing.ClassVar[DiagCode]
    UdpDupTransition: typing.ClassVar[DiagCode]
    UdpEdgeInComb: typing.ClassVar[DiagCode]
    UdpInvalidEdgeSymbol: typing.ClassVar[DiagCode]
    UdpInvalidInputOnly: typing.ClassVar[DiagCode]
    UdpInvalidMinus: typing.ClassVar[DiagCode]
    UdpInvalidOutput: typing.ClassVar[DiagCode]
    UdpInvalidSymbol: typing.ClassVar[DiagCode]
    UdpInvalidTransition: typing.ClassVar[DiagCode]
    UdpSequentialState: typing.ClassVar[DiagCode]
    UdpSingleChar: typing.ClassVar[DiagCode]
    UdpTransSameChar: typing.ClassVar[DiagCode]
    UdpTransitionLength: typing.ClassVar[DiagCode]
    UdpWrongInputCount: typing.ClassVar[DiagCode]
    UnassignedVariable: typing.ClassVar[DiagCode]
    UnbalancedMacroArgDims: typing.ClassVar[DiagCode]
    UnboundedNotAllowed: typing.ClassVar[DiagCode]
    UnclosedTranslateOff: typing.ClassVar[DiagCode]
    UnconnectedArg: typing.ClassVar[DiagCode]
    UnconnectedNamedPort: typing.ClassVar[DiagCode]
    UnconnectedUnnamedPort: typing.ClassVar[DiagCode]
    UndeclaredButFoundPackage: typing.ClassVar[DiagCode]
    UndeclaredIdentifier: typing.ClassVar[DiagCode]
    UndefineBuiltinDirective: typing.ClassVar[DiagCode]
    UndrivenNet: typing.ClassVar[DiagCode]
    UndrivenPort: typing.ClassVar[DiagCode]
    UnexpectedClockingExpr: typing.ClassVar[DiagCode]
    UnexpectedConditionalDirective: typing.ClassVar[DiagCode]
    UnexpectedConstraintBlock: typing.ClassVar[DiagCode]
    UnexpectedEndDelim: typing.ClassVar[DiagCode]
    UnexpectedLetPortKeyword: typing.ClassVar[DiagCode]
    UnexpectedNameToken: typing.ClassVar[DiagCode]
    UnexpectedPortDecl: typing.ClassVar[DiagCode]
    UnexpectedQualifiers: typing.ClassVar[DiagCode]
    UnexpectedSelection: typing.ClassVar[DiagCode]
    UnexpectedWithClause: typing.ClassVar[DiagCode]
    UnicodeBOM: typing.ClassVar[DiagCode]
    UniquePriorityAfterElse: typing.ClassVar[DiagCode]
    UnknownClassMember: typing.ClassVar[DiagCode]
    UnknownClassOrPackage: typing.ClassVar[DiagCode]
    UnknownConstraintLiteral: typing.ClassVar[DiagCode]
    UnknownCovergroupBase: typing.ClassVar[DiagCode]
    UnknownCovergroupMember: typing.ClassVar[DiagCode]
    UnknownDiagPragmaArg: typing.ClassVar[DiagCode]
    UnknownDirective: typing.ClassVar[DiagCode]
    UnknownEscapeCode: typing.ClassVar[DiagCode]
    UnknownFormatSpecifier: typing.ClassVar[DiagCode]
    UnknownInterface: typing.ClassVar[DiagCode]
    UnknownLibrary: typing.ClassVar[DiagCode]
    UnknownMember: typing.ClassVar[DiagCode]
    UnknownModule: typing.ClassVar[DiagCode]
    UnknownPackage: typing.ClassVar[DiagCode]
    UnknownPackageMember: typing.ClassVar[DiagCode]
    UnknownPragma: typing.ClassVar[DiagCode]
    UnknownPrimitive: typing.ClassVar[DiagCode]
    UnknownProtectEncoding: typing.ClassVar[DiagCode]
    UnknownProtectKeyword: typing.ClassVar[DiagCode]
    UnknownProtectOption: typing.ClassVar[DiagCode]
    UnknownSystemMethod: typing.ClassVar[DiagCode]
    UnknownSystemName: typing.ClassVar[DiagCode]
    UnknownSystemTimingCheck: typing.ClassVar[DiagCode]
    UnknownWarningOption: typing.ClassVar[DiagCode]
    UnpackedArrayParamType: typing.ClassVar[DiagCode]
    UnpackedConcatAssociative: typing.ClassVar[DiagCode]
    UnpackedConcatSize: typing.ClassVar[DiagCode]
    UnpackedSigned: typing.ClassVar[DiagCode]
    UnrecognizedKeywordVersion: typing.ClassVar[DiagCode]
    UnresolvedForwardTypedef: typing.ClassVar[DiagCode]
    UnsignedArithShift: typing.ClassVar[DiagCode]
    UnsizedInConcat: typing.ClassVar[DiagCode]
    UnterminatedBlockComment: typing.ClassVar[DiagCode]
    UnusedArgument: typing.ClassVar[DiagCode]
    UnusedAssertionDecl: typing.ClassVar[DiagCode]
    UnusedButSetNet: typing.ClassVar[DiagCode]
    UnusedButSetPort: typing.ClassVar[DiagCode]
    UnusedButSetVariable: typing.ClassVar[DiagCode]
    UnusedConfigCell: typing.ClassVar[DiagCode]
    UnusedConfigInstance: typing.ClassVar[DiagCode]
    UnusedDefinition: typing.ClassVar[DiagCode]
    UnusedGenvar: typing.ClassVar[DiagCode]
    UnusedImplicitNet: typing.ClassVar[DiagCode]
    UnusedImport: typing.ClassVar[DiagCode]
    UnusedNet: typing.ClassVar[DiagCode]
    UnusedParameter: typing.ClassVar[DiagCode]
    UnusedPort: typing.ClassVar[DiagCode]
    UnusedPortDecl: typing.ClassVar[DiagCode]
    UnusedResult: typing.ClassVar[DiagCode]
    UnusedTypeParameter: typing.ClassVar[DiagCode]
    UnusedTypedef: typing.ClassVar[DiagCode]
    UnusedVariable: typing.ClassVar[DiagCode]
    UnusedWildcardImport: typing.ClassVar[DiagCode]
    UsedBeforeDeclared: typing.ClassVar[DiagCode]
    UselessCast: typing.ClassVar[DiagCode]
    UserDefPartialDriver: typing.ClassVar[DiagCode]
    UserDefPortMixedConcat: typing.ClassVar[DiagCode]
    UserDefPortTwoSided: typing.ClassVar[DiagCode]
    ValueExceedsMaxBitWidth: typing.ClassVar[DiagCode]
    ValueMustBeIntegral: typing.ClassVar[DiagCode]
    ValueMustBePositive: typing.ClassVar[DiagCode]
    ValueMustNotBeUnknown: typing.ClassVar[DiagCode]
    ValueOutOfRange: typing.ClassVar[DiagCode]
    ValueRangeUnbounded: typing.ClassVar[DiagCode]
    VarDeclWithDelay: typing.ClassVar[DiagCode]
    VarWithInterfacePort: typing.ClassVar[DiagCode]
    VectorLiteralOverflow: typing.ClassVar[DiagCode]
    VirtualArgCountMismatch: typing.ClassVar[DiagCode]
    VirtualArgDirectionMismatch: typing.ClassVar[DiagCode]
    VirtualArgNameMismatch: typing.ClassVar[DiagCode]
    VirtualArgNoDerivedDefault: typing.ClassVar[DiagCode]
    VirtualArgNoParentDefault: typing.ClassVar[DiagCode]
    VirtualArgTypeMismatch: typing.ClassVar[DiagCode]
    VirtualIfaceConfigRule: typing.ClassVar[DiagCode]
    VirtualIfaceDefparam: typing.ClassVar[DiagCode]
    VirtualIfaceHierRef: typing.ClassVar[DiagCode]
    VirtualIfaceIfacePort: typing.ClassVar[DiagCode]
    VirtualInterfaceIfaceMember: typing.ClassVar[DiagCode]
    VirtualInterfaceUnionMember: typing.ClassVar[DiagCode]
    VirtualKindMismatch: typing.ClassVar[DiagCode]
    VirtualReturnMismatch: typing.ClassVar[DiagCode]
    VirtualVisibilityMismatch: typing.ClassVar[DiagCode]
    VoidAssignment: typing.ClassVar[DiagCode]
    VoidCastFuncCall: typing.ClassVar[DiagCode]
    VoidNotAllowed: typing.ClassVar[DiagCode]
    WarnUnknownLibrary: typing.ClassVar[DiagCode]
    WarningTask: typing.ClassVar[DiagCode]
    WidthExpand: typing.ClassVar[DiagCode]
    WidthTruncate: typing.ClassVar[DiagCode]
    WildcardPortGenericIface: typing.ClassVar[DiagCode]
    WireDataType: typing.ClassVar[DiagCode]
    WithClauseNotAllowed: typing.ClassVar[DiagCode]
    WriteToInputClockVar: typing.ClassVar[DiagCode]
    WrongBindTargetDef: typing.ClassVar[DiagCode]
    WrongLanguageVersion: typing.ClassVar[DiagCode]
    WrongNumberAssignmentPatterns: typing.ClassVar[DiagCode]
    WrongSpecifyDelayCount: typing.ClassVar[DiagCode]

class DimensionKind(metaclass=_metaclass):
    AbbreviatedRange: ClassVar[DimensionKind]
    """Value = 2"""
    Associative: ClassVar[DimensionKind]
    """Value = 4"""
    DPIOpenArray: ClassVar[DimensionKind]
    """Value = 6"""
    Dynamic: ClassVar[DimensionKind]
    """Value = 3"""
    Queue: ClassVar[DimensionKind]
    """Value = 5"""
    Range: ClassVar[DimensionKind]
    """Value = 1"""
    Unknown: ClassVar[DimensionKind]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DimensionSpecifierSyntax(SyntaxNode):
    pass

class DirectiveSyntax(SyntaxNode):
    directive: Token

class DisableConstraintSyntax(ConstraintItemSyntax):
    disable: Token
    name: ExpressionSyntax
    semi: Token
    soft: Token

class DisableForkStatement(Statement):
    pass

class DisableForkStatementSyntax(StatementSyntax):
    disable: Token
    fork: Token
    semi: Token

class DisableIffAssertionExpr(AssertionExpr):
    @property
    def condition(self) -> Any: ...
    @property
    def expr(self) -> AssertionExpr: ...

class DisableIffSyntax(SyntaxNode):
    closeParen: Token
    disable: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token

class DisableSoftConstraint(Constraint):
    @property
    def target(self) -> Any: ...

class DisableStatement(Statement):
    @property
    def target(self) -> Expression: ...

class DisableStatementSyntax(StatementSyntax):
    disable: Token
    name: NameSyntax
    semi: Token

class DistConstraintListSyntax(SyntaxNode):
    closeBrace: Token
    dist: Token
    items: Any
    openBrace: Token

class DistExpression(Expression):
    class DistItem(metaclass=_metaclass):
        @property
        def value(self) -> Expression: ...
        @property
        def weight(self) -> DistExpression.DistWeight | None: ...

    class DistWeight(metaclass=_metaclass):
        class Kind(metaclass=_metaclass):
            PerRange: ClassVar[Self]
            """Value = 1"""
            PerValue: ClassVar[Self]
            """Value = 0"""

            __members__: dict[str, Self]

            def __int__(self) -> int: ...
            def __index__(self, index: int) -> Self: ...
            @property
            def name(self) -> str: ...
            @property
            def value(self) -> int: ...

        PerRange: Final = Kind.PerRange
        PerValue: Final = Kind.PerValue

        @property
        def expr(self) -> Expression: ...
        @property
        def kind(self) -> Any: ...

    @property
    def defaultWeight(self) -> Any: ...
    @property
    def items(self) -> list[Any]: ...
    @property
    def left(self) -> Expression: ...

class DistItemBaseSyntax(SyntaxNode):
    pass

class DistItemSyntax(DistItemBaseSyntax):
    range: ExpressionSyntax
    weight: DistWeightSyntax

class DistWeightSyntax(SyntaxNode):
    expr: ExpressionSyntax
    extraOp: Token
    op: Token

class DividerClauseSyntax(SyntaxNode):
    divide: Token
    value: Token

class DoWhileLoopStatement(Statement):
    @property
    def body(self) -> Statement: ...
    @property
    def cond(self) -> Expression: ...

class DoWhileStatementSyntax(StatementSyntax):
    closeParen: Token
    doKeyword: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    statement: StatementSyntax
    whileKeyword: Token

class DotMemberClauseSyntax(SyntaxNode):
    dot: Token
    member: Token

class DriveStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    comma: Token
    openParen: Token
    strength0: Token
    strength1: Token

class Driver(metaclass=_metaclass):
    languageVersion: LanguageVersion
    def __init__(self) -> None: ...
    def addStandardArgs(self) -> None: ...
    def createCompilation(self) -> Compilation: ...
    def createOptionBag(self) -> Any: ...
    def getDepfiles(self, includesOnly: bool = False) -> list[os.PathLike]: ...
    def parseAllSources(self) -> bool: ...
    def parseCommandLine(self, arg: str, parseOptions: CommandLineOptions = ...) -> bool: ...
    def processCommandFiles(
        self, fileName: str, makeRelative: bool, separateUnit: bool
    ) -> bool: ...
    def processOptions(self) -> bool: ...
    def reportCompilation(self, compilation: Compilation, quiet: bool) -> None: ...
    def reportDiagnostics(self, quiet: bool) -> bool: ...
    def reportMacros(self) -> None: ...
    def reportParseDiags(self) -> bool: ...
    def runAnalysis(self, compilation: Compilation) -> AnalysisManager: ...
    def runFullCompilation(self, quiet: bool = False) -> bool: ...
    def runPreprocessor(
        self,
        includeComments: bool,
        includeDirectives: bool,
        obfuscateIds: bool,
        useFixedObfuscationSeed: bool = False,
    ) -> bool: ...
    def serializeDepfiles(
        self, files: list[os.PathLike], depfileTarget: str | None = None
    ) -> str: ...
    @property
    def diagEngine(self) -> Any: ...
    @property
    def sourceLoader(self) -> Any: ...
    @property
    def sourceManager(self) -> Any: ...
    @property
    def syntaxTrees(self) -> list[Any]: ...
    @property
    def textDiagClient(self) -> Any: ...

class DynamicArrayType(Type):
    @property
    def elementType(self) -> Type: ...

class EdgeControlSpecifierSyntax(SyntaxNode):
    closeBracket: Token
    descriptors: Any
    openBracket: Token

class EdgeDescriptorSyntax(SyntaxNode):
    t1: Token
    t2: Token

class EdgeKind(metaclass=_metaclass):
    BothEdges: ClassVar[EdgeKind]
    """Value = 3"""
    NegEdge: ClassVar[EdgeKind]
    """Value = 2"""
    None_: ClassVar[EdgeKind]
    """Value = 0"""
    PosEdge: ClassVar[EdgeKind]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class EdgeSensitivePathSuffixSyntax(PathSuffixSyntax):
    closeParen: Token
    colon: Token
    expr: ExpressionSyntax
    openParen: Token
    outputs: Any
    polarityOperator: Token

class ElabSystemTaskKind(metaclass=_metaclass):
    Error: ClassVar[ElabSystemTaskKind]
    """Value = 1"""
    Fatal: ClassVar[ElabSystemTaskKind]
    """Value = 0"""
    Info: ClassVar[ElabSystemTaskKind]
    """Value = 3"""
    StaticAssert: ClassVar[ElabSystemTaskKind]
    """Value = 4"""
    Warning: ClassVar[ElabSystemTaskKind]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ElabSystemTaskSymbol(Symbol):
    @property
    def assertCondition(self) -> Expression: ...
    @property
    def message(self) -> str | None: ...
    @property
    def taskKind(self) -> ElabSystemTaskKind: ...

class ElabSystemTaskSyntax(MemberSyntax):
    arguments: ArgumentListSyntax
    name: Token
    semi: Token

class ElementSelectExpression(Expression):
    @property
    def selector(self) -> Expression: ...
    @property
    def value(self) -> Expression: ...

class ElementSelectExpressionSyntax(ExpressionSyntax):
    left: ExpressionSyntax
    select: ElementSelectSyntax

class ElementSelectSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax

class ElseClauseSyntax(SyntaxNode):
    clause: SyntaxNode
    elseKeyword: Token

class ElseConstraintClauseSyntax(SyntaxNode):
    constraints: ConstraintItemSyntax
    elseKeyword: Token

class ElsePropertyClauseSyntax(SyntaxNode):
    elseKeyword: Token
    expr: PropertyExprSyntax

class EmptyArgumentExpression(Expression):
    pass

class EmptyArgumentSyntax(ArgumentSyntax):
    placeholder: Token

class EmptyIdentifierNameSyntax(NameSyntax):
    placeholder: Token

class EmptyMemberSymbol(Symbol):
    pass

class EmptyMemberSyntax(MemberSyntax):
    qualifiers: Any
    semi: Token

class EmptyNonAnsiPortSyntax(NonAnsiPortSyntax):
    placeholder: Token

class EmptyPortConnectionSyntax(PortConnectionSyntax):
    placeholder: Token

class EmptyQueueExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    openBrace: Token

class EmptyStatement(Statement):
    pass

class EmptyStatementSyntax(StatementSyntax):
    semicolon: Token

class EmptyTimingCheckArgSyntax(TimingCheckArgSyntax):
    placeholder: Token

class EnumType(IntegralType, Scope):
    @property
    def baseType(self) -> Type: ...
    @property
    def systemId(self) -> int: ...

class EnumTypeSyntax(DataTypeSyntax):
    baseType: DataTypeSyntax
    closeBrace: Token
    dimensions: Any
    keyword: Token
    members: Any
    openBrace: Token

class EnumValueSymbol(ValueSymbol):
    @property
    def value(self) -> ConstantValue: ...

class EqualsAssertionArgClauseSyntax(SyntaxNode):
    equals: Token
    expr: PropertyExprSyntax

class EqualsTypeClauseSyntax(SyntaxNode):
    equals: Token
    type: DataTypeSyntax

class EqualsValueClauseSyntax(SyntaxNode):
    equals: Token
    expr: ExpressionSyntax

class ErrorType(Type):
    pass

class EvalContext(metaclass=_metaclass):
    class Frame(metaclass=_metaclass):
        @property
        def callLocation(self) -> Any: ...
        @property
        def lookupLocation(self) -> Any: ...
        @property
        def subroutine(self) -> Any: ...
        @property
        def temporaries(self) -> dict[Any, Any]: ...

    queueTarget: Any
    def __init__(self, astCtx: Any, flags: EvalFlags = ...) -> None: ...
    def createLocal(self, symbol: Any, value: Any = None) -> Any: ...
    def deleteLocal(self, symbol: Any) -> None: ...
    def dumpStack(self) -> str: ...
    def findLocal(self, symbol: Any) -> Any: ...
    def popFrame(self) -> None: ...
    def popLValue(self) -> None: ...
    def pushEmptyFrame(self) -> None: ...
    def pushFrame(self, subroutine: Any, callLocation: Any, lookupLocation: Any) -> bool: ...
    def pushLValue(self, lval: Any) -> None: ...
    def setDisableTarget(self, arg0: Any, arg1: Any) -> None: ...
    def step(self, loc: Any) -> bool: ...
    @property
    def cacheResults(self) -> bool: ...
    @property
    def diagnostics(self) -> Any: ...
    @property
    def disableRange(self) -> Any: ...
    @property
    def disableTarget(self) -> Any: ...
    @property
    def flags(self) -> EvalFlags: ...
    @property
    def inFunction(self) -> bool: ...
    @property
    def topFrame(self) -> Any: ...
    @property
    def topLValue(self) -> Any: ...

class EvalResult(metaclass=_metaclass):
    Break: ClassVar[EvalResult]
    """Value = 3"""
    Continue: ClassVar[EvalResult]
    """Value = 4"""
    Disable: ClassVar[EvalResult]
    """Value = 5"""
    Fail: ClassVar[EvalResult]
    """Value = 0"""
    Return: ClassVar[EvalResult]
    """Value = 2"""
    Success: ClassVar[EvalResult]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class EvaluatedDimension(metaclass=_metaclass):
    @property
    def associativeType(self) -> Any: ...
    @property
    def isRange(self) -> bool: ...
    @property
    def kind(self) -> DimensionKind: ...
    @property
    def queueMaxSize(self) -> int: ...
    @property
    def range(self) -> Any: ...

class EventControlSyntax(TimingControlSyntax):
    at: Token
    eventName: ExpressionSyntax

class EventControlWithExpressionSyntax(TimingControlSyntax):
    at: Token
    expr: EventExpressionSyntax

class EventExpressionSyntax(SequenceExprSyntax):
    pass

class EventListControl(TimingControl):
    @property
    def events(self) -> list[TimingControl]: ...

class EventTriggerStatement(Statement):
    @property
    def isNonBlocking(self) -> bool: ...
    @property
    def target(self) -> Expression: ...
    @property
    def timing(self) -> TimingControl: ...

class EventTriggerStatementSyntax(StatementSyntax):
    name: NameSyntax
    semi: Token
    timing: TimingControlSyntax
    trigger: Token

class EventType(Type):
    pass

class ExplicitAnsiPortSyntax(MemberSyntax):
    closeParen: Token
    direction: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token

class ExplicitImportSymbol(Symbol):
    @property
    def importName(self) -> str: ...
    @property
    def importedSymbol(self) -> Symbol: ...
    @property
    def isFromExport(self) -> bool: ...
    @property
    def package(self) -> PackageSymbol: ...
    @property
    def packageName(self) -> str: ...

class ExplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    closeParen: Token
    dot: Token
    expr: PortExpressionSyntax
    name: Token
    openParen: Token

class Expression(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    def eval(self, context: EvalContext) -> Any: ...
    def evalLValue(self, context: EvalContext) -> LValue: ...
    def getSymbolReference(self, allowPacked: bool = True) -> Any: ...
    def isImplicitlyAssignableTo(self, compilation: Compilation, type: Any) -> bool: ...
    def visit(self, f: typing.Any) -> None:
        """Visit a pyslang object with a callback function `f`.
        The callback function `f` should take a single argument, which is the current node being
            visited.
        The return value of `f` determines the next node to visit.
        If `f` ever returns `pyslang.VisitAction.Interrupt`, the visit is aborted and no additional
            nodes are visited.
        If `f` returns `pyslang.VisitAction.Skip`, then no child nodes of the current node are
            visited. For any other return value, including `pyslang.VisitAction.Advance`,
            the return value is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool: ...
    @property
    def constant(self) -> Any: ...
    @property
    def effectiveWidth(self) -> int | None: ...
    @property
    def hasHierarchicalReference(self) -> bool: ...
    @property
    def isImplicitString(self) -> bool: ...
    @property
    def isUnsizedInteger(self) -> bool: ...
    @property
    def kind(self) -> ExpressionKind: ...
    @property
    def sourceRange(self) -> Any: ...
    @property
    def syntax(self) -> Any: ...
    @property
    def type(self) -> Any: ...

class ExpressionConstraint(Constraint):
    @property
    def expr(self) -> Any: ...
    @property
    def isSoft(self) -> bool: ...

class ExpressionConstraintSyntax(ConstraintItemSyntax):
    expr: ExpressionSyntax
    semi: Token
    soft: Token

class ExpressionCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    expr: ExpressionSyntax

class ExpressionKind(metaclass=_metaclass):
    ArbitrarySymbol: ClassVar[ExpressionKind]
    """Value = 25"""
    AssertionInstance: ClassVar[ExpressionKind]
    """Value = 39"""
    Assignment: ClassVar[ExpressionKind]
    """Value = 14"""
    BinaryOp: ClassVar[ExpressionKind]
    """Value = 11"""
    Call: ClassVar[ExpressionKind]
    """Value = 21"""
    ClockingEvent: ClassVar[ExpressionKind]
    """Value = 38"""
    Concatenation: ClassVar[ExpressionKind]
    """Value = 15"""
    ConditionalOp: ClassVar[ExpressionKind]
    """Value = 12"""
    Conversion: ClassVar[ExpressionKind]
    """Value = 22"""
    CopyClass: ClassVar[ExpressionKind]
    """Value = 36"""
    DataType: ClassVar[ExpressionKind]
    """Value = 23"""
    Dist: ClassVar[ExpressionKind]
    """Value = 32"""
    ElementSelect: ClassVar[ExpressionKind]
    """Value = 18"""
    EmptyArgument: ClassVar[ExpressionKind]
    """Value = 30"""
    HierarchicalValue: ClassVar[ExpressionKind]
    """Value = 9"""
    Inside: ClassVar[ExpressionKind]
    """Value = 13"""
    IntegerLiteral: ClassVar[ExpressionKind]
    """Value = 1"""
    Invalid: ClassVar[ExpressionKind]
    """Value = 0"""
    LValueReference: ClassVar[ExpressionKind]
    """Value = 26"""
    MemberAccess: ClassVar[ExpressionKind]
    """Value = 20"""
    MinTypMax: ClassVar[ExpressionKind]
    """Value = 37"""
    NamedValue: ClassVar[ExpressionKind]
    """Value = 8"""
    NewArray: ClassVar[ExpressionKind]
    """Value = 33"""
    NewClass: ClassVar[ExpressionKind]
    """Value = 34"""
    NewCovergroup: ClassVar[ExpressionKind]
    """Value = 35"""
    NullLiteral: ClassVar[ExpressionKind]
    """Value = 5"""
    RangeSelect: ClassVar[ExpressionKind]
    """Value = 19"""
    RealLiteral: ClassVar[ExpressionKind]
    """Value = 2"""
    ReplicatedAssignmentPattern: ClassVar[ExpressionKind]
    """Value = 29"""
    Replication: ClassVar[ExpressionKind]
    """Value = 16"""
    SimpleAssignmentPattern: ClassVar[ExpressionKind]
    """Value = 27"""
    Streaming: ClassVar[ExpressionKind]
    """Value = 17"""
    StringLiteral: ClassVar[ExpressionKind]
    """Value = 7"""
    StructuredAssignmentPattern: ClassVar[ExpressionKind]
    """Value = 28"""
    TaggedUnion: ClassVar[ExpressionKind]
    """Value = 40"""
    TimeLiteral: ClassVar[ExpressionKind]
    """Value = 3"""
    TypeReference: ClassVar[ExpressionKind]
    """Value = 24"""
    UnaryOp: ClassVar[ExpressionKind]
    """Value = 10"""
    UnbasedUnsizedIntegerLiteral: ClassVar[ExpressionKind]
    """Value = 4"""
    UnboundedLiteral: ClassVar[ExpressionKind]
    """Value = 6"""
    ValueRange: ClassVar[ExpressionKind]
    """Value = 31"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ExpressionOrDistSyntax(ExpressionSyntax):
    distribution: DistConstraintListSyntax
    expr: ExpressionSyntax

class ExpressionPatternSyntax(PatternSyntax):
    expr: ExpressionSyntax

class ExpressionStatement(Statement):
    @property
    def expr(self) -> Expression: ...

class ExpressionStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    semi: Token

class ExpressionSyntax(SyntaxNode):
    pass

class ExpressionTimingCheckArgSyntax(TimingCheckArgSyntax):
    expr: ExpressionSyntax

class ExtendsClauseSyntax(SyntaxNode):
    arguments: ArgumentListSyntax
    baseName: NameSyntax
    defaultedArg: DefaultExtendsClauseArgSyntax
    keyword: Token

class ExternInterfaceMethodSyntax(MemberSyntax):
    externKeyword: Token
    forkJoin: Token
    prototype: FunctionPrototypeSyntax
    semi: Token

class ExternModuleDeclSyntax(MemberSyntax):
    actualAttributes: Any
    externKeyword: Token
    header: ModuleHeaderSyntax

class ExternUdpDeclSyntax(MemberSyntax):
    actualAttributes: Any
    externKeyword: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token

class FieldSymbol(VariableSymbol):
    @property
    def bitOffset(self) -> int: ...
    @property
    def fieldIndex(self) -> int: ...
    @property
    def randMode(self) -> RandMode: ...

class FilePathSpecSyntax(SyntaxNode):
    path: Token

class FirstMatchAssertionExpr(AssertionExpr):
    @property
    def matchItems(self) -> list[Any]: ...
    @property
    def seq(self) -> AssertionExpr: ...

class FirstMatchSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    first_match: Token
    matchList: SequenceMatchListSyntax
    openParen: Token

class FixedSizeUnpackedArrayType(Type):
    @property
    def elementType(self) -> Type: ...
    @property
    def range(self) -> ConstantRange: ...

class FloatingType(Type):
    class Kind(metaclass=_metaclass):
        Real: ClassVar[Self]
        """Value = 0"""
        RealTime: ClassVar[Self]
        """Value = 2"""
        ShortReal: ClassVar[Self]
        """Value = 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Real: Final = Kind.Real
    RealTime: Final = Kind.RealTime
    ShortReal: Final = Kind.ShortReal

    @property
    def floatKind(self) -> Any: ...

class ForLoopStatement(Statement):
    @property
    def body(self) -> Statement: ...
    @property
    def initializers(self) -> list[Expression]: ...
    @property
    def loopVars(self) -> list[Any]: ...
    @property
    def steps(self) -> list[Expression]: ...
    @property
    def stopExpr(self) -> Expression: ...

class ForLoopStatementSyntax(StatementSyntax):
    closeParen: Token
    forKeyword: Token
    initializers: Any
    openParen: Token
    semi1: Token
    semi2: Token
    statement: StatementSyntax
    steps: Any
    stopExpr: ExpressionSyntax

class ForVariableDeclarationSyntax(SyntaxNode):
    declarator: DeclaratorSyntax
    type: DataTypeSyntax
    varKeyword: Token

class ForeachConstraint(Constraint):
    @property
    def arrayRef(self) -> Any: ...
    @property
    def body(self) -> Constraint: ...
    @property
    def loopDims(self) -> list[Any]: ...

class ForeachLoopListSyntax(SyntaxNode):
    arrayName: NameSyntax
    closeBracket: Token
    closeParen: Token
    loopVariables: Any
    openBracket: Token
    openParen: Token

class ForeachLoopStatement(Statement):
    class LoopDim(metaclass=_metaclass):
        @property
        def loopVar(self) -> Any: ...
        @property
        def range(self) -> ConstantRange | None: ...

    @property
    def arrayRef(self) -> Expression: ...
    @property
    def body(self) -> Statement: ...
    @property
    def loopDims(self) -> list[Any]: ...

class ForeachLoopStatementSyntax(StatementSyntax):
    keyword: Token
    loopList: ForeachLoopListSyntax
    statement: StatementSyntax

class ForeverLoopStatement(Statement):
    @property
    def body(self) -> Statement: ...

class ForeverStatementSyntax(StatementSyntax):
    foreverKeyword: Token
    statement: StatementSyntax

class FormalArgumentSymbol(VariableSymbol):
    @property
    def defaultValue(self) -> Expression: ...
    @property
    def direction(self) -> ArgumentDirection: ...

class ForwardTypeRestriction(metaclass=_metaclass):
    Class: ClassVar[ForwardTypeRestriction]
    """Value = 4"""
    Enum: ClassVar[ForwardTypeRestriction]
    """Value = 1"""
    InterfaceClass: ClassVar[ForwardTypeRestriction]
    """Value = 5"""
    None_: ClassVar[ForwardTypeRestriction]
    """Value = 0"""
    Struct: ClassVar[ForwardTypeRestriction]
    """Value = 2"""
    Union: ClassVar[ForwardTypeRestriction]
    """Value = 3"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ForwardTypeRestrictionSyntax(SyntaxNode):
    keyword1: Token
    keyword2: Token

class ForwardTypedefDeclarationSyntax(MemberSyntax):
    name: Token
    semi: Token
    typeRestriction: ForwardTypeRestrictionSyntax
    typedefKeyword: Token

class ForwardingTypedefSymbol(Symbol):
    @property
    def nextForwardDecl(self) -> ForwardingTypedefSymbol: ...
    @property
    def typeRestriction(self) -> ForwardTypeRestriction: ...
    @property
    def visibility(self) -> Visibility | None: ...

class FunctionDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: Any
    prototype: FunctionPrototypeSyntax
    semi: Token

class FunctionPortBaseSyntax(SyntaxNode):
    pass

class FunctionPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: Any

class FunctionPortSyntax(FunctionPortBaseSyntax):
    attributes: Any
    constKeyword: Token
    dataType: DataTypeSyntax
    declarator: DeclaratorSyntax
    direction: Token
    staticKeyword: Token
    varKeyword: Token

class FunctionPrototypeSyntax(SyntaxNode):
    keyword: Token
    lifetime: Token
    name: NameSyntax
    portList: FunctionPortListSyntax
    returnType: DataTypeSyntax
    specifiers: Any

class GenerateBlockArraySymbol(Symbol, Scope):
    @property
    def constructIndex(self) -> int: ...
    @property
    def entries(self) -> list[GenerateBlockSymbol]: ...
    @property
    def externalName(self) -> str: ...
    @property
    def valid(self) -> bool: ...

class GenerateBlockSymbol(Symbol, Scope):
    @property
    def arrayIndex(self) -> SVInt: ...
    @property
    def constructIndex(self) -> int: ...
    @property
    def externalName(self) -> str: ...
    @property
    def isUninstantiated(self) -> bool: ...

class GenerateBlockSyntax(MemberSyntax):
    begin: Token
    beginName: NamedBlockClauseSyntax
    end: Token
    endName: NamedBlockClauseSyntax
    label: NamedLabelSyntax
    members: Any

class GenerateRegionSyntax(MemberSyntax):
    endgenerate: Token
    keyword: Token
    members: Any

class GenericClassDefSymbol(Symbol):
    @property
    def defaultSpecialization(self) -> Type: ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol: ...
    @property
    def invalidSpecialization(self) -> Type: ...
    @property
    def isInterface(self) -> bool: ...

class GenvarDeclarationSyntax(MemberSyntax):
    identifiers: Any
    keyword: Token
    semi: Token

class GenvarSymbol(Symbol):
    pass

class HierarchicalInstanceSyntax(SyntaxNode):
    closeParen: Token
    connections: Any
    decl: InstanceNameSyntax
    openParen: Token

class HierarchicalValueExpression(ValueExpressionBase):
    pass

class HierarchyInstantiationSyntax(MemberSyntax):
    instances: Any
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: Token

class IdWithExprCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    id: Token
    withClause: WithClauseSyntax

class IdentifierNameSyntax(NameSyntax):
    identifier: Token

class IdentifierSelectNameSyntax(NameSyntax):
    identifier: Token
    selectors: Any

class IfGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElseClauseSyntax
    keyword: Token
    openParen: Token

class IfNonePathDeclarationSyntax(MemberSyntax):
    keyword: Token
    path: PathDeclarationSyntax

class IffEventClauseSyntax(SyntaxNode):
    expr: ExpressionSyntax
    iff: Token

class ImmediateAssertionMemberSyntax(MemberSyntax):
    statement: ImmediateAssertionStatementSyntax

class ImmediateAssertionStatement(Statement):
    @property
    def assertionKind(self) -> AssertionKind: ...
    @property
    def cond(self) -> Expression: ...
    @property
    def ifFalse(self) -> Statement: ...
    @property
    def ifTrue(self) -> Statement: ...
    @property
    def isDeferred(self) -> bool: ...
    @property
    def isFinal(self) -> bool: ...

class ImmediateAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    delay: DeferredAssertionSyntax
    expr: ParenthesizedExpressionSyntax
    keyword: Token

class ImplementsClauseSyntax(SyntaxNode):
    interfaces: Any
    keyword: Token

class ImplicationConstraint(Constraint):
    @property
    def body(self) -> Constraint: ...
    @property
    def predicate(self) -> Any: ...

class ImplicationConstraintSyntax(ConstraintItemSyntax):
    arrow: Token
    constraints: ConstraintItemSyntax
    left: ExpressionSyntax

class ImplicitAnsiPortSyntax(MemberSyntax):
    declarator: DeclaratorSyntax
    header: PortHeaderSyntax

class ImplicitEventControl(TimingControl):
    pass

class ImplicitEventControlSyntax(TimingControlSyntax):
    at: Token
    closeParen: Token
    openParen: Token
    star: Token

class ImplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    expr: PortExpressionSyntax

class ImplicitTypeSyntax(DataTypeSyntax):
    dimensions: Any
    placeholder: Token
    signing: Token

class IncludeDirectiveSyntax(DirectiveSyntax):
    fileName: Token

class IncludeMetadata(metaclass=_metaclass):
    def __init__(self) -> None: ...
    @property
    def buffer(self) -> SourceBuffer: ...
    @property
    def isSystem(self) -> bool: ...
    @property
    def path(self) -> str: ...
    @property
    def syntax(self) -> Any: ...

class InsideExpression(Expression):
    @property
    def left(self) -> Expression: ...
    @property
    def rangeList(self) -> list[Expression]: ...

class InsideExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    inside: Token
    ranges: RangeListSyntax

class InstanceArraySymbol(Symbol, Scope):
    @property
    def arrayName(self) -> str: ...
    @property
    def elements(self) -> list[Symbol]: ...
    @property
    def range(self) -> ConstantRange: ...

class InstanceBodySymbol(Symbol, Scope):
    def findPort(self, portName: str) -> Symbol: ...
    def hasSameType(self, other: InstanceBodySymbol) -> bool: ...
    @property
    def definition(self) -> DefinitionSymbol: ...
    @property
    def parameters(self) -> list[ParameterSymbolBase]: ...
    @property
    def parentInstance(self) -> InstanceSymbol: ...
    @property
    def portList(self) -> list[Symbol]: ...

class InstanceConfigRuleSyntax(ConfigRuleSyntax):
    instance: Token
    instanceNames: Any
    ruleClause: ConfigRuleClauseSyntax
    semi: Token
    topModule: Token

class InstanceNameSyntax(SyntaxNode):
    dimensions: Any
    name: Token

class InstanceSymbol(InstanceSymbolBase):
    @typing.overload
    def getPortConnection(self, port: PortSymbol) -> PortConnection: ...
    @typing.overload
    def getPortConnection(self, port: MultiPortSymbol) -> PortConnection: ...
    @typing.overload
    def getPortConnection(self, port: InterfacePortSymbol) -> PortConnection: ...
    @property
    def body(self) -> Any: ...
    @property
    def canonicalBody(self) -> Any: ...
    @property
    def definition(self) -> DefinitionSymbol: ...
    @property
    def isInterface(self) -> bool: ...
    @property
    def isModule(self) -> bool: ...
    @property
    def portConnections(self) -> list[PortConnection]: ...

class InstanceSymbolBase(Symbol):
    @property
    def arrayName(self) -> str: ...
    @property
    def arrayPath(self) -> list[int]: ...

class IntegerLiteral(Expression):
    @property
    def isDeclaredUnsized(self) -> bool: ...
    @property
    def value(self) -> Any: ...

class IntegerTypeSyntax(DataTypeSyntax):
    dimensions: Any
    keyword: Token
    signing: Token

class IntegerVectorExpressionSyntax(PrimaryExpressionSyntax):
    base: Token
    size: Token
    value: Token

class IntegralFlags(metaclass=_metaclass):
    FourState: ClassVar[IntegralFlags]
    """Value = 2"""
    Reg: ClassVar[IntegralFlags]
    """Value = 4"""
    Signed: ClassVar[IntegralFlags]
    """Value = 1"""
    TwoState: ClassVar[IntegralFlags]
    """Value = 0"""
    Unsigned: ClassVar[IntegralFlags]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class IntegralType(Type):
    def getBitVectorRange(self) -> ConstantRange: ...
    def isDeclaredReg(self) -> bool: ...

class InterfacePortHeaderSyntax(PortHeaderSyntax):
    modport: DotMemberClauseSyntax
    nameOrKeyword: Token

class InterfacePortSymbol(Symbol):
    @property
    def connection(self) -> tuple[Symbol, ...]: ...
    @property
    def declaredRange(self) -> list[ConstantRange] | None: ...
    @property
    def interfaceDef(self) -> DefinitionSymbol: ...
    @property
    def isGeneric(self) -> bool: ...
    @property
    def isInvalid(self) -> bool: ...
    @property
    def modport(self) -> str: ...

class IntersectClauseSyntax(SyntaxNode):
    intersect: Token
    ranges: RangeListSyntax

class InvalidAssertionExpr(AssertionExpr):
    pass

class InvalidBinsSelectExpr(BinsSelectExpr):
    pass

class InvalidConstraint(Constraint):
    pass

class InvalidExpression(Expression):
    pass

class InvalidPattern(Pattern):
    pass

class InvalidStatement(Statement):
    pass

class InvalidTimingControl(TimingControl):
    pass

class InvocationExpressionSyntax(ExpressionSyntax):
    arguments: ArgumentListSyntax
    attributes: Any
    left: ExpressionSyntax

class IteratorSymbol(TempVarSymbol):
    pass

class JumpStatementSyntax(StatementSyntax):
    breakOrContinue: Token
    semi: Token

class KeywordNameSyntax(NameSyntax):
    keyword: Token

class KeywordTypeSyntax(DataTypeSyntax):
    keyword: Token

class KnownSystemName(metaclass=_metaclass):
    Unknown: ClassVar[KnownSystemName]
    """Value = 0"""
    # and: ClassVar[KnownSystemName]
    """Value = 239"""
    atobin: ClassVar[KnownSystemName]
    """Value = 277"""
    atohex: ClassVar[KnownSystemName]
    """Value = 275"""
    atoi: ClassVar[KnownSystemName]
    """Value = 274"""
    atooct: ClassVar[KnownSystemName]
    """Value = 276"""
    atoreal: ClassVar[KnownSystemName]
    """Value = 278"""
    bintoa: ClassVar[KnownSystemName]
    """Value = 282"""
    compare: ClassVar[KnownSystemName]
    """Value = 272"""
    constraint_mode: ClassVar[KnownSystemName]
    """Value = 285"""
    delete: ClassVar[KnownSystemName]
    """Value = 232"""
    exists: ClassVar[KnownSystemName]
    """Value = 233"""
    find: ClassVar[KnownSystemName]
    """Value = 243"""
    find_first: ClassVar[KnownSystemName]
    """Value = 245"""
    find_first_index: ClassVar[KnownSystemName]
    """Value = 246"""
    find_index: ClassVar[KnownSystemName]
    """Value = 244"""
    find_last: ClassVar[KnownSystemName]
    """Value = 247"""
    find_last_index: ClassVar[KnownSystemName]
    """Value = 248"""
    first: ClassVar[KnownSystemName]
    """Value = 257"""
    getc: ClassVar[KnownSystemName]
    """Value = 268"""
    hextoa: ClassVar[KnownSystemName]
    """Value = 280"""
    icompare: ClassVar[KnownSystemName]
    """Value = 273"""
    index: ClassVar[KnownSystemName]
    """Value = 235"""
    insert: ClassVar[KnownSystemName]
    """Value = 234"""
    itoa: ClassVar[KnownSystemName]
    """Value = 279"""
    last: ClassVar[KnownSystemName]
    """Value = 258"""
    len: ClassVar[KnownSystemName]
    """Value = 266"""
    map: ClassVar[KnownSystemName]
    """Value = 236"""
    matched: ClassVar[KnownSystemName]
    """Value = 63"""
    max: ClassVar[KnownSystemName]
    """Value = 250"""
    min: ClassVar[KnownSystemName]
    """Value = 249"""
    # name: ClassVar[KnownSystemName]
    """Value = 265"""
    next: ClassVar[KnownSystemName]
    """Value = 259"""
    num: ClassVar[KnownSystemName]
    """Value = 256"""
    octtoa: ClassVar[KnownSystemName]
    """Value = 281"""
    # or: ClassVar[KnownSystemName]
    """Value = 238"""
    pop_back: ClassVar[KnownSystemName]
    """Value = 262"""
    pop_front: ClassVar[KnownSystemName]
    """Value = 261"""
    prev: ClassVar[KnownSystemName]
    """Value = 260"""
    product: ClassVar[KnownSystemName]
    """Value = 242"""
    push_back: ClassVar[KnownSystemName]
    """Value = 264"""
    push_front: ClassVar[KnownSystemName]
    """Value = 263"""
    putc: ClassVar[KnownSystemName]
    """Value = 267"""
    rand_mode: ClassVar[KnownSystemName]
    """Value = 284"""
    randomize: ClassVar[KnownSystemName]
    """Value = 61"""
    realtoa: ClassVar[KnownSystemName]
    """Value = 283"""
    reverse: ClassVar[KnownSystemName]
    """Value = 231"""
    rsort: ClassVar[KnownSystemName]
    """Value = 254"""
    shuffle: ClassVar[KnownSystemName]
    """Value = 255"""
    size: ClassVar[KnownSystemName]
    """Value = 237"""
    sort: ClassVar[KnownSystemName]
    """Value = 253"""
    substr: ClassVar[KnownSystemName]
    """Value = 269"""
    sum: ClassVar[KnownSystemName]
    """Value = 241"""
    tolower: ClassVar[KnownSystemName]
    """Value = 271"""
    toupper: ClassVar[KnownSystemName]
    """Value = 270"""
    triggered: ClassVar[KnownSystemName]
    """Value = 62"""
    unique: ClassVar[KnownSystemName]
    """Value = 251"""
    unique_index: ClassVar[KnownSystemName]
    """Value = 252"""
    xor: ClassVar[KnownSystemName]
    """Value = 240"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LValue(metaclass=_metaclass):
    def __init__(self) -> None: ...
    def bad(self) -> bool: ...
    def load(self) -> Any: ...
    def resolve(self) -> Any: ...
    def store(self, value: Any) -> None: ...

class LValueReferenceExpression(Expression):
    pass

class LanguageVersion(metaclass=_metaclass):
    Default: ClassVar[LanguageVersion]
    """Value = 0"""
    v1800_2017: ClassVar[LanguageVersion]
    """Value = 0"""
    v1800_2023: ClassVar[LanguageVersion]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LetDeclSymbol(Symbol, Scope):
    @property
    def ports(self) -> list[AssertionPortSymbol]: ...

class LetDeclarationSyntax(MemberSyntax):
    equals: Token
    expr: ExpressionSyntax
    identifier: Token
    let: Token
    portList: AssertionItemPortListSyntax
    semi: Token

class LexerOptions(metaclass=_metaclass):
    languageVersion: LanguageVersion
    maxErrors: int
    def __init__(self) -> None: ...

class LibraryDeclarationSyntax(MemberSyntax):
    filePaths: Any
    incDirClause: LibraryIncDirClauseSyntax
    library: Token
    name: Token
    semi: Token

class LibraryIncDirClauseSyntax(SyntaxNode):
    filePaths: Any
    incdir: Token
    minus: Token

class LibraryIncludeStatementSyntax(MemberSyntax):
    filePath: FilePathSpecSyntax
    include: Token
    semi: Token

class LibraryMapSyntax(SyntaxNode):
    endOfFile: Token
    members: Any

class LineDirectiveSyntax(DirectiveSyntax):
    fileName: Token
    level: Token
    lineNumber: Token

class LiteralBase(metaclass=_metaclass):
    Binary: ClassVar[LiteralBase]
    """Value = 0"""
    Decimal: ClassVar[LiteralBase]
    """Value = 2"""
    Hex: ClassVar[LiteralBase]
    """Value = 3"""
    Octal: ClassVar[LiteralBase]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LiteralExpressionSyntax(PrimaryExpressionSyntax):
    literal: Token

class LocalAssertionVarSymbol(VariableSymbol):
    pass

class LocalVariableDeclarationSyntax(MemberSyntax):
    declarators: Any
    semi: Token
    type: DataTypeSyntax
    var: Token

class Lookup(metaclass=_metaclass):
    @staticmethod
    def ensureAccessible(
        symbol: Any, context: ASTContext, sourceRange: SourceRange | None
    ) -> bool: ...
    @staticmethod
    def ensureVisible(
        symbol: Any, context: ASTContext, sourceRange: SourceRange | None
    ) -> bool: ...
    @staticmethod
    def findAssertionLocalVar(context: ASTContext, name: Any, result: LookupResult) -> bool: ...
    @staticmethod
    def findClass(
        name: Any, context: ASTContext, requireInterfaceClass: DiagCode | None = None
    ) -> Any: ...
    @staticmethod
    def findTempVar(scope: Any, symbol: Any, name: Any, result: LookupResult) -> bool: ...
    @staticmethod
    def getContainingClass(scope: Any) -> tuple[Any, bool]: ...
    @staticmethod
    def getVisibility(symbol: Any) -> Visibility: ...
    @staticmethod
    def isAccessibleFrom(target: Any, sourceScope: Any) -> bool: ...
    @staticmethod
    def isVisibleFrom(symbol: Any, scope: Any) -> bool: ...
    @staticmethod
    def name(
        syntax: Any, context: ASTContext, flags: LookupFlags, result: LookupResult
    ) -> None: ...
    @staticmethod
    def unqualified(scope: Any, name: str, flags: LookupFlags = ...) -> Any: ...
    @staticmethod
    def unqualifiedAt(
        scope: Any,
        name: str,
        location: LookupLocation,
        sourceRange: SourceRange,
        flags: LookupFlags = ...,
    ) -> Any: ...
    @staticmethod
    def withinClassRandomize(
        context: ASTContext, syntax: Any, flags: LookupFlags, result: LookupResult
    ) -> bool: ...

class LookupFlags(metaclass=_metaclass):
    AllowDeclaredAfter: ClassVar[LookupFlags]
    """Value = 2"""
    AllowIncompleteForwardTypedefs: ClassVar[LookupFlags]
    """Value = 32"""
    AllowRoot: ClassVar[LookupFlags]
    """Value = 256"""
    AllowUnit: ClassVar[LookupFlags]
    """Value = 512"""
    AlwaysAllowUpward: ClassVar[LookupFlags]
    """Value = 8192"""
    DisallowUnitReferences: ClassVar[LookupFlags]
    """Value = 16384"""
    DisallowWildcardImport: ClassVar[LookupFlags]
    """Value = 4"""
    ForceHierarchical: ClassVar[LookupFlags]
    """Value = 18"""
    IfacePortConn: ClassVar[LookupFlags]
    """Value = 1024"""
    NoParentScope: ClassVar[LookupFlags]
    """Value = 64"""
    NoSelectors: ClassVar[LookupFlags]
    """Value = 128"""
    NoUndeclaredError: ClassVar[LookupFlags]
    """Value = 8"""
    NoUndeclaredErrorIfUninstantiated: ClassVar[LookupFlags]
    """Value = 16"""
    None_: ClassVar[LookupFlags]
    """Value = 0"""
    StaticInitializer: ClassVar[LookupFlags]
    """Value = 2048"""
    Type: ClassVar[LookupFlags]
    """Value = 1"""
    TypeReference: ClassVar[LookupFlags]
    """Value = 4096"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LookupLocation(metaclass=_metaclass):
    max: ClassVar[LookupLocation]  # value = <pyslang.LookupLocation object>
    min: ClassVar[LookupLocation]  # value = <pyslang.LookupLocation object>

    @staticmethod
    def after(symbol: Any) -> LookupLocation: ...
    @staticmethod
    def before(symbol: Any) -> LookupLocation: ...
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, scope: Any, index: int) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    @property
    def index(self) -> Any: ...
    @property
    def scope(self) -> Any: ...

class LookupResult(metaclass=_metaclass):
    class MemberSelector(metaclass=_metaclass):
        @property
        def dotLocation(self) -> SourceLocation: ...
        @property
        def name(self) -> str: ...
        @property
        def nameRange(self) -> SourceRange: ...

    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def errorIfSelectors(self, context: ASTContext) -> None: ...
    def reportDiags(self, context: ASTContext) -> None: ...
    @property
    def diagnostics(self) -> Diagnostics: ...
    @property
    def flags(self) -> LookupResultFlags: ...
    @property
    def found(self) -> Any: ...
    @property
    def hasError(self) -> bool: ...
    @property
    def selectors(self) -> Any: ...
    @property
    def systemSubroutine(self) -> SystemSubroutine: ...
    @property
    def upwardCount(self) -> int: ...

class LookupResultFlags(metaclass=_metaclass):
    FromForwardTypedef: ClassVar[LookupResultFlags]
    """Value = 16"""
    FromTypeParam: ClassVar[LookupResultFlags]
    """Value = 8"""
    IsHierarchical: ClassVar[LookupResultFlags]
    """Value = 2"""
    None_: ClassVar[LookupResultFlags]
    """Value = 0"""
    SuppressUndeclared: ClassVar[LookupResultFlags]
    """Value = 4"""
    WasImported: ClassVar[LookupResultFlags]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LoopConstraintSyntax(ConstraintItemSyntax):
    constraints: ConstraintItemSyntax
    foreachKeyword: Token
    loopList: ForeachLoopListSyntax

class LoopGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    equals: Token
    genvar: Token
    identifier: Token
    initialExpr: ExpressionSyntax
    iterationExpr: ExpressionSyntax
    keyword: Token
    openParen: Token
    semi1: Token
    semi2: Token
    stopExpr: ExpressionSyntax

class LoopStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    repeatOrWhile: Token
    statement: StatementSyntax

class MacroActualArgumentListSyntax(SyntaxNode):
    args: Any
    closeParen: Token
    openParen: Token

class MacroActualArgumentSyntax(SyntaxNode):
    tokens: Any

class MacroArgumentDefaultSyntax(SyntaxNode):
    equals: Token
    tokens: Any

class MacroFormalArgumentListSyntax(SyntaxNode):
    args: Any
    closeParen: Token
    openParen: Token

class MacroFormalArgumentSyntax(SyntaxNode):
    defaultValue: MacroArgumentDefaultSyntax
    name: Token

class MacroUsageSyntax(DirectiveSyntax):
    args: MacroActualArgumentListSyntax

class MatchesClauseSyntax(SyntaxNode):
    matchesKeyword: Token
    pattern: PatternSyntax

class MemberAccessExpression(Expression):
    @property
    def member(self) -> Symbol: ...
    @property
    def value(self) -> Expression: ...

class MemberAccessExpressionSyntax(ExpressionSyntax):
    dot: Token
    left: ExpressionSyntax
    name: Token

class MemberSyntax(SyntaxNode):
    attributes: Any

class MethodFlags(metaclass=_metaclass):
    BuiltIn: ClassVar[MethodFlags]
    """Value = 512"""
    Constructor: ClassVar[MethodFlags]
    """Value = 8"""
    DPIContext: ClassVar[MethodFlags]
    """Value = 256"""
    DPIImport: ClassVar[MethodFlags]
    """Value = 128"""
    DefaultedSuperArg: ClassVar[MethodFlags]
    """Value = 4096"""
    Extends: ClassVar[MethodFlags]
    """Value = 16384"""
    Final: ClassVar[MethodFlags]
    """Value = 32768"""
    ForkJoin: ClassVar[MethodFlags]
    """Value = 2048"""
    Initial: ClassVar[MethodFlags]
    """Value = 8192"""
    InterfaceExtern: ClassVar[MethodFlags]
    """Value = 16"""
    ModportExport: ClassVar[MethodFlags]
    """Value = 64"""
    ModportImport: ClassVar[MethodFlags]
    """Value = 32"""
    None_: ClassVar[MethodFlags]
    """Value = 0"""
    Pure: ClassVar[MethodFlags]
    """Value = 2"""
    Randomize: ClassVar[MethodFlags]
    """Value = 1024"""
    Static: ClassVar[MethodFlags]
    """Value = 4"""
    Virtual: ClassVar[MethodFlags]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MethodPrototypeSymbol(Symbol, Scope):
    class ExternImpl(metaclass=_metaclass):
        @property
        def impl(self) -> SubroutineSymbol: ...
        @property
        def nextImpl(self) -> MethodPrototypeSymbol.ExternImpl: ...

    @property
    def arguments(self) -> list[FormalArgumentSymbol]: ...
    @property
    def firstExternImpl(self) -> ExternImpl: ...
    @property
    def flags(self) -> MethodFlags: ...
    @property
    def isVirtual(self) -> bool: ...
    @property
    def override(self) -> Symbol: ...
    @property
    def returnType(self) -> Type: ...
    @property
    def subroutine(self) -> SubroutineSymbol: ...
    @property
    def subroutineKind(self) -> SubroutineKind: ...
    @property
    def visibility(self) -> Visibility: ...

class MinTypMax(metaclass=_metaclass):
    Max: ClassVar[MinTypMax]
    """Value = 2"""
    Min: ClassVar[MinTypMax]
    """Value = 0"""
    Typ: ClassVar[MinTypMax]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MinTypMaxExpression(Expression):
    @property
    def max(self) -> Expression: ...
    @property
    def min(self) -> Expression: ...
    @property
    def selected(self) -> Expression: ...
    @property
    def typ(self) -> Expression: ...

class MinTypMaxExpressionSyntax(ExpressionSyntax):
    colon1: Token
    colon2: Token
    max: ExpressionSyntax
    min: ExpressionSyntax
    typ: ExpressionSyntax

class ModportClockingPortSyntax(MemberSyntax):
    clocking: Token
    name: Token

class ModportClockingSymbol(Symbol):
    @property
    def target(self) -> Symbol: ...

class ModportDeclarationSyntax(MemberSyntax):
    items: Any
    keyword: Token
    semi: Token

class ModportExplicitPortSyntax(ModportPortSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token

class ModportItemSyntax(SyntaxNode):
    name: Token
    ports: AnsiPortListSyntax

class ModportNamedPortSyntax(ModportPortSyntax):
    name: Token

class ModportPortSymbol(ValueSymbol):
    @property
    def direction(self) -> ArgumentDirection: ...
    @property
    def explicitConnection(self) -> Expression: ...
    @property
    def internalSymbol(self) -> Symbol: ...

class ModportPortSyntax(SyntaxNode):
    pass

class ModportSimplePortListSyntax(MemberSyntax):
    direction: Token
    ports: Any

class ModportSubroutinePortListSyntax(MemberSyntax):
    importExport: Token
    ports: Any

class ModportSubroutinePortSyntax(ModportPortSyntax):
    prototype: FunctionPrototypeSyntax

class ModportSymbol(Symbol, Scope):
    @property
    def hasExports(self) -> bool: ...

class ModuleDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    endmodule: Token
    header: ModuleHeaderSyntax
    members: Any

class ModuleHeaderSyntax(SyntaxNode):
    imports: Any
    lifetime: Token
    moduleKeyword: Token
    name: Token
    parameters: ParameterPortListSyntax
    ports: PortListSyntax
    semi: Token

class MultiPortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection: ...
    @property
    def initializer(self) -> Expression: ...
    @property
    def isNullPort(self) -> bool: ...
    @property
    def ports(self) -> list[PortSymbol]: ...
    @property
    def type(self) -> Any: ...

class MultipleConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    concatenation: ConcatenationExpressionSyntax
    expression: ExpressionSyntax
    openBrace: Token

class NameSyntax(ExpressionSyntax):
    pass

class NameValuePragmaExpressionSyntax(PragmaExpressionSyntax):
    equals: Token
    name: Token
    value: PragmaExpressionSyntax

class NamedArgumentSyntax(ArgumentSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token

class NamedBlockClauseSyntax(SyntaxNode):
    colon: Token
    name: Token

class NamedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    name: Token

class NamedLabelSyntax(SyntaxNode):
    colon: Token
    name: Token

class NamedParamAssignmentSyntax(ParamAssignmentSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token

class NamedPortConnectionSyntax(PortConnectionSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token

class NamedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    colon: Token
    name: Token
    pattern: PatternSyntax

class NamedTypeSyntax(DataTypeSyntax):
    name: NameSyntax

class NamedValueExpression(ValueExpressionBase):
    pass

class NetAliasSymbol(Symbol):
    @property
    def netReferences(self) -> list[Expression]: ...

class NetAliasSyntax(MemberSyntax):
    keyword: Token
    nets: Any
    semi: Token

class NetDeclarationSyntax(MemberSyntax):
    declarators: Any
    delay: TimingControlSyntax
    expansionHint: Token
    netType: Token
    semi: Token
    strength: NetStrengthSyntax
    type: DataTypeSyntax

class NetPortHeaderSyntax(PortHeaderSyntax):
    dataType: DataTypeSyntax
    direction: Token
    netType: Token

class NetStrengthSyntax(SyntaxNode):
    pass

class NetSymbol(ValueSymbol):
    class ExpansionHint(metaclass=_metaclass):
        None_ = 0
        Scalared = 2
        Vectored = 1

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    None_: Final = ExpansionHint.None_
    Scalared: Final = ExpansionHint.Scalared
    Vectored: Final = ExpansionHint.Vectored

    @property
    def chargeStrength(self) -> Any | None: ...
    @property
    def delay(self) -> TimingControl: ...
    @property
    def driveStrength(self) -> tuple[Any | None, Any | None]: ...
    @property
    def expansionHint(self) -> Any: ...
    @property
    def isImplicit(self) -> bool: ...
    @property
    def netType(self) -> Any: ...

class NetType(Symbol):
    class NetKind(metaclass=_metaclass):
        Interconnect: ClassVar[Self]
        """Value = 13"""
        Supply0: ClassVar[Self]
        """Value = 10"""
        Supply1: ClassVar[Self]
        """Value = 11"""
        Tri: ClassVar[Self]
        """Value = 4"""
        Tri0: ClassVar[Self]
        """Value = 7"""
        Tri1: ClassVar[Self]
        """Value = 8"""
        TriAnd: ClassVar[Self]
        """Value = 5"""
        TriOr: ClassVar[Self]
        """Value = 6"""
        TriReg: ClassVar[Self]
        """Value = 9"""
        UWire: ClassVar[Self]
        """Value = 12"""
        Unknown: ClassVar[Self]
        """Value = 0"""
        UserDefined: ClassVar[Self]
        """Value = 14"""
        WAnd: ClassVar[Self]
        """Value = 2"""
        WOr: ClassVar[Self]
        """Value = 3"""
        Wire: ClassVar[Self]
        """Value = 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Interconnect: Final = NetKind.Interconnect
    Supply0: Final = NetKind.Supply0
    Supply1: Final = NetKind.Supply1
    Tri: Final = NetKind.Tri
    Tri0: Final = NetKind.Tri0
    Tri1: Final = NetKind.Tri1
    TriAnd: Final = NetKind.TriAnd
    TriOr: Final = NetKind.TriOr
    TriReg: Final = NetKind.TriReg
    UWire: Final = NetKind.UWire
    Unknown: Final = NetKind.Unknown
    UserDefined: Final = NetKind.UserDefined
    WAnd: Final = NetKind.WAnd
    WOr: Final = NetKind.WOr
    Wire: Final = NetKind.Wire

    @staticmethod
    def getSimulatedNetType(internal: NetType, external: NetType, shouldWarn: bool) -> NetType: ...
    @property
    def declaredType(self) -> DeclaredType: ...
    @property
    def isBuiltIn(self) -> bool: ...
    @property
    def isError(self) -> bool: ...
    @property
    def netKind(self) -> NetKind: ...
    @property
    def resolutionFunction(self) -> SubroutineSymbol: ...

class NetTypeDeclarationSyntax(MemberSyntax):
    keyword: Token
    name: Token
    semi: Token
    type: DataTypeSyntax
    withFunction: WithFunctionClauseSyntax

class NewArrayExpression(Expression):
    @property
    def initExpr(self) -> Expression: ...
    @property
    def sizeExpr(self) -> Expression: ...

class NewArrayExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    initializer: ParenthesizedExpressionSyntax
    newKeyword: NameSyntax
    openBracket: Token
    sizeExpr: ExpressionSyntax

class NewClassExpression(Expression):
    @property
    def constructorCall(self) -> Expression: ...
    @property
    def isSuperClass(self) -> bool: ...

class NewClassExpressionSyntax(ExpressionSyntax):
    argList: ArgumentListSyntax
    scopedNew: NameSyntax

class NewCovergroupExpression(Expression):
    @property
    def arguments(self) -> list[Expression]: ...

class NonAnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: Any

class NonAnsiPortSyntax(SyntaxNode):
    pass

class NonAnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: Any
    semi: Token

class NonConstantFunction(SimpleSystemSubroutine):
    def __init__(
        self,
        name: str,
        returnType: Any,
        requiredArgs: int = 0,
        argTypes: list[Any] = [],
        isMethod: bool = False,
    ) -> None: ...

class Null(metaclass=_metaclass):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...

class NullLiteral(Expression):
    pass

class NullType(Type):
    pass

class NumberPragmaExpressionSyntax(PragmaExpressionSyntax):
    base: Token
    size: Token
    value: Token

class OneStepDelayControl(TimingControl):
    pass

class OneStepDelaySyntax(TimingControlSyntax):
    hash: Token
    oneStep: Token

class OrderedArgumentSyntax(ArgumentSyntax):
    expr: PropertyExprSyntax

class OrderedParamAssignmentSyntax(ParamAssignmentSyntax):
    expr: ExpressionSyntax

class OrderedPortConnectionSyntax(PortConnectionSyntax):
    expr: PropertyExprSyntax

class OrderedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    pattern: PatternSyntax

class PackageExportAllDeclarationSyntax(MemberSyntax):
    doubleColon: Token
    keyword: Token
    semi: Token
    star1: Token
    star2: Token

class PackageExportDeclarationSyntax(MemberSyntax):
    items: Any
    keyword: Token
    semi: Token

class PackageImportDeclarationSyntax(MemberSyntax):
    items: Any
    keyword: Token
    semi: Token

class PackageImportItemSyntax(SyntaxNode):
    doubleColon: Token
    item: Token
    package: Token

class PackageSymbol(Symbol, Scope):
    def findForImport(self, name: str) -> Symbol: ...
    @property
    def defaultLifetime(self) -> VariableLifetime: ...
    @property
    def defaultNetType(self) -> Any: ...
    @property
    def exportDecls(self) -> list[Any]: ...
    @property
    def hasExportAll(self) -> bool: ...
    @property
    def timeScale(self) -> TimeScale | None: ...

class PackedArrayType(IntegralType):
    @property
    def elementType(self) -> Type: ...
    @property
    def range(self) -> ConstantRange: ...

class PackedStructType(IntegralType, Scope):
    @property
    def systemId(self) -> int: ...

class PackedUnionType(IntegralType, Scope):
    @property
    def isSoft(self) -> bool: ...
    @property
    def isTagged(self) -> bool: ...
    @property
    def systemId(self) -> int: ...
    @property
    def tagBits(self) -> int: ...

class ParamAssignmentSyntax(SyntaxNode):
    pass

class ParameterDeclarationBaseSyntax(SyntaxNode):
    keyword: Token

class ParameterDeclarationStatementSyntax(MemberSyntax):
    parameter: ParameterDeclarationBaseSyntax
    semi: Token

class ParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: Any
    type: DataTypeSyntax

class ParameterPortListSyntax(SyntaxNode):
    closeParen: Token
    declarations: Any
    hash: Token
    openParen: Token

class ParameterSymbol(ValueSymbol, ParameterSymbolBase):
    @property
    def isOverridden(self) -> bool: ...
    @property
    def value(self) -> ConstantValue: ...

class ParameterSymbolBase(metaclass=_metaclass):
    @property
    def isBodyParam(self) -> bool: ...
    @property
    def isLocalParam(self) -> bool: ...
    @property
    def isPortParam(self) -> bool: ...

class ParameterValueAssignmentSyntax(SyntaxNode):
    closeParen: Token
    hash: Token
    openParen: Token
    parameters: Any

class ParenExpressionListSyntax(SyntaxNode):
    closeParen: Token
    expressions: Any
    openParen: Token

class ParenPragmaExpressionSyntax(PragmaExpressionSyntax):
    closeParen: Token
    openParen: Token
    values: Any

class ParenthesizedBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    openParen: Token

class ParenthesizedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    closeParen: Token
    openParen: Token
    operand: ConditionalDirectiveExpressionSyntax

class ParenthesizedEventExpressionSyntax(EventExpressionSyntax):
    closeParen: Token
    expr: EventExpressionSyntax
    openParen: Token

class ParenthesizedExpressionSyntax(PrimaryExpressionSyntax):
    closeParen: Token
    expression: ExpressionSyntax
    openParen: Token

class ParenthesizedPatternSyntax(PatternSyntax):
    closeParen: Token
    openParen: Token
    pattern: PatternSyntax

class ParenthesizedPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: PropertyExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token

class ParenthesizedSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token
    repetition: SequenceRepetitionSyntax

class ParserOptions(metaclass=_metaclass):
    languageVersion: LanguageVersion
    maxRecursionDepth: int
    def __init__(self) -> None: ...

class PathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    delays: Any
    desc: PathDescriptionSyntax
    equals: Token
    openParen: Token
    semi: Token

class PathDescriptionSyntax(SyntaxNode):
    closeParen: Token
    edgeIdentifier: Token
    inputs: Any
    openParen: Token
    pathOperator: Token
    polarityOperator: Token
    suffix: PathSuffixSyntax

class PathSuffixSyntax(SyntaxNode):
    pass

class Pattern(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    def eval(self, context: EvalContext, value: Any, conditionKind: Any) -> Any: ...
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> PatternKind: ...
    @property
    def sourceRange(self) -> Any: ...
    @property
    def syntax(self) -> Any: ...

class PatternCaseItemSyntax(CaseItemSyntax):
    colon: Token
    expr: ExpressionSyntax
    pattern: PatternSyntax
    statement: StatementSyntax
    tripleAnd: Token

class PatternCaseStatement(Statement):
    class ItemGroup(metaclass=_metaclass):
        @property
        def filter(self) -> Expression: ...
        @property
        def pattern(self) -> Pattern: ...
        @property
        def stmt(self) -> Statement: ...

    @property
    def check(self) -> UniquePriorityCheck: ...
    @property
    def condition(self) -> CaseStatementCondition: ...
    @property
    def defaultCase(self) -> Statement: ...
    @property
    def expr(self) -> Expression: ...
    @property
    def items(self) -> list[Any]: ...

class PatternKind(metaclass=_metaclass):
    Constant: ClassVar[PatternKind]
    """Value = 2"""
    Invalid: ClassVar[PatternKind]
    """Value = 0"""
    Structure: ClassVar[PatternKind]
    """Value = 5"""
    Tagged: ClassVar[PatternKind]
    """Value = 4"""
    Variable: ClassVar[PatternKind]
    """Value = 3"""
    Wildcard: ClassVar[PatternKind]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PatternSyntax(SyntaxNode):
    pass

class PatternVarSymbol(TempVarSymbol):
    pass

class PendingAnalysis(metaclass=_metaclass):
    def tryGet(self) -> AnalyzedScope: ...
    @property
    def symbol(self) -> Any: ...

class PortConcatenationSyntax(PortExpressionSyntax):
    closeBrace: Token
    openBrace: Token
    references: Any

class PortConnection(metaclass=_metaclass):
    @property
    def expression(self) -> Expression: ...
    @property
    def ifaceConn(self) -> tuple[Symbol, ...]: ...
    @property
    def port(self) -> Symbol: ...

class PortConnectionSyntax(SyntaxNode):
    attributes: Any

class PortDeclarationSyntax(MemberSyntax):
    declarators: Any
    header: PortHeaderSyntax
    semi: Token

class PortExpressionSyntax(SyntaxNode):
    pass

class PortHeaderSyntax(SyntaxNode):
    pass

class PortListSyntax(SyntaxNode):
    pass

class PortReferenceSyntax(PortExpressionSyntax):
    name: Token
    select: ElementSelectSyntax

class PortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection: ...
    @property
    def externalLoc(self) -> SourceLocation: ...
    @property
    def initializer(self) -> Expression: ...
    @property
    def internalExpr(self) -> Expression: ...
    @property
    def internalSymbol(self) -> Symbol: ...
    @property
    def isAnsiPort(self) -> bool: ...
    @property
    def isNetPort(self) -> bool: ...
    @property
    def isNullPort(self) -> bool: ...
    @property
    def type(self) -> Any: ...

class PostfixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: Any
    operand: ExpressionSyntax
    operatorToken: Token

class PragmaDirectiveSyntax(DirectiveSyntax):
    args: Any
    name: Token

class PragmaExpressionSyntax(SyntaxNode):
    pass

class PredefinedIntegerType(IntegralType):
    class Kind(metaclass=_metaclass):
        Byte: ClassVar[Self]
        """Value = 3"""
        Int: ClassVar[Self]
        """Value = 1"""
        Integer: ClassVar[Self]
        """Value = 4"""
        LongInt: ClassVar[Self]
        """Value = 2"""
        ShortInt: ClassVar[Self]
        """Value = 0"""
        Time: ClassVar[Self]
        """Value = 5"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Byte: Final = Kind.Byte
    Int: Final = Kind.Int
    Integer: Final = Kind.Integer
    LongInt: Final = Kind.LongInt
    ShortInt: Final = Kind.ShortInt
    Time: Final = Kind.Time

    @property
    def integerKind(self) -> Any: ...

class PrefixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: Any
    operand: ExpressionSyntax
    operatorToken: Token

class PreprocessorOptions(metaclass=_metaclass):
    additionalIncludePaths: list[os.PathLike]
    ignoreDirectives: set[str]
    languageVersion: LanguageVersion
    maxIncludeDepth: int
    predefineSource: str
    predefines: list[str]
    undefines: list[str]
    def __init__(self) -> None: ...

class PrimaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    keyword: Token
    name: NameSyntax

class PrimaryExpressionSyntax(ExpressionSyntax):
    pass

class PrimitiveInstanceSymbol(InstanceSymbolBase):
    @property
    def delay(self) -> TimingControl: ...
    @property
    def driveStrength(self) -> tuple[Any | None, Any | None]: ...
    @property
    def portConnections(self) -> list[Expression]: ...
    @property
    def primitiveType(self) -> Any: ...

class PrimitiveInstantiationSyntax(MemberSyntax):
    delay: TimingControlSyntax
    instances: Any
    semi: Token
    strength: NetStrengthSyntax
    type: Token

class PrimitivePortDirection(metaclass=_metaclass):
    In: ClassVar[PrimitivePortDirection]
    """Value = 0"""
    Out: ClassVar[PrimitivePortDirection]
    """Value = 1"""
    OutReg: ClassVar[PrimitivePortDirection]
    """Value = 2"""
    InOut: ClassVar[PrimitivePortDirection]
    """Value = 3"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PrimitivePortSymbol(ValueSymbol):
    @property
    def direction(self) -> PrimitivePortDirection: ...

class PrimitiveSymbol(Symbol, Scope):
    class PrimitiveKind(metaclass=_metaclass):
        Fixed: ClassVar[Self]
        """Value = 1"""
        NInput: ClassVar[Self]
        """Value = 2"""
        NOutput: ClassVar[Self]
        """Value = 3"""
        UserDefined: ClassVar[Self]
        """Value = 0"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    class TableEntry(metaclass=_metaclass):
        @property
        def inputs(self) -> str: ...
        @property
        def output(self) -> str: ...
        @property
        def state(self) -> str: ...

    Fixed = PrimitiveKind.Fixed
    NInput = PrimitiveKind.NInput
    NOutput = PrimitiveKind.NOutput
    UserDefined = PrimitiveKind.UserDefined

    @property
    def initVal(self) -> ConstantValue: ...
    @property
    def isSequential(self) -> bool: ...
    @property
    def ports(self) -> list[PrimitivePortSymbol]: ...
    @property
    def primitiveKind(self) -> PrimitiveKind: ...
    @property
    def table(self) -> list[Any]: ...

class ProceduralAssignStatement(Statement):
    @property
    def assignment(self) -> Expression: ...
    @property
    def isForce(self) -> bool: ...

class ProceduralAssignStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    keyword: Token
    semi: Token

class ProceduralBlockKind(metaclass=_metaclass):
    Always: ClassVar[ProceduralBlockKind]
    """Value = 2"""
    AlwaysComb: ClassVar[ProceduralBlockKind]
    """Value = 3"""
    AlwaysFF: ClassVar[ProceduralBlockKind]
    """Value = 5"""
    AlwaysLatch: ClassVar[ProceduralBlockKind]
    """Value = 4"""
    Final: ClassVar[ProceduralBlockKind]
    """Value = 1"""
    Initial: ClassVar[ProceduralBlockKind]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ProceduralBlockSymbol(Symbol):
    @property
    def body(self) -> Statement: ...
    @property
    def isSingleDriverBlock(self) -> bool: ...
    @property
    def procedureKind(self) -> ProceduralBlockKind: ...

class ProceduralBlockSyntax(MemberSyntax):
    keyword: Token
    statement: StatementSyntax

class ProceduralCheckerStatement(Statement):
    @property
    def instances(self) -> list[Any]: ...

class ProceduralDeassignStatement(Statement):
    @property
    def isRelease(self) -> bool: ...
    @property
    def lvalue(self) -> Expression: ...

class ProceduralDeassignStatementSyntax(StatementSyntax):
    keyword: Token
    semi: Token
    variable: ExpressionSyntax

class ProductionSyntax(SyntaxNode):
    colon: Token
    dataType: DataTypeSyntax
    name: Token
    portList: FunctionPortListSyntax
    rules: Any
    semi: Token

class PropertyCaseItemSyntax(SyntaxNode):
    pass

class PropertyDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    propertySpec: PropertySpecSyntax
    semi: Token
    variables: Any

class PropertyExprSyntax(SyntaxNode):
    pass

class PropertySpecSyntax(SyntaxNode):
    clocking: TimingControlSyntax
    disable: DisableIffSyntax
    expr: PropertyExprSyntax

class PropertySymbol(Symbol, Scope):
    @property
    def ports(self) -> list[AssertionPortSymbol]: ...

class PropertyType(Type):
    pass

class PullStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token

class PulseStyleDeclarationSyntax(MemberSyntax):
    inputs: Any
    keyword: Token
    semi: Token

class PulseStyleKind(metaclass=_metaclass):
    NoShowCancelled: ClassVar[PulseStyleKind]
    """Value = 3"""
    OnDetect: ClassVar[PulseStyleKind]
    """Value = 1"""
    OnEvent: ClassVar[PulseStyleKind]
    """Value = 0"""
    ShowCancelled: ClassVar[PulseStyleKind]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PulseStyleSymbol(Symbol):
    @property
    def pulseStyleKind(self) -> PulseStyleKind: ...
    @property
    def terminals(self) -> list[Expression]: ...

class QueueDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    dollar: Token
    maxSizeClause: ColonExpressionClauseSyntax

class QueueType(Type):
    @property
    def elementType(self) -> Type: ...
    @property
    def maxBound(self) -> int: ...

class RandCaseItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    statement: StatementSyntax

class RandCaseStatement(Statement):
    class Item(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def stmt(self) -> Statement: ...

    @property
    def items(self) -> list[Any]: ...

class RandCaseStatementSyntax(StatementSyntax):
    endCase: Token
    items: Any
    randCase: Token

class RandJoinClauseSyntax(SyntaxNode):
    expr: ParenthesizedExpressionSyntax
    join: Token
    rand: Token

class RandMode(metaclass=_metaclass):
    None_: ClassVar[RandMode]
    """Value = 0"""
    Rand: ClassVar[RandMode]
    """Value = 1"""
    RandC: ClassVar[RandMode]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class RandSeqProductionSymbol(Symbol, Scope):
    class ProdKind(metaclass=_metaclass):
        Case = 4
        CodeBlock = 1
        IfElse = 2
        Item = 0
        Repeat = 3

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    class ProdBase(metaclass=_metaclass):
        @property
        def kind(self) -> RandSeqProductionSymbol.ProdKind: ...

    class CaseItem(metaclass=_metaclass):
        @property
        def expressions(self) -> list[Expression]: ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem: ...

    class CaseProd(RandSeqProductionSymbol.ProdBase):
        @property
        def defaultItem(self) -> RandSeqProductionSymbol.ProdItem | None: ...
        @property
        def expr(self) -> Expression: ...
        @property
        def items(self) -> list[RandSeqProductionSymbol.CaseItem]: ...

    class CodeBlockProd(RandSeqProductionSymbol.ProdBase):
        @property
        def block(self) -> StatementBlockSymbol: ...

    class IfElseProd(ProdBase):
        @property
        def elseItem(self) -> RandSeqProductionSymbol.ProdItem | None: ...
        @property
        def expr(self) -> Expression: ...
        @property
        def ifItem(self) -> RandSeqProductionSymbol.ProdItem: ...

    class ProdItem(ProdBase):
        @property
        def args(self) -> list[Expression]: ...
        @property
        def target(self) -> RandSeqProductionSymbol: ...

    class RepeatProd(RandSeqProductionSymbol.ProdBase):
        @property
        def expr(self) -> Expression: ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem: ...

    class Rule(metaclass=_metaclass):
        @property
        def codeBlock(self) -> RandSeqProductionSymbol.CodeBlockProd | None: ...
        @property
        def isRandJoin(self) -> bool: ...
        @property
        def prods(self) -> list[RandSeqProductionSymbol.ProdBase]: ...
        @property
        def randJoinExpr(self) -> Expression: ...
        @property
        def ruleBlock(self) -> StatementBlockSymbol: ...
        @property
        def weightExpr(self) -> Expression: ...

    @property
    def arguments(self) -> list[FormalArgumentSymbol]: ...
    @property
    def returnType(self) -> Any: ...
    @property
    def rules(self) -> list[Any]: ...

class RandSequenceStatement(Statement):
    @property
    def firstProduction(self) -> Any: ...

class RandSequenceStatementSyntax(StatementSyntax):
    closeParen: Token
    endsequence: Token
    firstProduction: Token
    openParen: Token
    productions: Any
    randsequence: Token

class RangeCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    ranges: RangeListSyntax
    withClause: WithClauseSyntax

class RangeDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    selector: SelectorSyntax

class RangeListSyntax(SyntaxNode):
    closeBrace: Token
    openBrace: Token
    valueRanges: Any

class RangeSelectExpression(Expression):
    @property
    def left(self) -> Expression: ...
    @property
    def right(self) -> Expression: ...
    @property
    def selectionKind(self) -> RangeSelectionKind: ...
    @property
    def value(self) -> Expression: ...

class RangeSelectSyntax(SelectorSyntax):
    left: ExpressionSyntax
    range: Token
    right: ExpressionSyntax

class RangeSelectionKind(metaclass=_metaclass):
    IndexedDown: ClassVar[RangeSelectionKind]
    """Value = 2"""
    IndexedUp: ClassVar[RangeSelectionKind]
    """Value = 1"""
    Simple: ClassVar[RangeSelectionKind]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class RealLiteral(Expression):
    @property
    def value(self) -> float: ...

class RepeatLoopStatement(Statement):
    @property
    def body(self) -> Statement: ...
    @property
    def count(self) -> Expression: ...

class RepeatedEventControl(TimingControl):
    @property
    def event(self) -> TimingControl: ...
    @property
    def expr(self) -> Any: ...

class RepeatedEventControlSyntax(TimingControlSyntax):
    closeParen: Token
    eventControl: TimingControlSyntax
    expr: ExpressionSyntax
    openParen: Token
    repeat: Token

class ReplicatedAssignmentPatternExpression(AssignmentPatternExpressionBase):
    @property
    def count(self) -> Expression: ...

class ReplicatedAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    countExpr: ExpressionSyntax
    innerCloseBrace: Token
    innerOpenBrace: Token
    items: Any
    openBrace: Token

class ReplicationExpression(Expression):
    @property
    def concat(self) -> Expression: ...
    @property
    def count(self) -> Expression: ...

class ReportedDiagnostic(metaclass=_metaclass):
    @property
    def expansionLocs(self) -> list[SourceLocation]: ...
    @property
    def formattedMessage(self) -> str: ...
    @property
    def location(self) -> SourceLocation: ...
    @property
    def originalDiagnostic(self) -> Diagnostic: ...
    @property
    def ranges(self) -> list[SourceRange]: ...
    @property
    def severity(self) -> DiagnosticSeverity: ...
    @property
    def shouldShowIncludeStack(self) -> bool: ...

class ReturnStatement(Statement):
    @property
    def expr(self) -> Expression: ...

class ReturnStatementSyntax(StatementSyntax):
    returnKeyword: Token
    returnValue: ExpressionSyntax
    semi: Token

class RootSymbol(Symbol, Scope):
    @property
    def compilationUnits(self) -> list[CompilationUnitSymbol]: ...
    @property
    def topInstances(self) -> list[Any]: ...

class RsCaseItemSyntax(SyntaxNode):
    pass

class RsCaseSyntax(RsProdSyntax):
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: Any
    keyword: Token
    openParen: Token

class RsCodeBlockSyntax(RsProdSyntax):
    closeBrace: Token
    items: Any
    openBrace: Token

class RsElseClauseSyntax(SyntaxNode):
    item: RsProdItemSyntax
    keyword: Token

class RsIfElseSyntax(RsProdSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: RsElseClauseSyntax
    ifItem: RsProdItemSyntax
    keyword: Token
    openParen: Token

class RsProdItemSyntax(RsProdSyntax):
    argList: ArgumentListSyntax
    name: Token

class RsProdSyntax(SyntaxNode):
    pass

class RsRepeatSyntax(RsProdSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    item: RsProdItemSyntax
    keyword: Token
    openParen: Token

class RsRuleSyntax(SyntaxNode):
    prods: Any
    randJoin: RandJoinClauseSyntax
    weightClause: RsWeightClauseSyntax

class RsWeightClauseSyntax(SyntaxNode):
    codeBlock: RsProdSyntax
    colonEqual: Token
    weight: ExpressionSyntax

class SVInt(metaclass=_metaclass):
    @staticmethod
    def concat(arg0: list[SVInt]) -> SVInt: ...
    @staticmethod
    def conditional(condition: SVInt, lhs: SVInt, rhs: SVInt) -> SVInt: ...
    @staticmethod
    def createFillX(bitWidth: int, isSigned: bool) -> SVInt: ...
    @staticmethod
    def createFillZ(bitWidth: int, isSigned: bool) -> SVInt: ...
    @staticmethod
    def fromDigits(
        bits: int, base: LiteralBase, isSigned: bool, anyUnknown: bool, digits: list[logic_t]
    ) -> SVInt: ...
    @staticmethod
    def fromDouble(bits: int, value: float, isSigned: bool, round: bool = True) -> SVInt: ...
    @staticmethod
    def fromFloat(bits: int, value: float, isSigned: bool, round: bool = True) -> SVInt: ...
    @staticmethod
    def logicalEquiv(lhs: SVInt, rhs: SVInt) -> logic_t: ...
    @staticmethod
    def logicalImpl(lhs: SVInt, rhs: SVInt) -> logic_t: ...
    @typing.overload
    def __add__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __add__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __and__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __and__(self, arg0: int) -> SVInt: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: SVInt | int) -> logic_t:  # type: ignore[override]
        ...
    def __float__(self) -> float: ...
    @typing.overload
    def __ge__(self, arg0: SVInt) -> logic_t: ...
    @typing.overload
    def __ge__(self, arg0: int) -> logic_t: ...
    def __getitem__(self, arg0: int) -> logic_t: ...
    @typing.overload
    def __gt__(self, arg0: SVInt) -> logic_t: ...
    @typing.overload
    def __gt__(self, arg0: int) -> logic_t: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __iadd__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __iadd__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __iand__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __iand__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __imod__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __imod__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __imul__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __imul__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, bit: logic_t) -> None: ...
    @typing.overload
    def __init__(self, bits: int, value: int, isSigned: bool) -> None: ...
    @typing.overload
    def __init__(self, bits: int, bytes: list[Any], isSigned: bool) -> None: ...
    @typing.overload
    def __init__(self, str: str) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: float) -> None: ...
    def __int__(self) -> int: ...
    def __invert__(self) -> SVInt: ...
    @typing.overload
    def __ior__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __ior__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __isub__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __isub__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __itruediv__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __itruediv__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __ixor__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __ixor__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __le__(self, arg0: SVInt) -> logic_t: ...
    @typing.overload
    def __le__(self, arg0: int) -> logic_t: ...
    @typing.overload
    def __lt__(self, arg0: SVInt) -> logic_t: ...
    @typing.overload
    def __lt__(self, arg0: int) -> logic_t: ...
    @typing.overload
    def __mod__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __mod__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __mul__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __mul__(self, arg0: int) -> SVInt: ...
    def __ne__(self, arg0: SVInt | int) -> logic_t:  # type: ignore[override]
        ...
    def __neg__(self) -> SVInt: ...
    @typing.overload
    def __or__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __or__(self, arg0: int) -> SVInt: ...
    def __pow__(self, arg0: SVInt) -> SVInt: ...
    def __radd__(self, arg0: int) -> SVInt: ...
    def __rand__(self, arg0: int) -> SVInt: ...
    def __rdiv__(self, arg0: int) -> SVInt: ...
    def __repr__(self) -> str: ...
    def __rmod__(self, arg0: int) -> SVInt: ...
    def __rmul__(self, arg0: int) -> SVInt: ...
    def __ror__(self, arg0: int) -> SVInt: ...
    def __rsub__(self, arg0: int) -> SVInt: ...
    def __rxor__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __sub__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __sub__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __truediv__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __truediv__(self, arg0: int) -> SVInt: ...
    @typing.overload
    def __xor__(self, arg0: SVInt) -> SVInt: ...
    @typing.overload
    def __xor__(self, arg0: int) -> SVInt: ...
    def ashr(self, rhs: SVInt) -> SVInt: ...
    def countLeadingOnes(self) -> int: ...
    def countLeadingUnknowns(self) -> int: ...
    def countLeadingZeros(self) -> int: ...
    def countLeadingZs(self) -> int: ...
    def countOnes(self) -> int: ...
    def countXs(self) -> int: ...
    def countZeros(self) -> int: ...
    def countZs(self) -> int: ...
    def extend(self, bits: int, isSigned: bool) -> SVInt: ...
    def flattenUnknowns(self) -> None: ...
    def getActiveBits(self) -> int: ...
    def getMinRepresentedBits(self) -> int: ...
    def isEven(self) -> bool: ...
    def isNegative(self) -> bool: ...
    def isOdd(self) -> bool: ...
    def isSignExtendedFrom(self, msb: int) -> bool: ...
    def lshr(self, rhs: SVInt) -> SVInt: ...
    def reductionAnd(self) -> logic_t: ...
    def reductionOr(self) -> logic_t: ...
    def reductionXor(self) -> logic_t: ...
    def replicate(self, times: SVInt) -> SVInt: ...
    def resize(self, bits: int) -> SVInt: ...
    def reverse(self) -> SVInt: ...
    def set(self, msb: int, lsb: int, value: SVInt) -> None: ...
    def setAllOnes(self) -> None: ...
    def setAllX(self) -> None: ...
    def setAllZ(self) -> None: ...
    def setAllZeros(self) -> None: ...
    def setSigned(self, isSigned: bool) -> None: ...
    def sext(self, bits: int) -> SVInt: ...
    def shl(self, rhs: SVInt) -> SVInt: ...
    def shrinkToFit(self) -> None: ...
    def signExtendFrom(self, msb: int) -> None: ...
    def slice(self, msb: int, lsb: int) -> SVInt: ...
    def toString(
        self, base: LiteralBase, includeBase: bool, abbreviateThresholdBits: int = 16777215
    ) -> str: ...
    def trunc(self, bits: int) -> SVInt: ...
    def xnor(self, rhs: SVInt) -> SVInt: ...
    def zext(self, bits: int) -> SVInt: ...
    @property
    def bitWidth(self) -> int: ...
    @property
    def hasUnknown(self) -> bool: ...
    @property
    def isSigned(self) -> bool: ...

class ScalarType(IntegralType):
    class Kind(metaclass=_metaclass):
        Bit = 0
        Logic = 1
        Reg = 2

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Bit: Final = Kind.Bit
    Logic: Final = Kind.Logic
    Reg: Final = Kind.Reg

    @property
    def scalarKind(self) -> Any: ...

class Scope(metaclass=_metaclass):
    def __getitem__(self, arg0: int) -> typing.Any: ...
    def __iter__(self) -> typing.Iterator[Symbol]: ...
    def __len__(self) -> int: ...
    def find(self, arg0: str) -> Symbol: ...
    def lookupName(
        self, name: str, location: LookupLocation = ..., flags: LookupFlags = ...
    ) -> Symbol: ...
    @property
    def compilation(self) -> Compilation: ...
    @property
    def compilationUnit(self) -> Any: ...
    @property
    def containingInstance(self) -> Any: ...
    @property
    def defaultNetType(self) -> Any: ...
    @property
    def isProceduralContext(self) -> bool: ...
    @property
    def isUninstantiated(self) -> bool: ...
    @property
    def timeScale(self) -> TimeScale | None: ...

class ScopedNameSyntax(NameSyntax):
    left: NameSyntax
    right: NameSyntax
    separator: Token

class ScriptSession(metaclass=_metaclass):
    def __init__(self) -> None: ...
    def eval(self, text: str) -> ConstantValue: ...
    def evalExpression(self, expr: ExpressionSyntax) -> ConstantValue: ...
    def evalStatement(self, expr: StatementSyntax) -> None: ...
    def getDiagnostics(self) -> Diagnostics: ...
    @property
    def compilation(self) -> Compilation: ...

class SelectorSyntax(SyntaxNode):
    pass

class SequenceConcatExpr(AssertionExpr):
    class Element(metaclass=_metaclass):
        @property
        def delay(self) -> SequenceRange: ...
        @property
        def sequence(self) -> AssertionExpr: ...

    @property
    def elements(self) -> list[Any]: ...

class SequenceDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    semi: Token
    seqExpr: SequenceExprSyntax
    variables: Any

class SequenceExprSyntax(SyntaxNode):
    pass

class SequenceMatchListSyntax(SyntaxNode):
    comma: Token
    items: Any

class SequenceRange(metaclass=_metaclass):
    @property
    def max(self) -> int | None: ...
    @property
    def min(self) -> int: ...

class SequenceRepetition(metaclass=_metaclass):
    class Kind(metaclass=_metaclass):
        Consecutive = 0
        GoTo = 2
        Nonconsecutive = 1

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Consecutive = Kind.Consecutive
    GoTo = Kind.GoTo
    Nonconsecutive = Kind.Nonconsecutive

    @property
    def kind(self) -> Kind: ...
    @property
    def range(self) -> SequenceRange: ...

class SequenceRepetitionSyntax(SyntaxNode):
    closeBracket: Token
    op: Token
    openBracket: Token
    selector: SelectorSyntax

class SequenceSymbol(Symbol, Scope):
    @property
    def ports(self) -> list[AssertionPortSymbol]: ...

class SequenceType(Type):
    pass

class SequenceWithMatchExpr(AssertionExpr):
    @property
    def expr(self) -> AssertionExpr: ...
    @property
    def matchItems(self) -> list[Any]: ...
    @property
    def repetition(self) -> SequenceRepetition | None: ...

class SetExprBinsSelectExpr(BinsSelectExpr):
    @property
    def expr(self) -> Any: ...
    @property
    def matchesExpr(self) -> Any: ...

class SignalEventControl(TimingControl):
    @property
    def edge(self) -> Any: ...
    @property
    def expr(self) -> Any: ...
    @property
    def iffCondition(self) -> Any: ...

class SignalEventExpressionSyntax(EventExpressionSyntax):
    edge: Token
    expr: ExpressionSyntax
    iffClause: IffEventClauseSyntax

class SignedCastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    inner: ParenthesizedExpressionSyntax
    signing: Token

class SimpleAssertionExpr(AssertionExpr):
    @property
    def expr(self) -> Any: ...
    @property
    def repetition(self) -> SequenceRepetition | None: ...

class SimpleAssignmentPatternExpression(AssignmentPatternExpressionBase):
    pass

class SimpleAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: Any
    openBrace: Token

class SimpleBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax

class SimpleDirectiveSyntax(DirectiveSyntax):
    pass

class SimplePathSuffixSyntax(PathSuffixSyntax):
    outputs: Any

class SimplePragmaExpressionSyntax(PragmaExpressionSyntax):
    value: Token

class SimplePropertyExprSyntax(PropertyExprSyntax):
    expr: SequenceExprSyntax

class SimpleSequenceExprSyntax(SequenceExprSyntax):
    expr: ExpressionSyntax
    repetition: SequenceRepetitionSyntax

class SimpleSystemSubroutine(SystemSubroutine):
    def __init__(
        self,
        name: str,
        kind: SubroutineKind,
        requiredArgs: int,
        argTypes: list[Any],
        returnType: Any,
        isMethod: bool,
        isFirstArgLValue: bool = False,
    ) -> None: ...

class SolveBeforeConstraint(Constraint):
    @property
    def after(self) -> list[Any]: ...
    @property
    def solve(self) -> list[Any]: ...

class SolveBeforeConstraintSyntax(ConstraintItemSyntax):
    afterExpr: Any
    before: Token
    beforeExpr: Any
    semi: Token
    solve: Token

class SourceBuffer(metaclass=_metaclass):
    def __bool__(self) -> bool: ...
    def __init__(self) -> None: ...
    @property
    def data(self) -> str: ...
    @property
    def id(self) -> BufferID: ...
    @property
    def library(self) -> SourceLibrary: ...

class SourceLibrary(metaclass=_metaclass):
    def __init__(self) -> None: ...
    @property
    def name(self) -> str: ...

class SourceLoader(metaclass=_metaclass):
    def __init__(self, sourceManager: Any) -> None: ...
    def addFiles(self, pattern: str) -> None: ...
    def addLibraryFiles(self, libraryName: str, pattern: str) -> None: ...
    def addLibraryMaps(self, pattern: str, basePath: os.PathLike, optionBag: Any) -> None: ...
    def addSearchDirectories(self, pattern: str) -> None: ...
    def addSearchExtension(self, extension: str) -> None: ...
    def addSeparateUnit(
        self, filePatterns: list[str], includePaths: list[str], defines: list[str], libraryName: str
    ) -> None: ...
    def loadAndParseSources(self, optionBag: Any) -> list[Any]: ...
    def loadSources(self) -> list[Any]: ...
    @property
    def errors(self) -> list[str]: ...
    @property
    def hasFiles(self) -> bool: ...
    @property
    def libraryMaps(self) -> list[Any]: ...

class SourceLocation(metaclass=_metaclass):
    NoLocation: typing.ClassVar[SourceLocation]  # value = SourceLocation(268435455, 68719476735)
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __ge__(self, arg0: SourceLocation) -> bool: ...
    def __gt__(self, arg0: SourceLocation) -> bool: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, buffer: BufferID, offset: int) -> None: ...
    def __le__(self, arg0: SourceLocation) -> bool: ...
    def __lt__(self, arg0: SourceLocation) -> bool: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    @property
    def buffer(self) -> BufferID: ...
    @property
    def offset(self) -> int: ...

class SourceManager(metaclass=_metaclass):
    def __init__(self) -> None: ...
    def addDiagnosticDirective(
        self, location: SourceLocation, name: str, severity: Any
    ) -> None: ...
    def addLineDirective(
        self, location: SourceLocation, lineNum: int, name: str, level: int
    ) -> None: ...
    def addSystemDirectories(self, path: str) -> None: ...
    def addUserDirectories(self, path: str) -> None: ...
    @typing.overload
    def assignText(
        self, text: str, includedFrom: SourceLocation = ..., library: SourceLibrary | None = None
    ) -> SourceBuffer: ...
    @typing.overload
    def assignText(
        self,
        path: str,
        text: str,
        includedFrom: SourceLocation = ...,
        library: SourceLibrary | None = None,
    ) -> SourceBuffer: ...
    def getAllBuffers(self) -> list[BufferID]: ...
    def getColumnNumber(self, location: SourceLocation) -> int: ...
    def getExpansionLoc(self, location: SourceLocation) -> SourceLocation: ...
    def getExpansionRange(self, location: SourceLocation) -> SourceRange: ...
    def getFileName(self, location: SourceLocation) -> str: ...
    def getFullPath(self, buffer: BufferID) -> os.PathLike: ...
    def getFullyExpandedLoc(self, location: SourceLocation) -> SourceLocation: ...
    def getFullyOriginalLoc(self, location: SourceLocation) -> SourceLocation: ...
    def getFullyOriginalRange(self, range: SourceRange) -> SourceRange: ...
    def getIncludedFrom(self, buffer: BufferID) -> SourceLocation: ...
    def getLineNumber(self, location: SourceLocation) -> int: ...
    def getMacroName(self, location: SourceLocation) -> str: ...
    def getOriginalLoc(self, location: SourceLocation) -> SourceLocation: ...
    def getRawFileName(self, buffer: BufferID) -> str: ...
    def getSourceText(self, buffer: BufferID) -> str: ...
    def isBeforeInCompilationUnit(
        self, left: SourceLocation, right: SourceLocation
    ) -> bool | None: ...
    def isCached(self, path: os.PathLike) -> bool: ...
    def isFileLoc(self, location: SourceLocation) -> bool: ...
    def isIncludedFileLoc(self, location: SourceLocation) -> bool: ...
    def isMacroArgLoc(self, location: SourceLocation) -> bool: ...
    def isMacroLoc(self, location: SourceLocation) -> bool: ...
    def isPreprocessedLoc(self, location: SourceLocation) -> bool: ...
    def readHeader(
        self, path: str, includedFrom: SourceLocation, library: SourceLibrary, isSystemPath: bool
    ) -> SourceBuffer: ...
    def readSource(
        self, path: os.PathLike, library: SourceLibrary | None = None
    ) -> SourceBuffer: ...
    def setDisableProximatePaths(self, set: bool) -> None: ...

class SourceOptions(metaclass=_metaclass):
    librariesInheritMacros: bool
    numThreads: int | None
    onlyLint: bool
    singleUnit: bool
    def __init__(self) -> None: ...

class SourceRange(metaclass=_metaclass):
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, startLoc: SourceLocation, endLoc: SourceLocation) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    @property
    def end(self) -> SourceLocation: ...
    @property
    def start(self) -> SourceLocation: ...

class SpecifyBlockSymbol(Symbol, Scope):
    pass

class SpecifyBlockSyntax(MemberSyntax):
    endspecify: Token
    items: Any
    specify: Token

class SpecparamDeclarationSyntax(MemberSyntax):
    declarators: Any
    keyword: Token
    semi: Token
    type: ImplicitTypeSyntax

class SpecparamDeclaratorSyntax(SyntaxNode):
    closeParen: Token
    comma: Token
    equals: Token
    name: Token
    openParen: Token
    value1: ExpressionSyntax
    value2: ExpressionSyntax

class SpecparamSymbol(ValueSymbol):
    @property
    def isPathPulse(self) -> bool: ...
    @property
    def pathDest(self) -> Symbol: ...
    @property
    def pathSource(self) -> Symbol: ...
    @property
    def pulseErrorLimit(self) -> ConstantValue: ...
    @property
    def pulseRejectLimit(self) -> ConstantValue: ...
    @property
    def value(self) -> ConstantValue: ...

class StandardCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    expressions: Any

class StandardPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    expr: PropertyExprSyntax
    expressions: Any
    semi: Token

class StandardRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    expressions: Any
    item: RsProdItemSyntax
    semi: Token

class Statement(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    def eval(self, context: EvalContext) -> EvalResult: ...
    def visit(self, f: typing.Any) -> None:
        """Visit a pyslang object with a callback function `f`.
        The callback function `f` should take a single argument, which is the current node being
            visited.
        The return value of `f` determines the next node to visit.
        If `f` ever returns `pyslang.VisitAction.Interrupt`, the visit is aborted and no additional
            nodes are visited.
        If `f` returns `pyslang.VisitAction.Skip`, then no child nodes of the current node are
            visited. For any other return value, including `pyslang.VisitAction.Advance`,
            the return value is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> StatementKind: ...
    @property
    def sourceRange(self) -> SourceRange: ...
    @property
    def syntax(self) -> StatementSyntax: ...

class StatementBlockKind(metaclass=_metaclass):
    JoinAll: ClassVar[StatementBlockKind]
    """Value = 1"""
    JoinAny: ClassVar[StatementBlockKind]
    """Value = 2"""
    JoinNone: ClassVar[StatementBlockKind]
    """Value = 3"""
    Sequential: ClassVar[StatementBlockKind]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class StatementBlockSymbol(Symbol, Scope):
    @property
    def blockKind(self) -> StatementBlockKind: ...
    @property
    def defaultLifetime(self) -> VariableLifetime: ...

class StatementKind(metaclass=_metaclass):
    Block: ClassVar[StatementKind]
    """Value = 3"""
    Break: ClassVar[StatementKind]
    """Value = 8"""
    Case: ClassVar[StatementKind]
    """Value = 11"""
    ConcurrentAssertion: ClassVar[StatementKind]
    """Value = 21"""
    Conditional: ClassVar[StatementKind]
    """Value = 10"""
    Continue: ClassVar[StatementKind]
    """Value = 7"""
    Disable: ClassVar[StatementKind]
    """Value = 9"""
    DisableFork: ClassVar[StatementKind]
    """Value = 22"""
    DoWhileLoop: ClassVar[StatementKind]
    """Value = 17"""
    Empty: ClassVar[StatementKind]
    """Value = 1"""
    EventTrigger: ClassVar[StatementKind]
    """Value = 26"""
    ExpressionStatement: ClassVar[StatementKind]
    """Value = 4"""
    ForLoop: ClassVar[StatementKind]
    """Value = 13"""
    ForeachLoop: ClassVar[StatementKind]
    """Value = 15"""
    ForeverLoop: ClassVar[StatementKind]
    """Value = 18"""
    ImmediateAssertion: ClassVar[StatementKind]
    """Value = 20"""
    Invalid: ClassVar[StatementKind]
    """Value = 0"""
    List: ClassVar[StatementKind]
    """Value = 2"""
    PatternCase: ClassVar[StatementKind]
    """Value = 12"""
    ProceduralAssign: ClassVar[StatementKind]
    """Value = 27"""
    ProceduralChecker: ClassVar[StatementKind]
    """Value = 31"""
    ProceduralDeassign: ClassVar[StatementKind]
    """Value = 28"""
    RandCase: ClassVar[StatementKind]
    """Value = 29"""
    RandSequence: ClassVar[StatementKind]
    """Value = 30"""
    RepeatLoop: ClassVar[StatementKind]
    """Value = 14"""
    Return: ClassVar[StatementKind]
    """Value = 6"""
    Timed: ClassVar[StatementKind]
    """Value = 19"""
    VariableDeclaration: ClassVar[StatementKind]
    """Value = 5"""
    Wait: ClassVar[StatementKind]
    """Value = 23"""
    WaitFork: ClassVar[StatementKind]
    """Value = 24"""
    WaitOrder: ClassVar[StatementKind]
    """Value = 25"""
    WhileLoop: ClassVar[StatementKind]
    """Value = 16"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class StatementList(Statement):
    @property
    def list(self) -> list[Statement]: ...

class StatementSyntax(SyntaxNode):
    attributes: Any
    label: NamedLabelSyntax

class StreamExpressionSyntax(SyntaxNode):
    expression: ExpressionSyntax
    withRange: StreamExpressionWithRangeSyntax

class StreamExpressionWithRangeSyntax(SyntaxNode):
    range: ElementSelectSyntax
    withKeyword: Token

class StreamingConcatenationExpression(Expression):
    class StreamExpression(metaclass=_metaclass):
        @property
        def constantWithWidth(self) -> int | None: ...
        @property
        def operand(self) -> Expression: ...
        @property
        def withExpr(self) -> Expression: ...

    @property
    def bitstreamWidth(self) -> int: ...
    @property
    def isFixedSize(self) -> bool: ...
    @property
    def sliceSize(self) -> int: ...
    @property
    def streams(self) -> list[Any]: ...

class StreamingConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: Any
    innerCloseBrace: Token
    innerOpenBrace: Token
    openBrace: Token
    operatorToken: Token
    sliceSize: ExpressionSyntax

class StringLiteral(Expression):
    @property
    def intValue(self) -> Any: ...
    @property
    def rawValue(self) -> str: ...
    @property
    def value(self) -> str: ...

class StringType(Type):
    pass

class StrongWeakAssertionExpr(AssertionExpr):
    class Strength(metaclass=_metaclass):
        Strong: ClassVar[Self]
        """Value = 0"""
        Weak: ClassVar[Self]
        """Value = 1"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Strong = Strength.Strong
    Weak = Strength.Weak
    @property
    def expr(self) -> AssertionExpr: ...
    @property
    def strength(self) -> Strength: ...

class StrongWeakPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    keyword: Token
    openParen: Token

class StructUnionMemberSyntax(SyntaxNode):
    attributes: Any
    declarators: Any
    randomQualifier: Token
    semi: Token
    type: DataTypeSyntax

class StructUnionTypeSyntax(DataTypeSyntax):
    closeBrace: Token
    dimensions: Any
    keyword: Token
    members: Any
    openBrace: Token
    packed: Token
    signing: Token
    taggedOrSoft: Token

class StructurePattern(Pattern):
    class FieldPattern(metaclass=_metaclass):
        @property
        def field(self) -> Any: ...
        @property
        def pattern(self) -> Pattern: ...

    @property
    def patterns(self) -> list[Any]: ...

class StructurePatternMemberSyntax(SyntaxNode):
    pass

class StructurePatternSyntax(PatternSyntax):
    closeBrace: Token
    members: Any
    openBrace: Token

class StructuredAssignmentPatternExpression(AssignmentPatternExpressionBase):
    class IndexSetter(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def index(self) -> Expression: ...

    class MemberSetter(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def member(self) -> Any: ...

    class TypeSetter(metaclass=_metaclass):
        @property
        def expr(self) -> Expression: ...
        @property
        def type(self) -> Any: ...

    @property
    def defaultSetter(self) -> Expression: ...
    @property
    def indexSetters(self) -> list[Any]: ...
    @property
    def memberSetters(self) -> list[Any]: ...
    @property
    def typeSetters(self) -> list[Any]: ...

class StructuredAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: Any
    openBrace: Token

class SubroutineKind(metaclass=_metaclass):
    Function: ClassVar[SubroutineKind]
    """Value = 0"""
    Task: ClassVar[SubroutineKind]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SubroutineSymbol(Symbol, Scope):
    @property
    def arguments(self) -> list[FormalArgumentSymbol]: ...
    @property
    def body(self) -> Statement: ...
    @property
    def defaultLifetime(self) -> VariableLifetime: ...
    @property
    def flags(self) -> MethodFlags: ...
    @property
    def isVirtual(self) -> bool: ...
    @property
    def override(self) -> SubroutineSymbol: ...
    @property
    def prototype(self) -> Any: ...
    @property
    def returnType(self) -> Any: ...
    @property
    def subroutineKind(self) -> SubroutineKind: ...
    @property
    def visibility(self) -> Visibility: ...

class SuperNewDefaultedArgsExpressionSyntax(ExpressionSyntax):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token
    scopedNew: NameSyntax

class Symbol(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    @typing.overload
    def isDeclaredBefore(self, target: Symbol) -> bool | None: ...
    @typing.overload
    def isDeclaredBefore(self, location: LookupLocation) -> bool | None: ...
    def visit(self, f: typing.Any) -> None:
        """Visit a pyslang object with a callback function `f`.
        The callback function `f` should take a single argument, which is the current node being
            visited.
        The return value of `f` determines the next node to visit.
        If `f` ever returns `pyslang.VisitAction.Interrupt`, the visit is aborted and no additional
            nodes are visited.
        If `f` returns `pyslang.VisitAction.Skip`, then no child nodes of the current node are
            visited. For any other return value, including `pyslang.VisitAction.Advance`,
            the return value is ignored, and the walk continues.
        """
    @property
    def declaredType(self) -> Any: ...
    @property
    def declaringDefinition(self) -> Any: ...
    @property
    def hierarchicalPath(self) -> str: ...
    @property
    def isScope(self) -> bool: ...
    @property
    def isType(self) -> bool: ...
    @property
    def isValue(self) -> bool: ...
    @property
    def kind(self) -> SymbolKind: ...
    @property
    def lexicalPath(self) -> str: ...
    @property
    def location(self) -> SourceLocation: ...
    @property
    def name(self) -> str: ...
    @property
    def nextSibling(self) -> Symbol: ...
    @property
    def parentScope(self) -> Any: ...
    @property
    def randMode(self) -> RandMode: ...
    @property
    def sourceLibrary(self) -> SourceLibrary: ...
    @property
    def syntax(self) -> Any: ...

class SymbolKind(metaclass=_metaclass):
    AnonymousProgram: ClassVar[SymbolKind]
    """Value = 98"""
    AssertionPort: ClassVar[SymbolKind]
    """Value = 81"""
    AssociativeArrayType: ClassVar[SymbolKind]
    """Value = 16"""
    Attribute: ClassVar[SymbolKind]
    """Value = 53"""
    CHandleType: ClassVar[SymbolKind]
    """Value = 26"""
    Checker: ClassVar[SymbolKind]
    """Value = 86"""
    CheckerInstance: ClassVar[SymbolKind]
    """Value = 87"""
    CheckerInstanceBody: ClassVar[SymbolKind]
    """Value = 88"""
    ClassProperty: ClassVar[SymbolKind]
    """Value = 63"""
    ClassType: ClassVar[SymbolKind]
    """Value = 22"""
    ClockVar: ClassVar[SymbolKind]
    """Value = 83"""
    ClockingBlock: ClassVar[SymbolKind]
    """Value = 82"""
    CompilationUnit: ClassVar[SymbolKind]
    """Value = 3"""
    ConfigBlock: ClassVar[SymbolKind]
    """Value = 100"""
    ConstraintBlock: ClassVar[SymbolKind]
    """Value = 72"""
    ContinuousAssign: ClassVar[SymbolKind]
    """Value = 65"""
    CoverCross: ClassVar[SymbolKind]
    """Value = 92"""
    CoverCrossBody: ClassVar[SymbolKind]
    """Value = 93"""
    CoverageBin: ClassVar[SymbolKind]
    """Value = 94"""
    CovergroupBody: ClassVar[SymbolKind]
    """Value = 90"""
    CovergroupType: ClassVar[SymbolKind]
    """Value = 23"""
    Coverpoint: ClassVar[SymbolKind]
    """Value = 91"""
    DPIOpenArrayType: ClassVar[SymbolKind]
    """Value = 15"""
    DefParam: ClassVar[SymbolKind]
    """Value = 73"""
    DeferredMember: ClassVar[SymbolKind]
    """Value = 4"""
    Definition: ClassVar[SymbolKind]
    """Value = 2"""
    DynamicArrayType: ClassVar[SymbolKind]
    """Value = 14"""
    ElabSystemTask: ClassVar[SymbolKind]
    """Value = 66"""
    EmptyMember: ClassVar[SymbolKind]
    """Value = 6"""
    EnumType: ClassVar[SymbolKind]
    """Value = 10"""
    EnumValue: ClassVar[SymbolKind]
    """Value = 11"""
    ErrorType: ClassVar[SymbolKind]
    """Value = 36"""
    EventType: ClassVar[SymbolKind]
    """Value = 28"""
    ExplicitImport: ClassVar[SymbolKind]
    """Value = 51"""
    Field: ClassVar[SymbolKind]
    """Value = 62"""
    FixedSizeUnpackedArrayType: ClassVar[SymbolKind]
    """Value = 13"""
    FloatingType: ClassVar[SymbolKind]
    """Value = 9"""
    FormalArgument: ClassVar[SymbolKind]
    """Value = 61"""
    ForwardingTypedef: ClassVar[SymbolKind]
    """Value = 37"""
    GenerateBlock: ClassVar[SymbolKind]
    """Value = 55"""
    GenerateBlockArray: ClassVar[SymbolKind]
    """Value = 56"""
    GenericClassDef: ClassVar[SymbolKind]
    """Value = 67"""
    Genvar: ClassVar[SymbolKind]
    """Value = 54"""
    Instance: ClassVar[SymbolKind]
    """Value = 47"""
    InstanceArray: ClassVar[SymbolKind]
    """Value = 49"""
    InstanceBody: ClassVar[SymbolKind]
    """Value = 48"""
    InterfacePort: ClassVar[SymbolKind]
    """Value = 43"""
    Iterator: ClassVar[SymbolKind]
    """Value = 70"""
    LetDecl: ClassVar[SymbolKind]
    """Value = 85"""
    LocalAssertionVar: ClassVar[SymbolKind]
    """Value = 84"""
    MethodPrototype: ClassVar[SymbolKind]
    """Value = 68"""
    Modport: ClassVar[SymbolKind]
    """Value = 44"""
    ModportClocking: ClassVar[SymbolKind]
    """Value = 46"""
    ModportPort: ClassVar[SymbolKind]
    """Value = 45"""
    MultiPort: ClassVar[SymbolKind]
    """Value = 42"""
    Net: ClassVar[SymbolKind]
    """Value = 59"""
    NetAlias: ClassVar[SymbolKind]
    """Value = 99"""
    NetType: ClassVar[SymbolKind]
    """Value = 38"""
    NullType: ClassVar[SymbolKind]
    """Value = 25"""
    Package: ClassVar[SymbolKind]
    """Value = 50"""
    PackedArrayType: ClassVar[SymbolKind]
    """Value = 12"""
    PackedStructType: ClassVar[SymbolKind]
    """Value = 18"""
    PackedUnionType: ClassVar[SymbolKind]
    """Value = 20"""
    Parameter: ClassVar[SymbolKind]
    """Value = 39"""
    PatternVar: ClassVar[SymbolKind]
    """Value = 71"""
    Port: ClassVar[SymbolKind]
    """Value = 41"""
    PredefinedIntegerType: ClassVar[SymbolKind]
    """Value = 7"""
    Primitive: ClassVar[SymbolKind]
    """Value = 75"""
    PrimitiveInstance: ClassVar[SymbolKind]
    """Value = 77"""
    PrimitivePort: ClassVar[SymbolKind]
    """Value = 76"""
    ProceduralBlock: ClassVar[SymbolKind]
    """Value = 57"""
    Property: ClassVar[SymbolKind]
    """Value = 80"""
    PropertyType: ClassVar[SymbolKind]
    """Value = 33"""
    PulseStyle: ClassVar[SymbolKind]
    """Value = 96"""
    QueueType: ClassVar[SymbolKind]
    """Value = 17"""
    RandSeqProduction: ClassVar[SymbolKind]
    """Value = 89"""
    Root: ClassVar[SymbolKind]
    """Value = 1"""
    ScalarType: ClassVar[SymbolKind]
    """Value = 8"""
    Sequence: ClassVar[SymbolKind]
    """Value = 79"""
    SequenceType: ClassVar[SymbolKind]
    """Value = 32"""
    SpecifyBlock: ClassVar[SymbolKind]
    """Value = 78"""
    Specparam: ClassVar[SymbolKind]
    """Value = 74"""
    StatementBlock: ClassVar[SymbolKind]
    """Value = 58"""
    StringType: ClassVar[SymbolKind]
    """Value = 27"""
    Subroutine: ClassVar[SymbolKind]
    """Value = 64"""
    SystemTimingCheck: ClassVar[SymbolKind]
    """Value = 97"""
    TimingPath: ClassVar[SymbolKind]
    """Value = 95"""
    TransparentMember: ClassVar[SymbolKind]
    """Value = 5"""
    TypeAlias: ClassVar[SymbolKind]
    """Value = 35"""
    TypeParameter: ClassVar[SymbolKind]
    """Value = 40"""
    TypeRefType: ClassVar[SymbolKind]
    """Value = 30"""
    UnboundedType: ClassVar[SymbolKind]
    """Value = 29"""
    UninstantiatedDef: ClassVar[SymbolKind]
    """Value = 69"""
    Unknown: ClassVar[SymbolKind]
    """Value = 0"""
    UnpackedStructType: ClassVar[SymbolKind]
    """Value = 19"""
    UnpackedUnionType: ClassVar[SymbolKind]
    """Value = 21"""
    UntypedType: ClassVar[SymbolKind]
    """Value = 31"""
    Variable: ClassVar[SymbolKind]
    """Value = 60"""
    VirtualInterfaceType: ClassVar[SymbolKind]
    """Value = 34"""
    VoidType: ClassVar[SymbolKind]
    """Value = 24"""
    WildcardImport: ClassVar[SymbolKind]
    """Value = 52"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SyntaxKind(metaclass=_metaclass):
    AcceptOnPropertyExpr: ClassVar[SyntaxKind]
    """Value = 4"""
    ActionBlock: ClassVar[SyntaxKind]
    """Value = 5"""
    AddAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 6"""
    AddExpression: ClassVar[SyntaxKind]
    """Value = 7"""
    AlwaysBlock: ClassVar[SyntaxKind]
    """Value = 8"""
    AlwaysCombBlock: ClassVar[SyntaxKind]
    """Value = 9"""
    AlwaysFFBlock: ClassVar[SyntaxKind]
    """Value = 10"""
    AlwaysLatchBlock: ClassVar[SyntaxKind]
    """Value = 11"""
    AndAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 12"""
    AndPropertyExpr: ClassVar[SyntaxKind]
    """Value = 13"""
    AndSequenceExpr: ClassVar[SyntaxKind]
    """Value = 14"""
    AnonymousProgram: ClassVar[SyntaxKind]
    """Value = 15"""
    AnsiPortList: ClassVar[SyntaxKind]
    """Value = 16"""
    AnsiUdpPortList: ClassVar[SyntaxKind]
    """Value = 17"""
    ArgumentList: ClassVar[SyntaxKind]
    """Value = 18"""
    ArithmeticLeftShiftAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 19"""
    ArithmeticRightShiftAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 20"""
    ArithmeticShiftLeftExpression: ClassVar[SyntaxKind]
    """Value = 21"""
    ArithmeticShiftRightExpression: ClassVar[SyntaxKind]
    """Value = 22"""
    ArrayAndMethod: ClassVar[SyntaxKind]
    """Value = 23"""
    ArrayOrMethod: ClassVar[SyntaxKind]
    """Value = 24"""
    ArrayOrRandomizeMethodExpression: ClassVar[SyntaxKind]
    """Value = 25"""
    ArrayUniqueMethod: ClassVar[SyntaxKind]
    """Value = 26"""
    ArrayXorMethod: ClassVar[SyntaxKind]
    """Value = 27"""
    AscendingRangeSelect: ClassVar[SyntaxKind]
    """Value = 28"""
    AssertPropertyStatement: ClassVar[SyntaxKind]
    """Value = 29"""
    AssertionItemPort: ClassVar[SyntaxKind]
    """Value = 30"""
    AssertionItemPortList: ClassVar[SyntaxKind]
    """Value = 31"""
    AssignmentExpression: ClassVar[SyntaxKind]
    """Value = 32"""
    AssignmentPatternExpression: ClassVar[SyntaxKind]
    """Value = 33"""
    AssignmentPatternItem: ClassVar[SyntaxKind]
    """Value = 34"""
    AssumePropertyStatement: ClassVar[SyntaxKind]
    """Value = 35"""
    AttributeInstance: ClassVar[SyntaxKind]
    """Value = 36"""
    AttributeSpec: ClassVar[SyntaxKind]
    """Value = 37"""
    BadExpression: ClassVar[SyntaxKind]
    """Value = 38"""
    BeginKeywordsDirective: ClassVar[SyntaxKind]
    """Value = 39"""
    BinSelectWithFilterExpr: ClassVar[SyntaxKind]
    """Value = 40"""
    BinaryAndExpression: ClassVar[SyntaxKind]
    """Value = 41"""
    BinaryBinsSelectExpr: ClassVar[SyntaxKind]
    """Value = 42"""
    BinaryBlockEventExpression: ClassVar[SyntaxKind]
    """Value = 43"""
    BinaryConditionalDirectiveExpression: ClassVar[SyntaxKind]
    """Value = 44"""
    BinaryEventExpression: ClassVar[SyntaxKind]
    """Value = 45"""
    BinaryOrExpression: ClassVar[SyntaxKind]
    """Value = 46"""
    BinaryXnorExpression: ClassVar[SyntaxKind]
    """Value = 47"""
    BinaryXorExpression: ClassVar[SyntaxKind]
    """Value = 48"""
    BindDirective: ClassVar[SyntaxKind]
    """Value = 49"""
    BindTargetList: ClassVar[SyntaxKind]
    """Value = 50"""
    BinsSelectConditionExpr: ClassVar[SyntaxKind]
    """Value = 51"""
    BinsSelection: ClassVar[SyntaxKind]
    """Value = 52"""
    BitSelect: ClassVar[SyntaxKind]
    """Value = 53"""
    BitType: ClassVar[SyntaxKind]
    """Value = 54"""
    BlockCoverageEvent: ClassVar[SyntaxKind]
    """Value = 55"""
    BlockingEventTriggerStatement: ClassVar[SyntaxKind]
    """Value = 56"""
    ByteType: ClassVar[SyntaxKind]
    """Value = 57"""
    CHandleType: ClassVar[SyntaxKind]
    """Value = 58"""
    CaseEqualityExpression: ClassVar[SyntaxKind]
    """Value = 59"""
    CaseGenerate: ClassVar[SyntaxKind]
    """Value = 60"""
    CaseInequalityExpression: ClassVar[SyntaxKind]
    """Value = 61"""
    CasePropertyExpr: ClassVar[SyntaxKind]
    """Value = 62"""
    CaseStatement: ClassVar[SyntaxKind]
    """Value = 63"""
    CastExpression: ClassVar[SyntaxKind]
    """Value = 64"""
    CellConfigRule: ClassVar[SyntaxKind]
    """Value = 65"""
    CellDefineDirective: ClassVar[SyntaxKind]
    """Value = 66"""
    ChargeStrength: ClassVar[SyntaxKind]
    """Value = 67"""
    CheckerDataDeclaration: ClassVar[SyntaxKind]
    """Value = 68"""
    CheckerDeclaration: ClassVar[SyntaxKind]
    """Value = 69"""
    CheckerInstanceStatement: ClassVar[SyntaxKind]
    """Value = 70"""
    CheckerInstantiation: ClassVar[SyntaxKind]
    """Value = 71"""
    ClassDeclaration: ClassVar[SyntaxKind]
    """Value = 72"""
    ClassMethodDeclaration: ClassVar[SyntaxKind]
    """Value = 73"""
    ClassMethodPrototype: ClassVar[SyntaxKind]
    """Value = 74"""
    ClassName: ClassVar[SyntaxKind]
    """Value = 75"""
    ClassPropertyDeclaration: ClassVar[SyntaxKind]
    """Value = 76"""
    ClassSpecifier: ClassVar[SyntaxKind]
    """Value = 77"""
    ClockingDeclaration: ClassVar[SyntaxKind]
    """Value = 78"""
    ClockingDirection: ClassVar[SyntaxKind]
    """Value = 79"""
    ClockingItem: ClassVar[SyntaxKind]
    """Value = 80"""
    ClockingPropertyExpr: ClassVar[SyntaxKind]
    """Value = 81"""
    ClockingSequenceExpr: ClassVar[SyntaxKind]
    """Value = 82"""
    ClockingSkew: ClassVar[SyntaxKind]
    """Value = 83"""
    ColonExpressionClause: ClassVar[SyntaxKind]
    """Value = 84"""
    CompilationUnit: ClassVar[SyntaxKind]
    """Value = 85"""
    ConcatenationExpression: ClassVar[SyntaxKind]
    """Value = 86"""
    ConcurrentAssertionMember: ClassVar[SyntaxKind]
    """Value = 87"""
    ConditionalConstraint: ClassVar[SyntaxKind]
    """Value = 88"""
    ConditionalExpression: ClassVar[SyntaxKind]
    """Value = 89"""
    ConditionalPathDeclaration: ClassVar[SyntaxKind]
    """Value = 90"""
    ConditionalPattern: ClassVar[SyntaxKind]
    """Value = 91"""
    ConditionalPredicate: ClassVar[SyntaxKind]
    """Value = 92"""
    ConditionalPropertyExpr: ClassVar[SyntaxKind]
    """Value = 93"""
    ConditionalStatement: ClassVar[SyntaxKind]
    """Value = 94"""
    ConfigCellIdentifier: ClassVar[SyntaxKind]
    """Value = 95"""
    ConfigDeclaration: ClassVar[SyntaxKind]
    """Value = 96"""
    ConfigInstanceIdentifier: ClassVar[SyntaxKind]
    """Value = 97"""
    ConfigLiblist: ClassVar[SyntaxKind]
    """Value = 98"""
    ConfigUseClause: ClassVar[SyntaxKind]
    """Value = 99"""
    ConstraintBlock: ClassVar[SyntaxKind]
    """Value = 100"""
    ConstraintDeclaration: ClassVar[SyntaxKind]
    """Value = 101"""
    ConstraintPrototype: ClassVar[SyntaxKind]
    """Value = 102"""
    ConstructorName: ClassVar[SyntaxKind]
    """Value = 103"""
    ContinuousAssign: ClassVar[SyntaxKind]
    """Value = 104"""
    CopyClassExpression: ClassVar[SyntaxKind]
    """Value = 105"""
    CoverCross: ClassVar[SyntaxKind]
    """Value = 106"""
    CoverPropertyStatement: ClassVar[SyntaxKind]
    """Value = 107"""
    CoverSequenceStatement: ClassVar[SyntaxKind]
    """Value = 108"""
    CoverageBins: ClassVar[SyntaxKind]
    """Value = 109"""
    CoverageBinsArraySize: ClassVar[SyntaxKind]
    """Value = 110"""
    CoverageIffClause: ClassVar[SyntaxKind]
    """Value = 111"""
    CoverageOption: ClassVar[SyntaxKind]
    """Value = 112"""
    CovergroupDeclaration: ClassVar[SyntaxKind]
    """Value = 113"""
    Coverpoint: ClassVar[SyntaxKind]
    """Value = 114"""
    CycleDelay: ClassVar[SyntaxKind]
    """Value = 115"""
    DPIExport: ClassVar[SyntaxKind]
    """Value = 116"""
    DPIImport: ClassVar[SyntaxKind]
    """Value = 117"""
    DataDeclaration: ClassVar[SyntaxKind]
    """Value = 118"""
    Declarator: ClassVar[SyntaxKind]
    """Value = 119"""
    DefParam: ClassVar[SyntaxKind]
    """Value = 120"""
    DefParamAssignment: ClassVar[SyntaxKind]
    """Value = 121"""
    DefaultCaseItem: ClassVar[SyntaxKind]
    """Value = 122"""
    DefaultClockingReference: ClassVar[SyntaxKind]
    """Value = 123"""
    DefaultConfigRule: ClassVar[SyntaxKind]
    """Value = 124"""
    DefaultCoverageBinInitializer: ClassVar[SyntaxKind]
    """Value = 125"""
    DefaultDecayTimeDirective: ClassVar[SyntaxKind]
    """Value = 126"""
    DefaultDisableDeclaration: ClassVar[SyntaxKind]
    """Value = 127"""
    DefaultDistItem: ClassVar[SyntaxKind]
    """Value = 128"""
    DefaultExtendsClauseArg: ClassVar[SyntaxKind]
    """Value = 129"""
    DefaultFunctionPort: ClassVar[SyntaxKind]
    """Value = 130"""
    DefaultNetTypeDirective: ClassVar[SyntaxKind]
    """Value = 131"""
    DefaultPatternKeyExpression: ClassVar[SyntaxKind]
    """Value = 132"""
    DefaultPropertyCaseItem: ClassVar[SyntaxKind]
    """Value = 133"""
    DefaultRsCaseItem: ClassVar[SyntaxKind]
    """Value = 134"""
    DefaultSkewItem: ClassVar[SyntaxKind]
    """Value = 135"""
    DefaultTriregStrengthDirective: ClassVar[SyntaxKind]
    """Value = 136"""
    DeferredAssertion: ClassVar[SyntaxKind]
    """Value = 137"""
    DefineDirective: ClassVar[SyntaxKind]
    """Value = 138"""
    Delay3: ClassVar[SyntaxKind]
    """Value = 139"""
    DelayControl: ClassVar[SyntaxKind]
    """Value = 140"""
    DelayModeDistributedDirective: ClassVar[SyntaxKind]
    """Value = 141"""
    DelayModePathDirective: ClassVar[SyntaxKind]
    """Value = 142"""
    DelayModeUnitDirective: ClassVar[SyntaxKind]
    """Value = 143"""
    DelayModeZeroDirective: ClassVar[SyntaxKind]
    """Value = 144"""
    DelayedSequenceElement: ClassVar[SyntaxKind]
    """Value = 145"""
    DelayedSequenceExpr: ClassVar[SyntaxKind]
    """Value = 146"""
    DescendingRangeSelect: ClassVar[SyntaxKind]
    """Value = 147"""
    DisableConstraint: ClassVar[SyntaxKind]
    """Value = 148"""
    DisableForkStatement: ClassVar[SyntaxKind]
    """Value = 149"""
    DisableIff: ClassVar[SyntaxKind]
    """Value = 150"""
    DisableStatement: ClassVar[SyntaxKind]
    """Value = 151"""
    DistConstraintList: ClassVar[SyntaxKind]
    """Value = 152"""
    DistItem: ClassVar[SyntaxKind]
    """Value = 153"""
    DistWeight: ClassVar[SyntaxKind]
    """Value = 154"""
    DivideAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 155"""
    DivideExpression: ClassVar[SyntaxKind]
    """Value = 156"""
    DividerClause: ClassVar[SyntaxKind]
    """Value = 157"""
    DoWhileStatement: ClassVar[SyntaxKind]
    """Value = 158"""
    DotMemberClause: ClassVar[SyntaxKind]
    """Value = 159"""
    DriveStrength: ClassVar[SyntaxKind]
    """Value = 160"""
    EdgeControlSpecifier: ClassVar[SyntaxKind]
    """Value = 161"""
    EdgeDescriptor: ClassVar[SyntaxKind]
    """Value = 162"""
    EdgeSensitivePathSuffix: ClassVar[SyntaxKind]
    """Value = 163"""
    ElabSystemTask: ClassVar[SyntaxKind]
    """Value = 164"""
    ElementSelect: ClassVar[SyntaxKind]
    """Value = 165"""
    ElementSelectExpression: ClassVar[SyntaxKind]
    """Value = 166"""
    ElsIfDirective: ClassVar[SyntaxKind]
    """Value = 167"""
    ElseClause: ClassVar[SyntaxKind]
    """Value = 168"""
    ElseConstraintClause: ClassVar[SyntaxKind]
    """Value = 169"""
    ElseDirective: ClassVar[SyntaxKind]
    """Value = 170"""
    ElsePropertyClause: ClassVar[SyntaxKind]
    """Value = 171"""
    EmptyArgument: ClassVar[SyntaxKind]
    """Value = 172"""
    EmptyIdentifierName: ClassVar[SyntaxKind]
    """Value = 173"""
    EmptyMember: ClassVar[SyntaxKind]
    """Value = 174"""
    EmptyNonAnsiPort: ClassVar[SyntaxKind]
    """Value = 175"""
    EmptyPortConnection: ClassVar[SyntaxKind]
    """Value = 176"""
    EmptyQueueExpression: ClassVar[SyntaxKind]
    """Value = 177"""
    EmptyStatement: ClassVar[SyntaxKind]
    """Value = 178"""
    EmptyTimingCheckArg: ClassVar[SyntaxKind]
    """Value = 179"""
    EndCellDefineDirective: ClassVar[SyntaxKind]
    """Value = 180"""
    EndIfDirective: ClassVar[SyntaxKind]
    """Value = 181"""
    EndKeywordsDirective: ClassVar[SyntaxKind]
    """Value = 182"""
    EndProtectDirective: ClassVar[SyntaxKind]
    """Value = 183"""
    EndProtectedDirective: ClassVar[SyntaxKind]
    """Value = 184"""
    EnumType: ClassVar[SyntaxKind]
    """Value = 185"""
    EqualityExpression: ClassVar[SyntaxKind]
    """Value = 186"""
    EqualsAssertionArgClause: ClassVar[SyntaxKind]
    """Value = 187"""
    EqualsTypeClause: ClassVar[SyntaxKind]
    """Value = 188"""
    EqualsValueClause: ClassVar[SyntaxKind]
    """Value = 189"""
    EventControl: ClassVar[SyntaxKind]
    """Value = 190"""
    EventControlWithExpression: ClassVar[SyntaxKind]
    """Value = 191"""
    EventType: ClassVar[SyntaxKind]
    """Value = 192"""
    ExpectPropertyStatement: ClassVar[SyntaxKind]
    """Value = 193"""
    ExplicitAnsiPort: ClassVar[SyntaxKind]
    """Value = 194"""
    ExplicitNonAnsiPort: ClassVar[SyntaxKind]
    """Value = 195"""
    ExpressionConstraint: ClassVar[SyntaxKind]
    """Value = 196"""
    ExpressionCoverageBinInitializer: ClassVar[SyntaxKind]
    """Value = 197"""
    ExpressionOrDist: ClassVar[SyntaxKind]
    """Value = 198"""
    ExpressionPattern: ClassVar[SyntaxKind]
    """Value = 199"""
    ExpressionStatement: ClassVar[SyntaxKind]
    """Value = 200"""
    ExpressionTimingCheckArg: ClassVar[SyntaxKind]
    """Value = 201"""
    ExtendsClause: ClassVar[SyntaxKind]
    """Value = 202"""
    ExternInterfaceMethod: ClassVar[SyntaxKind]
    """Value = 203"""
    ExternModuleDecl: ClassVar[SyntaxKind]
    """Value = 204"""
    ExternUdpDecl: ClassVar[SyntaxKind]
    """Value = 205"""
    FilePathSpec: ClassVar[SyntaxKind]
    """Value = 206"""
    FinalBlock: ClassVar[SyntaxKind]
    """Value = 207"""
    FirstMatchSequenceExpr: ClassVar[SyntaxKind]
    """Value = 208"""
    FollowedByPropertyExpr: ClassVar[SyntaxKind]
    """Value = 209"""
    ForLoopStatement: ClassVar[SyntaxKind]
    """Value = 210"""
    ForVariableDeclaration: ClassVar[SyntaxKind]
    """Value = 211"""
    ForeachLoopList: ClassVar[SyntaxKind]
    """Value = 212"""
    ForeachLoopStatement: ClassVar[SyntaxKind]
    """Value = 213"""
    ForeverStatement: ClassVar[SyntaxKind]
    """Value = 214"""
    ForwardTypeRestriction: ClassVar[SyntaxKind]
    """Value = 215"""
    ForwardTypedefDeclaration: ClassVar[SyntaxKind]
    """Value = 216"""
    FunctionDeclaration: ClassVar[SyntaxKind]
    """Value = 217"""
    FunctionPort: ClassVar[SyntaxKind]
    """Value = 218"""
    FunctionPortList: ClassVar[SyntaxKind]
    """Value = 219"""
    FunctionPrototype: ClassVar[SyntaxKind]
    """Value = 220"""
    GenerateBlock: ClassVar[SyntaxKind]
    """Value = 221"""
    GenerateRegion: ClassVar[SyntaxKind]
    """Value = 222"""
    GenvarDeclaration: ClassVar[SyntaxKind]
    """Value = 223"""
    GreaterThanEqualExpression: ClassVar[SyntaxKind]
    """Value = 224"""
    GreaterThanExpression: ClassVar[SyntaxKind]
    """Value = 225"""
    HierarchicalInstance: ClassVar[SyntaxKind]
    """Value = 226"""
    HierarchyInstantiation: ClassVar[SyntaxKind]
    """Value = 227"""
    IdWithExprCoverageBinInitializer: ClassVar[SyntaxKind]
    """Value = 228"""
    IdentifierName: ClassVar[SyntaxKind]
    """Value = 229"""
    IdentifierSelectName: ClassVar[SyntaxKind]
    """Value = 230"""
    IfDefDirective: ClassVar[SyntaxKind]
    """Value = 231"""
    IfGenerate: ClassVar[SyntaxKind]
    """Value = 232"""
    IfNDefDirective: ClassVar[SyntaxKind]
    """Value = 233"""
    IfNonePathDeclaration: ClassVar[SyntaxKind]
    """Value = 234"""
    IffEventClause: ClassVar[SyntaxKind]
    """Value = 235"""
    IffPropertyExpr: ClassVar[SyntaxKind]
    """Value = 236"""
    ImmediateAssertStatement: ClassVar[SyntaxKind]
    """Value = 237"""
    ImmediateAssertionMember: ClassVar[SyntaxKind]
    """Value = 238"""
    ImmediateAssumeStatement: ClassVar[SyntaxKind]
    """Value = 239"""
    ImmediateCoverStatement: ClassVar[SyntaxKind]
    """Value = 240"""
    ImplementsClause: ClassVar[SyntaxKind]
    """Value = 241"""
    ImplicationConstraint: ClassVar[SyntaxKind]
    """Value = 242"""
    ImplicationPropertyExpr: ClassVar[SyntaxKind]
    """Value = 243"""
    ImplicitAnsiPort: ClassVar[SyntaxKind]
    """Value = 244"""
    ImplicitEventControl: ClassVar[SyntaxKind]
    """Value = 245"""
    ImplicitNonAnsiPort: ClassVar[SyntaxKind]
    """Value = 246"""
    ImplicitType: ClassVar[SyntaxKind]
    """Value = 247"""
    ImpliesPropertyExpr: ClassVar[SyntaxKind]
    """Value = 248"""
    IncludeDirective: ClassVar[SyntaxKind]
    """Value = 249"""
    InequalityExpression: ClassVar[SyntaxKind]
    """Value = 250"""
    InitialBlock: ClassVar[SyntaxKind]
    """Value = 251"""
    InsideExpression: ClassVar[SyntaxKind]
    """Value = 252"""
    InstanceConfigRule: ClassVar[SyntaxKind]
    """Value = 253"""
    InstanceName: ClassVar[SyntaxKind]
    """Value = 254"""
    IntType: ClassVar[SyntaxKind]
    """Value = 255"""
    IntegerLiteralExpression: ClassVar[SyntaxKind]
    """Value = 256"""
    IntegerType: ClassVar[SyntaxKind]
    """Value = 257"""
    IntegerVectorExpression: ClassVar[SyntaxKind]
    """Value = 258"""
    InterfaceDeclaration: ClassVar[SyntaxKind]
    """Value = 259"""
    InterfaceHeader: ClassVar[SyntaxKind]
    """Value = 260"""
    InterfacePortHeader: ClassVar[SyntaxKind]
    """Value = 261"""
    IntersectClause: ClassVar[SyntaxKind]
    """Value = 262"""
    IntersectSequenceExpr: ClassVar[SyntaxKind]
    """Value = 263"""
    InvocationExpression: ClassVar[SyntaxKind]
    """Value = 264"""
    JumpStatement: ClassVar[SyntaxKind]
    """Value = 265"""
    LessThanEqualExpression: ClassVar[SyntaxKind]
    """Value = 266"""
    LessThanExpression: ClassVar[SyntaxKind]
    """Value = 267"""
    LetDeclaration: ClassVar[SyntaxKind]
    """Value = 268"""
    LibraryDeclaration: ClassVar[SyntaxKind]
    """Value = 269"""
    LibraryIncDirClause: ClassVar[SyntaxKind]
    """Value = 270"""
    LibraryIncludeStatement: ClassVar[SyntaxKind]
    """Value = 271"""
    LibraryMap: ClassVar[SyntaxKind]
    """Value = 272"""
    LineDirective: ClassVar[SyntaxKind]
    """Value = 273"""
    LocalScope: ClassVar[SyntaxKind]
    """Value = 274"""
    LocalVariableDeclaration: ClassVar[SyntaxKind]
    """Value = 275"""
    LogicType: ClassVar[SyntaxKind]
    """Value = 276"""
    LogicalAndExpression: ClassVar[SyntaxKind]
    """Value = 277"""
    LogicalEquivalenceExpression: ClassVar[SyntaxKind]
    """Value = 278"""
    LogicalImplicationExpression: ClassVar[SyntaxKind]
    """Value = 279"""
    LogicalLeftShiftAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 280"""
    LogicalOrExpression: ClassVar[SyntaxKind]
    """Value = 281"""
    LogicalRightShiftAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 282"""
    LogicalShiftLeftExpression: ClassVar[SyntaxKind]
    """Value = 283"""
    LogicalShiftRightExpression: ClassVar[SyntaxKind]
    """Value = 284"""
    LongIntType: ClassVar[SyntaxKind]
    """Value = 285"""
    LoopConstraint: ClassVar[SyntaxKind]
    """Value = 286"""
    LoopGenerate: ClassVar[SyntaxKind]
    """Value = 287"""
    LoopStatement: ClassVar[SyntaxKind]
    """Value = 288"""
    MacroActualArgument: ClassVar[SyntaxKind]
    """Value = 289"""
    MacroActualArgumentList: ClassVar[SyntaxKind]
    """Value = 290"""
    MacroArgumentDefault: ClassVar[SyntaxKind]
    """Value = 291"""
    MacroFormalArgument: ClassVar[SyntaxKind]
    """Value = 292"""
    MacroFormalArgumentList: ClassVar[SyntaxKind]
    """Value = 293"""
    MacroUsage: ClassVar[SyntaxKind]
    """Value = 294"""
    MatchesClause: ClassVar[SyntaxKind]
    """Value = 295"""
    MemberAccessExpression: ClassVar[SyntaxKind]
    """Value = 296"""
    MinTypMaxExpression: ClassVar[SyntaxKind]
    """Value = 297"""
    ModAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 298"""
    ModExpression: ClassVar[SyntaxKind]
    """Value = 299"""
    ModportClockingPort: ClassVar[SyntaxKind]
    """Value = 300"""
    ModportDeclaration: ClassVar[SyntaxKind]
    """Value = 301"""
    ModportExplicitPort: ClassVar[SyntaxKind]
    """Value = 302"""
    ModportItem: ClassVar[SyntaxKind]
    """Value = 303"""
    ModportNamedPort: ClassVar[SyntaxKind]
    """Value = 304"""
    ModportSimplePortList: ClassVar[SyntaxKind]
    """Value = 305"""
    ModportSubroutinePort: ClassVar[SyntaxKind]
    """Value = 306"""
    ModportSubroutinePortList: ClassVar[SyntaxKind]
    """Value = 307"""
    ModuleDeclaration: ClassVar[SyntaxKind]
    """Value = 308"""
    ModuleHeader: ClassVar[SyntaxKind]
    """Value = 309"""
    MultipleConcatenationExpression: ClassVar[SyntaxKind]
    """Value = 310"""
    MultiplyAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 311"""
    MultiplyExpression: ClassVar[SyntaxKind]
    """Value = 312"""
    NameValuePragmaExpression: ClassVar[SyntaxKind]
    """Value = 313"""
    NamedArgument: ClassVar[SyntaxKind]
    """Value = 314"""
    NamedBlockClause: ClassVar[SyntaxKind]
    """Value = 315"""
    NamedConditionalDirectiveExpression: ClassVar[SyntaxKind]
    """Value = 316"""
    NamedLabel: ClassVar[SyntaxKind]
    """Value = 317"""
    NamedParamAssignment: ClassVar[SyntaxKind]
    """Value = 318"""
    NamedPortConnection: ClassVar[SyntaxKind]
    """Value = 319"""
    NamedStructurePatternMember: ClassVar[SyntaxKind]
    """Value = 320"""
    NamedType: ClassVar[SyntaxKind]
    """Value = 321"""
    NetAlias: ClassVar[SyntaxKind]
    """Value = 322"""
    NetDeclaration: ClassVar[SyntaxKind]
    """Value = 323"""
    NetPortHeader: ClassVar[SyntaxKind]
    """Value = 324"""
    NetTypeDeclaration: ClassVar[SyntaxKind]
    """Value = 325"""
    NewArrayExpression: ClassVar[SyntaxKind]
    """Value = 326"""
    NewClassExpression: ClassVar[SyntaxKind]
    """Value = 327"""
    NoUnconnectedDriveDirective: ClassVar[SyntaxKind]
    """Value = 328"""
    NonAnsiPortList: ClassVar[SyntaxKind]
    """Value = 329"""
    NonAnsiUdpPortList: ClassVar[SyntaxKind]
    """Value = 330"""
    NonblockingAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 331"""
    NonblockingEventTriggerStatement: ClassVar[SyntaxKind]
    """Value = 332"""
    NullLiteralExpression: ClassVar[SyntaxKind]
    """Value = 333"""
    NumberPragmaExpression: ClassVar[SyntaxKind]
    """Value = 334"""
    OneStepDelay: ClassVar[SyntaxKind]
    """Value = 335"""
    OrAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 336"""
    OrPropertyExpr: ClassVar[SyntaxKind]
    """Value = 337"""
    OrSequenceExpr: ClassVar[SyntaxKind]
    """Value = 338"""
    OrderedArgument: ClassVar[SyntaxKind]
    """Value = 339"""
    OrderedParamAssignment: ClassVar[SyntaxKind]
    """Value = 340"""
    OrderedPortConnection: ClassVar[SyntaxKind]
    """Value = 341"""
    OrderedStructurePatternMember: ClassVar[SyntaxKind]
    """Value = 342"""
    PackageDeclaration: ClassVar[SyntaxKind]
    """Value = 343"""
    PackageExportAllDeclaration: ClassVar[SyntaxKind]
    """Value = 344"""
    PackageExportDeclaration: ClassVar[SyntaxKind]
    """Value = 345"""
    PackageHeader: ClassVar[SyntaxKind]
    """Value = 346"""
    PackageImportDeclaration: ClassVar[SyntaxKind]
    """Value = 347"""
    PackageImportItem: ClassVar[SyntaxKind]
    """Value = 348"""
    ParallelBlockStatement: ClassVar[SyntaxKind]
    """Value = 349"""
    ParameterDeclaration: ClassVar[SyntaxKind]
    """Value = 350"""
    ParameterDeclarationStatement: ClassVar[SyntaxKind]
    """Value = 351"""
    ParameterPortList: ClassVar[SyntaxKind]
    """Value = 352"""
    ParameterValueAssignment: ClassVar[SyntaxKind]
    """Value = 353"""
    ParenExpressionList: ClassVar[SyntaxKind]
    """Value = 354"""
    ParenPragmaExpression: ClassVar[SyntaxKind]
    """Value = 355"""
    ParenthesizedBinsSelectExpr: ClassVar[SyntaxKind]
    """Value = 356"""
    ParenthesizedConditionalDirectiveExpression: ClassVar[SyntaxKind]
    """Value = 357"""
    ParenthesizedEventExpression: ClassVar[SyntaxKind]
    """Value = 358"""
    ParenthesizedExpression: ClassVar[SyntaxKind]
    """Value = 359"""
    ParenthesizedPattern: ClassVar[SyntaxKind]
    """Value = 360"""
    ParenthesizedPropertyExpr: ClassVar[SyntaxKind]
    """Value = 361"""
    ParenthesizedSequenceExpr: ClassVar[SyntaxKind]
    """Value = 362"""
    PathDeclaration: ClassVar[SyntaxKind]
    """Value = 363"""
    PathDescription: ClassVar[SyntaxKind]
    """Value = 364"""
    PatternCaseItem: ClassVar[SyntaxKind]
    """Value = 365"""
    PortConcatenation: ClassVar[SyntaxKind]
    """Value = 366"""
    PortDeclaration: ClassVar[SyntaxKind]
    """Value = 367"""
    PortReference: ClassVar[SyntaxKind]
    """Value = 368"""
    PostdecrementExpression: ClassVar[SyntaxKind]
    """Value = 369"""
    PostincrementExpression: ClassVar[SyntaxKind]
    """Value = 370"""
    PowerExpression: ClassVar[SyntaxKind]
    """Value = 371"""
    PragmaDirective: ClassVar[SyntaxKind]
    """Value = 372"""
    PrimaryBlockEventExpression: ClassVar[SyntaxKind]
    """Value = 373"""
    PrimitiveInstantiation: ClassVar[SyntaxKind]
    """Value = 374"""
    ProceduralAssignStatement: ClassVar[SyntaxKind]
    """Value = 375"""
    ProceduralDeassignStatement: ClassVar[SyntaxKind]
    """Value = 376"""
    ProceduralForceStatement: ClassVar[SyntaxKind]
    """Value = 377"""
    ProceduralReleaseStatement: ClassVar[SyntaxKind]
    """Value = 378"""
    Production: ClassVar[SyntaxKind]
    """Value = 379"""
    ProgramDeclaration: ClassVar[SyntaxKind]
    """Value = 380"""
    ProgramHeader: ClassVar[SyntaxKind]
    """Value = 381"""
    PropertyDeclaration: ClassVar[SyntaxKind]
    """Value = 382"""
    PropertySpec: ClassVar[SyntaxKind]
    """Value = 383"""
    PropertyType: ClassVar[SyntaxKind]
    """Value = 384"""
    ProtectDirective: ClassVar[SyntaxKind]
    """Value = 385"""
    ProtectedDirective: ClassVar[SyntaxKind]
    """Value = 386"""
    PullStrength: ClassVar[SyntaxKind]
    """Value = 387"""
    PulseStyleDeclaration: ClassVar[SyntaxKind]
    """Value = 388"""
    QueueDimensionSpecifier: ClassVar[SyntaxKind]
    """Value = 389"""
    RandCaseItem: ClassVar[SyntaxKind]
    """Value = 390"""
    RandCaseStatement: ClassVar[SyntaxKind]
    """Value = 391"""
    RandJoinClause: ClassVar[SyntaxKind]
    """Value = 392"""
    RandSequenceStatement: ClassVar[SyntaxKind]
    """Value = 393"""
    RangeCoverageBinInitializer: ClassVar[SyntaxKind]
    """Value = 394"""
    RangeDimensionSpecifier: ClassVar[SyntaxKind]
    """Value = 395"""
    RangeList: ClassVar[SyntaxKind]
    """Value = 396"""
    RealLiteralExpression: ClassVar[SyntaxKind]
    """Value = 397"""
    RealTimeType: ClassVar[SyntaxKind]
    """Value = 398"""
    RealType: ClassVar[SyntaxKind]
    """Value = 399"""
    RegType: ClassVar[SyntaxKind]
    """Value = 400"""
    RepeatedEventControl: ClassVar[SyntaxKind]
    """Value = 401"""
    ReplicatedAssignmentPattern: ClassVar[SyntaxKind]
    """Value = 402"""
    ResetAllDirective: ClassVar[SyntaxKind]
    """Value = 403"""
    RestrictPropertyStatement: ClassVar[SyntaxKind]
    """Value = 404"""
    ReturnStatement: ClassVar[SyntaxKind]
    """Value = 405"""
    RootScope: ClassVar[SyntaxKind]
    """Value = 406"""
    RsCase: ClassVar[SyntaxKind]
    """Value = 407"""
    RsCodeBlock: ClassVar[SyntaxKind]
    """Value = 408"""
    RsElseClause: ClassVar[SyntaxKind]
    """Value = 409"""
    RsIfElse: ClassVar[SyntaxKind]
    """Value = 410"""
    RsProdItem: ClassVar[SyntaxKind]
    """Value = 411"""
    RsRepeat: ClassVar[SyntaxKind]
    """Value = 412"""
    RsRule: ClassVar[SyntaxKind]
    """Value = 413"""
    RsWeightClause: ClassVar[SyntaxKind]
    """Value = 414"""
    SUntilPropertyExpr: ClassVar[SyntaxKind]
    """Value = 415"""
    SUntilWithPropertyExpr: ClassVar[SyntaxKind]
    """Value = 416"""
    ScopedName: ClassVar[SyntaxKind]
    """Value = 417"""
    SeparatedList: ClassVar[SyntaxKind]
    """Value = 3"""
    SequenceDeclaration: ClassVar[SyntaxKind]
    """Value = 418"""
    SequenceMatchList: ClassVar[SyntaxKind]
    """Value = 419"""
    SequenceRepetition: ClassVar[SyntaxKind]
    """Value = 420"""
    SequenceType: ClassVar[SyntaxKind]
    """Value = 421"""
    SequentialBlockStatement: ClassVar[SyntaxKind]
    """Value = 422"""
    ShortIntType: ClassVar[SyntaxKind]
    """Value = 423"""
    ShortRealType: ClassVar[SyntaxKind]
    """Value = 424"""
    SignalEventExpression: ClassVar[SyntaxKind]
    """Value = 425"""
    SignedCastExpression: ClassVar[SyntaxKind]
    """Value = 426"""
    SimpleAssignmentPattern: ClassVar[SyntaxKind]
    """Value = 427"""
    SimpleBinsSelectExpr: ClassVar[SyntaxKind]
    """Value = 428"""
    SimplePathSuffix: ClassVar[SyntaxKind]
    """Value = 429"""
    SimplePragmaExpression: ClassVar[SyntaxKind]
    """Value = 430"""
    SimplePropertyExpr: ClassVar[SyntaxKind]
    """Value = 431"""
    SimpleRangeSelect: ClassVar[SyntaxKind]
    """Value = 432"""
    SimpleSequenceExpr: ClassVar[SyntaxKind]
    """Value = 433"""
    SolveBeforeConstraint: ClassVar[SyntaxKind]
    """Value = 434"""
    SpecifyBlock: ClassVar[SyntaxKind]
    """Value = 435"""
    SpecparamDeclaration: ClassVar[SyntaxKind]
    """Value = 436"""
    SpecparamDeclarator: ClassVar[SyntaxKind]
    """Value = 437"""
    StandardCaseItem: ClassVar[SyntaxKind]
    """Value = 438"""
    StandardPropertyCaseItem: ClassVar[SyntaxKind]
    """Value = 439"""
    StandardRsCaseItem: ClassVar[SyntaxKind]
    """Value = 440"""
    StreamExpression: ClassVar[SyntaxKind]
    """Value = 441"""
    StreamExpressionWithRange: ClassVar[SyntaxKind]
    """Value = 442"""
    StreamingConcatenationExpression: ClassVar[SyntaxKind]
    """Value = 443"""
    StringLiteralExpression: ClassVar[SyntaxKind]
    """Value = 444"""
    StringType: ClassVar[SyntaxKind]
    """Value = 445"""
    StrongWeakPropertyExpr: ClassVar[SyntaxKind]
    """Value = 446"""
    StructType: ClassVar[SyntaxKind]
    """Value = 447"""
    StructUnionMember: ClassVar[SyntaxKind]
    """Value = 448"""
    StructurePattern: ClassVar[SyntaxKind]
    """Value = 449"""
    StructuredAssignmentPattern: ClassVar[SyntaxKind]
    """Value = 450"""
    SubtractAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 451"""
    SubtractExpression: ClassVar[SyntaxKind]
    """Value = 452"""
    SuperHandle: ClassVar[SyntaxKind]
    """Value = 453"""
    SuperNewDefaultedArgsExpression: ClassVar[SyntaxKind]
    """Value = 454"""
    SyntaxList: ClassVar[SyntaxKind]
    """Value = 1"""
    SystemName: ClassVar[SyntaxKind]
    """Value = 455"""
    SystemTimingCheck: ClassVar[SyntaxKind]
    """Value = 456"""
    TaggedPattern: ClassVar[SyntaxKind]
    """Value = 457"""
    TaggedUnionExpression: ClassVar[SyntaxKind]
    """Value = 458"""
    TaskDeclaration: ClassVar[SyntaxKind]
    """Value = 459"""
    ThisHandle: ClassVar[SyntaxKind]
    """Value = 460"""
    ThroughoutSequenceExpr: ClassVar[SyntaxKind]
    """Value = 461"""
    TimeLiteralExpression: ClassVar[SyntaxKind]
    """Value = 462"""
    TimeScaleDirective: ClassVar[SyntaxKind]
    """Value = 463"""
    TimeType: ClassVar[SyntaxKind]
    """Value = 464"""
    TimeUnitsDeclaration: ClassVar[SyntaxKind]
    """Value = 465"""
    TimingCheckEventArg: ClassVar[SyntaxKind]
    """Value = 466"""
    TimingCheckEventCondition: ClassVar[SyntaxKind]
    """Value = 467"""
    TimingControlExpression: ClassVar[SyntaxKind]
    """Value = 468"""
    TimingControlStatement: ClassVar[SyntaxKind]
    """Value = 469"""
    TokenList: ClassVar[SyntaxKind]
    """Value = 2"""
    TransListCoverageBinInitializer: ClassVar[SyntaxKind]
    """Value = 470"""
    TransRange: ClassVar[SyntaxKind]
    """Value = 471"""
    TransRepeatRange: ClassVar[SyntaxKind]
    """Value = 472"""
    TransSet: ClassVar[SyntaxKind]
    """Value = 473"""
    TypeAssignment: ClassVar[SyntaxKind]
    """Value = 474"""
    TypeParameterDeclaration: ClassVar[SyntaxKind]
    """Value = 475"""
    TypeReference: ClassVar[SyntaxKind]
    """Value = 476"""
    TypedefDeclaration: ClassVar[SyntaxKind]
    """Value = 477"""
    UdpBody: ClassVar[SyntaxKind]
    """Value = 478"""
    UdpDeclaration: ClassVar[SyntaxKind]
    """Value = 479"""
    UdpEdgeField: ClassVar[SyntaxKind]
    """Value = 480"""
    UdpEntry: ClassVar[SyntaxKind]
    """Value = 481"""
    UdpInitialStmt: ClassVar[SyntaxKind]
    """Value = 482"""
    UdpInputPortDecl: ClassVar[SyntaxKind]
    """Value = 483"""
    UdpOutputPortDecl: ClassVar[SyntaxKind]
    """Value = 484"""
    UdpSimpleField: ClassVar[SyntaxKind]
    """Value = 485"""
    UnaryBinsSelectExpr: ClassVar[SyntaxKind]
    """Value = 486"""
    UnaryBitwiseAndExpression: ClassVar[SyntaxKind]
    """Value = 487"""
    UnaryBitwiseNandExpression: ClassVar[SyntaxKind]
    """Value = 488"""
    UnaryBitwiseNorExpression: ClassVar[SyntaxKind]
    """Value = 489"""
    UnaryBitwiseNotExpression: ClassVar[SyntaxKind]
    """Value = 490"""
    UnaryBitwiseOrExpression: ClassVar[SyntaxKind]
    """Value = 491"""
    UnaryBitwiseXnorExpression: ClassVar[SyntaxKind]
    """Value = 492"""
    UnaryBitwiseXorExpression: ClassVar[SyntaxKind]
    """Value = 493"""
    UnaryConditionalDirectiveExpression: ClassVar[SyntaxKind]
    """Value = 494"""
    UnaryLogicalNotExpression: ClassVar[SyntaxKind]
    """Value = 495"""
    UnaryMinusExpression: ClassVar[SyntaxKind]
    """Value = 496"""
    UnaryPlusExpression: ClassVar[SyntaxKind]
    """Value = 497"""
    UnaryPredecrementExpression: ClassVar[SyntaxKind]
    """Value = 498"""
    UnaryPreincrementExpression: ClassVar[SyntaxKind]
    """Value = 499"""
    UnaryPropertyExpr: ClassVar[SyntaxKind]
    """Value = 500"""
    UnarySelectPropertyExpr: ClassVar[SyntaxKind]
    """Value = 501"""
    UnbasedUnsizedLiteralExpression: ClassVar[SyntaxKind]
    """Value = 502"""
    UnconnectedDriveDirective: ClassVar[SyntaxKind]
    """Value = 503"""
    UndefDirective: ClassVar[SyntaxKind]
    """Value = 504"""
    UndefineAllDirective: ClassVar[SyntaxKind]
    """Value = 505"""
    UnionType: ClassVar[SyntaxKind]
    """Value = 506"""
    UniquenessConstraint: ClassVar[SyntaxKind]
    """Value = 507"""
    UnitScope: ClassVar[SyntaxKind]
    """Value = 508"""
    Unknown: ClassVar[SyntaxKind]
    """Value = 0"""
    UntilPropertyExpr: ClassVar[SyntaxKind]
    """Value = 509"""
    UntilWithPropertyExpr: ClassVar[SyntaxKind]
    """Value = 510"""
    Untyped: ClassVar[SyntaxKind]
    """Value = 511"""
    UserDefinedNetDeclaration: ClassVar[SyntaxKind]
    """Value = 512"""
    ValueRangeExpression: ClassVar[SyntaxKind]
    """Value = 513"""
    VariableDimension: ClassVar[SyntaxKind]
    """Value = 514"""
    VariablePattern: ClassVar[SyntaxKind]
    """Value = 515"""
    VariablePortHeader: ClassVar[SyntaxKind]
    """Value = 516"""
    VirtualInterfaceType: ClassVar[SyntaxKind]
    """Value = 517"""
    VoidCastedCallStatement: ClassVar[SyntaxKind]
    """Value = 518"""
    VoidType: ClassVar[SyntaxKind]
    """Value = 519"""
    WaitForkStatement: ClassVar[SyntaxKind]
    """Value = 520"""
    WaitOrderStatement: ClassVar[SyntaxKind]
    """Value = 521"""
    WaitStatement: ClassVar[SyntaxKind]
    """Value = 522"""
    WildcardDimensionSpecifier: ClassVar[SyntaxKind]
    """Value = 523"""
    WildcardEqualityExpression: ClassVar[SyntaxKind]
    """Value = 524"""
    WildcardInequalityExpression: ClassVar[SyntaxKind]
    """Value = 525"""
    WildcardLiteralExpression: ClassVar[SyntaxKind]
    """Value = 526"""
    WildcardPattern: ClassVar[SyntaxKind]
    """Value = 527"""
    WildcardPortConnection: ClassVar[SyntaxKind]
    """Value = 528"""
    WildcardPortList: ClassVar[SyntaxKind]
    """Value = 529"""
    WildcardUdpPortList: ClassVar[SyntaxKind]
    """Value = 530"""
    WithClause: ClassVar[SyntaxKind]
    """Value = 531"""
    WithFunctionClause: ClassVar[SyntaxKind]
    """Value = 532"""
    WithFunctionSample: ClassVar[SyntaxKind]
    """Value = 533"""
    WithinSequenceExpr: ClassVar[SyntaxKind]
    """Value = 534"""
    XorAssignmentExpression: ClassVar[SyntaxKind]
    """Value = 535"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SyntaxNode(metaclass=_metaclass):
    def __getitem__(self, arg0: int) -> typing.Any: ...
    def __iter__(self) -> typing.Iterator[typing.Any]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def getFirstToken(self) -> Token: ...
    def getLastToken(self) -> Token: ...
    def isEquivalentTo(self, other: SyntaxNode) -> bool: ...
    def visit(self, f: typing.Any) -> None:
        """Visit a pyslang object with a callback function `f`.
        The callback function `f` should take a single argument, which is the current node being
            visited.
        The return value of `f` determines the next node to visit.
        If `f` ever returns `pyslang.VisitAction.Interrupt`, the visit is aborted and no additional
            nodes are visited.
        If `f` returns `pyslang.VisitAction.Skip`, then no child nodes of the current node are
            visited. For any other return value, including `pyslang.VisitAction.Advance`,
            the return value is ignored, and the walk continues.
        """
    @property
    def kind(self) -> SyntaxKind: ...
    @property
    def parent(self) -> SyntaxNode: ...
    @property
    def sourceRange(self) -> SourceRange: ...

class SyntaxPrinter(metaclass=_metaclass):
    @staticmethod
    def printFile(tree: SyntaxTree) -> str: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, sourceManager: SourceManager) -> None: ...
    def append(self, text: str) -> SyntaxPrinter: ...
    @typing.overload
    def print(self, trivia: Trivia) -> SyntaxPrinter: ...
    @typing.overload
    def print(self, token: Token) -> SyntaxPrinter: ...
    @typing.overload
    def print(self, node: SyntaxNode) -> SyntaxPrinter: ...
    @typing.overload
    def print(self, tree: SyntaxTree) -> SyntaxPrinter: ...
    def setExpandIncludes(self, expand: bool) -> SyntaxPrinter: ...
    def setExpandMacros(self, expand: bool) -> SyntaxPrinter: ...
    def setIncludeComments(self, include: bool) -> SyntaxPrinter: ...
    def setIncludeDirectives(self, include: bool) -> SyntaxPrinter: ...
    def setIncludeMissing(self, include: bool) -> SyntaxPrinter: ...
    def setIncludeSkipped(self, include: bool) -> SyntaxPrinter: ...
    def setIncludeTrivia(self, include: bool) -> SyntaxPrinter: ...
    def setSquashNewlines(self, include: bool) -> SyntaxPrinter: ...
    def str(self) -> str: ...

class SyntaxRewriter(metaclass=_metaclass):
    def insert_after(self, arg0: SyntaxNode, arg1: SyntaxNode) -> None: ...
    def insert_at_back(self, list: Any, newNode: SyntaxNode, separator: Token = ...) -> None: ...
    def insert_at_front(self, list: Any, newNode: SyntaxNode, separator: Token = ...) -> None: ...
    def insert_before(self, arg0: SyntaxNode, arg1: SyntaxNode) -> None: ...
    def remove(self, arg0: SyntaxNode) -> None: ...
    def replace(self, arg0: SyntaxNode, arg1: SyntaxNode) -> None: ...
    @property
    def factory(self) -> Any: ...

class SyntaxTree(metaclass=_metaclass):
    @staticmethod
    def fromBuffer(
        buffer: SourceBuffer,
        sourceManager: SourceManager,
        options: Bag = ...,
        inheritedMacros: list[Any] = [],
    ) -> SyntaxTree: ...
    @staticmethod
    def fromBuffers(
        buffers: list[SourceBuffer],
        sourceManager: SourceManager,
        options: Bag = ...,
        inheritedMacros: list[Any] = [],
    ) -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromFile(path: str) -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromFile(path: str, sourceManager: SourceManager, options: Bag = ...) -> SyntaxTree: ...
    @staticmethod
    def fromFileInMemory(
        text: str,
        sourceManager: SourceManager,
        name: str = "source",
        path: str = "",
        options: Bag = ...,
    ) -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromFiles(paths: list[str]) -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromFiles(
        paths: list[str], sourceManager: SourceManager, options: Bag = ...
    ) -> SyntaxTree: ...
    @staticmethod
    def fromLibraryMapBuffer(
        buffer: SourceBuffer, sourceManager: SourceManager, options: Bag = ...
    ) -> SyntaxTree: ...
    @staticmethod
    def fromLibraryMapFile(
        path: str, sourceManager: SourceManager, options: Bag = ...
    ) -> SyntaxTree: ...
    @staticmethod
    def fromLibraryMapText(
        text: str,
        sourceManager: SourceManager,
        name: str = "source",
        path: str = "",
        options: Bag = ...,
    ) -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromText(text: str, name: str = "source", path: str = "") -> SyntaxTree: ...
    @staticmethod
    @typing.overload
    def fromText(
        text: str,
        sourceManager: SourceManager,
        name: str = "source",
        path: str = "",
        options: Bag = ...,
        library: SourceLibrary | None = None,
    ) -> SyntaxTree: ...
    @staticmethod
    def getDefaultSourceManager() -> SourceManager: ...
    def getIncludeDirectives(self) -> list[IncludeMetadata]: ...
    @property
    def diagnostics(self) -> Diagnostics: ...
    @property
    def isLibraryUnit(self) -> bool: ...
    @property
    def options(self) -> Bag: ...
    @property
    def root(self) -> SyntaxNode: ...
    @property
    def sourceLibrary(self) -> SourceLibrary: ...
    @property
    def sourceManager(self) -> SourceManager: ...

class SystemNameSyntax(NameSyntax):
    systemIdentifier: Token

class SystemSubroutine(metaclass=_metaclass):
    class WithClauseMode(metaclass=_metaclass):
        Iterator = 1
        None_ = 0
        Randomize = 2

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    hasOutputArgs: bool
    kind: SubroutineKind
    knownNameId: Any
    name: str
    withClauseMode: Any

    @staticmethod
    def unevaluatedContext(sourceContext: ASTContext) -> ASTContext: ...
    def __init__(self, name: str, kind: SubroutineKind) -> None: ...
    def __repr__(self) -> str: ...
    def allowClockingArgument(self, argIndex: int) -> bool: ...
    def allowEmptyArgument(self, argIndex: int) -> bool: ...
    def badArg(self, context: ASTContext, arg: Any) -> Any: ...
    def bindArgument(
        self, argIndex: int, context: ASTContext, syntax: Any, previousArgs: list[Any]
    ) -> Any: ...
    def checkArgCount(
        self,
        context: ASTContext,
        isMethod: bool,
        args: list[Any],
        callRange: Any,
        min: int,
        max: int,
    ) -> bool: ...
    def checkArguments(
        self, context: ASTContext, args: list[Any], range: Any, iterOrThis: Any
    ) -> Any: ...
    def eval(self, context: EvalContext, args: list[Any], range: Any, callInfo: Any) -> Any: ...
    def kindStr(self) -> str: ...
    def noHierarchical(self, context: EvalContext, expr: Any) -> bool: ...
    def notConst(self, context: EvalContext, range: Any) -> bool: ...

class SystemTimingCheckKind(metaclass=_metaclass):
    FullSkew: ClassVar[SystemTimingCheckKind]
    """Value = 9"""
    Hold: ClassVar[SystemTimingCheckKind]
    """Value = 2"""
    NoChange: ClassVar[SystemTimingCheckKind]
    """Value = 12"""
    Period: ClassVar[SystemTimingCheckKind]
    """Value = 10"""
    RecRem: ClassVar[SystemTimingCheckKind]
    """Value = 6"""
    Recovery: ClassVar[SystemTimingCheckKind]
    """Value = 4"""
    Removal: ClassVar[SystemTimingCheckKind]
    """Value = 5"""
    Setup: ClassVar[SystemTimingCheckKind]
    """Value = 1"""
    SetupHold: ClassVar[SystemTimingCheckKind]
    """Value = 3"""
    Skew: ClassVar[SystemTimingCheckKind]
    """Value = 7"""
    TimeSkew: ClassVar[SystemTimingCheckKind]
    """Value = 8"""
    Unknown: ClassVar[SystemTimingCheckKind]
    """Value = 0"""
    Width: ClassVar[SystemTimingCheckKind]
    """Value = 11"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SystemTimingCheckSymbol(Symbol):
    class Arg(metaclass=_metaclass):
        @property
        def condition(self) -> Expression: ...
        @property
        def edge(self) -> EdgeKind: ...
        @property
        def edgeDescriptors(
            self,
        ) -> list[list[str]]: ...
        @property
        def expr(self) -> Expression: ...

    @property
    def arguments(self) -> list[Any]: ...
    @property
    def timingCheckKind(self) -> SystemTimingCheckKind: ...

class SystemTimingCheckSyntax(MemberSyntax):
    args: Any
    closeParen: Token
    name: Token
    openParen: Token
    semi: Token

class TaggedPattern(Pattern):
    @property
    def member(self) -> Any: ...
    @property
    def valuePattern(self) -> Pattern: ...

class TaggedPatternSyntax(PatternSyntax):
    memberName: Token
    pattern: PatternSyntax
    tagged: Token

class TaggedUnionExpression(Expression):
    @property
    def member(self) -> Any: ...
    @property
    def valueExpr(self) -> Expression: ...

class TaggedUnionExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    member: Token
    tagged: Token

class TempVarSymbol(VariableSymbol):
    pass

class TextDiagnosticClient(DiagnosticClient):
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def getString(self) -> str: ...
    def report(self, diag: ReportedDiagnostic) -> None: ...
    def showColors(self, show: bool) -> None: ...
    def showColumn(self, show: bool) -> None: ...
    def showHierarchyInstance(self, show: Any) -> None: ...
    def showIncludeStack(self, show: bool) -> None: ...
    def showLocation(self, show: bool) -> None: ...
    def showMacroExpansion(self, show: bool) -> None: ...
    def showOptionName(self, show: bool) -> None: ...
    def showSourceLine(self, show: bool) -> None: ...

class TimeLiteral(Expression):
    @property
    def value(self) -> float: ...

class TimeScale(metaclass=_metaclass):
    base: TimeScaleValue
    precision: TimeScaleValue
    @staticmethod
    def fromString(str: str) -> TimeScale | None: ...
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, base: TimeScaleValue, precision: TimeScaleValue) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def apply(self, value: float, unit: TimeUnit, roundToPrecision: bool) -> float: ...

class TimeScaleDirectiveSyntax(DirectiveSyntax):
    slash: Token
    timePrecision: Token
    timeUnit: Token

class TimeScaleMagnitude(metaclass=_metaclass):
    Hundred: ClassVar[TimeScaleMagnitude]
    """Value = 100"""
    One: ClassVar[TimeScaleMagnitude]
    """Value = 1"""
    Ten: ClassVar[TimeScaleMagnitude]
    """Value = 10"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TimeScaleValue(metaclass=_metaclass):
    magnitude: TimeScaleMagnitude
    unit: TimeUnit
    @staticmethod
    def fromLiteral(value: float, unit: TimeUnit) -> TimeScaleValue | None: ...
    @staticmethod
    def fromString(str: str) -> TimeScaleValue | None: ...
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, unit: TimeUnit, magnitude: TimeScaleMagnitude) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...

class TimeUnit(metaclass=_metaclass):
    Femtoseconds: ClassVar[TimeUnit]
    """Value = 5"""
    Microseconds: ClassVar[TimeUnit]
    """Value = 2"""
    Milliseconds: ClassVar[TimeUnit]
    """Value = 1"""
    Nanoseconds: ClassVar[TimeUnit]
    """Value = 3"""
    Picoseconds: ClassVar[TimeUnit]
    """Value = 4"""
    Seconds: ClassVar[TimeUnit]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TimeUnitsDeclarationSyntax(MemberSyntax):
    divider: DividerClauseSyntax
    keyword: Token
    semi: Token
    time: Token

class TimedStatement(Statement):
    @property
    def stmt(self) -> Statement: ...
    @property
    def timing(self) -> TimingControl: ...

class TimingCheckArgSyntax(SyntaxNode):
    pass

class TimingCheckEventArgSyntax(TimingCheckArgSyntax):
    condition: TimingCheckEventConditionSyntax
    controlSpecifier: EdgeControlSpecifierSyntax
    edge: Token
    terminal: ExpressionSyntax

class TimingCheckEventConditionSyntax(SyntaxNode):
    expr: ExpressionSyntax
    tripleAnd: Token

class TimingControl(metaclass=_metaclass):
    def __repr__(self) -> str: ...
    def visit(self, f: typing.Any) -> None:
        """Visit a pyslang object with a callback function `f`.
        The callback function `f` should take a single argument, which is the current node being
            visited.
        The return value of `f` determines the next node to visit.
        If `f` ever returns `pyslang.VisitAction.Interrupt`, the visit is aborted and no additional
            nodes are visited.
        If `f` returns `pyslang.VisitAction.Skip`, then no child nodes of the current node are
            visited. For any other return value, including `pyslang.VisitAction.Advance`,
            the return value is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool: ...
    @property
    def kind(self) -> TimingControlKind: ...
    @property
    def sourceRange(self) -> Any: ...
    @property
    def syntax(self) -> Any: ...

class TimingControlExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    timing: TimingControlSyntax

class TimingControlKind(metaclass=_metaclass):
    BlockEventList: ClassVar[TimingControlKind]
    """Value = 9"""
    CycleDelay: ClassVar[TimingControlKind]
    """Value = 8"""
    Delay: ClassVar[TimingControlKind]
    """Value = 1"""
    Delay3: ClassVar[TimingControlKind]
    """Value = 6"""
    EventList: ClassVar[TimingControlKind]
    """Value = 3"""
    ImplicitEvent: ClassVar[TimingControlKind]
    """Value = 4"""
    Invalid: ClassVar[TimingControlKind]
    """Value = 0"""
    OneStepDelay: ClassVar[TimingControlKind]
    """Value = 7"""
    RepeatedEvent: ClassVar[TimingControlKind]
    """Value = 5"""
    SignalEvent: ClassVar[TimingControlKind]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TimingControlStatementSyntax(StatementSyntax):
    statement: StatementSyntax
    timingControl: TimingControlSyntax

class TimingControlSyntax(SyntaxNode):
    pass

class TimingPathSymbol(Symbol):
    class ConnectionKind(metaclass=_metaclass):
        Full = 0
        Parallel = 1

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    class Polarity(metaclass=_metaclass):
        Negative = 2
        Positive = 1
        Unknown = 0

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    @property
    def conditionExpr(self) -> Expression: ...
    @property
    def connectionKind(self) -> Any: ...
    @property
    def delays(self) -> list[Expression]: ...
    @property
    def edgeIdentifier(self) -> EdgeKind: ...
    @property
    def edgePolarity(self) -> Any: ...
    @property
    def edgeSourceExpr(self) -> Expression: ...
    @property
    def inputs(self) -> list[Expression]: ...
    @property
    def isStateDependent(self) -> bool: ...
    @property
    def outputs(self) -> list[Expression]: ...
    @property
    def polarity(self) -> Any: ...

class Token(metaclass=_metaclass):
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: object) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        strText: str,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        directive: SyntaxKind,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        bit: logic_t,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        value: SVInt,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        value: float,
        outOfRange: bool,
        timeUnit: TimeUnit | None,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        alloc: BumpAllocator,
        kind: TokenKind,
        trivia: list[Trivia],
        rawText: str,
        location: SourceLocation,
        base: LiteralBase,
        isSigned: bool,
    ) -> None: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @property
    def isMissing(self) -> bool: ...
    @property
    def isOnSameLine(self) -> bool: ...
    @property
    def kind(self) -> TokenKind: ...
    @property
    def location(self) -> SourceLocation: ...
    @property
    def range(self) -> SourceRange: ...
    @property
    def rawText(self) -> str: ...
    @property
    def trivia(self) -> list[Trivia]: ...
    @property
    def value(self) -> typing.Any: ...
    @property
    def valueText(self) -> str: ...

class TokenKind(metaclass=_metaclass):
    AcceptOnKeyword: ClassVar[TokenKind]
    """Value = 93"""
    AliasKeyword: ClassVar[TokenKind]
    """Value = 94"""
    AlwaysCombKeyword: ClassVar[TokenKind]
    """Value = 96"""
    AlwaysFFKeyword: ClassVar[TokenKind]
    """Value = 97"""
    AlwaysKeyword: ClassVar[TokenKind]
    """Value = 95"""
    AlwaysLatchKeyword: ClassVar[TokenKind]
    """Value = 98"""
    And: ClassVar[TokenKind]
    """Value = 89"""
    AndEqual: ClassVar[TokenKind]
    """Value = 61"""
    AndKeyword: ClassVar[TokenKind]
    """Value = 99"""
    Apostrophe: ClassVar[TokenKind]
    """Value = 11"""
    ApostropheOpenBrace: ClassVar[TokenKind]
    """Value = 12"""
    AssertKeyword: ClassVar[TokenKind]
    """Value = 100"""
    AssignKeyword: ClassVar[TokenKind]
    """Value = 101"""
    AssumeKeyword: ClassVar[TokenKind]
    """Value = 102"""
    At: ClassVar[TokenKind]
    """Value = 87"""
    AutomaticKeyword: ClassVar[TokenKind]
    """Value = 103"""
    BeforeKeyword: ClassVar[TokenKind]
    """Value = 104"""
    BeginKeyword: ClassVar[TokenKind]
    """Value = 105"""
    BindKeyword: ClassVar[TokenKind]
    """Value = 106"""
    BinsKeyword: ClassVar[TokenKind]
    """Value = 107"""
    BinsOfKeyword: ClassVar[TokenKind]
    """Value = 108"""
    BitKeyword: ClassVar[TokenKind]
    """Value = 109"""
    BreakKeyword: ClassVar[TokenKind]
    """Value = 110"""
    BufIf0Keyword: ClassVar[TokenKind]
    """Value = 112"""
    BufIf1Keyword: ClassVar[TokenKind]
    """Value = 113"""
    BufKeyword: ClassVar[TokenKind]
    """Value = 111"""
    ByteKeyword: ClassVar[TokenKind]
    """Value = 114"""
    CHandleKeyword: ClassVar[TokenKind]
    """Value = 119"""
    CaseKeyword: ClassVar[TokenKind]
    """Value = 115"""
    CaseXKeyword: ClassVar[TokenKind]
    """Value = 116"""
    CaseZKeyword: ClassVar[TokenKind]
    """Value = 117"""
    CellKeyword: ClassVar[TokenKind]
    """Value = 118"""
    CheckerKeyword: ClassVar[TokenKind]
    """Value = 120"""
    ClassKeyword: ClassVar[TokenKind]
    """Value = 121"""
    ClockingKeyword: ClassVar[TokenKind]
    """Value = 122"""
    CloseBrace: ClassVar[TokenKind]
    """Value = 14"""
    CloseBracket: ClassVar[TokenKind]
    """Value = 16"""
    CloseParenthesis: ClassVar[TokenKind]
    """Value = 18"""
    CmosKeyword: ClassVar[TokenKind]
    """Value = 123"""
    Colon: ClassVar[TokenKind]
    """Value = 20"""
    ColonEquals: ClassVar[TokenKind]
    """Value = 21"""
    ColonSlash: ClassVar[TokenKind]
    """Value = 22"""
    Comma: ClassVar[TokenKind]
    """Value = 24"""
    ConfigKeyword: ClassVar[TokenKind]
    """Value = 124"""
    ConstKeyword: ClassVar[TokenKind]
    """Value = 125"""
    ConstraintKeyword: ClassVar[TokenKind]
    """Value = 126"""
    ContextKeyword: ClassVar[TokenKind]
    """Value = 127"""
    ContinueKeyword: ClassVar[TokenKind]
    """Value = 128"""
    CoverGroupKeyword: ClassVar[TokenKind]
    """Value = 130"""
    CoverKeyword: ClassVar[TokenKind]
    """Value = 129"""
    CoverPointKeyword: ClassVar[TokenKind]
    """Value = 131"""
    CrossKeyword: ClassVar[TokenKind]
    """Value = 132"""
    DeassignKeyword: ClassVar[TokenKind]
    """Value = 133"""
    DefParamKeyword: ClassVar[TokenKind]
    """Value = 135"""
    DefaultKeyword: ClassVar[TokenKind]
    """Value = 134"""
    DesignKeyword: ClassVar[TokenKind]
    """Value = 136"""
    Directive: ClassVar[TokenKind]
    """Value = 343"""
    DisableKeyword: ClassVar[TokenKind]
    """Value = 137"""
    DistKeyword: ClassVar[TokenKind]
    """Value = 138"""
    DoKeyword: ClassVar[TokenKind]
    """Value = 139"""
    Dollar: ClassVar[TokenKind]
    """Value = 44"""
    Dot: ClassVar[TokenKind]
    """Value = 25"""
    DoubleAnd: ClassVar[TokenKind]
    """Value = 90"""
    DoubleAt: ClassVar[TokenKind]
    """Value = 88"""
    DoubleColon: ClassVar[TokenKind]
    """Value = 23"""
    DoubleEquals: ClassVar[TokenKind]
    """Value = 53"""
    DoubleEqualsQuestion: ClassVar[TokenKind]
    """Value = 54"""
    DoubleHash: ClassVar[TokenKind]
    """Value = 47"""
    DoubleMinus: ClassVar[TokenKind]
    """Value = 36"""
    DoubleOr: ClassVar[TokenKind]
    """Value = 84"""
    DoublePlus: ClassVar[TokenKind]
    """Value = 31"""
    DoubleStar: ClassVar[TokenKind]
    """Value = 28"""
    EdgeKeyword: ClassVar[TokenKind]
    """Value = 140"""
    ElseKeyword: ClassVar[TokenKind]
    """Value = 141"""
    EmptyMacroArgument: ClassVar[TokenKind]
    """Value = 350"""
    EndCaseKeyword: ClassVar[TokenKind]
    """Value = 143"""
    EndCheckerKeyword: ClassVar[TokenKind]
    """Value = 144"""
    EndClassKeyword: ClassVar[TokenKind]
    """Value = 145"""
    EndClockingKeyword: ClassVar[TokenKind]
    """Value = 146"""
    EndConfigKeyword: ClassVar[TokenKind]
    """Value = 147"""
    EndFunctionKeyword: ClassVar[TokenKind]
    """Value = 148"""
    EndGenerateKeyword: ClassVar[TokenKind]
    """Value = 149"""
    EndGroupKeyword: ClassVar[TokenKind]
    """Value = 150"""
    EndInterfaceKeyword: ClassVar[TokenKind]
    """Value = 151"""
    EndKeyword: ClassVar[TokenKind]
    """Value = 142"""
    EndModuleKeyword: ClassVar[TokenKind]
    """Value = 152"""
    EndOfFile: ClassVar[TokenKind]
    """Value = 1"""
    EndPackageKeyword: ClassVar[TokenKind]
    """Value = 153"""
    EndPrimitiveKeyword: ClassVar[TokenKind]
    """Value = 154"""
    EndProgramKeyword: ClassVar[TokenKind]
    """Value = 155"""
    EndPropertyKeyword: ClassVar[TokenKind]
    """Value = 156"""
    EndSequenceKeyword: ClassVar[TokenKind]
    """Value = 158"""
    EndSpecifyKeyword: ClassVar[TokenKind]
    """Value = 157"""
    EndTableKeyword: ClassVar[TokenKind]
    """Value = 159"""
    EndTaskKeyword: ClassVar[TokenKind]
    """Value = 160"""
    EnumKeyword: ClassVar[TokenKind]
    """Value = 161"""
    Equals: ClassVar[TokenKind]
    """Value = 52"""
    EqualsArrow: ClassVar[TokenKind]
    """Value = 56"""
    EventKeyword: ClassVar[TokenKind]
    """Value = 162"""
    EventuallyKeyword: ClassVar[TokenKind]
    """Value = 163"""
    Exclamation: ClassVar[TokenKind]
    """Value = 73"""
    ExclamationDoubleEquals: ClassVar[TokenKind]
    """Value = 76"""
    ExclamationEquals: ClassVar[TokenKind]
    """Value = 74"""
    ExclamationEqualsQuestion: ClassVar[TokenKind]
    """Value = 75"""
    ExpectKeyword: ClassVar[TokenKind]
    """Value = 164"""
    ExportKeyword: ClassVar[TokenKind]
    """Value = 165"""
    ExtendsKeyword: ClassVar[TokenKind]
    """Value = 166"""
    ExternKeyword: ClassVar[TokenKind]
    """Value = 167"""
    FinalKeyword: ClassVar[TokenKind]
    """Value = 168"""
    FirstMatchKeyword: ClassVar[TokenKind]
    """Value = 169"""
    ForKeyword: ClassVar[TokenKind]
    """Value = 170"""
    ForceKeyword: ClassVar[TokenKind]
    """Value = 171"""
    ForeachKeyword: ClassVar[TokenKind]
    """Value = 172"""
    ForeverKeyword: ClassVar[TokenKind]
    """Value = 173"""
    ForkJoinKeyword: ClassVar[TokenKind]
    """Value = 175"""
    ForkKeyword: ClassVar[TokenKind]
    """Value = 174"""
    FunctionKeyword: ClassVar[TokenKind]
    """Value = 176"""
    GenVarKeyword: ClassVar[TokenKind]
    """Value = 178"""
    GenerateKeyword: ClassVar[TokenKind]
    """Value = 177"""
    GlobalKeyword: ClassVar[TokenKind]
    """Value = 179"""
    GreaterThan: ClassVar[TokenKind]
    """Value = 81"""
    GreaterThanEquals: ClassVar[TokenKind]
    """Value = 82"""
    Hash: ClassVar[TokenKind]
    """Value = 46"""
    HashEqualsHash: ClassVar[TokenKind]
    """Value = 49"""
    HashMinusHash: ClassVar[TokenKind]
    """Value = 48"""
    HighZ0Keyword: ClassVar[TokenKind]
    """Value = 180"""
    HighZ1Keyword: ClassVar[TokenKind]
    """Value = 181"""
    Identifier: ClassVar[TokenKind]
    """Value = 2"""
    IfKeyword: ClassVar[TokenKind]
    """Value = 182"""
    IfNoneKeyword: ClassVar[TokenKind]
    """Value = 184"""
    IffKeyword: ClassVar[TokenKind]
    """Value = 183"""
    IgnoreBinsKeyword: ClassVar[TokenKind]
    """Value = 185"""
    IllegalBinsKeyword: ClassVar[TokenKind]
    """Value = 186"""
    ImplementsKeyword: ClassVar[TokenKind]
    """Value = 187"""
    ImpliesKeyword: ClassVar[TokenKind]
    """Value = 188"""
    ImportKeyword: ClassVar[TokenKind]
    """Value = 189"""
    InOutKeyword: ClassVar[TokenKind]
    """Value = 193"""
    IncDirKeyword: ClassVar[TokenKind]
    """Value = 190"""
    IncludeFileName: ClassVar[TokenKind]
    """Value = 344"""
    IncludeKeyword: ClassVar[TokenKind]
    """Value = 191"""
    InitialKeyword: ClassVar[TokenKind]
    """Value = 192"""
    InputKeyword: ClassVar[TokenKind]
    """Value = 194"""
    InsideKeyword: ClassVar[TokenKind]
    """Value = 195"""
    InstanceKeyword: ClassVar[TokenKind]
    """Value = 196"""
    IntKeyword: ClassVar[TokenKind]
    """Value = 197"""
    IntegerBase: ClassVar[TokenKind]
    """Value = 6"""
    IntegerKeyword: ClassVar[TokenKind]
    """Value = 198"""
    IntegerLiteral: ClassVar[TokenKind]
    """Value = 5"""
    InterconnectKeyword: ClassVar[TokenKind]
    """Value = 199"""
    InterfaceKeyword: ClassVar[TokenKind]
    """Value = 200"""
    IntersectKeyword: ClassVar[TokenKind]
    """Value = 201"""
    JoinAnyKeyword: ClassVar[TokenKind]
    """Value = 203"""
    JoinKeyword: ClassVar[TokenKind]
    """Value = 202"""
    JoinNoneKeyword: ClassVar[TokenKind]
    """Value = 204"""
    LargeKeyword: ClassVar[TokenKind]
    """Value = 205"""
    LeftShift: ClassVar[TokenKind]
    """Value = 69"""
    LeftShiftEqual: ClassVar[TokenKind]
    """Value = 65"""
    LessThan: ClassVar[TokenKind]
    """Value = 78"""
    LessThanEquals: ClassVar[TokenKind]
    """Value = 79"""
    LessThanMinusArrow: ClassVar[TokenKind]
    """Value = 80"""
    LetKeyword: ClassVar[TokenKind]
    """Value = 206"""
    LibListKeyword: ClassVar[TokenKind]
    """Value = 207"""
    LibraryKeyword: ClassVar[TokenKind]
    """Value = 208"""
    LineContinuation: ClassVar[TokenKind]
    """Value = 351"""
    LocalKeyword: ClassVar[TokenKind]
    """Value = 209"""
    LocalParamKeyword: ClassVar[TokenKind]
    """Value = 210"""
    LogicKeyword: ClassVar[TokenKind]
    """Value = 211"""
    LongIntKeyword: ClassVar[TokenKind]
    """Value = 212"""
    MacroEscapedQuote: ClassVar[TokenKind]
    """Value = 348"""
    MacroPaste: ClassVar[TokenKind]
    """Value = 349"""
    MacroQuote: ClassVar[TokenKind]
    """Value = 346"""
    MacroTripleQuote: ClassVar[TokenKind]
    """Value = 347"""
    MacroUsage: ClassVar[TokenKind]
    """Value = 345"""
    MacromoduleKeyword: ClassVar[TokenKind]
    """Value = 213"""
    MatchesKeyword: ClassVar[TokenKind]
    """Value = 214"""
    MediumKeyword: ClassVar[TokenKind]
    """Value = 215"""
    Minus: ClassVar[TokenKind]
    """Value = 35"""
    MinusArrow: ClassVar[TokenKind]
    """Value = 38"""
    MinusColon: ClassVar[TokenKind]
    """Value = 37"""
    MinusDoubleArrow: ClassVar[TokenKind]
    """Value = 39"""
    MinusEqual: ClassVar[TokenKind]
    """Value = 58"""
    ModPortKeyword: ClassVar[TokenKind]
    """Value = 216"""
    ModuleKeyword: ClassVar[TokenKind]
    """Value = 217"""
    NandKeyword: ClassVar[TokenKind]
    """Value = 218"""
    NegEdgeKeyword: ClassVar[TokenKind]
    """Value = 219"""
    NetTypeKeyword: ClassVar[TokenKind]
    """Value = 220"""
    NewKeyword: ClassVar[TokenKind]
    """Value = 221"""
    NextTimeKeyword: ClassVar[TokenKind]
    """Value = 222"""
    NmosKeyword: ClassVar[TokenKind]
    """Value = 223"""
    NoShowCancelledKeyword: ClassVar[TokenKind]
    """Value = 225"""
    NorKeyword: ClassVar[TokenKind]
    """Value = 224"""
    NotIf0Keyword: ClassVar[TokenKind]
    """Value = 227"""
    NotIf1Keyword: ClassVar[TokenKind]
    """Value = 228"""
    NotKeyword: ClassVar[TokenKind]
    """Value = 226"""
    NullKeyword: ClassVar[TokenKind]
    """Value = 229"""
    OneStep: ClassVar[TokenKind]
    """Value = 92"""
    OpenBrace: ClassVar[TokenKind]
    """Value = 13"""
    OpenBracket: ClassVar[TokenKind]
    """Value = 15"""
    OpenParenthesis: ClassVar[TokenKind]
    """Value = 17"""
    Or: ClassVar[TokenKind]
    """Value = 83"""
    OrEqual: ClassVar[TokenKind]
    """Value = 62"""
    OrEqualsArrow: ClassVar[TokenKind]
    """Value = 86"""
    OrKeyword: ClassVar[TokenKind]
    """Value = 230"""
    OrMinusArrow: ClassVar[TokenKind]
    """Value = 85"""
    OutputKeyword: ClassVar[TokenKind]
    """Value = 231"""
    PackageKeyword: ClassVar[TokenKind]
    """Value = 232"""
    PackedKeyword: ClassVar[TokenKind]
    """Value = 233"""
    ParameterKeyword: ClassVar[TokenKind]
    """Value = 234"""
    Percent: ClassVar[TokenKind]
    """Value = 77"""
    PercentEqual: ClassVar[TokenKind]
    """Value = 63"""
    Placeholder: ClassVar[TokenKind]
    """Value = 10"""
    Plus: ClassVar[TokenKind]
    """Value = 30"""
    PlusColon: ClassVar[TokenKind]
    """Value = 32"""
    PlusDivMinus: ClassVar[TokenKind]
    """Value = 33"""
    PlusEqual: ClassVar[TokenKind]
    """Value = 57"""
    PlusModMinus: ClassVar[TokenKind]
    """Value = 34"""
    PmosKeyword: ClassVar[TokenKind]
    """Value = 235"""
    PosEdgeKeyword: ClassVar[TokenKind]
    """Value = 236"""
    PrimitiveKeyword: ClassVar[TokenKind]
    """Value = 237"""
    PriorityKeyword: ClassVar[TokenKind]
    """Value = 238"""
    ProgramKeyword: ClassVar[TokenKind]
    """Value = 239"""
    PropertyKeyword: ClassVar[TokenKind]
    """Value = 240"""
    ProtectedKeyword: ClassVar[TokenKind]
    """Value = 241"""
    Pull0Keyword: ClassVar[TokenKind]
    """Value = 242"""
    Pull1Keyword: ClassVar[TokenKind]
    """Value = 243"""
    PullDownKeyword: ClassVar[TokenKind]
    """Value = 244"""
    PullUpKeyword: ClassVar[TokenKind]
    """Value = 245"""
    PulseStyleOnDetectKeyword: ClassVar[TokenKind]
    """Value = 246"""
    PulseStyleOnEventKeyword: ClassVar[TokenKind]
    """Value = 247"""
    PureKeyword: ClassVar[TokenKind]
    """Value = 248"""
    Question: ClassVar[TokenKind]
    """Value = 45"""
    RandCKeyword: ClassVar[TokenKind]
    """Value = 250"""
    RandCaseKeyword: ClassVar[TokenKind]
    """Value = 251"""
    RandKeyword: ClassVar[TokenKind]
    """Value = 249"""
    RandSequenceKeyword: ClassVar[TokenKind]
    """Value = 252"""
    RcmosKeyword: ClassVar[TokenKind]
    """Value = 253"""
    RealKeyword: ClassVar[TokenKind]
    """Value = 254"""
    RealLiteral: ClassVar[TokenKind]
    """Value = 8"""
    RealTimeKeyword: ClassVar[TokenKind]
    """Value = 255"""
    RefKeyword: ClassVar[TokenKind]
    """Value = 256"""
    RegKeyword: ClassVar[TokenKind]
    """Value = 257"""
    RejectOnKeyword: ClassVar[TokenKind]
    """Value = 258"""
    ReleaseKeyword: ClassVar[TokenKind]
    """Value = 259"""
    RepeatKeyword: ClassVar[TokenKind]
    """Value = 260"""
    RestrictKeyword: ClassVar[TokenKind]
    """Value = 261"""
    ReturnKeyword: ClassVar[TokenKind]
    """Value = 262"""
    RightShift: ClassVar[TokenKind]
    """Value = 70"""
    RightShiftEqual: ClassVar[TokenKind]
    """Value = 67"""
    RnmosKeyword: ClassVar[TokenKind]
    """Value = 263"""
    RootSystemName: ClassVar[TokenKind]
    """Value = 342"""
    RpmosKeyword: ClassVar[TokenKind]
    """Value = 264"""
    RtranIf0Keyword: ClassVar[TokenKind]
    """Value = 266"""
    RtranIf1Keyword: ClassVar[TokenKind]
    """Value = 267"""
    RtranKeyword: ClassVar[TokenKind]
    """Value = 265"""
    SAlwaysKeyword: ClassVar[TokenKind]
    """Value = 268"""
    SEventuallyKeyword: ClassVar[TokenKind]
    """Value = 269"""
    SNextTimeKeyword: ClassVar[TokenKind]
    """Value = 270"""
    SUntilKeyword: ClassVar[TokenKind]
    """Value = 271"""
    SUntilWithKeyword: ClassVar[TokenKind]
    """Value = 272"""
    ScalaredKeyword: ClassVar[TokenKind]
    """Value = 273"""
    Semicolon: ClassVar[TokenKind]
    """Value = 19"""
    SequenceKeyword: ClassVar[TokenKind]
    """Value = 274"""
    ShortIntKeyword: ClassVar[TokenKind]
    """Value = 275"""
    ShortRealKeyword: ClassVar[TokenKind]
    """Value = 276"""
    ShowCancelledKeyword: ClassVar[TokenKind]
    """Value = 277"""
    SignedKeyword: ClassVar[TokenKind]
    """Value = 278"""
    Slash: ClassVar[TokenKind]
    """Value = 26"""
    SlashEqual: ClassVar[TokenKind]
    """Value = 59"""
    SmallKeyword: ClassVar[TokenKind]
    """Value = 279"""
    SoftKeyword: ClassVar[TokenKind]
    """Value = 280"""
    SolveKeyword: ClassVar[TokenKind]
    """Value = 281"""
    SpecParamKeyword: ClassVar[TokenKind]
    """Value = 283"""
    SpecifyKeyword: ClassVar[TokenKind]
    """Value = 282"""
    Star: ClassVar[TokenKind]
    """Value = 27"""
    StarArrow: ClassVar[TokenKind]
    """Value = 29"""
    StarEqual: ClassVar[TokenKind]
    """Value = 60"""
    StaticKeyword: ClassVar[TokenKind]
    """Value = 284"""
    StringKeyword: ClassVar[TokenKind]
    """Value = 285"""
    StringLiteral: ClassVar[TokenKind]
    """Value = 4"""
    Strong0Keyword: ClassVar[TokenKind]
    """Value = 287"""
    Strong1Keyword: ClassVar[TokenKind]
    """Value = 288"""
    StrongKeyword: ClassVar[TokenKind]
    """Value = 286"""
    StructKeyword: ClassVar[TokenKind]
    """Value = 289"""
    SuperKeyword: ClassVar[TokenKind]
    """Value = 290"""
    Supply0Keyword: ClassVar[TokenKind]
    """Value = 291"""
    Supply1Keyword: ClassVar[TokenKind]
    """Value = 292"""
    SyncAcceptOnKeyword: ClassVar[TokenKind]
    """Value = 293"""
    SyncRejectOnKeyword: ClassVar[TokenKind]
    """Value = 294"""
    SystemIdentifier: ClassVar[TokenKind]
    """Value = 3"""
    TableKeyword: ClassVar[TokenKind]
    """Value = 295"""
    TaggedKeyword: ClassVar[TokenKind]
    """Value = 296"""
    TaskKeyword: ClassVar[TokenKind]
    """Value = 297"""
    ThisKeyword: ClassVar[TokenKind]
    """Value = 298"""
    ThroughoutKeyword: ClassVar[TokenKind]
    """Value = 299"""
    Tilde: ClassVar[TokenKind]
    """Value = 40"""
    TildeAnd: ClassVar[TokenKind]
    """Value = 41"""
    TildeOr: ClassVar[TokenKind]
    """Value = 42"""
    TildeXor: ClassVar[TokenKind]
    """Value = 43"""
    TimeKeyword: ClassVar[TokenKind]
    """Value = 300"""
    TimeLiteral: ClassVar[TokenKind]
    """Value = 9"""
    TimePrecisionKeyword: ClassVar[TokenKind]
    """Value = 301"""
    TimeUnitKeyword: ClassVar[TokenKind]
    """Value = 302"""
    TranIf0Keyword: ClassVar[TokenKind]
    """Value = 304"""
    TranIf1Keyword: ClassVar[TokenKind]
    """Value = 305"""
    TranKeyword: ClassVar[TokenKind]
    """Value = 303"""
    Tri0Keyword: ClassVar[TokenKind]
    """Value = 307"""
    Tri1Keyword: ClassVar[TokenKind]
    """Value = 308"""
    TriAndKeyword: ClassVar[TokenKind]
    """Value = 309"""
    TriKeyword: ClassVar[TokenKind]
    """Value = 306"""
    TriOrKeyword: ClassVar[TokenKind]
    """Value = 310"""
    TriRegKeyword: ClassVar[TokenKind]
    """Value = 311"""
    TripleAnd: ClassVar[TokenKind]
    """Value = 91"""
    TripleEquals: ClassVar[TokenKind]
    """Value = 55"""
    TripleLeftShift: ClassVar[TokenKind]
    """Value = 71"""
    TripleLeftShiftEqual: ClassVar[TokenKind]
    """Value = 66"""
    TripleRightShift: ClassVar[TokenKind]
    """Value = 72"""
    TripleRightShiftEqual: ClassVar[TokenKind]
    """Value = 68"""
    TypeKeyword: ClassVar[TokenKind]
    """Value = 312"""
    TypedefKeyword: ClassVar[TokenKind]
    """Value = 313"""
    UWireKeyword: ClassVar[TokenKind]
    """Value = 322"""
    UnbasedUnsizedLiteral: ClassVar[TokenKind]
    """Value = 7"""
    UnionKeyword: ClassVar[TokenKind]
    """Value = 314"""
    Unique0Keyword: ClassVar[TokenKind]
    """Value = 316"""
    UniqueKeyword: ClassVar[TokenKind]
    """Value = 315"""
    UnitSystemName: ClassVar[TokenKind]
    """Value = 341"""
    Unknown: ClassVar[TokenKind]
    """Value = 0"""
    UnsignedKeyword: ClassVar[TokenKind]
    """Value = 317"""
    UntilKeyword: ClassVar[TokenKind]
    """Value = 318"""
    UntilWithKeyword: ClassVar[TokenKind]
    """Value = 319"""
    UntypedKeyword: ClassVar[TokenKind]
    """Value = 320"""
    UseKeyword: ClassVar[TokenKind]
    """Value = 321"""
    VarKeyword: ClassVar[TokenKind]
    """Value = 323"""
    VectoredKeyword: ClassVar[TokenKind]
    """Value = 324"""
    VirtualKeyword: ClassVar[TokenKind]
    """Value = 325"""
    VoidKeyword: ClassVar[TokenKind]
    """Value = 326"""
    WAndKeyword: ClassVar[TokenKind]
    """Value = 329"""
    WOrKeyword: ClassVar[TokenKind]
    """Value = 338"""
    WaitKeyword: ClassVar[TokenKind]
    """Value = 327"""
    WaitOrderKeyword: ClassVar[TokenKind]
    """Value = 328"""
    Weak0Keyword: ClassVar[TokenKind]
    """Value = 331"""
    Weak1Keyword: ClassVar[TokenKind]
    """Value = 332"""
    WeakKeyword: ClassVar[TokenKind]
    """Value = 330"""
    WhileKeyword: ClassVar[TokenKind]
    """Value = 333"""
    WildcardKeyword: ClassVar[TokenKind]
    """Value = 334"""
    WireKeyword: ClassVar[TokenKind]
    """Value = 335"""
    WithKeyword: ClassVar[TokenKind]
    """Value = 336"""
    WithinKeyword: ClassVar[TokenKind]
    """Value = 337"""
    XnorKeyword: ClassVar[TokenKind]
    """Value = 339"""
    Xor: ClassVar[TokenKind]
    """Value = 50"""
    XorEqual: ClassVar[TokenKind]
    """Value = 64"""
    XorKeyword: ClassVar[TokenKind]
    """Value = 340"""
    XorTilde: ClassVar[TokenKind]
    """Value = 51"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TransListCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    sets: Any

class TransRangeSyntax(SyntaxNode):
    items: Any
    repeat: TransRepeatRangeSyntax

class TransRepeatRangeSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax
    specifier: Token

class TransSetSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ranges: Any

class TransparentMemberSymbol(Symbol):
    @property
    def wrapped(self) -> Symbol: ...

class Trivia(metaclass=_metaclass):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, kind: TriviaKind, rawText: str) -> None: ...
    def __repr__(self) -> str: ...
    def getExplicitLocation(self) -> SourceLocation | None: ...
    def getRawText(self) -> str: ...
    def getSkippedTokens(self) -> list[Any]: ...
    def syntax(self) -> Any: ...
    @property
    def kind(self) -> TriviaKind: ...

class TriviaKind(metaclass=_metaclass):
    BlockComment: ClassVar[TriviaKind]
    """Value = 4"""
    Directive: ClassVar[TriviaKind]
    """Value = 8"""
    DisabledText: ClassVar[TriviaKind]
    """Value = 5"""
    EndOfLine: ClassVar[TriviaKind]
    """Value = 2"""
    LineComment: ClassVar[TriviaKind]
    """Value = 3"""
    SkippedSyntax: ClassVar[TriviaKind]
    """Value = 7"""
    SkippedTokens: ClassVar[TriviaKind]
    """Value = 6"""
    Unknown: ClassVar[TriviaKind]
    """Value = 0"""
    Whitespace: ClassVar[TriviaKind]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Type(Symbol):
    @staticmethod
    def getCommonBase(left: Type, right: Type) -> Type: ...
    def __repr__(self) -> str: ...
    def coerceValue(self, value: ConstantValue) -> ConstantValue: ...
    def implements(self, rhs: Type) -> bool: ...
    def isAssignmentCompatible(self, rhs: Type) -> bool: ...
    def isBitstreamCastable(self, rhs: Type) -> bool: ...
    def isBitstreamType(self, destination: bool = False) -> bool: ...
    def isCastCompatible(self, rhs: Type) -> bool: ...
    def isDerivedFrom(self, rhs: Type) -> bool: ...
    def isEquivalent(self, rhs: Type) -> bool: ...
    def isMatching(self, rhs: Type) -> bool: ...
    def isValidForRand(self, mode: RandMode, languageVersion: LanguageVersion) -> bool: ...
    def makeSigned(self, compilation: Compilation) -> Type: ...
    def makeUnsigned(self, compilation: Compilation) -> Type: ...
    @property
    def arrayElementType(self) -> Type: ...
    @property
    def associativeIndexType(self) -> Type: ...
    @property
    def bitWidth(self) -> int: ...
    @property
    def bitstreamWidth(self) -> int: ...
    @property
    def canBeStringLike(self) -> bool: ...
    @property
    def canonicalType(self) -> Type: ...
    @property
    def defaultValue(self) -> ConstantValue: ...
    @property
    def fixedRange(self) -> ConstantRange: ...
    @property
    def hasFixedRange(self) -> bool: ...
    @property
    def integralFlags(self) -> IntegralFlags: ...
    @property
    def isAggregate(self) -> bool: ...
    @property
    def isAlias(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isAssociativeArray(self) -> bool: ...
    @property
    def isBooleanConvertible(self) -> bool: ...
    @property
    def isByteArray(self) -> bool: ...
    @property
    def isCHandle(self) -> bool: ...
    @property
    def isClass(self) -> bool: ...
    @property
    def isCovergroup(self) -> bool: ...
    @property
    def isDynamicallySizedArray(self) -> bool: ...
    @property
    def isEnum(self) -> bool: ...
    @property
    def isError(self) -> bool: ...
    @property
    def isEvent(self) -> bool: ...
    @property
    def isFixedSize(self) -> bool: ...
    @property
    def isFloating(self) -> bool: ...
    @property
    def isFourState(self) -> bool: ...
    @property
    def isHandleType(self) -> bool: ...
    @property
    def isIntegral(self) -> bool: ...
    @property
    def isIterable(self) -> bool: ...
    @property
    def isNull(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isPackedArray(self) -> bool: ...
    @property
    def isPackedUnion(self) -> bool: ...
    @property
    def isPredefinedInteger(self) -> bool: ...
    @property
    def isPropertyType(self) -> bool: ...
    @property
    def isQueue(self) -> bool: ...
    @property
    def isScalar(self) -> bool: ...
    @property
    def isSequenceType(self) -> bool: ...
    @property
    def isSigned(self) -> bool: ...
    @property
    def isSimpleBitVector(self) -> bool: ...
    @property
    def isSimpleType(self) -> bool: ...
    @property
    def isSingular(self) -> bool: ...
    @property
    def isString(self) -> bool: ...
    @property
    def isStruct(self) -> bool: ...
    @property
    def isTaggedUnion(self) -> bool: ...
    @property
    def isTypeRefType(self) -> bool: ...
    @property
    def isUnbounded(self) -> bool: ...
    @property
    def isUnpackedArray(self) -> bool: ...
    @property
    def isUnpackedStruct(self) -> bool: ...
    @property
    def isUnpackedUnion(self) -> bool: ...
    @property
    def isUntypedType(self) -> bool: ...
    @property
    def isValidForDPIArg(self) -> bool: ...
    @property
    def isValidForDPIReturn(self) -> bool: ...
    @property
    def isValidForSequence(self) -> bool: ...
    @property
    def isVirtualInterface(self) -> bool: ...
    @property
    def isVoid(self) -> bool: ...
    @property
    def selectableWidth(self) -> int: ...

class TypeAliasType(Type):
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol: ...
    @property
    def targetType(self) -> DeclaredType: ...
    @property
    def visibility(self) -> Visibility: ...

class TypeAssignmentSyntax(SyntaxNode):
    assignment: EqualsTypeClauseSyntax
    name: Token

class TypeParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: Any
    typeKeyword: Token
    typeRestriction: ForwardTypeRestrictionSyntax

class TypeParameterSymbol(Symbol, ParameterSymbolBase):
    @property
    def isOverridden(self) -> bool: ...
    @property
    def targetType(self) -> Any: ...
    @property
    def typeAlias(self) -> Any: ...

class TypePrinter(metaclass=_metaclass):
    options: TypePrintingOptions
    def __init__(self) -> None: ...
    def append(self, type: Type) -> None: ...
    def clear(self) -> None: ...
    def toString(self) -> str: ...

class TypePrintingOptions(metaclass=_metaclass):
    class AnonymousTypeStyle(metaclass=_metaclass):
        FriendlyName: ClassVar[Self]
        """ Value = 1"""
        SystemName: ClassVar[Self]
        """ Value = 0"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    FriendlyName = AnonymousTypeStyle.FriendlyName
    SystemName = AnonymousTypeStyle.SystemName
    addSingleQuotes: bool
    anonymousTypeStyle: Any
    elideScopeNames: bool
    fullEnumType: bool
    printAKA: bool
    skipScopedTypeNames: bool
    skipTypeDefs: bool

class TypeRefType(Type):
    pass

class TypeReferenceExpression(Expression):
    @property
    def targetType(self) -> Any: ...

class TypeReferenceSyntax(DataTypeSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    typeKeyword: Token

class TypedefDeclarationSyntax(MemberSyntax):
    dimensions: Any
    name: Token
    semi: Token
    type: DataTypeSyntax
    typedefKeyword: Token

class UdpBodySyntax(SyntaxNode):
    endtable: Token
    entries: Any
    initialStmt: UdpInitialStmtSyntax
    portDecls: Any
    table: Token

class UdpDeclarationSyntax(MemberSyntax):
    body: UdpBodySyntax
    endBlockName: NamedBlockClauseSyntax
    endprimitive: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token

class UdpEdgeFieldSyntax(UdpFieldBaseSyntax):
    closeParen: Token
    first: Token
    openParen: Token
    second: Token

class UdpEntrySyntax(SyntaxNode):
    colon1: Token
    colon2: Token
    current: UdpFieldBaseSyntax
    inputs: Any
    next: UdpFieldBaseSyntax
    semi: Token

class UdpFieldBaseSyntax(SyntaxNode):
    pass

class UdpInitialStmtSyntax(SyntaxNode):
    equals: Token
    initial: Token
    name: Token
    semi: Token
    value: ExpressionSyntax

class UdpInputPortDeclSyntax(UdpPortDeclSyntax):
    keyword: Token
    names: Any

class UdpOutputPortDeclSyntax(UdpPortDeclSyntax):
    initializer: EqualsValueClauseSyntax
    keyword: Token
    name: Token
    reg: Token

class UdpPortDeclSyntax(SyntaxNode):
    attributes: Any

class UdpPortListSyntax(SyntaxNode):
    pass

class UdpSimpleFieldSyntax(UdpFieldBaseSyntax):
    field: Token

class UnaryAssertionExpr(AssertionExpr):
    @property
    def expr(self) -> AssertionExpr: ...
    @property
    def op(self) -> UnaryAssertionOperator: ...
    @property
    def range(self) -> SequenceRange | None: ...

class UnaryAssertionOperator(metaclass=_metaclass):
    Always: ClassVar[UnaryAssertionOperator]
    """Value = 3"""
    Eventually: ClassVar[UnaryAssertionOperator]
    """Value = 5"""
    NextTime: ClassVar[UnaryAssertionOperator]
    """Value = 1"""
    Not: ClassVar[UnaryAssertionOperator]
    """Value = 0"""
    SAlways: ClassVar[UnaryAssertionOperator]
    """Value = 4"""
    SEventually: ClassVar[UnaryAssertionOperator]
    """Value = 6"""
    SNextTime: ClassVar[UnaryAssertionOperator]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UnaryBinsSelectExpr(BinsSelectExpr):
    class Op(metaclass=_metaclass):
        Negation: ClassVar[Self]
        """Value = 0"""

        __members__: dict[str, Self]

        def __int__(self) -> int: ...
        def __index__(self, index: int) -> Self: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    Negation = Op.Negation

    @property
    def expr(self) -> BinsSelectExpr: ...
    @property
    def op(self) -> Any: ...

class UnaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: BinsSelectConditionExprSyntax
    op: Token

class UnaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    op: Token
    operand: ConditionalDirectiveExpressionSyntax

class UnaryExpression(Expression):
    @property
    def op(self) -> UnaryOperator: ...
    @property
    def operand(self) -> Expression: ...

class UnaryOperator(metaclass=_metaclass):
    BitwiseAnd: ClassVar[UnaryOperator]
    """Value = 3"""
    BitwiseNand: ClassVar[UnaryOperator]
    """Value = 6"""
    BitwiseNor: ClassVar[UnaryOperator]
    """Value = 7"""
    BitwiseNot: ClassVar[UnaryOperator]
    """Value = 2"""
    BitwiseOr: ClassVar[UnaryOperator]
    """Value = 4"""
    BitwiseXnor: ClassVar[UnaryOperator]
    """Value = 8"""
    BitwiseXor: ClassVar[UnaryOperator]
    """Value = 5"""
    LogicalNot: ClassVar[UnaryOperator]
    """Value = 9"""
    Minus: ClassVar[UnaryOperator]
    """Value = 1"""
    Plus: ClassVar[UnaryOperator]
    """Value = 0"""
    Postdecrement: ClassVar[UnaryOperator]
    """Value = 13"""
    Postincrement: ClassVar[UnaryOperator]
    """Value = 12"""
    Predecrement: ClassVar[UnaryOperator]
    """Value = 11"""
    Preincrement: ClassVar[UnaryOperator]
    """Value = 10"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UnaryPropertyExprSyntax(PropertyExprSyntax):
    expr: PropertyExprSyntax
    op: Token

class UnarySelectPropertyExprSyntax(PropertyExprSyntax):
    closeBracket: Token
    expr: PropertyExprSyntax
    op: Token
    openBracket: Token
    selector: SelectorSyntax

class UnbasedUnsizedIntegerLiteral(Expression):
    @property
    def literalValue(self) -> Any: ...
    @property
    def value(self) -> Any: ...

class Unbounded(metaclass=_metaclass):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...

class UnboundedLiteral(Expression):
    pass

class UnboundedType(Type):
    pass

class UnconditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: Any

class UnconnectedDrive(metaclass=_metaclass):
    None_: ClassVar[UnconnectedDrive]
    """Value = 0"""
    Pull0: ClassVar[UnconnectedDrive]
    """Value = 1"""
    Pull1: ClassVar[UnconnectedDrive]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UnconnectedDriveDirectiveSyntax(DirectiveSyntax):
    strength: Token

class UndefDirectiveSyntax(DirectiveSyntax):
    name: Token

class UninstantiatedDefSymbol(Symbol):
    @property
    def definitionName(self) -> str: ...
    @property
    def isChecker(self) -> bool: ...
    @property
    def paramExpressions(self) -> list[Expression]: ...
    @property
    def portConnections(self) -> list[AssertionExpr]: ...
    @property
    def portNames(self) -> list[str]: ...

class UniquePriorityCheck(metaclass=_metaclass):
    None_: ClassVar[UniquePriorityCheck]
    """Value = 0"""
    Priority: ClassVar[UniquePriorityCheck]
    """Value = 3"""
    Unique: ClassVar[UniquePriorityCheck]
    """Value = 1"""
    Unique0: ClassVar[UniquePriorityCheck]
    """Value = 2"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UniquenessConstraint(Constraint):
    @property
    def items(self) -> list[Any]: ...

class UniquenessConstraintSyntax(ConstraintItemSyntax):
    ranges: RangeListSyntax
    semi: Token
    unique: Token

class UnpackedStructType(Type, Scope):
    @property
    def systemId(self) -> int: ...

class UnpackedUnionType(Type, Scope):
    @property
    def isTagged(self) -> bool: ...
    @property
    def systemId(self) -> int: ...

class UntypedType(Type):
    pass

class UserDefinedNetDeclarationSyntax(MemberSyntax):
    declarators: Any
    delay: TimingControlSyntax
    netType: Token
    semi: Token

class ValueDriver(metaclass=_metaclass):
    @property
    def containingSymbol(self) -> Any: ...
    @property
    def flags(self) -> Any: ...
    @property
    def isClockVar(self) -> bool: ...
    @property
    def isFromSideEffect(self) -> bool: ...
    @property
    def isInSingleDriverProcedure(self) -> bool: ...
    @property
    def isInputPort(self) -> bool: ...
    @property
    def isUnidirectionalPort(self) -> bool: ...
    @property
    def kind(self) -> Any: ...
    @property
    def prefixExpression(self) -> Any: ...
    @property
    def procCallExpression(self) -> Any: ...
    @property
    def source(self) -> Any: ...
    @property
    def sourceRange(self) -> Any: ...

class ValueExpressionBase(Expression):
    @property
    def symbol(self) -> Any: ...

class ValueRangeExpression(Expression):
    @property
    def left(self) -> Expression: ...
    @property
    def right(self) -> Expression: ...

class ValueRangeExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    left: ExpressionSyntax
    op: Token
    openBracket: Token
    right: ExpressionSyntax

class ValueRangeKind(metaclass=_metaclass):
    AbsoluteTolerance: ClassVar[ValueRangeKind]
    """Value = 1"""
    RelativeTolerance: ClassVar[ValueRangeKind]
    """Value = 2"""
    Simple: ClassVar[ValueRangeKind]
    """Value = 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ValueSymbol(Symbol):
    @property
    def initializer(self) -> Expression: ...
    @property
    def type(self) -> Any: ...

class VariableDeclStatement(Statement):
    @property
    def symbol(self) -> Any: ...

class VariableDimensionSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    specifier: DimensionSpecifierSyntax

class VariableFlags(metaclass=_metaclass):
    CheckerFreeVariable: ClassVar[VariableFlags]
    """Value = 16"""
    CompilerGenerated: ClassVar[VariableFlags]
    """Value = 2"""
    Const: ClassVar[VariableFlags]
    """Value = 1"""
    CoverageSampleFormal: ClassVar[VariableFlags]
    """Value = 8"""
    ImmutableCoverageOption: ClassVar[VariableFlags]
    """Value = 4"""
    None_: ClassVar[VariableFlags]
    """Value = 0"""
    RefStatic: ClassVar[VariableFlags]
    """Value = 32"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VariableLifetime(metaclass=_metaclass):
    Automatic: ClassVar[VariableLifetime]
    """Value = 0"""
    Static: ClassVar[VariableLifetime]
    """Value = 1"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VariablePattern(Pattern):
    @property
    def variable(self) -> Any: ...

class VariablePatternSyntax(PatternSyntax):
    dot: Token
    variableName: Token

class VariablePortHeaderSyntax(PortHeaderSyntax):
    constKeyword: Token
    dataType: DataTypeSyntax
    direction: Token
    varKeyword: Token

class VariableSymbol(ValueSymbol):
    @property
    def flags(self) -> VariableFlags: ...
    @property
    def lifetime(self) -> VariableLifetime: ...

class VersionInfo(metaclass=_metaclass):
    @staticmethod
    def getHash() -> str: ...
    @staticmethod
    def getMajor() -> int: ...
    @staticmethod
    def getMinor() -> int: ...
    @staticmethod
    def getPatch() -> int: ...

class VirtualInterfaceType(Type):
    @property
    def iface(self) -> InstanceSymbol: ...
    @property
    def modport(self) -> ModportSymbol: ...

class VirtualInterfaceTypeSyntax(DataTypeSyntax):
    interfaceKeyword: Token
    modport: DotMemberClauseSyntax
    name: Token
    parameters: ParameterValueAssignmentSyntax
    virtualKeyword: Token

class Visibility(metaclass=_metaclass):
    Local: ClassVar[Visibility]
    """ Value: 2"""
    Protected: ClassVar[Visibility]
    """ Value: 1"""
    Public: ClassVar[Visibility]
    """ Value: 0"""

    __members__: dict[str, Self]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VisitAction(metaclass=_metaclass):
    Advance: ClassVar[VisitAction]
    """Value: 0"""
    Interrupt: ClassVar[VisitAction]
    """Value: 2"""
    Skip: ClassVar[VisitAction]
    """Value: 1"""

    __members__: dict[str, VisitAction]

    def __int__(self) -> int: ...
    def __index__(self, index: int) -> VisitAction: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VoidCastedCallStatementSyntax(StatementSyntax):
    apostrophe: Token
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    voidKeyword: Token

class VoidType(Type):
    pass

class WaitForkStatement(Statement):
    pass

class WaitForkStatementSyntax(StatementSyntax):
    fork: Token
    semi: Token
    wait: Token

class WaitOrderStatement(Statement):
    @property
    def events(self) -> list[Expression]: ...
    @property
    def ifFalse(self) -> Statement: ...
    @property
    def ifTrue(self) -> Statement: ...

class WaitOrderStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    names: Any
    openParen: Token
    wait_order: Token

class WaitStatement(Statement):
    @property
    def cond(self) -> Expression: ...
    @property
    def stmt(self) -> Statement: ...

class WaitStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    statement: StatementSyntax
    wait: Token

class WhileLoopStatement(Statement):
    @property
    def body(self) -> Statement: ...
    @property
    def cond(self) -> Expression: ...

class WildcardDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    star: Token

class WildcardImportSymbol(Symbol):
    @property
    def isFromExport(self) -> bool: ...
    @property
    def package(self) -> PackageSymbol: ...
    @property
    def packageName(self) -> str: ...

class WildcardPattern(Pattern):
    pass

class WildcardPatternSyntax(PatternSyntax):
    dot: Token
    star: Token

class WildcardPortConnectionSyntax(PortConnectionSyntax):
    dot: Token
    star: Token

class WildcardPortListSyntax(PortListSyntax):
    closeParen: Token
    dot: Token
    openParen: Token
    star: Token

class WildcardUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    dot: Token
    openParen: Token
    semi: Token
    star: Token

class WithClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    with_: Token

class WithFunctionClauseSyntax(SyntaxNode):
    name: NameSyntax
    with_: Token

class WithFunctionSampleSyntax(SyntaxNode):
    function: Token
    portList: FunctionPortListSyntax
    sample: Token
    with_: Token

class logic_t(metaclass=_metaclass):
    x: typing.ClassVar[logic_t]  # value = x
    z: typing.ClassVar[logic_t]  # value = z
    value: int
    def __and__(self, arg0: logic_t) -> logic_t: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: logic_t) -> logic_t:  # type: ignore[override]
        ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __invert__(self) -> logic_t: ...
    def __ne__(self, arg0: logic_t) -> logic_t:  # type: ignore[override]
        ...
    def __or__(self, arg0: logic_t) -> logic_t: ...
    def __repr__(self) -> str: ...
    def __xor__(self, arg0: logic_t) -> logic_t: ...
    @property
    def isUnknown(self) -> bool: ...

def clog2(value) -> int: ...
def literalBaseFromChar(base: str, result: LiteralBase) -> bool: ...
def rewrite(tree: SyntaxTree, handler: typing.Callable) -> SyntaxTree: ...

__version__: str = "9.0.0"
