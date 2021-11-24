import pyupbit
import time
import pandas as pd
import myUpbit.py




access = "eBxRxPC9YIZ637OxoI31039aWCx4YNa5TdAUJF6a"          # 본인 값으로 변경
secret = "bnxPLUdOx8MWEiwpq37z99MKSCFDkztb4NXsZUox"            # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.buy_market_order("KRW-TT", 180000))

print(upbit.get_balance("KRW-TT"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
