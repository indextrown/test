#-*-coding:utf-8 -*-
import myUpbit   #우리가 만든 함수들이 들어있는 모듈
import time
import pyupbit



access = "eBxRxPC9YIZ637OxoI31039aWCx4YNa5TdAUJF6a"          # 본인 값으로 변경
secret = "bnxPLUdOx8MWEiwpq37z99MKSCFDkztb4NXsZUox"            # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

balances = upbit.get_balances()

print(balances)
