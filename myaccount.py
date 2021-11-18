#-*-coding:utf-8 -*-
import myUpbit   #우리가 만든 함수들이 들어있는 모듈
import time
import pyupbit



access = "eBxRxPC9YIZ637OxoI31039aWCx4YNa5TdAUJF6a"          # 본인 값으로 변경
secret = "bnxPLUdOx8MWEiwpq37z99MKSCFDkztb4NXsZUox"            # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)




balances = upbit.get_balances()

print(balances)



#내가 매수할 총 코인 개수
MaxCoinCnt = 5.0

#처음 매수할 비중(퍼센트)
FirstRate = 10.0
#추가 매수할 비중 (퍼센트)
WaterRate = 5.0

#내가 가진 잔고 데이터를 다 가져온다.
balances = upbit.get_balances()

TotalMoeny = GetTotalMoney(balances) #총 원금
TotalRealMoney = GetTotalRealMoney(balances) #총 평가금액

#내 총 수익율
TotalRevenue = (TotalRealMoney - TotalMoeny) * 100.0/ TotalMoeny

#코인당 매수할 최대 매수금액
CoinMaxMoney = TotalMoeny / MaxCoinCnt


#처음에 매수할 금액 
FirstEnterMoney = CoinMaxMoney / 100.0 * FirstRate 

#그 이후 매수할 금액 
WaterEnterMoeny = CoinMaxMoney / 100.0 * WaterRate

print("-----------------------------------------------")
print ("Total Money:", GetTotalMoney(balances))
print ("Total Real Money:", GetTotalRealMoney(balances))
print ("Total Revenue", TotalRevenue)
print("-----------------------------------------------")
print ("CoinMaxMoney : ", CoinMaxMoney)
print ("FirstEnterMoney : ", FirstEnterMoney)
print ("WaterEnterMoeny : ", WaterEnterMoeny)


