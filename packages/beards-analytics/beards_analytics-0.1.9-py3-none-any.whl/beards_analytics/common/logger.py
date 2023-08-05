from beards_analytics.public_api.client import BaPublicApiClient
from beards_analytics.public_api.models import LogSeverity
from beards_analytics.public_api._metadata import K_SERVICE, PROJECT_ID
from google.auth.exceptions import GoogleAuthError
from google.auth.credentials import Credentials
import typing as t
import ujson


class Logger:
    _instance: "Logger" = None
    
    def __new__(cls) -> "Logger":
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, credentials: t.Optional[Credentials] = None) -> None:
        self._ba_api_client = None
        self._credentials = credentials

    def _log(self, severity: LogSeverity, message: str, send_to_ba=False, log_name=None, **kwargs):
        message = str(message)
        log_obj = dict(severity=severity.name, message=message, **kwargs)
        print(ujson.dumps(log_obj))
        
        if not send_to_ba or not K_SERVICE or not PROJECT_ID:
            return
        
        client = self._ba_api_client or BaPublicApiClient(credentials=self._credentials)
        self._ba_api_client = client
        
        if not log_name:
            log_name = 'cloud_service'
            
        try:
            client.create_cloud_log(log_name, message, severity, k_service=K_SERVICE, project_id=PROJECT_ID, extra=kwargs)
        except (GoogleAuthError, RuntimeWarning) as e:
            self.warning(e, send_to_ba=False)
            
    def deafult(self, message: str, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.DEFAULT, message, send_to_ba, **kwargs)
    
    def debug(self, message: str, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.DEBUG, message, send_to_ba, **kwargs)
    
    def info(self, message: str, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.INFO, message, send_to_ba, **kwargs)
    
    def notice(self, message: str, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.NOTICE, message, send_to_ba, **kwargs)
        
    def warning(self, message: str, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.WARNING, message, send_to_ba, **kwargs)
    
    def error(self, message: str, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.ERROR, message, send_to_ba, **kwargs)
    
    def critical(self, message: str, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.CRITICAL, message, send_to_ba, **kwargs)
    
    def alert(self, message: str, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.ALERT, message, send_to_ba, **kwargs)
    
    def emergency(self, message: str, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.EMERGENCY, message, send_to_ba, **kwargs)
    
    def log_dbt_output(self, output: str):
        raise NotImplementedError()
