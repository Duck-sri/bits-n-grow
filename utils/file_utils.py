import yaml

def load_config(file:str) -> dict:
  with open(file,'r') as config_file:
    config = yaml.load(config_file,Loader=yaml.Loader)
  
  return config