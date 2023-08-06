"""
Python interface to SAP HDLFS.

Status: Work in progress, unsupported

by Thorsten Hapke, thorsten.hapke@sap.com
"""

import json
import re
import logging
from pathlib import PurePath, Path
import requests_pkcs12
import requests

logging.basicConfig(level=logging.INFO)


def get_path_content(response: dict) -> list:
    """
    Extracts the path items from response of LISTSTATUS API
    :param response: Response from LISTSTATUS
    :return: List of path items (folders and files)
    """
    return [f['pathSuffix'] for f in response['FileStatuses']['FileStatus']]


def get_recursive_path_content(response: dict) -> list:
    """
    Extracts the path items from response of LISTSTATUS_RECURSIVE API
    :param response: Response from LISTSTATUS_RECURSIVE
    :return: List of path items (folders and files)
    """
    page_id = response['DirectoryListing']['pageId']
    logging.info(f"Page ID: {page_id}")
    f_list = response['DirectoryListing']['partialListing']['FileStatuses']['FileStatus']
    return [f['pathSuffix'] for f in f_list]


def hdlfs_api(method: str, operation: str) -> dict:
    """
    DECORATOR for all API-calls
    :param method: HTTP-method [get, put, ..]
    :param operation: RESTAPI name
    :return: response of Rest API
    """
    def inner_hdlfs_api(func):
        def call_api(endpoint, certificate, password, verify=True, **kwargs):
            container = re.match(r".+\/\/([^.]+)", endpoint).group(1)
            headers = {'x-sap-filecontainer': container}
            params = {'op': operation}
            endpoint = endpoint.replace('hdlfs://', 'https://') + '/webhdfs/v1/'
            updated = func(endpoint, certificate, password, **kwargs)
            if 'path' in updated and updated['path'][0] =='/':
                updated['path'] = updated['path'][1:]
            endpoint = endpoint + str(updated.pop('path', ''))
            headers.update(updated.pop('headers', dict()))
            params.update(updated.pop('params', dict()))
            data = updated.pop('data', None)
            suffix = PurePath(certificate).suffix
            if suffix in ['.crt', '.pem']:
                r = requests.request(method, endpoint, cert=(certificate, password), headers=headers, params=params,
                                     data=data, verify=verify)
            elif suffix in ['.pkcs12', '.p12', '.pfx']:
                r = requests_pkcs12.request(method, endpoint, pkcs12_filename=certificate, pkcs12_password=password,
                                            headers=headers, params=params, data=data, verify=verify)

            if r.status_code not in [200, 201]:
                raise ValueError(f"Unsuccessful API-call - Status code: {r.status_code} - {r.text}")
            return json.loads(r.text)

        return call_api
    return inner_hdlfs_api


@hdlfs_api(method='put', operation='CREATE')
def upload(endpoint: str, certificate: str, password: str, destination='', data="", noredirect=False, headers={}, verify=True) \
        -> dict:
    """
    Upload file to HDFS using CREATE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param destination: destination path of file
    :param data: file content
    :param noredirect: API parameter
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'path': destination,
            'data': data,
            'params': {'noredirect': noredirect},
            'headers': {'Content-Type': 'application/octet-stream'}}


@hdlfs_api(method='put', operation='RENAME')
def rename(endpoint: str, certificate: str, password: str, path='', destination='', headers={}, verify=True) -> dict:
    """
    Rename/Move file in HDFS with RENAME-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param destination: destination of file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    destination = '/' + destination if destination[0] != '/' else destination
    return {'path': path,
            'params': {'destination': destination},
            'headers': headers}


@hdlfs_api(method='put', operation='COPY')
def copy(endpoint, certificate, password, path='', destination='', a_sync=False, headers={}, verify=True):
    """
    Copy file in HDFS with Copy-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param destination: destination of file
    :param a_sync: API parameter
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    destination = '/' + destination if destination[0] != '/' else destination
    return {'path': path,
            'params': {'destination': destination, 'async': a_sync},
            'headers': headers}


@hdlfs_api(method='del', operation='DELETE')
def delete(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True) -> dict:
    """
    Delete file in HDFS with DELETE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'headers': headers}


@hdlfs_api(method='get', operation='GETFILESTATUS')
def file_status(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True):
    """
    Get file status
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'headers': headers}


@hdlfs_api(method='get', operation='LISTSTATUS')
def list_path(endpoint: str, certificate: str, password: str, path='', headers={}, verify=True):
    """
    Get all items of folder by using LISTSTATUS-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'headers': headers}


@hdlfs_api(method='get', operation='LISTSTATUS_RECURSIVE')
def list_path_recursive(endpoint: str, certificate: str, password: str, path='', start_after=None, headers={},
                        verify=True) -> dict:
    """
    Get all items of folder and sub-folders by using LISTSTATUS_RECURSIVE-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param path: path to source file
    :param start_after: API parameter for paging result
    :param headers: Passing optional parameter to API
    :param verify: Enables/ disables server verification
    :return: response
    """
    headers.update({'Content-Type': 'application/json'})
    return {'path': path,
            'params': {'startAfter': start_after},
            'headers': headers}


@hdlfs_api(method='get', operation='WHOAMI')
def whoami(endpoint: str, certificate: str, password: str, verify=True):
    """
    Get user information by WHOAMI-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'headers': {'Content-Type': 'application/json'}}


# UNTESTED
@hdlfs_api(method='get', operation='GETOPERATIONSTATUS')
def get_operations_status(endpoint: str, certificate: str, password: str, token='',verify=True) -> dict:
    """
    Get operation status by GETOPERATIONSTATUS-API
    :param endpoint: endpoint url
    :param certificate: filename with path to certificate or pkcs12-keystore
    :param password: filename with path to key or passphrase for keystore
    :param verify: Enables/ disables server verification
    :return: response
    """
    return {'params': {'token': token},
            'headers': {'Content-Type': 'application/json'}}

# UNTESTED
@hdlfs_api(method='get', operation='GETRESTORESNAPSHOTSTATUS')
def get_operations_status(endpoint, certificate, password, token='', verify=True):
    return {'params': {'token': token},
            'headers': {'Content-Type': 'application/json'}}


def main():
    pass


if __name__ == '__main__':
    main()