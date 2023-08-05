import os
import requests


class Secret():
    _name = None
    _value = None


    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        if self._value is None:
            self._value = os.environ[self._name]
            if self._value is None:
                raise Exception(f'The variable {self._name} is not set on Cortex or local environment variables.')
        return self._value


    def __init__(self, name, value):
        self._name = name
        self._value = value


class SecretsManager():
    _api_url = None
    _headers = None
    _secrets = []


    def __init__(self, api_url, headers):
        self._api_url = api_url
        self._headers = headers


    def get_secret(self, name):
        for secrets in self._secrets:
            if secrets.name == name:
                return secrets.value
        # Override secret if it exists in local environment variables
        env_var = os.environ.get(name)

        if env_var is not None:
            secret = Secret(name, env_var)
            self._secrets.append(secret)
            return secret.value

        # If secret is not in local environment variables, get it from Cortex
        value = None
        # Get secret
        response = requests.get(
            f'{self._api_url}/secrets/{name}',
                headers=self._headers
        )

        if 'status' not in response:
            value = response.text

        secret = Secret(name, value)
        self._secrets.append(secret)

        return secret.value


    def reset_secrets(self):
        self._secrets = []
