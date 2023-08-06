import json
import os
import sys
from typing import Protocol, runtime_checkable, Set, Optional, List
from colorama import Fore, Style, init
from core.services.runner_input_service import RunnerInputService
from core.bp_metadata_utils.customer_blueprint_repo import CustomerBlueprintRepo
from core.bp_metadata_utils.python_source_file_utils import get_blueprint_classes
from core.types import Blueprint, Finding
import core.utilities as Utilities

@runtime_checkable
class SupportsValidation(Protocol):
    def validate(self) -> Set[Finding]:
        """
        Entry point into component's validation logic
        """


class Runner:

    @staticmethod
    def run(validation_target: SupportsValidation):
        return validation_target.validate()


def main(argv):
    print(f"{Fore.LIGHTRED_EX}************************************************************************")
    print(f"    Running oak9's Python Framework                        ")
    print(f"************************************************************************{Style.RESET_ALL}")


    try:
        init(convert=True) # Ensure that colorama works on Windows

        args_path = None
        
        if len(argv) > 0:
            args_path = argv[0]
        
        args_obj = None
        try:
            args_file = open(args_path)
            args_obj = json.load(args_file)
            args_file.close()
            Utilities.verify_config_arguments(args_obj)
        except:
            # TODO: CLOUD-9058 save back a JSON instead with understandable errors for CLI to deal with
            print("Runner arguments not found or could not be understood.")
            return
        
        path = args_obj["blueprint_package_path"]
        command = args_obj["command"] if "command" in args_obj else "test"
        
        runner = Runner()
        blueprint_dir = ""

        if path:
            blueprint_dir = path
        else:
            # TODO: We could default to /blueprints here
            raise Exception("Blueprints directory was not provided.")

        findings = set()

        blueprint_repo = CustomerBlueprintRepo(blueprint_dir)

        # TODO: make this conditional on a CLI command
        blueprint_repo.print_blueprint_summary()

        # Verify config/credentials for runner endpoint

        # Fetch runner input data
        runner_inputs = RunnerInputService.fetch_runner_input(args_obj)

        # Runner input available?

        # TODO: initialize blueprint properly
        '''
        Run all blueprints
        '''
        print(f"{Fore.LIGHTBLACK_EX}************************************************************************\n"
              f"    {Fore.BLUE}Running Blueprints{Style.RESET_ALL}\n"
              f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")

        # get all blueprint classes
        # TODO: filter out import of base Blueprint class
        blueprint_classes = []
        for path in blueprint_repo.blueprint_file_paths:
            blueprint_classes.extend(get_blueprint_classes(path))

        # Run each blueprint
        for blueprint in blueprint_classes:
            for runner_input in runner_inputs:
                customer_blueprint = blueprint[1](graph=runner_input.graph)
                # TODO: check usage guidelines to see if findings should be reported
                bp_findings = runner.run(customer_blueprint)
                print(f"[✓] Successfully ran checks in {blueprint[0]}")
                if bp_findings:
                    for finding in bp_findings:
                        finding.req_id = runner_input.meta_info.resource_id
                        finding.req_name = runner_input.meta_info.resource_name
                    findings.update(bp_findings)

        # TODO: send gaps to validation broker for the apply command
        print(f"\n{Fore.LIGHTBLACK_EX}************************************************************************\n"
              f"    {Fore.BLUE}Found {Style.BRIGHT}{len(findings)}{Style.NORMAL} Findings{Style.RESET_ALL}\n"
              f"{Fore.LIGHTBLACK_EX}************************************************************************{Style.RESET_ALL}")

        if findings:
            # if command == "test":
            #     RunnerInputService.apply_findings(args_obj, findings)
            for finding in findings:
                print(finding)
        sys.exit(0)

    except Exception as e:
        print("Raised Exception: " + str(e))
        sys.exit(1)


if __package__ == "":
    # Resulting path is the name of the wheel itself
    path = os.path.dirname(__file__)
    sys.path.insert(0, path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
