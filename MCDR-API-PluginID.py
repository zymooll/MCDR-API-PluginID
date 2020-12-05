#coding:utf-8
#MCDR-API-PluginID
#(C) 2020 SFR-Server

#一些空列表/字典
pluginIDList = []
pluginList = {}

#插件本身的一些变量
selfPluginName = "MCDR-API-PluginID"
selfPluginID = "vip.sfrserver.api.pluginid"
selfPluginVer = "0.0.2.201205-Alpha"
selfPluginAuthor = "SFR-Server"

#导入插件
def get_plugin_instance(server,pluginID):
    return server.get_plugin_instance(pluginList[pluginID][1])

#注册插件
def regPlugin(server,pluginName,pluginID,pluginVer,pluginAuthor):
    pluginIDList.append(pluginID)
    pluginInfo = [pluginName,pluginVer,pluginAuthor]
    pluginList[pluginID] = pluginInfo
    server.logger.info(pluginID+' 插件注册成功')

#获取"PluginID"列表
def getIDList():
    return pluginIDList

#获取插件列表
def getPluginList():
    return pluginList

def on_load(server, old_module):
    #输出版权信息
    server.logger.info('(C) 2020 SFR-Server')
    #注册插件
    regPlugin(server,selfPluginName,selfPluginID,selfPluginVer,selfPluginAuthor)
    #添加帮助信息
    server.add_help_message('!!PluginList', '获取插件列表')

def on_info(server, info):
    #指令相关
    if info.content == '!!PluginList':
        if info.is_player:
            server.tell(info.player,str(pluginList))
        else:
            server.logger.info(str(pluginList))

