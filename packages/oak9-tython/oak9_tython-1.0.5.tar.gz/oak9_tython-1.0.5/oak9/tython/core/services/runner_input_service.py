import json
import requests
import core.sdk.helper as Helper
from models.shared.shared_pb2 import RunnerInput
from core.types import Finding

class RunnerInputService:
    '''
    Provides access to the runner input data
    '''

    def fetch_runner_input(args_obj):
        # TODO: WARNING - MUST REPLACE WITH PROD URL ONLY BEFORE RELEASE!!!!
        endpoint = "https://devapi.oak9.cloud/console/"

        if "data_endpoint" in args_obj and args_obj["data_endpoint"] != "":
            endpoint = args_obj['data_endpoint']

        url = f"{endpoint}{args_obj['org_id']}/sac/{args_obj['project_id']}/runnerinput/"
        response = requests.get(url, auth=(args_obj['org_id'], args_obj['api_key']))

        if response.status_code == 401:
            print(f"WARNING: Unable to fetch {args_obj['project_id']} data, please verify your credentials.")
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


    def apply_findings(args_obj, findings: list[Finding]):
        '''
        Apply a findings list to the oak9 project
        '''
        endpoint = "https://devapi.oak9.cloud/console/"

        if "data_endpoint" in args_obj and args_obj["data_endpoint"] != "":
            endpoint = args_obj['data_endpoint']

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

        url = f"{endpoint}{args_obj['org_id']}/sac/{args_obj['project_id']}/validation/apply/"
        response = requests.post(url, auth=(args_obj['org_id'], args_obj['api_key']), json=payload)

        if response.status_code != 200:
            print(f"WARNING: Unable to apply {args_obj['api_key']} findings, please verify your credentials.")
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
