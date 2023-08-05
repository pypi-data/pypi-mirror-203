import os
import urllib.request
import urllib.error


_METADATA = {}

# https://cloud.google.com/appengine/docs/standard/java/accessing-instance-metadata
key_list = {
    # The project number assigned to your project.
    "numeric_project_id": "/computeMetadata/v1/project/numeric-project-id",
    # The project ID assigned to your project.
    "project_id": "/computeMetadata/v1/project/project-id",
    # The zone the instance is running in.
    "zone": "/computeMetadata/v1/instance/zone",
    # no description
    "aliases": "/computeMetadata/v1/instance/service-accounts/default/aliases",
    # The default service account email assigned to your project.
    "email": "/computeMetadata/v1/instance/service-accounts/default/email",
    # Lists all the default service accounts for your project.
    "service-accounts": "/computeMetadata/v1/instance/service-accounts/default/",
    # Lists all the supported scopes for the default service accounts.
    "scopes": "/computeMetadata/v1/instance/service-accounts/default/scopes",
    # Returns the auth token that can be used to authenticate your application to other Google Cloud APIs.
    "token": "/computeMetadata/v1/instance/service-accounts/default/token",
}

def _get_metadata(key: str) -> str | None:
    """Get metadata string. Works on GAE, GCF, and the others.
    This file will be used on GAE/GCF/others.
    https://cloud.google.com/appengine/docs/standard/java/accessing-instance-metadata
    Args:
        key (str): Metadata endpoint or a key of key_list(see below).
    Returns:
        str: return string from metadata server.
    Note:
        key_list
            numeric_project_id: /computeMetadata/v1/project/numeric-project-id
            project_id: /computeMetadata/v1/project/project-id
            zone: /computeMetadata/v1/instance/zone
            aliases: /computeMetadata/v1/instance/service-accounts/default/aliases
            email: /computeMetadata/v1/instance/service-accounts/default/email
            service-accounts: /computeMetadata/v1/instance/service-accounts/default/
            scopes: /computeMetadata/v1/instance/service-accounts/default/scopes
            token: /computeMetadata/v1/instance/service-accounts/default/token
    """
    global _METADATA, key_list
    if key in key_list.keys():
        url = key_list[key]
    else:
        url = key

    if url not in _METADATA.keys():

        headers = {"Metadata-Flavor": "Google"}

        req = urllib.request.Request(
            "http://metadata.google.internal" + url, headers=headers
        )

        try:
            with urllib.request.urlopen(req) as res:
                _METADATA[key] = res.read().decode()
        except urllib.error.URLError:
            return None

    return _METADATA[key]


K_SERVICE = os.environ.get('K_SERVICE')
PROJECT_ID = _get_metadata('project_id')
