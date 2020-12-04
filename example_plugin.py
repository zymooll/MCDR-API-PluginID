#Example
#2020/12/3
#(C) 2020 SFR-Server

def on_load(server, old_module):
    # 导入插件
    global PluginID
    PluginID = server.get_plugin_instance("MCDR-API-PluginID")
    #注册插件
    PluginID.regPlugin(server,__name__,"vip.sfrserver.api.pluginid.example","1.0.0","SFR-Server")
    #使用"PluginID"导入某个插件
    PluginID.get_plugin_instance(server,"vip.sfrserver.api.pluginid")

#获取"PluginID"列表
PluginIDList=PluginID.getIDList()
#获取插件列表
PluginList=PluginID.getPluginList()