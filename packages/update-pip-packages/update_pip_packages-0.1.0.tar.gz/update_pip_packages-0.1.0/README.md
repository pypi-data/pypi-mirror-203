# Update Pip and App Packages
## v0.1.0

This Python script provides an efficient way to update Pip and app packages on various Linux distributions. The script supports Ubuntu, Debian, Fedora, CentOS, Red Hat, Arch, Manjaro, OpenSUSE, and SUSE distributions. It updates packages using the appropriate package manager for each distribution.

## Features

- Update Pip and its packages to the latest versions.
- Update app packages for supported Linux distributions using the corresponding package manager.
- Command-line interface with options for updating Pip packages, app packages, or both.

## Usage

To use the script, run the following command with the desired options:

```
python update_packages.py [--pip] [--app]
```
- -h, --help: Show this help message and exit
- --pip: Update Pip packages.
- --app: Update app packages.
- If no options are provided, the script will display help information.

## Tests
The tests cover various aspects of the script, including the following:

- Getting the Linux distribution.
- Updating Pip packages.
- Updating app packages for each supported Linux distribution.
- Handling unsupported Linux distributions.



## Dependencies
- [Python](https://www.python.org/) 3.6 or later
- [Poetry](https://python-poetry.org/)
- [pytest](https://pytest.org/)
- [distro](https://pypi.org/project/distro/)

## Installation
```
pip3 install update-pip-packages
```
or
```
python3 -m pip install update-pip-packages
```

## GitHub Repository
For more information, source code, and installation instructions, please visit the GitHub repository: [GitHub: update_packages](https://github.com/OleksandrMakarov/Scripts/tree/main/update_project)