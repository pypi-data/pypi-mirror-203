import os, sys, json
from epkernel import epcam, BASE
from epkernel.Action import Information,Selection

def save_eps(job:str, path:str)->bool:
    try:
        filename = os.path.basename(path)
        suffix = os.path.splitext(filename)[1]
        if suffix == '.eps':
            BASE.setJobParameter(job,job)
            BASE.save_eps(job,path)
            return True
        else:
            pass
    except Exception as e:
        print(e)
    return False


def save_gerber( job:str, step:str, layer:str, filename:str,  resize:int=0, angle:float=0, 
                scalingX:float=1, scalingY:float=1, mirror:bool=False, rotate:bool=False, 
                scale:bool=False, cw:bool=False,  mirrorpointX:int=0, mirrorpointY:int=0, 
                rotatepointX:int=0, rotatepointY:int=0, scalepointX:int=0, scalepointY:int=0, 
                mirrorX:bool = False, mirrorY:bool = False, numberFormatL:int=2, 
                numberFormatR:int=6, zeros:int=0, unit:int=0)->bool:
    try:
        _type = 0
        gdsdbu = 0.01
        profiletop = False
        cutprofile = True
        isReverse = False
        cut_polygon = []
        if scalingX == 0:
            scalingX == 1
        if scalingY == 0:
            scalingY == 1
        if mirrorX == True and mirrorY ==True:
            mirrordirection = 'XY'
        elif mirrorX==True and mirrorY ==False:
            mirrordirection = 'Y'
        elif mirrorX==False and mirrorY ==True:
            mirrordirection = 'X'
        else:
            mirrordirection = 'NO'
        _ret = BASE.layer_export(job, step, layer, _type, filename, gdsdbu, resize, angle, scalingX, scalingY, isReverse,
                    mirror, rotate, scale, profiletop, cw, cutprofile, mirrorpointX, mirrorpointY, rotatepointX,
                    rotatepointY, scalepointX, scalepointY, mirrordirection, cut_polygon,numberFormatL,numberFormatR,
                    zeros,unit)
        ret = json.loads(_ret)['status']
        if ret == 'true':
            ret = True
        else:
            ret = False
        return ret
    except Exception as e:
        print(e)
    return False

def save_excellon2(job:str, step:str, layer:str, path:str, number_format_l:int=2, 
                   number_format_r:int=6, zeroes:int=2, unit:int=0, tool_unit:int=1, 
                   x_scale:float=1, y_scale:float=1, x_anchor:int=0, y_anchor:int=0)->bool:
    try:
        isMetric = unit
        layer_info = Information.get_layer_information(job)
        for i in range(0,len(layer_info)):
            if layer_info[i]['name']==layer and layer_info[i]['context'] == 'board' and layer_info[i]['type'] =='drill':
                BASE.drill2file(job, step, layer,path,isMetric,number_format_l,number_format_r,
                    zeroes,unit,tool_unit,x_scale,y_scale,x_anchor,y_anchor, manufacator = '', tools_order = [])
                return True
    except Exception as e:
        print(e)
    return False



def save_rout(job:str, step:str, layer:str, path:str, number_format_l:int=2,
              number_format_r:int=6,zeroes:int=2,unit:int=0,tool_unit:int=1,x_scale:float=1,
              y_scale:float=1,x_anchor:int=0,y_anchor:int=0, break_arcs:bool = False)->dict:
    try:
        check = BASE.check_rout_output(job,step,layer)
        info = json.loads(check)['paras']
        errorResult1 = info['checkResult1']['errorResult']
        errorResult2 = info['checkResult2']['errorResult']
        errorResult3 = info['checkResult3']['errorResult']
        error = {}
        for i in errorResult1:
            featureinfo = i['featureInfo']
            if featureinfo != []:
                infos = featureinfo[:3]
                infor = []
                for m in infos:
                    infor.append(m['feature_index'])
                error['featureInfo'] = infor
                error['step'] = i['step']
                error['errorType'] = 0
                error['result'] = False
                break
        if error == {}:
            for j in errorResult2:
                featureinfo = j['featureInfo']
                if featureinfo != []:
                    infos = featureinfo[:3]
                    infor = []
                    for m in infos:
                        infor.append(m['feature_index'])
                    error['featureInfo'] = infor
                    error['step'] = j['step']
                    error['errorType'] = 1
                    error['result'] = False
                    break
        if error == {}:
            for n in errorResult3:
                featureinfo = n['featureInfo']
                if featureinfo != []:
                    infos = featureinfo[:3]
                    infor = []
                    for m in infos:
                        infor.append(m['feature_index'])
                    error['featureInfo'] = infor
                    error['step'] = n['step']
                    error['errorType'] = 2
                    error['result'] = False
                    break
        if error == {}:
            ret = BASE.rout2file(job, step, layer,path,number_format_l,number_format_r,zeroes,unit,tool_unit,x_scale,y_scale,x_anchor,y_anchor, 0, 0, 0, 0, 0, break_arcs)
            if 'status' in ret:
                ret = {'result':False,'errorType':3}
            else:
                ret = json.loads(ret)['paras']
                if ret == True:
                    ret = {'result':True}
                else:
                    ret = {'result':False,'errorType':3}
            return ret
        else:
            return error
    except Exception as e:
        print(e)
    return {}




def save_job(job:str,path:str)->bool:
    try:
        layers = Information.get_layers(job)
        steps = Information.get_steps(job)
        for step in steps:
            for layer in layers:
                BASE.load_layer(job,step,layer)
        BASE.save_job_as(job,path)
        return True
    except Exception as e:
        print(e)
    return False


def save_dxf(job:str,step:str,layers:list,savePath:str)->bool:
    try:
        _ret = BASE.dxf2file(job,step,layers,savePath)
        ret = json.loads(_ret)['paras']['result']
        return ret
    except Exception as e:
        print(e)
    return False

def save_pdf(job:str, step:str, layers:list, layercolors:list, outputpath:str, overlap:bool)->bool:
    try:
        (outputpath,pdfname) = os.path.split(outputpath)
        layer_sum = len(layers)
        colors_sum = len(layercolors)
        b = True
        if layer_sum != colors_sum:
            b = False
        else:
            for i in range(0,colors_sum):
                color = layercolors[i]
                if len(color) !=4:
                    b = False
                    break
        if b == True:
            _ret = BASE.output_pdf(job,step,layers,layercolors,outputpath,pdfname,overlap)
            ret = json.loads(_ret)['status']
            if ret == 'true':
                ret = True
            else:
                ret = False
            return ret
    except Exception as e:
        print(e)
    return False

def save_png(job:str, step:str, layers:list, xmin:int, ymin:int, xmax:int, ymax:int, picpath:str, backcolor:list, layercolors:list)->bool:
    try:
        (picpath,picname) = os.path.split(picpath)
        layer_sum = len(layers)
        color_sum = len(layercolors)
        back_sum = len(backcolor)
        b = True
        if  back_sum != 4:
            b = False
        else:
            if layer_sum != color_sum:
                b = False
            else:
                for i in range(0,color_sum):
                    color = layercolors[i]
                    if len(color) != 4:
                        b = False
                        break
        if b == True:
            _ret = BASE.save_png(job,step,layers,xmin,ymin,xmax,ymax,picpath,picname,backcolor,layercolors)
            ret = json.loads(_ret)['status']
            if ret == 'true':
                ret = True
            else:
                ret = False
            return ret
    except Exception as e:
        print(e)
    return False

# 输出文件
def save_drill(data:list,filename:str, unit:bool=True, tool_unit:bool=False, 
               number_format_l:int=2, number_format_r:int=6, zeroes:int=2, 
               x_scale:float=1, y_scale:float=1, x_anchor:int=0, y_anchor:int=0)->bool:
  try:
    file = open(filename, 'w', encoding = 'utf-8')
    file.write('M48'+'\n')
    if unit == True:
        file.write('INCH')
    else:
        file.write('METRIC')
    if zeroes == 0:
        file.write(',LZ'+'\n')
    elif zeroes == 1:
        file.write(',TZ'+'\n')
    else:
        file.write('\n')
    file.write(';FILE_FORMAT='+str(number_format_l)+':'+str(number_format_r)+'\n')
    for n in data:
        toolIdx = n['iToolIdx']
        to = str(toolIdx).rjust(2,'0')
        size_nm = n['iHoleSize']
        if tool_unit == True:
            size_mm = BASE.nm2inch(size_nm)
        else:
            size_mm =BASE.nm2mm(size_nm)
        size = ('%.4f'%size_mm)
        content = 'T'+to+'C'+size
        file.write(content+'\n')
    file.write('%'+'\n'+'G93X0Y0'+'\n')
    if unit == True:
        x_anchor = BASE.nm2inch(x_anchor)
        y_anchor = BASE.nm2inch(y_anchor)
    else:
        x_anchor = BASE.nm2mm(x_anchor)
        y_anchor = BASE.nm2mm(y_anchor)
    for i in data:
        toolIdx = i['iToolIdx']
        to = str(toolIdx).rjust(2,'0')
        part = 'T'+to
        file.write(part+'\n')
        location = i['vLocations']
        vLocations_slots = i['vLocations_slots']
        if vLocations_slots!=[]:
            for j in vLocations_slots:
                digital = BASE.slotLenth(j, unit, 0, False, number_format_l, number_format_r, zeroes, x_anchor, y_anchor, 0, 0, x_scale, y_scale)
                file.write(digital+'\n')
        else:
            for pad in location:
                xy = BASE.isPad(pad, unit, 0, False, number_format_l, number_format_r, zeroes, x_anchor, y_anchor, 0, 0, x_scale, y_scale)
                file.write(xy+'\n')
    file.write('M30')
    file.close()
    print("保存文件成功")
    return True
  except Exception as e:
    print(e)
  return False


def save_gds(job:str, step:str, layer:str, filename:str, gdsdbu:float)->bool:
    try:
        _type = 1
        resize = 0
        angle = 0
        scalingX = 1
        scalingY = 1
        isReverse = False
        mirror = False
        rotate = False
        scale = False
        profiletop =False
        cw = False
        cutprofile =   True
        mirrorpointX = 0
        mirrorpointY = 0
        rotatepointX = 0
        rotatepointY = 0
        scalepointX = 0
        scalepointY = 0
        mirrordirection = 'X'
        cut_polygon = []
        numberFormatL = 2
        numberFormatR = 6
        zeros = 0
        unit = 0
        _ret = BASE.layer_export(job, step, layer, _type, filename, gdsdbu, resize, angle, scalingX, scalingY, isReverse,
                    mirror, rotate, scale, profiletop, cw, cutprofile, mirrorpointX, mirrorpointY, rotatepointX,
                    rotatepointY, scalepointX, scalepointY, mirrordirection, cut_polygon,numberFormatL,numberFormatR,
                    zeros,unit)
        ret = json.loads(_ret)['status']
        if ret == 'true':
            ret = True
        else:
            ret = False
        return ret
    except Exception as e:
        print(e)
    return False

def save_svg(job:str, step:str, layersinfo:dict, savepath:str)->bool:
    try:
        layersinfo = [layersinfo]
        BASE.save_svg(job, step, layersinfo,savepath)
        return True
    except Exception as e:
        print(e)
    return False




