ndspod_ddns
===========

通过Dnspod的Api，动态修改Dnspod域名，达到3322效果

##场景：

我家里使用的长城宽带，拨号后有公网ip，然后在家弄了树莓派，但想远程连接回来。就看了一下Dnspod的Api，[官方demo](https://github.com/DNSPod/dnspod-python)，发现了有地方不太满足情况，就修改了一下，用了几天还不错，就开源了给大家使用。


##主要做了以下优化：

1. 修改了获取ip的方法
原demo的方法在我们这总获取不正确，我们这使用的的长城宽带。
修改为访问万网的接口（测试过ip138的接口，返回的ip也不是路由器上得到的ip）

2. 修改了判断ip是否变化的逻辑
原demo是本地记录了上一次修改过的ip，然后再读取路由器的ip，对比这两个ip是否一致，不一致的时候就写入到二级域名下。
但我遇到了一个问题就是，不小心手动修改了一下二级域名的指向，但本地记录的ip和路由器ip还是一致，导致永远不会更新域名。
我修改的逻辑为获取到路由器ip后，然后尝试解析一下二级域名的ip，判断两个ip是否一致，不一致就更新。

3. 修改检查时间为600秒

##使用的时候主要修改以下几个字：

1. strDomain = "subDomain.domain.com"   #替换为你要动态修改的二级域名

2. login_email="youremail"   #在Dnspod上登录的邮箱

3. login_password="yourpassword"   #在Dnspod上登录的密码

4. domain_id=1000   #在Dnspod上要动态修改的主域名id

5. record_id=1000    #在Dnspod上要动态修改的二级域名id

6. sub_domain="subDomain"   #要动态修改的二级域名

###注：

获得domain_id可以用 `curl curl -k https://dnsapi.cn/Domain.List -d "login_email=xxx&login_password=xxx" `

获得record_id类似 `curl -k https://dnsapi.cn/Record.List -d "login_email=xxx&login_password=xxx&domain_id=xxx" `




