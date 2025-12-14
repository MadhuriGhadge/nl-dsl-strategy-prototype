from lark import Transformer, Tree

class ASTBuilder(Transformer):
    def and_expr(self, items):
        return {"type": "and", "left": self._to_dict(items[0]), "right": self._to_dict(items[1])}

    def or_expr(self, items):
        return {"type": "or", "left": self._to_dict(items[0]), "right": self._to_dict(items[1])}

    def comparison(self, items):
        left = self._to_dict(items[0])
        op = str(items[1])
        right = self._to_dict(items[2])
        return {"type": "comparison", "left": left, "op": op, "right": right}

    def METRIC(self, token):
        return {"type": "metric", "value": str(token)}

    def INDICATOR(self, token):
        name, rest = token.split("(")
        metric, period = rest[:-1].split(",")
        return {
            "type": "indicator",
            "name": name.lower(),
            "metric": metric,
            "period": int(period)
        }

    def NUMBER(self, token):
        return float(token)

    def _to_dict(self, obj):
        if isinstance(obj, Tree):
            return obj.children[0] if len(obj.children) == 1 else [self._to_dict(c) for c in obj.children]
        return obj
