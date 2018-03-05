# ipip.net相关脚本说明

-------------------

## Step 1

执行load.py, 将从[china_ip_list](https://github.com/17mon/china_ip_list.git)上下载的中国IP子网列表，载入数据库中。

## Step 2

执行lookup.py, 将数据库中的国内IP, 利用ipip.net的免费API, 查询归属运营商，并将结果保存回数据库。
需要注意, ipip.net的免费API有查询次数限制，所以脚本里限制了查询数量为1000。
可以在具备不同外网IP的主机上分散执行查询。

## Step 3

所有的IP都查询完毕归属后，执行split.py, 将查询结果输出的不同ISP的IP列表文件中。

## 相关URL

 * https://github.com/17mon/china_ip_list.git
