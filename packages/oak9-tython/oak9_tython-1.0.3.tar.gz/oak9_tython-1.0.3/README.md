# oak9.sac.fw



This repository stores the runner that will be available for our customers to test and execute custom blueprints locally in the BYOL approach.

### Note:
As of Dec 25th, the code artifact package needs to be updated.  The local package version is 0.0.11b.

## Requirements

Python 3.10+

## Development Process

1. Install the appropriate python packages locally

```sh
pip install -r requirements.txt
```

2. Call the runner with arguments

```sh
python runner.py example_blueprints_directory
```

### Note:
In case that the developer wants to test the package before uploading to code articact, it is possible to install it locally using pip with this command:

```sh
pip install /d/git/oak9.sac.fw/py/package
```

### Building
1. Make sure you have installed the appropriate python packages locally (requirements.txt)
2. To avoid publishing the generated package, comment line 37 of the `build_py_runner.sh` script.
3. On the root of the repository execute:

```sh
./python/build_py_runner.sh
```

4. At this point you will have built the actual python package that we would normally upload. Go into the `packages` directory and find the `.tar.gz` file named `oak9.sac.framework-{version}` in the `dist` folder
