# 什么是WiFi 6（802.11ax）？

WiFi 6（Wi-Fi 6），也被称为802.11ax，是继[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")  ([802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac"))之后的最新一代[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")工业标准。在Wi-Fi 6发布之前，Wi-Fi标准是通过从802.11b到802.11ac的版本号来标识的。随着Wi-Fi标准的演进，Wi-Fi联盟为了便于Wi-Fi用户和设备厂商轻松了解Wi-Fi标准，选择使用数字序号来对Wi-Fi重新命名。  
Wi-Fi 6标准引入了[OFDMA](https://info.support.huawei.com/info-finder/encyclopedia/zh/OFDMA.html "OFDMA")、上/下行[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")、BSS Coloring、TWT等新技术，性能上得到跨越式提升，带宽和并发用户数相比Wi-Fi 5提升了4倍，并且[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")更低、更节能。

目录

-   [Wi-Fi 6解决了什么问题？](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html#content1)
-   [Wi-Fi 6 vs Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html#content2)
-   [Wi-Fi 6核心技术](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html#content3)
-   [Wi-Fi 6设备](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html#content4)

## Wi-Fi 6解决了什么问题？

Wi-Fi 6设计之初就是为了应对高密度无线接入和高容量的无线业务，比如室外大型公共场所、高密场馆、室内高密无线办公、电子教室等场景。

在这些场景中，接入[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")网络的客户端设备将呈现巨大增长，另外，还在不断增加的语音及视频流量也对Wi-Fi网络带来调整。众所周知，4K视频流（带宽要求50Mbps/人）、语音流（[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")小于30ms）、VR流（带宽要求75Mbps/人，时延小于15ms）对带宽和时延是十分敏感的，如果网络拥塞或重传导致传输延时，将对用户体验带来较大影响。

现有的[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")（[802.11ac](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")）虽然也能提供大带宽能力，但是随着接入密度的不断上升，吞吐量性能遇到瓶颈。而Wi-Fi 6则是通过引入[OFDMA](https://info.support.huawei.com/info-finder/encyclopedia/zh/OFDMA.html "OFDMA")以及上/下行[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")等新技术，使得性能上得到跨越式提升，带宽和并发用户数相比Wi-Fi 5提升4倍，并且时延更低。电子教室为例，以前如果是100多位学生的大课授课形式，传输视频或是上下行的交互挑战都比较大，而Wi-Fi 6网络将轻松应对该场景。

## Wi-Fi 6 vs Wi-Fi 5

Wi-Fi 6作[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")的继任者，相比Wi-Fi 5不仅仅体现在速率的提升上，更主要体现在高密场景下的用户性能提升。

![WiFi 6 vs WiFi 5](https://download.huawei.com/mdl/image/download?uuid=397834b996744d41995f3625c5371928 "WiFi 6 vs WiFi 5")  
WiFi 6 vs WiFi 5

### 大带宽

过去每一代[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")的标准，一直致力于提升速率。经过20多年的发展，Wi-Fi 6在160MHz信道宽度下，理论最大速率已经达到9.6Gbps，是802.11b的近900倍。

Wi-Fi 6速率的提升除了采用更高阶的1024-QAM编码方式外，也得益于Wi-Fi 6相较于Wi-Fi 5增加了子载波数量、空间流数，以及Symbol传输时间（单次单终端）由Wi-Fi 5的3.2μs提升到12.8μs。

### 高并发

Wi-Fi 6引入了[OFDMA](https://info.support.huawei.com/info-finder/encyclopedia/zh/OFDMA.html "OFDMA")和上行[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")等多用户技术，进一步提升了频谱利用率，使得Wi-Fi 6相比于Wi-Fi 5，并发用户数提升了**4倍**。

### 低时延

在[低时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")场景，例如VR/AR-互动操作模拟、全景直播、互动式游戏、沉浸式会议、高清无线投屏等，Wi-Fi 5的30ms[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")已经无法满足需求，而Wi-Fi 6则是通过OFDMA有效减少冲突，提升频谱利用率，并且空间复用技术BSS Coloring减少了同频干扰，令时延降低至**20ms**。

### 节能

随着IoT设备广泛应用，除了提升终端速率外，Wi-Fi 6更是关注了终端的耗电情况。

Wi-Fi 6采用TWT技术，按需唤醒终端Wi-Fi，加上20MHz-Only技术，能进一步降低终端的功耗。

## Wi-Fi 6核心技术

以下是Wi-Fi 6的核心新技术。

### OFDMA频分复用技术

Wi-Fi 6之前，数据传输采用的是OFDM模式，用户是通过不同时间片段区分出来的。每一个时间片段，一个用户完整占据所有的信道资源，并且发送一个完整的数据包。

Wi-Fi 6中引入了一种更高效的数据传输模式，叫[OFDMA](https://info.support.huawei.com/info-finder/encyclopedia/zh/OFDMA.html "OFDMA")（因为Wi-Fi 6支持上下行多用户模式，因此也可称为MU-OFDMA），它通过将子载波分配给不同用户并在OFDM系统中添加多址的方法来实现多用户复用信道资源。迄今为止，它已被许多无线技术采用，例如3GPP LTE。在该模式下，单个用户不再是独占完整的子载波，而是多用户共享信道资源，实现频谱利用率的提升。

![WiFi 6 OFDMA频分复用技术](https://download.huawei.com/mdl/image/download?uuid=a1047376424d4f28aca12ff23ba0dd47 "WiFi 6 OFDMA频分复用技术")  
WiFi 6 OFDMA频分复用技术

### 上/下行MU-MIMO技术

[MU-MIMO](https://info.support.huawei.com/info-finder/encyclopedia/zh/MU-MIMO.html "MU-MIMO")使用信道的空间分集来在相同带宽上发送独立的数据流，与OFDMA不同，所有用户都使用全部带宽，从而带来多路复用增益。终端受天线数量受限于尺寸，一般来说只有1个或2个空间流（天线），比[AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")的空间流（天线）要少，因此，在AP中引入MU-MIMO技术，同一时刻就可以实现AP与多个终端之间同时传输数据，大大提升了吞吐量。

MU-MIMO在[Wi-Fi 5](https://info.support.huawei.com/info-finder/encyclopedia/zh/802.11ac.html "802.11ac")就已经引入，但只支持下行4x4 MU-MIMO。在Wi-Fi 6中进一步增加了MU-MIMO数量，可同时支持上/下行8x8 MU-MIMO。

![WiFi 6的上/下行MU-MIMO技术](https://download.huawei.com/mdl/image/download?uuid=fd8dde04d00c47b1a62cb946b8e23171 "WiFi 6的上/下行MU-MIMO技术")  
WiFi 6的上/下行MU-MIMO技术

虽然Wi-Fi 6标准允许OFDMA与MU-MIMO同时使用，但不要将OFDMA与MU-MIMO混淆。OFDMA支持多用户通过细分信道（子信道）来提高并发效率，MU-MIMO支持多用户通过使用不同的空间流来提高吞吐量。OFDMA与MU-MIMO的对比如下：

![OFDMA与MU-MIMO对比](https://download.huawei.com/mdl/image/download?uuid=29b3088d63da4d72b8cde5c071281fb8 "OFDMA与MU-MIMO对比")  
OFDMA与MU-MIMO对比

### 空分复用技术（SR）和BSS Coloring

802.11ax中引入了一种新的同频传输识别机制，叫BSS Coloring着色机制，在PHY报文头中添加BSS color字段对来自不同BSS的数据进行“染色”，为每个通道分配一种颜色，该颜色标识一组不应干扰的基本服务集（BSS），接收端可以及早识别同频传输干扰信号并停止接收，避免浪费收发机时间。如果颜色相同，则认为是同一BSS内的干扰信号，发送将推迟；如果颜色不同，则认为两者之间无干扰，两个[Wi-Fi](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi.html "WiFi")设备可同信道同频并行传输。以这种方式设计的网络，那些具有相同颜色的信道彼此相距很远，此时可将这种信号设置为不敏感，从而实现空间复用。

![WiFi 6 BSS Coloring](https://download.huawei.com/mdl/image/download?uuid=a6f58e0fcd6947b08cdee46ae7a64834 "WiFi 6 BSS Coloring")  
WiFi 6 BSS Coloring

### 目标唤醒时间（TWT）

目标唤醒时间TWT（Target Wake Time）是802.11ax支持的另一个重要的资源调度功能，它借鉴于802.11ah标准。它允许设备协商什么时候和多久会被唤醒，然后发送或接收数据。此外，Wi-Fi AP可以将客户端设备分组到不同的TWT周期，从而减少唤醒后同时竞争无线介质的设备数量。TWT还增加了设备睡眠时间，对采用电池供电的终端来说，大大提高了电池寿命。

![WiFi 6 目标唤醒时间（TWT）](https://download.huawei.com/mdl/image/download?uuid=757f7c17e2e54cef8c4149ed0228da92 "WiFi 6 目标唤醒时间（TWT）")  
WiFi 6 目标唤醒时间（TWT）

### 更高阶的调制技术（1024-QAM）

Wi-Fi 6标准的主要目标是增加系统容量，降[低时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")，提高多用户高密场景下的效率，但更好的效率与更快的速度并不互斥。Wi-Fi 5采用的256-QAM正交幅度调制，每个符号传输8bit数据，Wi-Fi 6将采用1024-QAM正交幅度调制，每个符号位传输10bit数据，从8到10的提升是25%，也就是相对于Wi-Fi 5来说，Wi-Fi 6的单条空间流数据吞吐量又提高了25%。

![WiFi 6 1024-QAM](https://download.huawei.com/mdl/image/download?uuid=b90999c587f045218f5a6cf9b0d7e1e9 "WiFi 6 1024-QAM")  
WiFi 6 1024-QAM

### 支持2.4GHz频段

我们都知道2.4GHz频宽窄，且仅有3个20MHz的互不干扰信道（1，6和11），在Wi-Fi 5标准中已经被抛弃，但是有一点不可否认的是2.4GHz仍然是一个可用的Wi-Fi频段，在很多场景下依然被广泛使用，因此，Wi-Fi 6标准中选择继续支持2.4GHz，目的就是要充分利用这一频段特有的优势。

### 覆盖范围提升

由于Wi-Fi 6标准采用的是Long OFDM Symbol发送机制，每次数据发送持续时间从原来的3.2μs提升到12.8μs，更长的发送时间可降低终端丢包率；另外Wi-Fi 6最小可仅使用2MHz频宽进行窄带传输，有效降低频段噪声干扰，提升了终端接受灵敏度，增加了覆盖距离。

![WiFi 6 Long OFDM Symbol与窄带传输带来的覆盖距离提升](https://download.huawei.com/mdl/image/download?uuid=c1d58dbd3db24e928d743d3099b7987c "WiFi 6 Long OFDM Symbol与窄带传输带来的覆盖距离提升")  
WiFi 6 Long OFDM Symbol与窄带传输带来的覆盖距离提升

## Wi-Fi 6设备

华为公司2017年10月发布首款Wi-Fi 6  [AP](https://info.support.huawei.com/info-finder/encyclopedia/zh/Access+Point.html "Access Point")。随后，华为推出了全系列全场景AirEngine系列Wi-Fi 6产品，可满足企业、教育、金融、医疗、政府、制造、商业、场馆等各行业构建数字化、无线化、物联化的办公和生产作业空间。

![华为AirEngine系列AP产品](https://download.huawei.com/mdl/image/download?uuid=d0acfb2e1fb04bd6991b5c7f7b5699fc "华为AirEngine系列AP产品")  
华为AirEngine系列AP产品

华为AirEngine系列AP产品有：

-   AirEngine 8760系列：华为室内型旗舰Wi-Fi 6AP，适合大型企业高密高带宽场景。
-   AirEngine 6760系列：华为室内型AirEngine 6760系列是适合中、大型企业高密部署场景的Wi-Fi 6 AP。
-   AirEngine 5760系列：华为室内型AirEngine 5760系列是面向中、小型企业办公、商业、零售等场景的 Wi-Fi 6 AP。
-   AirEngine 8760R系列：华为室外型旗舰Wi-Fi 6 AP，适用于大型企业、体育场馆、公共场所等高密应用场景。
-   AirEngine 6760R系列：华为高性能室外型Wi-Fi 6 AP，广泛适用于广场、公园、步行街等室外场景。

更多产品相关介绍请参见：[AirEngine Wi-Fi 6产品](https://e.huawei.com/cn/products/enterprise-networking/wlan/wifi-6/new-products-launch)，产品相关配置维护请参见：[WLAN AC和FIT AP 产品文档](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100169923)。

参考资源

1[阅读eBook：Wi-Fi 6](https://support.huawei.com/enterprise/zh/doc/EDOC1100195173)

2[华为Wi-Fi 6（802.11ax）技术白皮书](https://e.huawei.com/cn/material/networking/wlan/b3f46485597c4d72b43a6a27c6480646)

3[了解华为AirEngine Wi-Fi 6产品](https://e.huawei.com/cn/products/enterprise-networking/wlan/wifi-6/new-products-launch)

4[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/WiFi+6.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3MTc2MDcwNF19
-->