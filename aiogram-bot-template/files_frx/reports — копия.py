# -*- coding: utf-8 -*-

from requests import get, post, delete, put
import urllib3

TOKEN = 'yuptozbh36s5uj1qkojexo5w91snjjmcw3sya8s84zy8t8yjow9y'
PROS = '6377865f5f620ebfce9a07ce'
USER_NAME = 'apikey'



class Base:
    def __init__(self, username, token, sub_id):
        self._username = username
        self._token = token
        self._sub_id = sub_id

    def _config(self):
        auth = urllib3.util.make_headers(
            basic_auth=self._username + ':' + self._token
        ).get('authorization')

        headers = {
            'accept': 'application/json',
            'Authorization': auth
        }
        return headers, f'?subscriptionId={self._sub_id}'


class Reports(Base):
    def __init__(self, username, token, sub_id):
        super().__init__(username, token, sub_id)
        self.headers, self.sub_id = self._config()
        self.domen = 'https://fastreport.cloud'

    def get_root_dir(self):
        response = get(f'{self.domen}/api/rp/v1/Reports/Root{self.sub_id}', headers=self.headers)
        return response.json()['id']

    def delite_file(self, id_file):
        response = delete(f'{self.domen}/api/rp/v1/Reports/File/{id_file}{self.sub_id}', headers=self.headers)
        return response.status_code

    def delite_folder(self, id_folder):
        response = delete(f'{self.domen}/api/rp/v1/Reports/Folder/{id_folder}{self.sub_id}', headers=self.headers)
        return response.status_code
    def get_all_file_and_folder(self, id_file):
        response = get(f'{self.domen}/api/rp/v1/Reports/Folder/{id_file}/ListFolderAndFiles{self.sub_id}',
                       headers=self.headers)
        return response.json()['files']

    def upload_file(self, id_folder, path_file, name_file):
        import base64
        with open(path_file, 'r') as xml:
            a = base64.b64encode(xml.read().encode('utf-8'))
            print(a)
        self.headers['name'] = name_file
        self.headers['content'] = a
        print(self.headers)
        response = get(f'{self.domen}/api/rp/v1/Reports/Folder/{id_folder}/File{self.sub_id}', headers=self.headers)
        return response.status_code

    def get_file(self, id_file):
        response = get(f'{self.domen}/api/rp/v1/Reports/File/{id_file}{self.sub_id}', headers=self.headers)
        return response.json()

    def download_file(self, id_file):
        name = self.get_file(id_file)["name"]
        response = get(f'{self.domen}/download/r/{id_file}{self.sub_id}', headers=self.headers)
        with open(f'{name}', 'wb') as f:
            f.write(response.content)
        return name

    def export_file(self, id_file: str, format: str, export_name: str = None):
        json = {
            "fileName": export_name,
            "pagesCount": 2147483647,
            "format": format
        }
        # file = self._get_file_rep(file_name, folder_name=folder_name)
        # print(file_id)
        file = post(f'{self.domen}/api/rp/v1/Reports/File/{id_file}/Export', headers=self.headers,
                             json=json)
        return self.domen + '/download/e/' + file.json()['id']

rep = Reports(USER_NAME, TOKEN, PROS)
id_root = rep.get_root_dir()
print(id_root)
print(rep.export_file('63788c605f620ebfce9a1c37', format='svg'))
# print(rep.download_file('637892c75f620ebfce9a1d42'))
# print(rep.upload_file(id_root, 'не удалять.fpx', 'my_file_oaoaoaoaoa.fpx'))
# print(rep.delite_file('637811b05f620ebfce9a10c8'))