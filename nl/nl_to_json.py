import json

def nl_to_json(nl: str) -> dict:
    if "moving average" in nl.lower():
        return {
            "entry": [
                {"left": "close", "op": ">", "right": {"type": "sma", "metric": "close", "period": 20}},
                {"left": "volume", "op": ">", "right": 1000000}
            ],
            "exit": [
                {"left": {"type": "rsi", "metric": "close", "period": 14}, "op": "<", "right": 30}
            ]
        }

    raise ValueError("Unsupported NL input")
