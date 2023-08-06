import os, sys, json,requests,time
from epkernel import Input,epcam,BASE
from epkernel.Action import Information


def init(path:str): 
    epcam.init(path)
    BASE.set_config_path(path)
    v = epcam.getVersion()
    version = v['ep_version'] + v['sub_version']
    if not version == '1.1.3.19':
        print("Epkernel与bin包版本不匹配，请谨慎使用")

def set_sysattr_path(path:str):
    try:
        BASE.set_sysAttr_path(path)
    except Exception as e:
        print(e)
    return 

def set_userattr_path(path:str):
    try:
        BASE.set_userAttr_path(path)
    except Exception as e:
        print(e)
    return    
    
def read_auto_matrix_rule(path:str)->dict:
    try:
        ccc = BASE.read_auto_matrix_rule(path)
        return json.loads(ccc)
    except Exception as e:
        print(e)
        return None

def read_auto_matrix_template(path:str)->dict:
    try:
        ccc = BASE.read_auto_matrix_template(path)
        return json.loads(ccc)
    except Exception as e:
        print(e)
        return None

def add_new_match_rule(layer_infos:list, path:str)->dict:
    try:
        ruleName=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        ret = BASE.saveNewMatchRule(layer_infos,path,ruleName)
        ret = json.loads(ret)
        return ret
    except Exception as e:
        print(e)
    return {}





