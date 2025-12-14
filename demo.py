from nl.nl_to_json import nl_to_json
from dsl.parser import parse_dsl
from codegen.generator import generate_condition
from execution.data import load_data
from execution.simulator import run_backtest
from execution.indicators import rsi

nl = "Buy when the close price is above the 20-day moving average and volume is above 1 million."

structured = nl_to_json(nl)

dsl = """
ENTRY:
close > SMA(close,20) AND volume > 1000000
EXIT:
RSI(close,14) < 30
"""

ast = parse_dsl(dsl)

df = load_data()

entry_expr = generate_condition(ast.children[0])
exit_expr = generate_condition(ast.children[1])

entry_signal = eval(entry_expr)
exit_signal = eval(exit_expr)

result = run_backtest(df, entry_signal, exit_signal)

print("NL:", nl)
print("DSL:", dsl)
print("AST:", ast)
print("RESULT:", result)
