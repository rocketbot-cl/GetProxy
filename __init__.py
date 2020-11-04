# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import sys
import os
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'GetProxy' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Reviso que tipo de modulo es
"""
if module == "GetProxy":
    Category = GetParams("category")
    resvar = GetParams("result")
    data = []
    try:
        from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
        scrapper = Scrapper(category=Category, print_err_trace=False)
        data_ = scrapper.getProxies()
        for item in data_.proxies:
            data.append(str(item.ip) + ":"+str(item.port))
    except Exception as e:
        PrintException()
        raise e    
    print(data)
    SetVar(resvar, data)

