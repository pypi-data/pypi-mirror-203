from typing import Any, Mapping, Optional
from .models import LogSeverity
import google.auth
import requests
from google.auth.credentials import Credentials
from google.auth.exceptions import GoogleAuthError
from google.auth.transport.requests import Request as GoogleRequest


class BaPublicApiClient:
    _url_base = 'https://data-workshop.beardsanalytics.com:2701/public-api'
    
    def __init__(self, credentials: Optional[Credentials] = None, project_id: Optional[str] = None) -> None:
        self._credentials, self._project_id = (credentials, None) if credentials else google.auth.default()
        if project_id:
            self._project_id = project_id

    def _request(self, method: str, endpoint: str, json=None, params=None):
        if not self._credentials:
            raise GoogleAuthError('Failed to authorise BA public API service (401)')
                
        if self._credentials.expired or not self._credentials.token:
            self._credentials.refresh(GoogleRequest())
            
        res = requests.request(method, self._url_base + endpoint, json=json, params=params, headers={'x-id-token': self._credentials.token})
        
        if res.status_code == 403:
            raise GoogleAuthError(f'Failed to use a BA service: {res.json()}')
        
        if res.status_code >= 500:
            raise RuntimeWarning('Failed to use a BA service. Please report the issue to developers of Beards Analytics.')
        
        return res.json()
    
    def create_cloud_log(self, log_name: str, message: str, severity: LogSeverity, k_service: str, project_id: Optional[str] = None, labels: Optional[Mapping[str, str]] = None, extra: Optional[Any] = None):
        payload = {
            'logName': log_name,
            'message': message,
            'kService': k_service,
            'severity': severity.value,
            'projectId': project_id or self._project_id or 'UNKNOWN',
            'labels': labels,
            'extra': extra
        }

        response = self._request('POST', '/create-cloud-log', json=payload)
                
        if not response.get('success'):
            raise RuntimeWarning(response)
