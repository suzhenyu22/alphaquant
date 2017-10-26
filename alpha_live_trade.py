import sys

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from alpha_trade import AlphaTrade

import time

class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


_g_session_str = ""
_g_server = "127.0.0.1"
_g_port = 58899

ERR_BROKER_NOT_EXIST = 1
ERR_NOT_SUPPORT = 2
ERR_GET_ACCOUNT_INFO_FAILED = 3
ERR_EXCEPTION = 4
ERR_INTERNAL = 5
ERR_NETWORK = 6
ERR_SIGNATURE= 7
ERR_NOT_LOGIN = 10

def _create_client():

    transport = TTransport.TFramedTransport(TSocket.TSocket(_g_server, _g_port))
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = AlphaTrade.Client(protocol)

    transport.open()

    return client


def StartSDK(str2):
    global _g_session_str
    _g_session_str = str2

    try:
        _create_client().KeepAlive(str2)
    except:
        print("except: ", sys.exc_info())

def SetServer(host, port):
    global _g_server
    global _g_port

    _g_server = host
    _g_port = port

def Running():
    return _create_client().Running()

def GetPID():
    return _create_client().GetPID()


def LiveTradeLogin(account, password1, password2, brokerstr, wait_result = True):

    ret = Map({})

    try:
        login_ret = _create_client().LiveTradeLogin(_g_session_str, account, password1, password2, brokerstr)
        liveTradeID = login_ret.result

        while wait_result:
            state = GetAccountState(liveTradeID)
            if state.state == "idle" or state.state == "logining":
                time.sleep(0.05)
            else:
                break

        return login_ret
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret


def LiveTradeLogout(liveTradeID):

    ret = Map({})

    try:
        return _create_client().LiveTradeLogout(_g_session_str, liveTradeID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def GetAccountState(liveTradeID):

    ret = Map({})


    try:
        return _create_client().GetAccountState(_g_session_str, liveTradeID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def GetAccountBalance(liveTradeID):

    """
    struct AccountBalance {
      1: double total_value,
      2: double money_left,
    }
    """
    ret = Map({})


    try:
        return _create_client().GetAccountBalance(_g_session_str, liveTradeID)

    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def GetHoldingStock(liveTradeID):

    ret = Map({})

    try:
        return _create_client().GetHoldingStock(_g_session_str, liveTradeID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def GetOrderState(liveTradeID, orderID):

    ret = Map({})

    try:

        return _create_client().GetOrderState(_g_session_str, liveTradeID, orderID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def GetAllOrder(liveTradeID):
    ret = Map({})

    try:

        return _create_client().GetAllOrder(_g_session_str, liveTradeID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def CancelOrder(liveTradeID, orderID):

    ret = Map({})

    try:
        return _create_client().CancelOrder(_g_session_str, liveTradeID, orderID)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def LiveTradeBuy(liveTradeID, sid, price, quant, orderType):
    return LiveTradeBuyOpen(liveTradeID, sid, price, quant, orderType)

def LiveTradeBuyOpen(liveTradeID, sid, price, quant, orderType):

    ret = Map({})

    try:
        return _create_client().LiveTradeBuyOpen(_g_session_str, liveTradeID, sid, price, quant, orderType)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def LiveTradeBuyClose(liveTradeID, sid, price, quant, orderType, closeToday=True):

    ret = Map({})

    try:
        return _create_client().LiveTradeBuyClose(_g_session_str, liveTradeID, sid, price, quant, orderType, closeToday)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def LiveTradeSell(liveTradeID, sid, price, quant, orderType, closeToday=True):
    return LiveTradeSellClose(liveTradeID, sid, price, quant, orderType, closeToday)

def LiveTradeSellClose(liveTradeID, sid, price, quant, orderType, closeToday=True):

    ret = Map({})

    try:
        return _create_client().LiveTradeSellClose(_g_session_str, liveTradeID, sid, price, quant, orderType, closeToday)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret

def LiveTradeSellOpen(liveTradeID, sid, price, quant, orderType):

    ret = Map({})

    try:
        return _create_client().LiveTradeSellOpen(_g_session_str, liveTradeID, sid, price, quant, orderType)
    except:
        print("except: ", sys.exc_info())

        ret.ret_code = ERR_EXCEPTION

        return ret
