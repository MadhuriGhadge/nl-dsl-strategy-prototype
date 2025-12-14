def run_backtest(df, entry_signal, exit_signal):
    in_position = False
    trades = []

    for i in range(len(df)):
        if entry_signal.iloc[i] and not in_position:
            entry_price = df["open"].iloc[i]
            in_position = True

        elif exit_signal.iloc[i] and in_position:
            exit_price = df["open"].iloc[i]
            trades.append(exit_price - entry_price)
            in_position = False

    return {
        "trades": len(trades),
        "total_pnl": sum(trades)
    }
