# 什么是信道利用率？

信道利用率是指在一定时间内信道繁忙时间与总时间之比，是衡量[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")网络性能的重要指标之一。

目录

-   [信道利用率是如何计算的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E9%81%93%E5%88%A9%E7%94%A8%E7%8E%87.html#content1)
-   [信道利用率越高越好吗？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E9%81%93%E5%88%A9%E7%94%A8%E7%8E%87.html#content2)
-   [信道利用率过高怎么办？](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E9%81%93%E5%88%A9%E7%94%A8%E7%8E%87.html#content3)

## 信道利用率是如何计算的？

信道利用率的计算公式如下：

![](https://download.huawei.com/mdl/image/download?uuid=c26f0ddd82804531925c4c23cfd110a4)

[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")中的信道利用率通常由[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")设备通过硬件检测实现。其中，信道繁忙时间是AP检测到信道上存在信号的总时长，不仅包含了AP发送和接收信号占用的“有效”时间，也包含了环境中干扰信号占用的“无效”时间。因此，当网络业务量变大或存在信号干扰时，信道利用率会提高。

## 信道利用率越高越好吗？

信道利用率并非越高越好。评估信道利用率时，可以从用户体验和资源分配两个视角来考虑。

从用户体验来看，一般认为信道利用率低于60%时，用户可以获得较好的上网体验；当信道利用率较高时，说明该信道处于繁忙状态，数据处理时需要排队，可能导致网络拥塞、[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")增加。因此，为了保障用户体验，信道利用率往往越低越好。

然而从资源分配来看，信道利用率过低意味着信道资源利用不充分，网络性能远大于实际需求，浪费网络建设成本。

因此，网络建设和维护人员应根据实际业务需求，通过监测信道利用率，合理部署网络资源。

## 信道利用率过高怎么办？

根据信道利用率过高的原因，网络管理员可以采取不同的网络优化策略。

### 配置动态限速功能

[WLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/WLAN.html "WLAN")中所有终端共享带宽，相互竞争带宽资源。如果周围环境中无线终端多，业务流量大，则容易引起空口网络拥塞。例如某个用户下载或上传大文件时，占用过多带宽资源，可能影响其他用户访问网络。为避免此类问题，可配置动态限速功能。

开启动态限速功能后，设备会根据空口是否拥塞来判定是否进行无线用户限速，从而提升无线用户网络使用体验。动态限速功能会周期性（2秒）计算信道利用率。若连续5个周期（10秒）信道利用率均高于80%，则认为发生了拥塞，从而触发速率限制；若连续30个周期（1分钟）信道利用率均低于70%，则认为空口不再拥塞，从而解除速率限制。

### 排查信号干扰问题

无线空口环境会受到各种外界干扰，严重影响用户体验。干扰主要有[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")干扰和非Wi-Fi干扰。Wi-Fi干扰通常包括[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")之间的同频和邻频干扰以及其它Wi-Fi干扰；非Wi-Fi干扰通常包括微波炉、蓝牙、无线影音、婴儿监控器、无线摄像头、红外传感器、无绳电话等干扰。

在故障定位的过程中，如果AP上业务量较小，但信道利用率比较高（超过60%），则说明空口干扰比较严重。此时，需要对AP的信道进行合理的规划，降低干扰。可以手动将信道切换至信道利用率低的信道，或者在无业务影响时进行调优操作。

### 排查组播或者广播报文泛洪到空口问题

WLAN网络中发送[组播](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E7%BB%84%E6%92%AD.html "组播")、广播报文时，因为报文不会重传，所以为了确保接收端的收包成功率，都是以较低速率发送。如果网络中有大量的组播、广播报文往空口发送，会导致空口资源浪费严重，信道利用率持续升高，影响无线终端正常的上网体验，出现[延迟](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")大、丢包的情况。

在故障定位的过程中，如果信道利用率很高，但是干扰率并不大，说明信道利用率高主要由于本AP导致。此时建议查看AP上组播、广播报文的接收情况，观察报文增长速率。如果广播或组播报文的增长速率超过100pps，说明接收到的广播、组播报文较多。此时，可以在上层的[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")或AC上开启二层网络隔离功能，或开启广播和组播报文限速功能。

参考资源

1[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BF%A1%E9%81%93%E5%88%A9%E7%94%A8%E7%8E%87.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MzUzNTQxMzZdfQ==
-->