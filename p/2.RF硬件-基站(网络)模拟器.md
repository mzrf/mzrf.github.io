## RF硬件

### 18. 网络模拟器、基站模拟器

在无线通信系统的研发、测试和教学中，网络模拟器与基站模拟器是极为重要的两类测试设备。它们能够在实验室或产线环境中重建真实的蜂窝网络条件，使被测设备（Device Under Test, DUT）无需接入运营商的商用网络，即可完成注册、呼叫、数据传输、切换等操作。这类设备的引入不仅大幅降低了研发与测试成本，同时也提升了实验的可控性和可重复性。

随着 2G/3G 向 4G/5G 演进，网络架构日趋复杂，终端类型也更加多样化（智能手机、物联网模组、车联网终端、可穿戴设备等）。因此，对网络模拟器与基站模拟器的需求也越来越多样：既要满足科研级别的深度协议测试，又要支持生产线上快速的功能验证。

#### 18.1 定义、功能、用途

##### 18.1.1 网络模拟器的定义与功能

网络模拟器（Network Simulator）是一种通过软硬件结合的方式，完整再现蜂窝通信网络的设备。它能够仿真基站（eNodeB/gNodeB）、核心网（EPC/5GC）、IMS子系统，甚至包括业务层应用，从而为被测终端提供一个接近真实网络的实验环境。

-   **定义**：  
    网络模拟器是模拟蜂窝网络端到端结构的综合测试平台，涵盖接入网、核心网和业务层。
    
-   **主要功能**：
    
    1.  **接入功能**：支持终端的注册与鉴权。
        
    2.  **呼叫与会话**：支持语音（VoLTE/VoNR）、视频、数据业务。
        
    3.  **移动性管理**：切换、漫游、多小区并发测试。
        
    4.  **信道仿真**：多径衰落、噪声、干扰、用户移动速度。
        
    5.  **业务层仿真**：FTP下载、网页浏览、视频流传输、IoT数据包。
        
-   **主要用途**：
    
    -   研发阶段：协议一致性、互操作性、功能验证。
        
    -   运营商认证：GCF、PTCRB一致性测试。
        
    -   学术研究：新型网络架构与协议算法评估。
        
    -   教学实验：向学生展示蜂窝网络端到端工作过程。
        

##### 18.1.2 基站模拟器的定义与功能

基站模拟器（Base Station Simulator，也称 Call Box）侧重于模拟单个或少量基站的功能，尤其是空口协议部分。与网络模拟器相比，它通常不具备完整的核心网，但能够直接与终端建立无线链路，并完成基本的信令交互。

-   **定义**：  
    基站模拟器是一类模拟基站无线接入功能的测试设备，用于验证终端的射频和协议功能。
    
-   **主要功能**：
    
    1.  **射频链路建立**：通过空口与终端同步、接入。
        
    2.  **信令流程**：注册、鉴权、呼叫建立与释放。
        
    3.  **基本数据通信**：支持语音呼叫、短信、简单数据连接。
        
    4.  **多频段支持**：不同频率下的发射接收测试。
        
-   **主要用途**：
    
    -   生产线测试：验证手机/模组的呼叫、短信功能。
        
    -   射频一致性：测试功率、灵敏度、调制精度。
        
    -   研发验证：验证芯片或终端的基本接入能力。
        

##### 18.1.3 网络模拟器与基站模拟器的区别

-   **覆盖范围不同**：网络模拟器包含接入网 + 核心网；基站模拟器主要是接入网。
    
-   **复杂度不同**：网络模拟器能仿真复杂场景；基站模拟器更简洁高效。
    
-   **应用场景不同**：网络模拟器适合研发、认证；基站模拟器更常见于产线。

#### 📘 专栏：为什么要使用模拟器而不是真实基站？

在无线通信测试中，很多学生常常会提出一个疑问：**既然我们最终是要接入运营商的真实基站，为什么实验和测试阶段不直接使用商用基站，而要引入复杂且昂贵的网络模拟器/基站模拟器呢？**

**原因主要有以下几点：**

1.  **可控性**
    
    -   商用基站的配置由运营商控制，频段、功率、切换策略无法调整。
        
    -   模拟器可以完全控制网络参数（频率、带宽、信道模型），实验可重复。
        
2.  **安全性**
    
    -   在真实网络中进行实验，可能干扰普通用户，甚至违反法规。
        
    -   模拟器运行在实验室的封闭环境，数据与信号不外泄，安全可控。
        
3.  **成本与效率**
    
    -   部署多个真实基站成本极高，还需运营商授权。
        
    -   一台模拟器即可支持多制式/多频段，切换灵活，效率更高。
        
4.  **测试覆盖范围**
    
    -   真实基站无法人为制造极端情况（弱覆盖、掉话、多径衰落）。
        
    -   模拟器能灵活重现各种复杂环境，验证终端极限性能。
        
5.  **认证需求**
    
    -   国际认证（GCF、PTCRB）和运营商入网测试要求 **可控、可复现的环境**。
        
    -   只有模拟器能满足这些标准化需求。
        
6.  **研发阶段必需**
    
    -   新标准（如 5G/6G）商用基站尚未普及，研发早期必须依赖模拟器。


#### 18.2 核心指标

在评价一台网络模拟器或基站模拟器时，工程师通常会从以下几个维度考量：

1.  **支持的通信制式**
    
    -   2G: GSM/GPRS/EDGE
        
    -   3G: WCDMA, CDMA2000
        
    -   4G: LTE, LTE-Advanced, NB-IoT, eMTC
        
    -   5G: NR FR1 (Sub-6GHz), NR FR2 (mmWave)
        
    -   特殊：未来的 6G 架构探索
        
2.  **协议栈完整性**
    
    -   是否内置核心网功能（EPC/5GC）。
        
    -   是否支持 IMS/VoLTE/VoNR。
        
    -   是否可模拟多小区与异系统切换（LTE→NR）。
        
3.  **频段与带宽支持**
    
    -   网络模拟器：典型支持 1.4–100 MHz，5G 可达 400 MHz。
        
    -   基站模拟器：覆盖常见商用频段，如 LTE Band 1/3/7/20。
        
4.  **射频性能指标**
    
    -   输出功率范围：从 -120 dBm 到 +20 dBm。
        
    -   信号质量：EVM（误差矢量幅度）、ACLR（邻道功率比）、相位噪声。
        
5.  **信道与干扰仿真能力**
    
    -   能否模拟瑞利衰落、多普勒频移。
        
    -   是否支持噪声注入、邻频干扰。
        
6.  **自动化与可扩展性**
    
    -   支持脚本控制（Python、C#、LabVIEW）。
        
    -   提供远程 API。
        
    -   可升级到最新标准版本（如 3GPP Rel-17/18）。
        
7.  **应用级别仿真**
    
    -   是否支持 FTP、HTTP、VoIP 测试。
        
    -   是否支持 QoS、时延抖动、丢包率测量。
        


#### 18.3 各种模拟器对比

##### 18.3.1 网络模拟器典型设备

-   **Keysight UXM 5G**：支持 5G NR SA/NSA，集成完整核心网，适合一致性与互操作性测试。
    ![5G Wireless Test Platforms | Keysight][1]
    
-   **Rohde & Schwarz CMW500**：经典多制式平台，从 2G 到 5G，既可作为网络模拟器，也可配置为基站模拟器。
    ![CMW500 wideband radio communication tester | Rohde & Schwarz][2]
    
-   **Anritsu ME7834**：常用于 PTCRB/GCF 协议一致性认证。
    ![Anritsu ME7834NR][3]

##### 18.3.2 基站模拟器典型设备

-   **LitePoint IQcell**：专注产线快速测试，提供多终端并行接入。
![IQcell-5G Signaling Callbox Test Solution - LitePoint][4]
    
-   **R&S CMW100**：简化版 Call Box，适用于大规模生产测试。
    ![CMW100 | Leasametric][5]
    
-   **鼎桥、展锐定制版本**：结合本地运营商需求，支持 NB-IoT 和 eMTC。
    

##### 18.3.3 二者对比表述

-   **网络模拟器**：全面、复杂、价格高，常用于研发与认证。
    
-   **基站模拟器**：简洁、快速、成本低，常用于量产与基础验证。
    

#### 18.4 示意图与应用场景

##### 18.4.1 示意图

```mermaid
flowchart LR
    subgraph 网络模拟器
        A1[接入网 eNodeB/gNodeB]
        A2[核心网 EPC/5GC]
        A3[IMS/应用层]
    end
    subgraph 基站模拟器
        B1[空口仿真模块]
    end
    UE[终端设备 UE/IoT模块]
    A1 --> UE
    A2 --> A1
    A3 --> A2
    B1 --> UE
```

##### 18.4.2 应用场景

-   **研发实验室**：新型协议验证、切换与载波聚合测试。
    
-   **产线工厂**：快速验证手机的呼叫、数据功能。
    
-   **运营商认证**：一致性测试、互操作性测试。
    
-   **教学科研**：演示网络结构，验证学生实验。
    


#### 18.5 常见问题与发展趋势

##### 18.5.1 常见问题

1.  **终端无法注册**：通常与鉴权参数设置、核心网配置有关。
    
2.  **信号质量不稳定**：需检查射频线缆与隔离环境。
    
3.  **协议版本不兼容**：需确认设备是否支持最新 3GPP Release。
    

##### 18.5.2 发展趋势

-   **向 6G 过渡**：支持 THz 频段、智能表面、多链路。
    
-   **软件化与虚拟化**：利用云平台运行核心网功能。
    
-   **AI 驱动测试**：智能选择场景、自动化结果分析。
    

#### 18.6 总结

网络模拟器与基站模拟器是射频与通信测试领域的两大核心设备。前者偏重于完整网络环境的重建，后者偏重于空口和快速接入。在研发、认证、生产、教学等不同场景中，工程师会根据需求选择合适的设备。随着 5G NR 和未来 6G 的发展，网络/基站模拟器将继续演化，承担更重要的角色。


[5]:
data:image/jpeg;base64,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

[4]:
data:image/jpeg;base64,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

[3]:
data:image/jpeg;base64,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

[1]:
data:image/jpeg;base64,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

[2]:
data:image/jpeg;base64,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
<!--stackedit_data:
eyJoaXN0b3J5IjpbODU4MzYyODY2XX0=
-->