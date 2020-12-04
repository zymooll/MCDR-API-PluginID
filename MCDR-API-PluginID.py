#coding:utf-8
#MCDR-API-PluginID
#(C) 2020 SFR-Server

pluginIDList = []
pluginList = {}

selfPluginName = "MCDR-API-PluginID"
selfPluginID = "vip.sfrserver.api.pluginid"
selfPluginVer = "0.0.1.201203-Alpha"
selfPluginAuthor = "SFR-Server"

def get_plugin_instance(server,pluginID):
    return server.get_plugin_instance(pluginList[pluginID][1])

def regPlugin(server,pluginName,pluginID,pluginVer,pluginAuthor):
    pluginIDList.append(pluginID)
    pluginInfo = [pluginName,pluginVer,pluginAuthor]
    pluginList[pluginID] = pluginInfo
    server.logger.info(pluginID+' 插件注册成功')

def getIDList():
    return pluginIDList

def getPluginList():
    return pluginList

def on_load(server, old_module):
    server.logger.info('(C) 2020 SFR-Server')
    regPlugin(server,selfPluginName,selfPluginID,selfPluginVer,selfPluginAuthor)
    server.add_help_message('!!PluginList', '获取插件列表')

def on_info(server, info):
    if info.content == '!!PluginList':
        if info.is_player:
            server.tell(info.player,str(pluginList))
        else:
            server.logger.info(str(pluginList))

