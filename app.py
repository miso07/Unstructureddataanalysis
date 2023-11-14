# flask run --host=0.0.0.0 --port=80


from flask import Flask, request, make_response, jsonify, render_template, Blueprint
from flask import Flask, request, make_response, jsonify, render_template, Blueprint
from flask_cors import CORS

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

req = urllib.request

def create_app():
    
    app = Flask(__name__)
    CORS(app)

    # 주소와 가격을 가져오는 view
    from .views import main_views
    app.register_blueprint(main_views.bp)

    # 블랙리터만 관련 자료를 가져오는 view
    from .views import main_views2
    app.register_blueprint(main_views2.bp)

    # 분할 futechAI 관련 자료를 가져오는 view
    from .views import main_views3
    app.register_blueprint(main_views3.bp)

    @app.route("/mynft")
    def lands_price():
        # 지역코드: 행정표준코드관리시스템의 법정동코드
        lawdCd = request.args.get('lawdCd') 
        # 계약월: 실거래 자료의 계약년월(6자리)
        dealYmd = request.args.get('dealYmd')
        # 아파트 매매 자료: 지역코드와 계약월(기간)을 이용하여 해당지역의 아파트 매매 신고자료 정보를 조회
        ret = getRTMSDataSvcAptTrade(lawdCd, dealYmd,'K6mCWRYYKmxkX9Z3KGULuHm83nxAiiNh0aFb93xQoZbThPn0w66I4WQPJo2K%2BzT2aj0kmpSTj92eelEOKKkuBA%3D%3D')
        js = ret.to_json(orient='table')
        return js

    @app.route("/hello")
    def hello():
        pop_info = {'Seoul':1155555, 'Pusan':1133333 }
        return jsonify(pop_info)

    @app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
    def test():
        if request.method == 'GET':
            print('GET')
            user = request.args.get('email')
            print(user)
        return make_response(jsonify({'status': True}), 200)


    @app.route("/test2", methods=['GET', 'POST', 'PUT', 'DELETE'])
    def test2():
        if request.method == 'GET':
            print('GET')
            user = request.args.get('email')
            print(user)
        return make_response(jsonify({'status': True}), 200)


    @app.route("/")
    def root():
        return render_template('content.html')
        
    @app.route("/index.html")
    def index():
        return render_template('content.html')

    @app.route("/main.html")
    def main():
        print("app.py")
        return render_template('main.html')

    @app.route("/content.html")
    def content2():
        print("app.py")
        return render_template('content.html')

    @app.route("/content.html/<button>")
    def content(button):
        print("app.py")
        return render_template('content.html', btn_state=button)

    @app.route("/qna.html")
    def qna2():
        print("app.py")
        return render_template('qna.html')

    @app.route("/qna.html/<button>")
    def qna(button):
        print("app.py")
        return render_template('qna.html', btn_state=button)

    @app.route("/qna2.html")
    def qna22():
        print("app.py")
        return render_template('qna2.html')



    @app.route("/sum.html")
    def sum():
        print("app.py")
        return render_template('sum.html')

    if __name__ == '__main__':
        print("0.0.0.0 port=80")
        app.run(host="localhost", port="80")

    return app


'''
    @app.route("/content.html")
    def content():
        print("app.py")
        return render_template('content.html')

    @app.route("/qna.html")
    def qna():
        print("app.py")
        return render_template('qna.html')
'''



def getRTMSDataSvcAptTrade(LAWD_CD, DEAL_YMD, serviceKey):
    url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
    url = url + "?&LAWD_CD=" + LAWD_CD
    url = url + "&DEAL_YMD=" + DEAL_YMD
    url = url + "&serviceKey=" + serviceKey

    xml = req.urlopen(url)
    result = xml.read()
    soup = BeautifulSoup(result, 'lxml-xml')

    items = soup.findAll("item")
    aptTrade = pd.DataFrame()

    for item in items:
        dealAmount = item.find("거래금액").text
        buildYear = item.find("건축년도").text
        dealYear = item.find("년").text
        dong = item.find("법정동").text
        apartmentName = item.find("아파트").text
        dealMonth = item.find("월").text
        dealDay = item.find("일").text
        areaForExclusiveUse = item.find("전용면적").text
        jibun = item.find("지번").text
        regionalCode = item.find("지역코드").text
        floor = item.find("층").text
        buildYear = item.find("건축년도").text

        temp = pd.DataFrame(([
            [dealAmount, buildYear, dealYear, dong, apartmentName, dealMonth, dealDay, areaForExclusiveUse, jibun,
             regionalCode, floor, buildYear]]),
                            columns=["dealAmount", "buildYear", "dealYear", "dong", "apartmentName", "dealMonth",
                                     "dealDay", "areaForExclusiveUse", "jibun", "regionalCode", "floor", "buildYear"])
        aptTrade = pd.concat([aptTrade, temp]).head(10)

    aptTrade = aptTrade.reset_index(drop=True)

    print(aptTrade);

    return aptTrade