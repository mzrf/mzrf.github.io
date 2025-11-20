# 什么是Keychain？

Keychain中的Key，不是算法，也不是密钥，而是一套加密和认证的规则。keychain通过对它拥有的一系列Key进行集中控制和灵活管理，为应用程序提供动态的安全认证服务。本文从为什么需要keychain，组成部分，如何工作，典型应用这几个方面展开介绍。

目录

-   [为什么需要keychain？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Keychain.html#content1)
-   [keychain是由哪些部分组成？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Keychain.html#content2)
-   [keychain是如何工作的？](https://info.support.huawei.com/info-finder/encyclopedia/zh/Keychain.html#content3)
-   [keychain的典型应用](https://info.support.huawei.com/info-finder/encyclopedia/zh/Keychain.html#content4)

## 为什么需要keychain？

RIP、[IS-IS](https://info.support.huawei.com/info-finder/encyclopedia/zh/IS-IS.html "IS-IS")、[OSPF](https://info.support.huawei.com/info-finder/encyclopedia/zh/OSPF.html "OSPF")、[BGP](https://info.support.huawei.com/info-finder/encyclopedia/zh/BGP.html "BGP")等应用程序在和对端进行会话之前，需要首先建立传输层的连接。

为了保证应用程序会话连接和交互数据的安全性，可以对报文进行MD5算法的认证，但MD5认证存在如下缺点：

-   MD5算法相对简单，无法满足安全性要求高的网络。
-   考虑到密钥安全，应定期更换密钥。MD5算法和密钥直接在应用程序中配置，与应用程序之间是一对一的静态绑定。因此，需要分别在两端设备的多个应用程序上逐个进行手动更换。

为了替代MD5，Keychain定义了应用程序认证的Key的集合：

-   Keychain中的每个Key中可以灵活挑选相对MD5更安全的算法，后续还能扩展选择更安全的算法。
-   Keychain中的每个Key拥有独立的算法、密钥和活跃时间。两端设备的应用程序使用了Keychain认证，即会匹配多个Key。因此可以根据Key的活跃时间实现在两端设备的多个应用程序上定期自动更换认证算法和密钥。
-   Keychain中的Key在进行动态更换时，不需要断开重连正在使用的传输层连接，可以始终保持应用程序会话连接的稳定性，不会中断业务。

## keychain是由哪些部分组成？

Keychain是加密规则（key）的集合。每个规则必须含有以下三部分：认证算法、认证密钥、Key的活跃时间。其中认证算法和认证密钥用来控制加密/解密报文，Key的活跃时间表示在这段时间内，能够使用配置的算法和密钥对报文认证后发送/接收。

-   认证算法：支持MD5、SHA-1、HMAC-MD5、HMAC-SHA1-12、HMAC-SHA1-20、HMAC-SHA-256、SHA-256、SM3、HMAC-SHA-384、HMAC-SHA-512算法。
-   认证密钥：一段用于加密的字符串。同一明文信息使用不同的密钥加密，会得到不同的密文；只有使用同一个密钥加密，才会得到相同的密文。
-   Key的活跃时间：代表了这个Key生效的时间段，当一个Key没有处于活跃时间时，会由另一个活跃的Key来替代。

## keychain是如何工作的？

按照不同应用程序应用Keychain进行认证的不同处理流程，可分为非TCP应用程序使用Keychain认证和TCP应用程序使用Keychain认证。

### Keychain的实现原理（非TCP）

Keychain本身只对加密和认证的Key进行管理，只有在被应用程序使用时，Keychain才能发挥作用。

应用程序在使用Keychain认证时，是通过绑定一条Keychain来实现，例如绑定KeychainA，则可以使用这条Keychain中的Key集合来进行加密和解密。

-   加密过程
    
    ![非TCP应用程序使用Keychain认证的加密过程](https://download.huawei.com/mdl/image/download?uuid=9a83da0322a04bc4aa416dca7095e99e "非TCP应用程序使用Keychain认证的加密过程")  
    非TCP应用程序使用Keychain认证的加密过程
    
-   解密过程
    
    ![非TCP应用程序使用Keychain认证的解密过程](https://download.huawei.com/mdl/image/download?uuid=85463e0ded1c46cc9782a5e4ac61c41c "非TCP应用程序使用Keychain认证的解密过程")  
    非TCP应用程序使用Keychain认证的解密过程
    

### Keychain的实现原理（TCP）

TCP应用程序使用Keychain认证的原理与非TCP应用程序类似，只是增加了TCP增强认证选项。

-   TCP增强认证选项
    
    TCP增强认证选项的格式如下图所示，TCP报文头中会携带此认证选项，专门用于为TCP连接提供认证保护。
    
    ![TCP增强认证选项的格式](https://download.huawei.com/mdl/image/download?uuid=9e26609d0b504ebd9195c6f922107c3a "TCP增强认证选项的格式")  
    TCP增强认证选项的格式
    
    -   Kind：8个比特，用于标识此选项的类型，由IANA分配。
    -   Length：8个比特，用于标识此选项的总长度。
    -   T：1个比特，用于标识此选项是否被包含在TCP增强认证计算的对象中，0表示包含，默认值是0。
    -   K：1个比特，为以后预留，当前值是0。
    -   Alg-id：6个比特，用于标识TCP增强认证的算法。
    -   Res：2个比特，为以后预留，当前值是0。
    -   Key-id：6个比特，用于标识Keychain认证的Key。
    -   Authentication Data：长度可变，至少包含TCP增强认证计算的结果。
    
    由于IANA没有统一定义Kind和Alg-id字段的取值，各设备商使用不同的取值。为了使不同厂商的设备能够互通，Keychain支持配置TCP Kind和TCP algrithm-id。
    
-   加密过程
    
    ![TCP应用程序使用Keychain认证的加密过程](https://download.huawei.com/mdl/image/download?uuid=a6c0c4a5e8a646d3a3b7d0f9d9a2ceba "TCP应用程序使用Keychain认证的加密过程")  
    TCP应用程序使用Keychain认证的加密过程
    
-   解密过程
    
    ![TCP应用程序使用Keychain认证的解密过程](https://download.huawei.com/mdl/image/download?uuid=ae539f29c8f342c0a50c174a7e880bd1 "TCP应用程序使用Keychain认证的解密过程")  
    TCP应用程序使用Keychain认证的解密过程
    

## keychain的典型应用

RIP、[IS-IS](https://info.support.huawei.com/info-finder/encyclopedia/zh/IS-IS.html "IS-IS")、[OSPF](https://info.support.huawei.com/info-finder/encyclopedia/zh/OSPF.html "OSPF")、[BGP](https://info.support.huawei.com/info-finder/encyclopedia/zh/BGP.html "BGP")等协议报文都需要进行加密才能符合网络完全性，Keychain为这些协议报文提供了认证保护，Keychain通过动态的更改认证算法和密钥，提高了协议报文的安全性。下面以Keychain在IS-IS协议报文上的应用进行简要介绍。

IS-IS作为一种广泛应用的[路由](https://info.support.huawei.com/info-finder/encyclopedia/zh/IP%E8%B7%AF%E7%94%B1.html "IP路由")协议，提高IS-IS协议的安全性是保证IS-IS正确路由的基础。IS-IS可以通过配置固定认证算法或密钥的方式对其进行认证，但是固定认证算法和密钥很容易被破解。为了增强IS-IS协议的安全性，可以使用Keychain对IS-IS协议报文进行认证。

如下图所示，需要在每台设备上建立Keychain，然后在IS-IS进程下配置路由域认证和区域认证，同时在接口下配置接口认证，才能实现所有设备之间通过IS-IS协议实现网络互连。

![使用Keychain对IS-IS协议进行认证](https://download.huawei.com/mdl/image/download?uuid=d4a568bc66e9410db3f8e5e945cc5fac "使用Keychain对IS-IS协议进行认证")  
使用Keychain对IS-IS协议进行认证

参考资源

1[Keychain配置指南（CloudEngine S系列交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100458533&id=ZH-CN_CONCEPT_0000001130782708)

2[Keychain配置指南（CloudEngine 数据中心交换机）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100411906&id=ZH-CN_CONCEPT_0000001130782708)

3[Keychain配置指南（NetEngine AR路由器）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100458332&id=ZH-CN_CONCEPT_0000001130782708)

4[Keychain配置指南（USG6000F防火墙）](https://support.huawei.com/hedex/hdx.do?docid=EDOC1100435565&id=ZH-CN_CONCEPT_0000001130782708)

5[华为百科](https://info.support.huawei.com/info-finder/encyclopedia/zh/Keychain.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMjQ3MzI5MzhdfQ==
-->