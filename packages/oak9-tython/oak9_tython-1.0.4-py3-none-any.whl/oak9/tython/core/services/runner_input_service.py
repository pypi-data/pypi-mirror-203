import json
import requests
import core.sdk.helper as Helper
from models.shared.shared_pb2 import RunnerInput
from core.types import Finding

class RunnerInputService:
    '''
    Provides access to the runner input data
    '''

    def fetch_runner_input(argsObj):
        # TODO: WARNING - MUST REPLACE WITH PROD URL ONLY BEFORE RELEASE!!!!
        endpoint = "https://devapi.oak9.cloud/console/"

        # TODO: Safety check the values in the argsObj. No reason to call the API
        # if any of these values are missing/invalid
        if argsObj["data_endpoint"] != None and argsObj["data_endpoint"] != "":
            endpoint = argsObj['data_endpoint']

        url = f"{endpoint}{argsObj['org_id']}/sac/{argsObj['project_id']}/runnerinput/"
        response = requests.get(url, auth=(argsObj['org_id'], argsObj['api_key']))

        if response.status_code == 401:
            print(f"WARNING: Unable to fetch {argsObj['project_id']} data, please verify your credentials.")
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


    def apply_findings(findings: list[Finding]):
        '''
        Apply a findings list to the oak9 project
        '''
        violations = []

        for finding in findings:
            violations.append(finding.to_violation().__json__())

        payload = {
            "runtime": "Python",
            "author": "",
            "designGaps": [
                {
                    "capabilityId": "",
                    "capabilityName": "",
                    "source": "",
                    "resourceName": "",
                    "resourceId": "",
                    "resourceType": "",
                    "resourceGap": "",
                    "resourceImpact": "",
                    "violations": violations,
                    "oak9Guidance": "",
                    "mappedIndustryFrameworks": []
                }
            ]
        }

        json_config = None
        config_path = "D:\\git\\oak9.sac.fw\\cli\\config.json" # fetch from env vars?
        with open(config_path, 'r') as file:
            json_config = json.load(file)

        url = f"{json_config['dataEndpoint']}{json_config['orgId']}/sac/{json_config['projectId']}/validation/apply/"
        headers = {"Authorization": f"Bearer {json_config['apiKey']}"}
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            print(f"WARNING: Unable to apply {json_config['projectId']} findings, please verify your credentials.")
            return None
        
        return response.text
    

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
