# NL → DSL → Strategy Execution Prototype

This repository contains a minimal end-to-end prototype that demonstrates how
natural-language trading rules can be translated into a domain-specific language (DSL),
parsed into an abstract syntax tree (AST), converted into executable Python logic,
and evaluated using a simplified backtest simulator.

The goal of this project is to showcase **DSL design, parsing, AST construction,
code generation, and execution**, rather than to build a production-grade trading
or NLP system.


## Overview

The system implements the following pipeline:

1. **Natural Language Input**
   - Example:  
     *"Buy when the close price is above the 20-day moving average and volume is above 1 million."*

2. **Natural Language → Structured Representation**
   - Converts the input into a constrained, structured rule format

3. **DSL Generation**
   - Produces a readable, unambiguous domain-specific language

4. **DSL Parsing & AST Construction**
   - Uses a formal grammar to validate syntax and build an AST

5. **AST → Python Code Generation**
   - Generates vectorized pandas logic for entry and exit conditions

6. **Strategy Execution**
   - Evaluates signals on OHLCV time-series data

7. **Backtest Simulation**
   - Executes a simplified trade lifecycle and reports results

## Project Structure

nl/ # Natural language → structured rule conversion
dsl/ # DSL grammar, parser, and AST construction
codegen/ # AST → Python (pandas) code generator
execution/ # Indicators, simulator, and sample data
demo.py # End-to-end demonstration script
DSL_SPEC.md # DSL grammar specification
README.md 

## Requirements
- Python 3.9 or higher
- pandas
- lark

Install dependencies and run:

```bash

pip install pandas lark
python demo.py

'''

The demo script performs the following steps:

Accepts a natural-language trading rule

Converts it into a structured representation

Generates DSL text

Parses the DSL into an AST

Generates executable pandas-based logic

Evaluates entry and exit signals on sample data

Runs a simplified backtest simulation

Prints a summary of results (trades, PnL)

