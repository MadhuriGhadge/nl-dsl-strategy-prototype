from lark import Lark
from .ast_builder import ASTBuilder

with open("dsl/grammar.lark") as f:
    grammar = f.read()

parser = Lark(grammar, parser="lalr", transformer=ASTBuilder())

def parse_dsl(dsl_text: str):
    tree = parser.parse(dsl_text)
    return tree

