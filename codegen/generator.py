def generate_condition(ast, df_name="df"):
    if ast["type"] == "comparison":
        left = render_value(ast["left"], df_name)
        right = render_value(ast["right"], df_name)
        return f"({left} {ast['op']} {right})"

    if ast["type"] == "and":
        return f"{generate_condition(ast['left'])} & {generate_condition(ast['right'])}"

    if ast["type"] == "or":
        return f"{generate_condition(ast['left'])} | {generate_condition(ast['right'])}"

def render_value(node, df_name):
    if isinstance(node, float):
        return str(node)

    if node["type"] == "metric":
        return f"{df_name}['{node['value']}']"

    if node["type"] == "indicator":
        if node["name"] == "sma":
            return f"{df_name}['{node['metric']}'].rolling({node['period']}).mean()"
        if node["name"] == "rsi":
            return f"rsi({df_name}['{node['metric']}'], {node['period']})"
