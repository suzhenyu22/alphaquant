import alpha_live_trade
import time

if __name__ == "__main__":
    #alpha_live_trade.SetServer("ip or host", 58899)

    ret = alpha_live_trade.StartSDK("")

    ret = alpha_live_trade.LiveTradeLogin("XXXXXXXXXXXX", "XXXXXX", "XXXXXX", "stock_huatai")

    #ret = alpha_live_trade.LiveTradeLogin("XXXXXXXXXXXX", "XXXXXX", "", "stock_guangfa")

    live_trade_id = ret.result

    ret = alpha_live_trade.LiveTradeSell(live_trade_id, '600016', 8.95, 100, 'limit')

    ret = alpha_live_trade.LiveTradeSell(live_trade_id, '002610', 2.65, 100, 'market')

    alpha_live_trade.LiveTradeLogout(live_trade_id)
