## RF硬件

### 20. 功率计

#### 20.1 定义、功能与用途

功率计（Power Meter）是射频与微波测试中最基础、最常见的测量仪器之一，主要用于精确测量射频信号或微波信号的平均功率、峰值功率以及包络功率等参数。其核心任务是通过传感器将高频电磁能量转换为可测量的电压或电流，再经过仪表电路或数字处理系统计算出功率大小，以 dBm 或 Watt 为单位进行显示。

在射频测试领域，功率是最直观、最关键的指标之一。功率的准确性不仅决定了发射机是否满足规范要求，也直接关系到接收机的灵敏度校准、放大器的线性度测试、天线的辐射效率以及系统链路预算的可靠性。因此功率计在 **研发、生产、校准、维护** 各环节都有广泛应用。

典型功能包括：

1.  **平均功率测量**：用于连续波（CW）或长期平均信号的测量，是最常见的测试需求。
    
2.  **峰值功率测量**：捕捉脉冲信号、调制信号的峰值，常见于雷达、5G NR、WLAN 等系统。
    
3.  **包络功率与时间分辨**：对调制信号功率随时间变化的曲线进行测量，例如 LTE/5G OFDM 信号。
    
4.  **脉冲参数测量**：测量脉冲宽度、上升时间、下降时间、脉冲重复频率（PRF）等。
    
5.  **功率比与归一化**：通过相对测量方式比较不同通道或不同设备的功率差异。
    

**主要用途**：

-   **发射机功率校准**：验证无线发射设备是否达到标称输出功率。
    
-   **放大器特性测试**：如增益、饱和输出功率、P1dB 点等。
    
-   **天线与系统测试**：测量辐射功率、链路预算参数。
    
-   **生产线检测**：快速验证模块输出功率是否在规格范围内。
    
-   **科研实验**：在通信、雷达、微波加热、医疗设备等多领域作为能量检测的基准工具。
    

功率计在 RF 测试中常被称为“功率的黄金标准（gold standard）”，因为其测量精度通常高于频谱分析仪、网络分析仪中的功率读数。

![NRP2 高精度吸收式射频功率计-R&S NRP2-射频/微波功率计-东方中科][1]

#### 20.2 核心指标

功率计的核心性能指标决定了其适用场景与测量精度，主要包括：

1.  **频率范围**
    
    -   定义：功率计能够准确测量信号的频率范围。
        
    -   常见规格：10 MHz – 6 GHz（通信），可扩展至 40 GHz、110 GHz（毫米波）。
        
    -   影响因素：探头结构、检波器材料。
        
2.  **功率测量范围（Dynamic Range）**
    
    -   通常覆盖 -70 dBm ~ +44 dBm。
        
    -   动态范围越宽，适用信号类型越多。
        
3.  **测量精度（Accuracy）**
    
    -   包括绝对精度（如 ±0.2 dB）、相对精度、线性度。
        
    -   决定能否作为校准基准。
        
4.  **采样速率 / 时间分辨率**
    
    -   高速功率计可达 100 MSa/s，能捕捉亚微秒级脉冲。
        
    -   对于 5G、雷达、UWB 系统尤为重要。
        
5.  **平均 / 峰值检测模式**
    
    -   平均检测适合连续波或 OFDM 信号。
        
    -   峰值检测适合脉冲雷达、突发信号。
        
6.  **输入驻波比 (VSWR)**
    
    -   影响测量不确定度。常见指标 VSWR < 1.1。
        
7.  **接口与软件功能**
    
    -   USB、LAN、GPIB 接口便于自动化测试。
        
    -   支持功率随时间曲线显示、脉冲统计分析。
        
8.  **探头类型**
    
    -   热电探头：高精度、响应慢。
        
    -   二极管探头：快速响应、动态范围大。
        
    -   传输型探头：用于在线监测，不影响链路传输。
        

这些指标综合决定了功率计在 **科研、产线、系统集成** 中的应用价值。


#### 20.3 功率计的分类与对比

根据结构和应用，功率计主要分为以下几类：

### 20.3.1 终端式功率计（Absorptive / Terminating Power Meter）

**原理**：信号通过功率探头被完全吸收并转化为热能或电能，然后换算为功率值。

**特点**：

-   高精度，常用于基准校准。
    
-   不能在信号路径中继续传输。
    
-   适合实验室单点测量。
    

**应用场景**：

-   校准信号源输出功率。
    
-   放大器饱和输出功率测试。
    

**示意图**：
```mermaid
flowchart LR
    A[信号源] --> B[功率探头/传感器]
    B --> C[(吸收终端)]
```

##### 20.3.2 通过式功率计（Through-line / Directional Power Meter）

**原理**：通过耦合器或传输探头，测量链路中流动的功率，同时保证大部分能量继续传输。

**特点**：

-   能实现在线监测，不中断信号。
    
-   可同时测量正向功率与反射功率。
    
-   精度相对低于终端式。
    

**应用场景**：

-   基站、雷达系统在线功率监控。
    
-   天线驻波比（VSWR）测量。
    

**示意图**：
```mermaid
flowchart LR
    A[信号源] --> B[通过式功率计]
    B --> C[天线/负载]
    B -.耦合检测.-> D[测量模块/显示]
```


##### 20.3.3 热电型功率计

**原理**：通过热敏电阻吸收能量，转化为温度升高，再转换为电信号。

**特点**：

-   绝对精度高，可作为校准基准。
    
-   响应时间慢（ms 级）。
    
-   不适合捕捉瞬态脉冲。
    
**示意图**：
```mermaid
flowchart LR
    A[射频信号] --> B[热敏电阻/热电堆]
    B --> C[温度变化 -> 电压]
    C --> D[功率换算 & 显示]
```


##### 20.3.4 二极管检波功率计

**原理**：利用二极管的非线性特性，将 RF 信号整流为直流电压。

**特点**：

-   响应快（ns~μs 级）。
    
-   动态范围宽。
    
-   在低功率下精度受限。

**示意图**：
```mermaid
flowchart LR
    A[射频信号] --> B[二极管检波器]
    B --> C[低通滤波器]
    C --> D[直流电压]
    D --> E[功率换算 & 显示]
```

##### 20.3.5 数字化功率计

现代功率计多采用数字信号处理（DSP）技术，具备：

-   高速采样。
    
-   信号分析（峰值保持、RMS、CCDF 分布）。
    
-   远程控制与数据记录。
    

#### 20.4 功率计对比表

| 类型 | 优点 | 缺点 | 应用场景 |
| ------ | --------------- | ------------ | ------------ |
| 终端式 | 精度高、绝对测量 | 信号被吸收，不可透传 | 校准、单点测量 |
| 通过式 | 在线监测，支持正向/反向功率 | 精度略低，受插入损耗影响 | 基站、系统链路监控 |
| 热电型 | 高精度、频率范围宽 | 响应慢，体积大 | 标准实验室校准 |
| 二极管型 | 响应快、动态范围大 | 低功率精度差，需线性补偿 | 通用测量、脉冲捕捉 |
| 数字化功率计 | 功能丰富，支持自动化、统计分析 | 成本高，对操作有一定要求 | 5G、雷达、复杂信号分析 |


#### 20.5 工程应用实例

1.  **5G 基站产线测试**
    
    -   使用通过式功率计监测基站 PA 输出功率，确保不超标。
        
    -   同时检测反射功率，用于判断天线匹配情况。
        
2.  **雷达发射机功率测量**
    
    -   使用峰值功率计测量雷达脉冲信号峰值。
        
    -   结合时间分辨率测量脉宽、PRF。
        
3.  **实验室校准**
    
    -   使用热电型功率计作为参考基准，校准二极管型探头与信号源输出。
        
4.  **无线终端一致性测试**
    
    -   使用数字化功率计测量 LTE/NR 信号的平均功率与包络波动。
        


#### 20.6 小结

功率计作为射频测试的基础工具，具有精度高、可靠性强的特点，是信号源、放大器、天线等设备测试不可或缺的基准仪表。随着 5G、毫米波与雷达的发展，现代功率计正逐步向 **宽带化、高速化、数字化** 方向演进。

在实际应用中：

-   **终端式功率计**适合校准。
    
-   **通过式功率计**适合在线监测。
    
-   **热电型**提供高精度基准。
    
-   **二极管型**适合快速测量。
    
-   **数字化功率计**则满足复杂信号测试与自动化需求。


[1]:
data:image/jpeg;base64,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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODM2OTg0ODNdfQ==
-->