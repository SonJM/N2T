from flask import Flask
from flask_oauthlib.client import OAuth

def get_tistory_access_code(Self, client_id, redirect_uri):
        app = Flask(__name__)
        app.secret_key = '  '

        oauth = OAuth(app)

        tistory = oauth.remote_app(
            'tistory',
            consumer_key='your_tistory_consumer_key',
            consumer_secret='your_tistory_consumer_secret',
            request_token_params={
                'scope': 'email',
                'prompt': 'select_account'
            },
            base_url='https://www.tistoryapis.com/oauth2/v1/',
            request_token_url=None,
            access_token_method='POST',
            access_token_url='https://accounts.tistory.com/o/oauth2/token',
            authorize_url='https://accounts.tistory.com/o/oauth2/auth',
        )

        @app.route('/login')
        def login():
            return tistory.authorize(callback=url_for('authorized', _external=True))

        @app.route('/authorized')
        def authorized():
            resp = tistory.authorized_response()
            if resp is None:
                return 'Access denied: reason={0} error={1}'.format(
                    request.args['error_reason'],
                    request.args['error_description']
                )
            access_token = resp['access_token']
            # access_token을 사용하여 사용자 정보를 가져올 수 있음
            # 사용자 정보 가져오기는 인증 서비스의 API 문서를 참조하세요 

            return 'Logged in as {0}'.format(tistory.get('https://www.tistoryapis.com/oauth2/v1/userinfo').data['email'])

        @tistory.tokengetter
        def get_tistory_oauth_token():
            return session.get('tistory_token')