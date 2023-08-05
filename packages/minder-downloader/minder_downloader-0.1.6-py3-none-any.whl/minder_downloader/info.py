import requests
import pandas as pd
from .utils import BearerAuth, load_yaml
from .config import check_config
import os 
from pathlib import Path



def setup() -> tuple:
    # Load credentials and server information from YAML file
    check_config()
    ROOT = os.environ.get('MINDER_DOWNLOADER_HOME', Path(__file__).parent)
    INFO_PATH = f'{ROOT}{os.sep}info.yaml'
    os.environ['MINDER_TOKEN'] = load_yaml(INFO_PATH)['token']
    server = load_yaml(INFO_PATH)['server'] + '/export'
    token = os.getenv('MINDER_TOKEN')
    return server,token


def _minder_datasets_info() -> pd.DataFrame:
    """
    Returns a Pandas DataFrame with information about Minder research portal datasets.
    Parameters:
    None

    Returns:
    A Pandas DataFrame with the following columns:
    - datasets: The name of the dataset.
    - type: The type of the dataset (e.g., clinical, survey).
    - description: A brief description of the dataset.
    - availableColumns: A list of available columns in the dataset.
    - domain: The domain the dataset belongs to.
    """
    server,token = setup()
    url = "https://research.minder.care/api/info/datasets"
    headers = {"accept": "application/json", "Authorization" : f"Bearer {token}"}

    request = requests.get(url, headers=headers)
    domains = request.json()['Categories'].keys()
    info = pd.concat([
        pd.DataFrame(request.json()['Categories'][domain])
        .T.assign(domain=domain)
        for domain in domains
    ])
    info.index = info.index.rename('datasets')
    info = info.reset_index()
    return info


def _minder_organizations_info() -> pd.DataFrame:
    """
    Returns a Pandas DataFrame with information about Minder research portal organizations.
    Parameters:
    None

    Returns:
    A Pandas DataFrame with the following columns:
    - organization: The name of the organization.
    - acronym: The organization's acronym.
    - description: A brief description of the organization.
    """    
    server,token = setup()
    url = "https://research.minder.care/api/info/organizations"
    headers = {"accept": "application/json", "Authorization" : f"Bearer {token}"}
    request = requests.get(url, headers=headers)
    info = pd.DataFrame(request.json()['organizations'])
    return info