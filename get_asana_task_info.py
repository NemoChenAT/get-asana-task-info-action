# Copyright (c) 2021 NemoChenTW
#
# This file is modified from asana-cli project attributed to Mr. Atul Shanker Johri
# and originally released under MIT license on https://github.com/AlJohri/asana-cli.
#

import sys
import requests


class AsanaAPIRequest():

    def __init__(self, access_token):
        self.__access_token = access_token
        self.s = requests.Session()
        self.s.headers = {
            "Authorization": f"Bearer {self.__access_token}", 'Accept': 'application/json'}

    def get_task_info(self, taskId):
        task = self.get_task(taskId)
        task_info = {'name': task['name'],
                     'link': task['permalink_url']}
        return task_info

    def get_task_title(self, taskId):
        info = self.get_task_info(taskId)
        return info['name']

    def get_task(self, taskId):
        task = self.get_json(f'https://app.asana.com/api/1.0/tasks/{taskId}')
        return task

    def get_json(self, url):
        response_json = self.get(url)
        return response_json['data']

    def get(self, url):
        response = self.s.get(url)
        response_json = self.response_to_json(response)
        return response_json

    def response_to_json(self, response):
        if response.status_code != 200:
            error = self.parse_asana_error_response(response)
            print(error, file=sys.stderr)
            sys.exit(1)
        else:
            data = response.json()
            return data

    def parse_asana_error_response(self, response):
        try:
            data = response.json()
            error = str(data)
            if data.get('errors') and len(data['errors']) == 1:
                try:
                    message = data['errors'][0]['message']
                    help_text = data['errors'][0]['help']
                    error = f"{message}. {help_text}"
                except (IndexError, KeyError,) as e:
                    print(e)
                    pass
        except ValueError:
            error = response.text
        return error


def get_asana_task_title(task_url, access_token):
    task_id = getAsanaTaskId(task_url)
    asana_api_request = AsanaAPIRequest(access_token=access_token)
    task_title = asana_api_request.get_task_title(task_id)
    return task_title


def getAsanaTaskId(task_url):
    return task_url.rsplit('/', 1).pop()


def show_github_issue(asana_task_info):
    print(asana_task_info['name'])


def main(args):
    """ get_asana_task_info.py [task_url] [access_token]
    """
    print(get_asana_task_title(args[1], args[2]))


if __name__ == '__main__':
    main(sys.argv)
