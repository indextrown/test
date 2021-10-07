import pybithumb
import time
정보보안기사
CEH(윤리적 해커)
CHFI(포렌식 전문가)
네트워크관리사
리눅스마스터
ISO 27001 인증심사원
한국정보기술연구원(KITRI) 침해대응전문가 수료
저는 사실 진로를 개발자로 전환한 케이스에요. 원래 정보보안 엔지니어
import datetime
try:
    def get_target_price():  #목표가를 반환하는 함수  함수의 정의
      df = pybithumb.get_ohlcv("XEC") #비트코인의 ohlcv값 가져옴
      변동폭 = df.iloc[-2]['high'] - df.iloc[-2]['low']
      목표가 = df.iloc[-1]['open'] + 변동폭
      return 목표가
    #매수기능
    def buy_cryto_currency(bithumb, price): #전달받은 빗썸 객체 함수 안에서 밸런스 조회 가능
      krw = bithumb.get_balance("XEC")[2]  #보유한 한화
      unit = (krw * 0.7)/ price            #원화 나누기 현재가, 0.7은 수수료
      return bithumb.buy_market_order("XEC", unit) #시장가 주문 사용, unit 개수만큼 구매

    def sell_crypto_currency(bithumb):   #매도기능
      unit = bithumb.get_balance("XEC")[0]  #잔고 얻어오기
      return bithumb.sell_market_order("XEC", unit) #BTC unit만큼 팔아라

    with open("bithumb.txt", "r") as f: #파일로부터 데이터 읽어옴
      key1 = f.readline().strip()       #파일을 읽어오고 양쪽 공백 제거
      key2 = f.readline().strip()       
  
    bithumb = pybithumb.Bithumb(key1, key2)  #읽어온 키값을 넣어줌, 빗썸클래스 생성
    목표가 = get_target_price()
    hold_flag = False #매수했다면True 아니면 False

    while True:

      price = pybithumb.get_current_price("XEC") #비트코인의 현재가 얻어오기


  
      if 목표가 <= price and hold_flag == False:#조건을 총족하면 매수
  
        ret = buy_cryto_currency(bithumb, price) #매수 기능 추가(빗썸클래스, 현재가 객체 입력받음)
        print("매수!!", ret)
        hold_flag = True
  


      now = datetime.datetime.now()
      mid = datetime.datetime(now.year, now.month, now.day, 00, 0, 0)
      delta = datetime.timedelta(seconds=10)


  
      if mid <= now <= mid + delta:
        ret = sell_crypto_currency(bithumb) #sell_crypto_currency함수에 bithumb객체전달 -> 매도
        print("매도", ret)
        목표가 = get_target_price()
        hold_flag = False
  
      print("현재시간:", now + delta ,"목표가:", 목표가, "현재가", price)
      time.sleep(1)
except:
     def get_target_price():  #목표가를 반환하는 함수  함수의 정의
       df = pybithumb.get_ohlcv("XEC") #비트코인의 ohlcv값 가져옴
       변동폭 = df.iloc[-2]['high'] - df.iloc[-2]['low']
       목표가 = df.iloc[-1]['open'] + 변동폭
       return 목표가
    #매수기능
     def buy_cryto_currency(bithumb, price): #전달받은 빗썸 객체 함수 안에서 밸런스 조회 가능
       krw = bithumb.get_balance("XEC")[2]  #보유한 한화
       unit = (krw * 0.7)/ price            #원화 나누기 현재가, 0.7은 수수료
       return bithumb.buy_market_order("XEC", unit) #시장가 주문 사용, unit 개수만큼 구매

     def sell_crypto_currency(bithumb):   #매도기능
       unit = bithumb.get_balance("XEC")[0]  #잔고 얻어오기
       return bithumb.sell_market_order("XEC", unit) #BTC unit만큼 팔아라

     with open("bithumb.txt", "r") as f: #파일로부터 데이터 읽어옴
       key1 = f.readline().strip()       #파일을 읽어오고 양쪽 공백 제거
       key2 = f.readline().strip()       
  
     bithumb = pybithumb.Bithumb(key1, key2)  #읽어온 키값을 넣어줌, 빗썸클래스 생성
     목표가 = get_target_price()
     hold_flag = False #매수했다면True 아니면 False

     while True:

       price = pybithumb.get_current_price("XEC") #비트코인의 현재가 얻어오기


  
       if 목표가 <= price and hold_flag == False:#조건을 총족하면 매수
  
         ret = buy_cryto_currency(bithumb, price) #매수 기능 추가(빗썸클래스, 현재가 객체 입력받음)
         print("매수!!", ret)
         hold_flag = True
  


       now = datetime.datetime.now()
       mid = datetime.datetime(now.year, now.month, now.day, 00, 0, 0)
       delta = datetime.timedelta(seconds=10)


  
       if mid <= now <= mid + delta:
         ret = sell_crypto_currency(bithumb) #sell_crypto_currency함수에 bithumb객체전달 -> 매도
         print("매도", ret)
         목표가 = get_target_price()
         hold_flag = False
  
       print("현재시간:", now + delta ,"목표가:", 목표가, "현재가", price)
       time.sleep(1)
