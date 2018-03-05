# ROS策略路由

-------------------

## 目的

从外部收集中国国内的IP已经三大运营商的IP, 并据此设置ROS网关的策略路由。

## 方式和原理

目前主要通过两个来源进行自动收集
 * [ipip.net](http://ipip.net)
 * APNIC

由于IP地址库是个庞大工程，目前单纯根据收集的IP地址数量看，ipip.net的数据可能更加准确。

## 使用方法

首先，用apnic或ipip目录下的脚本获取各ISP和国内IP列表

对于需要特殊调整的路由策略，可以将目标IP地址记入FIX_ISP文件中，每个文件对应相应的ISP出口。

然后执行:

```
ros-script.sh > ros-route.rsc
```

生成ros的脚本，将该脚本上传到ros上用import命令执行即可。

```
[admin@MikroTik] > /import ros-route.rsc
```
