#-*-coding:utf-8 -*-
import myUpbit   #우리가 만든 함수들이 들어있는 모듈
import time
import pyupbit



access = "eBxRxPC9YIZ637OxoI31039aWCx4YNa5TdAUJF6a"          # 본인 값으로 변경
secret = "bnxPLUdOx8MWEiwpq37z99MKSCFDkztb4NXsZUox"            # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


#업비트 객체를 만든다
upbit = pyupbit.Upbit(access, secret)

#내가 매수할 총 코인 개수
MaxCoinCnt = 10.0

#처음 매수할 비중(퍼센트)
FirstRate = 10.0
#추가 매수할 비중 (퍼센트)
WaterRate = 5.0

#내가 가진 잔고 데이터를 다 가져온다.
balances = upbit.get_balances()

TotalMoeny = myUpbit.GetTotalMoney(balances) #총 원금
TotalRealMoney = myUpbit.GetTotalRealMoney(balances) #총 평가금액

#내 총 수익율
TotalRevenue = (TotalRealMoney - TotalMoeny) * 100.0/ TotalMoeny

#코인당 매수할 최대 매수금액
CoinMaxMoney = TotalMoeny / MaxCoinCnt


#처음에 매수할 금액 
FirstEnterMoney = CoinMaxMoney / 100.0 * FirstRate 

#그 이후 매수할 금액 
WaterEnterMoeny = CoinMaxMoney / 100.0 * WaterRate

print("-----------------------------------------------")
print ("Total Money:", myUpbit.GetTotalMoney(balances))
print ("Total Real Money:", myUpbit.GetTotalRealMoney(balances))
print ("Total Revenue", TotalRevenue)
print("-----------------------------------------------")
print ("CoinMaxMoney : ", CoinMaxMoney)
print ("FirstEnterMoney : ", FirstEnterMoney)
print ("WaterEnterMoeny : ", WaterEnterMoeny)



#거래대금이 많은 탑코인 30개의 리스트
TopCoinList = myUpbit.GetTopCoinList("minute3",30)

#구매 제외 코인 리스트
OutCoinList = ['KRW-MARO','KRW-TSHP','KRW-PXL','KRW-BTC']

#나의 코인
LovelyCoinList = ['KRW-BTC','KRW-ETH','KRW-DOGE','KRW-DOT']


Tickers = pyupbit.get_tickers("KRW")


for ticker in Tickers:
    try: 
        print("Coin Ticker: ",ticker)

          
  
        ############영상엔 없지만 여기서 물을 타줄 수도 있다.
        if myUpbit.IsHasCoin(balances,ticker) == True:

            #예로 수익율이 마이너스 5% 미만이라면 물탈 비중만큼 물을 탄다.
            #수익율을 구한다.
            revenu_rate = myUpbit.GetRevenueRate(balances,ticker)

            #수익율이 마이너스 5%이면서 
            if revenu_rate < -5.0:
                            
                #현재 코인의 총 매수금액
                NowCoinTotalMoney = myUpbit.GetCoinNowMoney(balances,ticker)
                print("CHEK WATER")
                print(CoinMaxMoney, " >", NowCoinTotalMoney)

                #매수 비중이 남았다면
                if CoinMaxMoney > NowCoinTotalMoney:
                    #이전 주문들을 취소하고
                    myUpbit.CancelCoinOrder(upbit,ticker)

                    #시장가 매수를 한다.
                    balances = myUpbit.BuyCoinMarket(upbit,ticker,FirstEnterMoney)

                    #평균매입단가와 매수개수를 구해서 0.5% 상승한 가격으로 지정가 매도주문을 걸어놓는다.
                    avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
                    coin_volume = upbit.get_balance(ticker)

                    avgPrice *= 1.005
                    #지정가 매도를 한다.
                    myUpbit.SellCoinLimit(upbit,ticker,avgPrice,coin_volume)


            continue

  
  
        #거래량 많은 탑코인 리스트안의 코인이 아니라면 스킵! 탑코인에 해당하는 코인만 이후 로직을 수행한다.
        if myUpbit.CheckCoinInList(TopCoinList,ticker) == False:
            continue
        #위험한 코인이라면 스킵!!!
        if myUpbit.CheckCoinInList(OutCoinList,ticker) == True:
            continue
        #나만의 러블리만 사겠다! 그 이외의 코인이라면 스킵!!!
         #if CheckCoinInList(LovelyCoinList,ticker) == False:
        #    continue

        print("!!!!! Target Coin!!! :",ticker)


            
        time.sleep(0.05)
        #영상에선 1분봉으로 만들었지만 최종적으로 5분으로 변경해 봅니다
        df = pyupbit.get_ohlcv(ticker,interval="minute3") #5분봉 데이타를 가져온다.


        #5일선 값을 구한다.
        ma5_before3 = myUpbit.GetMA(df,5,-4)
        ma5_before2 = myUpbit.GetMA(df,5,-3)
        ma5 = myUpbit.GetMA(df,5,-2)

        #20일선 값을 구한다.
        ma20 = myUpbit.GetMA(df,20,-2)

        print("ma20 :", ma20)
        print("ma5 :", ma5 , " <- ", ma5_before2, " <- ", ma5_before3)

        rsi_min = myUpbit.GetRSI(df,14,-1)
        print("-rsi_min:", rsi_min)




        print("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        ################################새로 추가된 지표 참고용으로 필요하시면 봇에 활용해 보세요!##############################################################

        #볼린저 밴드 구하는 함수는 실제 차트와 다소 오차가 존재하지만 활용하는데는 무리가 없습니다!
        #볼린저 밴드 함수는 아래와 같이 딕셔너리 형식으로 값을 리턴하며 upper가 상단, ma는 기준이 되는 이동평균선(여기선 20일선),lower가 하단이 됩니다.
        print("-----------------------------------------------")
        #이전 캔들의 볼린저 밴드 상하단
        BB_dic_before = myUpbit.GetBB(df,20,-2)
        print("before - MA:",BB_dic_before['ma'],", Upper:", BB_dic_before['upper'] ,", Lower:" ,BB_dic_before['lower'])

        print("-----------------------------------------------")
        #현재 볼린저 밴드 상하단
        BB_dic_now = myUpbit.GetBB(df,20,-1)
        print("now - MA:",BB_dic_now['ma'],", Upper:", BB_dic_now['upper'] ,", Lower:" ,BB_dic_now['lower'])



        #MACD값을 구해줍니다!
        #MACD함수는 아래와 같이 딕셔너리 형식으로 값을 리턴하며 macd는 MACD값, macd_siginal값이 시그널값, ocl이 오실레이터 값이 됩니다
        print("-----------------------------------------------")
        macd_before = myUpbit.GetMACD(df,-2) #이전캔들의 MACD
        print("before - MACD:",macd_before['macd'], ", MACD_SIGNAL:", macd_before['macd_siginal'],", ocl:", macd_before['ocl'])
        print("-----------------------------------------------")
        macd = myUpbit.GetMACD(df,-1) #현재캔들의 MACD
        print("now - MACD:",macd['macd'], ", MACD_SIGNAL:", macd['macd_siginal'],", ocl:", macd['ocl'])




        #일목균형표(일목구름) 구해줍니다! 다소 오차는 있을 수 있으나 활용하는데 무리는 없습니다.
        #일목균형표(일목구름)함수는 아래와 같이 딕셔너리 형식으로 값을 리턴하며 conversion는 전환선, base는 기준선
        #huhang_span은 후행스팬, sunhang_span_a는 선행스팬1, sunhang_span_b는 선행스팬2 입니다.
        print("-----------------------------------------------")
        ic_before = myUpbit.GetIC(df,-2) #이전캔들의 일목균형표
        print("before - Conversion:",ic_before['conversion'], ", Base:", ic_before['base'],", HuHang_Span:", ic_before['huhang_span'],", SunHang_Span_a:", ic_before['sunhang_span_a'],", SunHang_Span_b:", ic_before['sunhang_span_b'])

        print("-----------------------------------------------")
        ic = myUpbit.GetIC(df,-1) #현재캔들의 일목균형표
        print("now - Conversion:",ic['conversion'], ", Base:", ic['base'],", HuHang_Span:", ic['huhang_span'],", SunHang_Span_a:", ic['sunhang_span_a'],", SunHang_Span_b:", ic['sunhang_span_b'])




        print("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")




        #5일선이 20일선 밑에 있을 때 5일선이 상승추세로 꺽이면 매수를 진행하자!!
        if ma5 < ma20 and ma5_before3 > ma5_before2 and ma5_before2 < ma5 and myUpbit.GetHasCoinCnt(balances) < MaxCoinCnt  :
            print("!!!!!!!!!!!!!!!DANTA DANTA First Buy GoGoGo!!!!!!!!!!!!!!!!!!!!!!!!")
            #영상엔 없지만 지정가 주문을 걸기 전에 이전 주문들을 취소해야 된다.
            myUpbit.CancelCoinOrder(upbit,ticker)

            #시장가 매수를 한다.
            balances = myUpbit.BuyCoinMarket(upbit,ticker,FirstEnterMoney)

            #평균매입단가와 매수개수를 구해서 0.5% 상승한 가격으로 지정가 매도주문을 걸어놓는다.
            avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
            coin_volume = upbit.get_balance(ticker)

            avgPrice *= 1.005
            #지정가 매도를 한다.
            myUpbit.SellCoinLimit(upbit,ticker,avgPrice,coin_volume)



        #1분봉 기준으로 30이하일때 매수를 한다.
        if rsi_min < 30.0 and myUpbit.GetHasCoinCnt(balances) < MaxCoinCnt :
            print("!!!!!!!!!!!!!!!DANTA DANTA RSI First Buy GoGoGo!!!!!!!!!!!!!!!!!!!!!!!!")
            #영상엔 없지만 지정가 주문을 걸기 전에 이전 주문들을 취소해야 된다.
            myUpbit.CancelCoinOrder(upbit,ticker)
            
            #시장가 매수를 한다.
            balances = myUpbit.BuyCoinMarket(upbit,ticker,FirstEnterMoney)

            #평균매입단가와 매수개수를 구해서 0.5% 상승한 가격으로 지정가 매도주문을 걸어놓는다.
            avgPrice = myUpbit.GetAvgBuyPrice(balances,ticker)
            coin_volume = upbit.get_balance(ticker)

            avgPrice *= 1.005

            #지정가 매도를 한다.
            myUpbit.SellCoinLimit(upbit,ticker,avgPrice,coin_volume)

            

    except Exception as e:
        print("---:", e)



























