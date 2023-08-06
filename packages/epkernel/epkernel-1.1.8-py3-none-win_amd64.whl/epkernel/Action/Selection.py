import os, sys, json
import math
from epkernel import BASE
from epkernel.Action import Information


def set_attribute_filter(logic:int, attribute_list:list):
    """
    #设置属性筛选
    :param     logic:0 ：全部满足  1:有其一
    :param     attribute_list:要设置的属性列表
    :returns   :
    :raise    error:
    """
    try:
        BASE.filter_set_attribute(logic, attribute_list)
    except Exception as e:
        print(e)
    return 0

def select_features_by_filter(job:str, step:str, layers:list):
    """
    #根据筛选条件选择
    :param     job:
    :param     step:
    :param     layers:layer列表
    :returns   :
    :raises    error:
    """
    try:
        BASE.select_features_by_filter(job, step, layers)
    except Exception as e:
        print(e)
    return 0

def reset_select_filter():
    try:
        BASE.set_select_param(0x7F, False, [], -1, -1, [], 0, True)
    except Exception as e:
        print(e)
    return 0

def clear_select(job:str, step:str, layer:str = ''):
    try:
        layers = Information.get_layers(job)
        if layer == '':
            for layer in layers:
                BASE.clear_selected_features(job, step, layer)
        else:
            BASE.clear_selected_features(job, step, layer)
    except Exception as e:
        print(e)
    return 0
    
def set_featuretype_filter(positive:bool,negative:bool,text:bool,surface:bool,arc:bool,line:bool,pad:bool):
    '''
    需要筛选的feature类型,以二进制计算,计算顺序依次为:正极性,负极性,text,surface,arc,line,pad
    七个参数类型是bool,参数是True:参与计算求和,否则不参与计算求和。
    '''
    try:
        featuretype_sum=0
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        #print(data)  
        flag = select_param['attributes_flag']
        value = select_param['attributes_value']   
        symbols = select_param['symbols']
        pr_value = select_param['profile_value']
        sele = select_param['use_selection']
        dcode = select_param['dcode']
        has_symbol = select_param['has_symbols']
        featuretype_list= [positive,negative,text,surface,arc,line,pad]
        for index in range(len(featuretype_list)):
            if featuretype_list[index]==True:
                featuretype_list[index]=len(featuretype_list)-index-1
            else:
                featuretype_list[index]=None
        for type_ in featuretype_list:
            if type_!=None:
                featuretype_sum += math.pow(2,type_)
        BASE.set_select_param(featuretype_sum, has_symbol, symbols,dcode, flag,value, pr_value,sele)
    except Exception as e:
        print(e)
        return None

def set_include_symbol_filter(symbol_list:list):
    """
    #设置include symbol筛选
    :param     symbol_list:设置筛选include_symbol的list
    :returns   :
    :raises    error:
    """
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretype = select_param['featuretypes']
        flag = select_param['attributes_flag']
        value = select_param['attributes_value']   
        pr_value = select_param['profile_value']
        sele = select_param['use_selection']
        dcode = select_param['dcode']
        BASE.set_select_param(featuretype, True, symbol_list,dcode, flag,value, pr_value,sele)
    except Exception as e:
        print(e)
    return 0

def reverse_select(job:str, step:str, layer:str):
    """
    #反选
    :param     job:
    :param     step:
    :param     layer:
    :returns   :
    :raises    error:
    """
    try:
        BASE.counter_election(job, step, layer)
    except Exception as e:
        print(e)
    return 0

def set_selection(is_standard:bool, is_clear:bool, all_layers:bool, is_select:bool, inside:bool, exclude:bool):
    try:
        BASE.set_selection(is_standard, is_clear, all_layers, is_select, inside, exclude)
    except Exception as e:
        print(e)
    return 0

#重置设置模式
def reset_selection():
    try:
        BASE.set_selection(True, True, True, True, True, True)
    except Exception as e:
        print(e)
    return 0
#取消选中
def unselect_features(job:str, step:str, layer:str):
    try:
        BASE.unselect_features(job, step, layer)
    except Exception as e:
        print(e)
    return 0

def select_feature_by_polygon(job:str, step:str, layer:str, selectpolygon:list):
    try:
        BASE.select_feature(job, step, layer, selectpolygon, {}, 1, True) # 1：框选 
    except Exception as e:
        print(e)
    return 0
    

def select_feature_by_point(job:str, step:str, layer:str, location_x:int,location_y:int):
    try:
        selectpolygon=[]
        min = 1 #nm
        selectpolygon.append([location_x-min,location_y-min])
        selectpolygon.append([location_x+min,location_y-min])
        selectpolygon.append([location_x+min,location_y+min])
        selectpolygon.append([location_x-min,location_y+min])
        selectpolygon.append([location_x-min,location_y-min])
        BASE.select_feature(job, step, layer, selectpolygon, {}, 0, True) # 0：点选  
    except Exception as e:
        print(e)
    return 0
    
#0:all 1:in 2:out
def set_inprofile_filter(mode:int):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        BASE.set_select_param(select_param['featuretypes'], select_param['has_symbols'], select_param['symbols'], 
                                select_param['dcode'], select_param['attributes_flag'],
                                select_param['attributes_value'], mode,
                                select_param['use_selection'])
    except Exception as e:
        print(e)
    return 0

def select_feature_by_id(job:str, step:str, layer:str, ids:list):
    try:
        BASE.select_feature_by_id(job, step, layer, ids)
    except Exception as e:
        print(e)
    return 

def unselect_features_by_filter(job:str, step:str, layers:list):
    try:
        BASE.unselect_features_by_filter(job, step, layers)
    except Exception as e:
        print(e)
    return 

def filter_by_mode(job:str, step:str, layer:str, reference_layers:list, mode:int, positive:bool,
                   negative:bool,text:bool,surface:bool,arc:bool,line:bool,pad:bool, 
                   symbolflag:int , symbolnames:list, attrflag:int = -1,attrlogic:int = 0, 
                   attributes:list = [],use_symbol_range:bool=False,symboltype:str='',
                   symbolrange:list=[],use_attr_range:bool=False,attrtype:str='',
                   attrrange:list=[]):
    try:
        feature_type_ref=0
        featuretype_list= [positive,negative,text,surface,arc,line,pad]
        for index in range(len(featuretype_list)):
            if featuretype_list[index]==True:
                featuretype_list[index]=len(featuretype_list)-index-1
            else:
                featuretype_list[index]=None
        for type_ in featuretype_list:
            if type_!=None:
                feature_type_ref += math.pow(2,type_)

        dict_new = dict(symbolrange)
        keys = list(dict_new.keys())
        key_list = [str(i) for i in keys]
        value_list = list(dict_new.values())
        ranges = dict(zip(key_list,value_list))
        new_list = []
        for key,value in ranges.items():
            dict_new = {}
            dict_new[key] = value
            new_list.append(dict_new)
        symbol_range = {}
        symbol_range['range'] = new_list
        symbol_range['symbol_type'] = symboltype  

        dict_new1 = dict(attrrange)
        keys1 = list(dict_new1.keys())
        key_list1 = [str(i) for i in keys1]
        value_list1 = list(dict_new1.values())
        ranges1 = dict(zip(key_list1,value_list1))
        new_list1 = []
        for key,value in ranges1.items():
            dict_new1 = {}
            dict_new1[key] = value
            new_list1.append(dict_new1)
        attr_range = {}
        attr_range['attr_value_range'] = new_list1
        attr_range['attr_name'] = attrtype
        BASE.filter_by_mode(job, step, layer, reference_layers, mode, feature_type_ref, symbolflag , symbolnames, 
                    attrflag ,attrlogic, attributes,use_symbol_range,symbol_range,
                    use_attr_range,attr_range)
    except Exception as e:
        print(e)
        return None

def set_symbol_filter(has_symbols:bool, symbol_list:list):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretype = select_param['featuretypes']
        flag = select_param['attributes_flag']
        value = select_param['attributes_value']   
        pr_value = select_param['profile_value']
        sele = select_param['use_selection']
        dcode = select_param['dcode']
        BASE.set_select_param(featuretype, has_symbols, symbol_list, dcode, flag, value, pr_value, sele)
    except Exception as e:
        print(e)
    return 0

def set_symbol_range_filter(type:str, range:list):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretypes = select_param['featuretypes']
        attributes_flag = select_param['attributes_flag']
        attributes_value = select_param['attributes_value']   
        profile_value = select_param['profile_value']
        use_selection = select_param['use_selection']
        dcode = select_param['dcode']
        has_symbols=select_param['has_symbols']
        symbols=select_param['symbols']
        use_attr_range = select_param['use_attr_range']
        attr_range = select_param['attr_range']
        exclude_attributes_value = select_param['exclude_attributes_value']
        exclude_attr_range = select_param['exclude_attr_range']
        # 合并参数
        dict_new = dict(range)
        keys = list(dict_new.keys())
        key_list = [str(i) for i in keys]
        value_list = list(dict_new.values())
        ranges = dict(zip(key_list,value_list))
        new_list = []
        for k,v in ranges.items():
            dict_new = {}
            dict_new[k] = v
            new_list.append(dict_new)
        symbol_range = {}
        symbol_range['range'] = new_list
        symbol_range['symbol_type'] = type
        BASE.set_select_param(featuretypes,has_symbols,symbols,dcode,
                              attributes_flag,attributes_value,profile_value,use_selection,
                              True,symbol_range,use_attr_range,attr_range,exclude_attributes_value,exclude_attr_range)
    except Exception as e:
        print(e)
    return None

def set_attr_range_filter(logic:int,attr_range:list):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretypes = select_param['featuretypes']
        attributes_value = select_param['attributes_value']   
        profile_value = select_param['profile_value']
        use_selection = select_param['use_selection']
        dcode = select_param['dcode']
        has_symbols=select_param['has_symbols']
        symbols=select_param['symbols']
        use_symbol_range = select_param['use_symbol_range']
        symbol_range = select_param['symbol_range']
        exclude_attributes_value = select_param['exclude_attributes_value']
        exclude_attr_range = select_param['exclude_attr_range']
        BASE.set_select_param(featuretypes,has_symbols,symbols,dcode,
                              logic,attributes_value,profile_value,use_selection,
                              use_symbol_range,symbol_range,True,attr_range,exclude_attributes_value,exclude_attr_range)
    except Exception as e:
        print(e)
    return None

def set_exclude_attr_filter(attr:list):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretypes = select_param['featuretypes']
        attributes_value = select_param['attributes_value']   
        profile_value = select_param['profile_value']
        use_selection = select_param['use_selection']
        dcode = select_param['dcode']
        has_symbols=select_param['has_symbols']
        symbols=select_param['symbols']
        symbol_range = select_param['symbol_range']
        attr_range = select_param['attr_range']
        exclude_attr_range = select_param['exclude_attr_range']
        use_symbol_range = select_param['use_symbol_range']
        BASE.set_select_param(featuretypes,has_symbols,symbols,dcode,0,
                            attributes_value,profile_value,use_selection,use_symbol_range,
                            symbol_range,True,attr_range,attr,exclude_attr_range)
    except Exception as e:
        print(e)

def set_exclude_attr_range_filter(attr_range:list):
    try:
        ret = BASE.get_select_param()
        data = json.loads(ret)
        select_param = data['paras']['param']
        featuretypes = select_param['featuretypes']
        attributes_value = select_param['attributes_value']   
        profile_value = select_param['profile_value']
        use_selection = select_param['use_selection']
        dcode = select_param['dcode']
        has_symbols=select_param['has_symbols']
        symbols=select_param['symbols']
        symbol_range = select_param['symbol_range']
        include_attr_range = select_param['attr_range']
        exclude_attributes_value = select_param['exclude_attributes_value']
        use_symbol_range = select_param['use_symbol_range']
        BASE.set_select_param(featuretypes, has_symbols, symbols,  dcode, 0, attributes_value, 
                        profile_value, use_selection,use_symbol_range,symbol_range,True,include_attr_range,
                        exclude_attributes_value,attr_range)
    except Exception as e:
        print(e)

def select_features_by_net(job:str,step:str,layer:str,use_select_info:bool,location_x:int,location_y:int,tolerance:int):
    try:
        selectpolygon=[]
        selectpolygon.append({'ix':location_x-tolerance,'iy':location_y-tolerance})
        selectpolygon.append({'ix':location_x+tolerance,'iy':location_y-tolerance})
        selectpolygon.append({'ix':location_x+tolerance,'iy':location_y+tolerance})
        selectpolygon.append({'ix':location_x-tolerance,'iy':location_y+tolerance})
        selectpolygon.append({'ix':location_x-tolerance,'iy':location_y-tolerance})
        BASE.select_features_by_net(job,step,layer,[],use_select_info,selectpolygon)
    except Exception as e:
        print(e)


    
    
    
    