# 什么是Voice VLAN？

Voice  [VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")是为用户的语音流专门划分的VLAN。

目录

-   [为什么需要Voice VLAN？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Voice+VLAN.html#content1)
-   [Voice VLAN应用场景有哪些？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Voice+VLAN.html#content2)
-   [Voice VLAN是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Voice+VLAN.html#content3)

## 为什么需要Voice VLAN？

网络中经常有数据、语音、视频等多种流量同时传输。因为丢包和[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")对通话质量的影响很大，用户对语音的质量比数据或者视频的质量更为敏感，因此在带宽有限的情况下就需要优先保证通话质量。通过配置Voice  [VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")，[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")可识别语音流，将语音流加入到Voice VLAN中传输，并对其进行有针对性的[QoS](https://info.support.huawei.com/info-finder/encyclopedia/zh/QoS.html "QoS")保障，当网络发生拥塞时可以优先保证语音流的传输。

## Voice VLAN应用场景有哪些？

如下图所示，PC和[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")电话同时通过[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")接入网络。因用户对语音的[时延](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BD%8E%E6%97%B6%E5%BB%B6.html "低时延")和抖动比较敏感，所以需要提高网络中语音数据流的传输优先级，在网络发生拥塞时优先保证语音数据的传输。

![Voice VLAN的应用场景](https://download.huawei.com/mdl/image/download?uuid=1e36ae55ea764a24b6f1c4bf151f7f51 "Voice VLAN的应用场景")  
  
Voice VLAN的应用场景

可根据IP电话上送的语音报文是否带Tag选择以下的一种方案：

-   如果IP电话发送的是untagged或Tag0语音报文，可配置基于MAC地址的Voice  [VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")。
-   如果IP电话支持通过协议获取交换机上配置的Voice VLAN信息，此时IP电话发送的是带Tag的语音报文，可配置基于VLAN的Voice VLAN。

## Voice VLAN是如何工作的？

若要提高语音数据流的传输优先级，首先要能识别出语音数据流。识别出语音数据流后，再对语音数据流提升优先级后传输。

Voice  [VLAN](https://info.support.huawei.com/info-finder/encyclopedia/zh/VLAN.html "VLAN")可以通过以下两种方式来实现对语音数据流的识别：

-   通过收到报文的源MAC地址，即基于MAC地址的方式
    
    设备可以根据进入接口的数据报文中的源MAC地址字段来判断该数据流是否为语音数据流。源MAC地址匹配系统设置的语音设备的组织唯一标识符OUI（Organizationally Unique Identifier）的报文被认为是语音数据流。用户需要预先设置OUI，适用于[IP](https://info.support.huawei.com/info-finder/encyclopedia/zh/IPv4.html "IPv4")电话上送untagged语音报文的场景。
    
-   通过报文携带的VLAN Tag，即基于VLAN的方式
    
    若有大量IP电话接入[交换机](https://info.support.huawei.com/info-finder/encyclopedia/zh/%E4%BA%A4%E6%8D%A2%E6%9C%BA.html "交换机")，配置IP电话的OUI会非常繁琐。可在交换机上配置基于VLAN来提升语音报文的优先级，此时设备会根据进入接口的报文的VLAN ID来判断该数据报文是否为语音报文。当VLAN ID匹配系统配置的Voice VLAN后，则认为是语音数据流。这种方式实现的前提是IP电话支持获取交换机上配置的Voice VLAN信息的功能，在大量IP电话接入的情况下，可以简化配置。
    

以上方案是从方便配置的角度给出的。实际上，不管IP电话上送的语音报文是否带VLAN Tag，基于MAC地址和基于VLAN的Voice VLAN都可以实现。主要区别在于：当IP电话上送的是untagged语音报文时，必须配置OUI，才能把语音报文和数据报文区分开来；如果IP电话上送的是带Tag语音报文，则可配置基于VLAN的Voice VLAN，这样在大量IP电话接入的情况下，就不用配置繁琐的OUI，简化配置

### 基于MAC地址的Voice VLAN

-   OUI
    
    OUI指的是MAC地址的前24位（二进制），可以用来表示一个MAC地址段，是IEEE为不同设备供应商分配的一个全球唯一的标识符，各设备厂商再从这个地址段中分配24位，从而形成48位的MAC地址。所以根据OUI识别IP电话机的原理就是根据IP电话厂商申请的MAC地址段来识别哪些报文是电话机发送的，以此来判断哪些报文属于语音报文。
    
    Voice VLAN中的OUI有别于上述的通常意义的OUI，这个OUI是由用户来配置的，而且可以使用掩码，即不需要一定是24位掩码的，掩码长度用户可以自己指定。OUI的值为**voice-vlan mac-address**命令中的mac-address和mask参数相与的结果。
    
-   实现原理
    
    如下图所示，交换机接收到PC和IP Phone发出的untagged报文后会做如下处理：如果源MAC匹配交换机上配置的OUI（源MAC地址与配置的OUI掩码进行与运算后等于OUI视为匹配），则为该报文加上Voice VLAN的Tag，并提升报文优先级；如果不匹配，就会为其加上PVID的VLAN Tag，从而保证语音报文的优先发送。
    
    ![基于MAC地址的Voice VLAN示意图](https://download.huawei.com/mdl/image/download?uuid=294df4fb138543b2905990f5aa07769a "基于MAC地址的Voice VLAN示意图")  
    基于MAC地址的Voice VLAN示意图
    

### 基于VLAN的Voice VLAN

基于VLAN的Voice VLAN实现原理为：交换机收到PC和IP Phone发来的报文后会判断报文的VLAN ID与接口上配置的Voice VLAN ID是否相同，如果相同则认为此数据流为语音数据流并提升优先级。PC发出的untagged报文则会被加上PVID的VLAN Tag。因此基于VLAN的Voice VLAN需要IP Phone可以获取交换机上配置的Voice VLAN信息。

IP Phone获取交换机上Voice VLAN信息的方法有很多种，以下以IP Phone通过LLDP协议获取交换机Voice VLAN信息为例介绍一下实现过程。

![基于VLAN的Voice VLAN示意图](https://download.huawei.com/mdl/image/download?uuid=efc11bc5950d40b3bde918d8ce82c23f "基于VLAN的Voice VLAN示意图")  
基于VLAN的Voice VLAN示意图

1.  如上图所示，IP电话上线会主动发送LLDP报文，以获取交换机上配置的Voice VLAN信息。
2.  交换机收到IP电话发送的LLDP报文，会在相关字段填充Voice VLAN信息发给IP电话。
3.  IP电话收到携带Voice VLAN信息的LLDP报文后，再次发送语音报文时就会带Tag发送。
4.  交换机收到带Tag的语音报文，如果Tag和交换机上配置的Voice VLAN匹配，则为其提升优先级后转发。

交换机收到untagged报文，仍然会加入到PVID所在的VLAN中。这样，当发生网络拥塞的时候交换机就能保证语音报文的优先发送。

参考资源

1[Voice VLAN配置（S300, S500, S2700, S5700, S6700 V200R024C00）](https://support.huawei.com/enterprise/zh/doc/EDOC1100410518/7ccdf11d?idPath=24030814|21782164|21782167|259602657)

2[Voice VLAN配置（S1700, S5700, S6700 V600R024C00）](https://support.huawei.com/enterprise/zh/doc/EDOC1100411515/9dff3af8?idPath=24030814|21782164|21782167|259602657)

3[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/Voice+VLAN.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg2NjM2MDQ3OV19
-->