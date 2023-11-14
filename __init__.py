# flask run --host=0.0.0.0 --port=80

from flask import Flask, request, make_response, jsonify, render_template, Blueprint
from flask import Flask, request, make_response, jsonify, render_template, Blueprint
from flask_cors import CORS


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

    @app.route("/hello")
    def hello():
        pop_info = {'Seoul':2255555, 'Pusan':223333 }
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

    @app.route("/fonts/Noto_Sans_KR/NotoSansKR-Regular.woff", methods=['GET'])
    def NotoSansKR_Regular():
        return render_template('/static/fonts/Noto_Sans_KR/NotoSansKR-Regular.woff')

    @app.route("/fonts/Noto_Sans_KR/NotoSansKR-Medium.woff", methods=['GET'])
    def NotoSansKR_Medium():
        return render_template('/static/fonts/Noto_Sans_KR/NotoSansKR-Medium.woff')

    @app.route("/")
    def root():
        return render_template('index.html')
        
    @app.route("/index.html")
    def index():
        return render_template('index.html')

    @app.route("/mynft.html")
    def mynft():
        return render_template('mynft.html')

    @app.route("/sale.html")
    def sale():
        return render_template('sale.html')

    @app.route("/main.html")
    def main():
        print("init.py")
        return render_template('main.html')

    @app.route("/content.html")
    def content():
        print("init.py")
        return render_template('content.html')


    if __name__ == '__main__':
        #app.run(host="0.0.0.0", port="80")
        print("0.0.0.0 port=80")
        app.run(host="14.39.10.69", port="80")

    return app

'''
    @app.route("/mynft_detail.html")
    def mynft_detail():
        return render_template('mynft_detail.html') 

    @app.route("/mynft_detail_buy.html")
    def mynft_detail_buy():
        return render_template('mynft_detail_buy.html') 
'''