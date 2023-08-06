from .utils import path_exists, write_yaml,load_yaml
from .update import get_token
from pathlib import Path
import os

CONFIG_CHECKED = False

def check_config():
    """Check if a configuration file exists, and create/update it with required information.

    This function checks if a YAML configuration file named 'info.yaml' exists in the same directory as this script. If the file doesn't exist, it creates it with default headers and server information, and sets the TOKEN value to None. If the file exists, it loads its contents, retrieves the TOKEN value, and updates it with a new token if the value is None. It then writes the updated information back to the file.

    Returns:
    None
    """

    global CONFIG_CHECKED
    if CONFIG_CHECKED:
        return os.environ['MINDER_DOWNLOADER_HOME']
    CONFIG_CHECKED = True

    root = check_root_folder()

    check_token_file(root) # check if token is set at the environment level

    return root
        


def check_root_folder():
    root = os.environ.get('MINDER_DOWNLOADER_HOME')
    if root is None:
        root = Path.home()

    minder_home = Path(f'{root}{os.sep}.minder')
    if not minder_home.exists():
        minder_home.mkdir(parents=True)
    os.environ['MINDER_DOWNLOADER_HOME'] = f'{minder_home}'
    return f'{minder_home}'


def check_token_file(root):
    token_path = os.environ.get('RESEARCH_PORTAL_TOKEN_PATH') 
    TOKEN = None 
    info_path = f'{root}{os.sep}info.yaml'
    tmp = {'headers':{ 'Accept': 'text/plain',
                    'Connection': 'keep-alive',
                    'Content-type': 'application/json'},  
            'server': 'https://research.minder.care/api'}
    if token_path is None:
        if path_exists(info_path):
            tmp = load_yaml(info_path)
        if 'token' in tmp.keys():    
            TOKEN = tmp['token']
        else:     
            TOKEN = get_token()
    elif Path(token_path).exists(): 
        with open(token_path, 'r') as file:
            TOKEN = file.read() 
    if not (TOKEN is None):
        tmp['token'] = TOKEN    
        os.environ['MINDER_TOKEN'] = TOKEN
        if not path_exists(info_path):   
            write_yaml(info_path,tmp)
    else:
        raise NameError("Token is missing or wasn't set")        