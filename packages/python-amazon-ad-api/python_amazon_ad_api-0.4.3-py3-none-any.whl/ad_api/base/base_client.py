import ad_api.version as vd
from ad_api.base.credential_provider import CredentialProvider


class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-ad-api'
    credential_provider_class = CredentialProvider

    def __init__(self, account='default', credentials=None):
        try:
            version = vd.__version__
            self.user_agent += f'-{version}'
        except:
            pass
        self.credentials = self.credential_provider_class(account, credentials).credentials
