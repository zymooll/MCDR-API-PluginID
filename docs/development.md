## MCDR-API-PluginID 开发文档

它很简单

如果你熟悉MCDR的[插件文档](https://github.com/Fallen-Breath/MCDReforged/blob/master/doc/plugin_cn.md)那应该在可以1分钟内上手编写



### 导入MCDR-API-PluginID

这一步很简单，只需要在on_load()里写:

```
global PluginID
PluginID = server.get_plugin_instance("MCDR-API-PluginID")
```

即可



### 注册插件

建议这一步在on_load()内执行以确保没问题

```
regPlugin(server,pluginName,pluginID,pluginVer,pluginAuthor)
```

##### 各项参数干啥用/填啥:

| 参数名       | 干啥用的，或者说填啥                                         |
| ------------ | ------------------------------------------------------------ |
| server       | 纯粹只是让使函数内可以执行server下的函数，直接写server即可   |
| pluginName   | 插件的文件名，填_\_name__即可                                |
| pluginID     | 插件的"PluginID"，例如MCDR-API-PluginID的"PluginID"为: `vip.sfrserver.api.pluginid` |
| pluginVer    | 插件的版本号                                                 |
| pluginAuthor | 插件的作者                                                   |



### 使用"PluginID"导入某个插件

直接:

```
get_plugin_instance(server,pluginID)
```

即可

##### 各项参数干啥用/填啥:

| 参数名   | 干啥用的，或者说填啥                                         |
| -------- | ------------------------------------------------------------ |
| server   | 纯粹只是让使函数内可以执行server下的函数，直接写server即可   |
| pluginID | 插件的"PluginID"，例如MCDR-API-PluginID的"PluginID"为: `vip.sfrserver.api.pluginid` |



### 获取"PluginID"列表

使用`getIDList()`函数即可获得

##### 解析后的样式:

```
[
    pluginID
]
```

``pluginID``: 插件的"PluginID"，例如MCDR-API-PluginID的"PluginID"为: `vip.sfrserver.api.pluginid`



### 获取插件列表

使用``getPluginList()``即可获得

##### 解析后的样式:

```
{
	pluginID:[
		pluginName,
        pluginVer,
        pluginAuthor
	]
}
```

``pluginID``: 插件的"PluginID"，例如MCDR-API-PluginID的"PluginID"为: `vip.sfrserver.api.pluginid`

`pluginName`: 插件的文件名

`pluginVer`: 插件的版本号

`pluginAuthor`: 插件的作者
