"""Checker for optional non-keyword only parameters."""

from __future__ import annotations

import ast
import enum
from typing import ClassVar, Dict, TYPE_CHECKING, Tuple

import flake8_keyword_params

from typing_extensions import Protocol

if (TYPE_CHECKING):
	import tokenize
	from collections.abc import Iterator
	from flake8.options.manager import OptionManager


try:
	try:
		from importlib.metadata import version
	except ModuleNotFoundError:  # python < 3.8 use polyfill
		from importlib_metadata import version  # type: ignore
	package_version = version(__package__)
except Exception:
	package_version = 'unknown'


LogicalResult = Tuple[Tuple[int, int], str]  # (line, column), text
PhysicalResult = Tuple[int, str]  # (column, text)
ASTResult = Tuple[int, int, str, type]  # (line, column, text, type)


class Options(Protocol):
	"""Protocol for options."""

	keyword_params_include_name: bool


class Message(enum.Enum):
	"""Messages."""

	NON_KEWORD_OPTIONAL = (1, "Optional parameter '{param}' should be keyword only")

	@property
	def code(self) -> str:
		return (flake8_keyword_params.plugin_prefix + str(self.value[0]).rjust(6 - len(flake8_keyword_params.plugin_prefix), '0'))

	def text(self, **kwargs) -> str:
		return self.value[1].format(**kwargs)


class Checker:
	"""Base class for checkers."""

	name: ClassVar[str] = __package__.replace('_', '-')
	version: ClassVar[str] = package_version
	plugin_name: ClassVar[str]

	@classmethod
	def add_options(cls, option_manager: OptionManager) -> None:
		option_manager.add_option('--keyword-params-include-name', default=False, action='store_true',
		                          parse_from_config=True, dest='keyword_params_include_name',
		                          help='Include plugin name in messages (enabled by default)')
		option_manager.add_option('--keyword-params-no-include-name', default=None, action='store_false',
		                          parse_from_config=False, dest='keyword_params_include_name',
		                          help='Remove plugin name from messages')

	@classmethod
	def parse_options(cls, options: Options) -> None:
		cls.plugin_name = (' (' + cls.name + ')') if (options.keyword_params_include_name) else ''

	def _logical_token_message(self, token: tokenize.TokenInfo, message: Message, **kwargs) -> LogicalResult:
		return (token.start, f'{message.code}{self.plugin_name} {message.text(**kwargs)}')

	def _pyhsical_token_message(self, token: tokenize.TokenInfo, message: Message, **kwargs) -> PhysicalResult:
		return (token.start[1], f'{message.code}{self.plugin_name} {message.text(**kwargs)}')

	def _ast_token_message(self, token: tokenize.TokenInfo, message: Message, **kwargs) -> ASTResult:
		return (token.start[0], token.start[1], f'{message.code}{self.plugin_name} {message.text(**kwargs)}', type(self))

	def _ast_node_message(self, node: ast.AST, message: Message, **kwargs) -> ASTResult:
		return (node.lineno, node.col_offset, f'{message.code}{self.plugin_name} {message.text(**kwargs)}', type(self))


Violation = Tuple[ast.AST, Message, Dict[str, str]]


class ParamVisitor(ast.NodeVisitor):
	"""Param visitor."""

	violations: list[Violation]

	def __init__(self) -> None:
		self.violations = []

	def visit_arguments(self, node: ast.arguments) -> None:
		self.generic_visit(node)
		defaults = (node.defaults[len(node.posonlyargs):] if (hasattr(node, 'posonlyargs')) else node.defaults)
		if (defaults):
			for arg in node.args[-len(defaults):]:
				self.violations.append((arg, Message.NON_KEWORD_OPTIONAL, {'param': arg.arg}))


class ParamChecker(Checker):
	"""Parameter checker."""

	tree: ast.AST

	def __init__(self, tree: ast.AST) -> None:
		self.tree = tree

	def __iter__(self) -> Iterator[ASTResult]:
		"""Primary call from flake8, yield error messages."""
		param_visitor = ParamVisitor()
		param_visitor.visit(self.tree)

		for node, message, kwargs in param_visitor.violations:
			yield self._ast_node_message(node, message, **kwargs)
