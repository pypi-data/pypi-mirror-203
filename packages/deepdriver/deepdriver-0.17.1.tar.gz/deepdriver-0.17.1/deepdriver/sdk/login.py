from assertpy import assert_that
import requests
from deepdriver.sdk.interface import interface
from deepdriver import logger
from deepdriver.sdk import util
# deepdriver 실험환경을 사용하기위한 로그인 과정
# 서버의 login api를 호출하여 key를 서버로 전송하고 결과로서 jwt key를 받는다

def login(key: str=None, id: str =None, pw: str=None) -> (bool, str):
    #assert_that(key).is_not_none()
    gtoken = None
    if key is None and id is None:

        if util.is_notebook():
            import ipywidgets as widgets
            selected_login_method = widgets.Dropdown(
                options=['email', 'google'],
                value='email',
                description='login method')
            if selected_login_method =='google':
                login_with_google = "g"
            else:
                login_with_google = "e"
        else:
            login_with_google = input('login with Google: \n( Enter "g" to sign in with Google.If other characters are entered, email login proceeds.)')
        if selected_login_method == "e":
            import getpass
            id = input('Enter your email:')
            pw = getpass.getpass('Enter your password:')
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            client_secrets_file =None
            import os
            import site
            for path in site.getsitepackages():
                if os.path.isfile(path + "/deepdriver/" + "client_secrets.json"):
                    client_secrets_file = path + "/deepdriver/" + "client_secrets.json"
            assert_that(client_secrets_file).is_not_none()

            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scopes=['openid', 'https://www.googleapis.com/auth/userinfo.profile',
                        'https://www.googleapis.com/auth/userinfo.email'], redirect_uri='urn:ietf:wg:oauth:2.0:oob')

            auth_url, _ = flow.authorization_url(prompt='consent')

            print('Please go to this URL: {}'.format(auth_url))
            code = input('Enter the authorization code: ')
            a = flow.fetch_token(code=code)
            gtoken = a['id_token']

            # You can use flow.credentials, or you can just get a requests session
            # using flow.authorized_session.
            session = flow.authorized_session()
            user_info =session.get('https://www.googleapis.com/userinfo/v2/me').json()
            id = user_info["email"]

    else:
        assert_that(pw).is_not_none()

    try:
        return interface.login(key,id,pw, gtoken)[0]
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError) as e:
        logger.error(f"Could Login to Server[{interface.get_http_host()}]. Set Server IP/PORT using deepdriver.setting()")
        return False



