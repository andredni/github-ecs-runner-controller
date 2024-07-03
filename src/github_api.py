import requests
import logging
from config import GITHUB_TOKEN, ORG_NAME

def get_org_runners():
    url = f'https://api.github.com/orgs/{ORG_NAME}/actions/runners'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
 
    runners = []
    runners_info = {}
    for runner in response.json()['runners']: 
        runners.append({"id": runner['id'], "name": runner['name'], "status": runner['status']})

        if 'total' not in runners_info:
            runners_info['total'] = response.json()['total_count']

        if runner['status'] not in runners_info:
            runners_info[runner['status']] = 0

        runners_info[runner['status']] += 1

    return runners_info, runners

def register_new_runner():
    url = f'https://api.github.com/orgs/{ORG_NAME}/actions/runners/registration-token'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.post(url, headers=headers)
    response.raise_for_status()

    logging.debug(response.json())
    return response.json()['token']


def delete_org_runner(runner_id):
    url = f'https://api.github.com/orgs/{ORG_NAME}/actions/runners/{runner_id}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.delete(url, headers=headers)
    response.raise_for_status()

    if response.status_code == 204:
        logging.info(f"Deleting the Runner with id {runner_id} was successful.")
        return True
    else:
        logging.error(f"Deleting the Runner with id {runner_id} was not successful.")
        return False
