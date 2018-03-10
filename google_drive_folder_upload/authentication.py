from pydrive.auth import GoogleAuth


class Authenticator:

    client_secrets_file_path = 'config/client_secrets.json'
    credentials_file_path = 'config/mycreds.txt'

    def __new__(cls):

        auth = GoogleAuth(cls.client_secrets_file_path)
        auth.LoadCredentialsFile(cls.credentials_file_path)

        if auth.credentials is None:
            auth.LocalWebserverAuth()
        elif auth.access_token_expired:
            auth.Refresh()
        else:
            auth.Authorize()
        auth.SaveCredentialsFile(cls.credentials_file_path)
        return auth
