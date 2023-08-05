import json
import requests
import core.sdk.helper as Helper
from models.shared.shared_pb2 import RunnerInput

class RunnerInputService:
    '''
    Provides access to the runner input data
    '''

    def fetch_runner_input():
        
        json_config = None
        config_path = "D:\\git\\oak9.sac.fw\\cli\\config.json" # fetch from env vars?
        with open(config_path, 'r') as file:
            json_config = json.load(file)

        url = f"{json_config['dataEndpoint']}{json_config['orgId']}/sac/{json_config['projectId']}/runnerinput/"
        headers = {"Authorization": f"Bearer {json_config['apiKey']}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            print(f"WARNING: Unable to fetch {json_config['projectId']} data, please verify your credentials.")
            return []

        runner_inputs = []

        raw_snake_case_input = Helper.snake_case_json(response.json())

        for raw_item in raw_snake_case_input:
            item = raw_item['item1']
            for root_node in item['graph']['root_nodes']:
                root_node['node']['resource']['data']['value'] = bytes(root_node['node']['resource']['data']['value'])
            Helper.remove_attributes(item, "has_")
            runner_inputs.append(RunnerInput(**item))

        return runner_inputs


    def fetch_runner_input_local(request_id: str):

        """
        DEPRECATED: This function is obsolete and should not be used.
        Please use the fetch_runner_input() instead.
        """

        if not request_id:
            return None

        runner_input: RunnerInput = None

        with open('D:\\poc\\runner_package_test\\runner_input_tython_complete.json', 'r') as file:
            raw_input = json.load(file)
            raw_snake_case_input = Helper.snake_case_json(raw_input)
            raw_item1 = raw_snake_case_input[0]['item1']
            for root_node in raw_item1['graph']['root_nodes']:
                root_node['node']['resource']['data']['value'] = bytes(root_node['node']['resource']['data']['value'])
            Helper.remove_attributes(raw_item1, "has_")
            runner_input = RunnerInput(**raw_item1)
        
        return runner_input
