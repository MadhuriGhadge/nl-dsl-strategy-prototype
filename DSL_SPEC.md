# Trading Strategy DSL Specification

## Purpose
This DSL defines a minimal, unambiguous way to express rule-based trading strategies.
It is designed to sit between natural-language instructions and executable Python code.

The goal is clarity and correctness, not full market coverage.

## Strategy Structure

A strategy consists of two mandatory sections:

ENTRY:
<expression>

EXIT:
<expression>

- `ENTRY` defines when to open a position
- `EXIT` defines when to close a position

## Grammar (Simplified)

strategy := ENTRY expression EXIT expression

expression := comparison
| expression AND expression
| expression OR expression
| "(" expression ")"

comparison := value operator value

operator := > | < | >= | <= | ==

value := metric
| indicator
| number

metric := open | high | low | close | volume

indicator := sma(metric, number)
| rsi(metric, number)

number := integer | float


## Supported Metrics

- `open`
- `high`
- `low`
- `close`
- `volume`

These map directly to columns in a pandas DataFrame.


## Supported Indicators

### Simple Moving Average (SMA)
sma(close, 20)
Rolling mean over N periods.

### Relative Strength Index (RSI)
rsi(close, 14)

Momentum indicator computed using rolling gains/losses.

## Boolean Logic

- `AND`
- `OR`
- Parentheses for grouping

Example:
(close > sma(close,20)) AND (volume > 1000000)


## Example Strategy

ENTRY:
close > sma(close,20) AND volume > 1000000

EXIT:
rsi(close,14) < 30

## AST Representation (Example)

{
  "type": "binary_op",
  "op": "AND",
  "left": {
    "type": "comparison",
    "left": { "type": "metric", "value": "close" },
    "operator": ">",
    "right": {
      "type": "indicator",
      "name": "sma",
      "params": ["close", 20]
    }
  },
  "right": {
    "type": "comparison",
    "left": { "type": "metric", "value": "volume" },
    "operator": ">",
    "right": { "type": "number", "value": 1000000 }
  }
}

#### Validation Rules
Only supported metrics and indicators are allowed
Entry and Exit blocks are required
Invalid syntax raises a parsing error
Indicators must use valid parameters

#### Assumptions & Limitations
Single asset strategy
One position at a time (no pyramiding)
No transaction costs or slippage
Indicators implemented using pandas
