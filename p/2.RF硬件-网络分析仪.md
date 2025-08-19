## RF硬件

### 19 网络分析仪（Network Analyzer）

#### 19.1. 定义、功能与用途

##### 19.1.1 定义

网络分析仪是一种专门用于测量电路网络频率响应的仪器。它通过向器件端口输入已知的射频或微波信号，并检测反射和透射信号，从而获得被测器件的散射参数，即通常所说的 S 参数。  
按照测量能力的不同，网络分析仪分为两类：  
第一类是 **标量网络分析仪（SNA）**，它只能测量幅度大小，比如增益、插入损耗，但无法提供相位信息。  
第二类是 **矢量网络分析仪（VNA）**，它不仅可以测量幅度，还能同时测量相位，因此可以得到完整的 S 参数矩阵，是射频和微波工程中最常用的一类分析仪。

##### 19.1.2 功能

网络分析仪的功能十分广泛，核心可以概括为“测量反射和透射”。具体来说：

-   它能够测量 **输入端口的回波损耗**，通常表现为 S11 参数，用来判断器件输入端口是否匹配。
    
-   它可以测量 **输出端口的反射**，对应 S22 参数。
    
-   它能够测量 **正向传输特性**，即 S21，常用来描述器件的插入损耗或增益。
    
-   它同样可以测量 **反向隔离**，即 S12，这在双向器件或隔离器件中尤为重要。
    

除了基本的 S 参数，网络分析仪还可以实现更高级的测试功能。例如，它可以显示 **史密斯圆图**，用来观察阻抗轨迹，辅助工程师进行匹配网络设计；它可以计算 **群延迟**，帮助分析信号通过系统时的相位畸变；它还能够结合外部电源和偏置网络，对有源放大器等器件进行小信号增益与稳定性测试。

##### 19.1.3 用途

网络分析仪的用途极其广泛，涵盖了无源器件、有源器件、系统级模块以及科研材料研究。  
在无源器件方面，它用于测试天线的带宽与回波损耗、滤波器的通带与抑制特性、功分器的分配比与隔离度、耦合器的耦合度、射频开关的通断特性等。  
在有源器件方面，它可以评估放大器的小信号增益、输入输出匹配情况，以及混频器的端口隔离性能。  
在系统应用中，它被广泛用于无线通信前端模块、汽车毫米波雷达收发机、卫星通信转发器等领域的综合测试。  
在科研方面，它还可以配合专用夹具，用于测量高频 PCB 材料的介电常数、介质损耗角正切，或是超材料、电磁带隙结构的频率特性。


#### 📘专栏 矢量网络分析仪的 S 参数与史密斯圆图

##### 1. S 参数简介

矢量网络分析仪（VNA）主要用于测量射频器件的 **散射参数（S-parameters）**。

-   **S 参数**描述了射频网络在特定端口的反射与传输特性，是频域分析的核心指标。
    
-   对于常见的 **二端口网络**（如放大器、滤波器、天线），主要有四个 S 参数：
    
    -   **S11**：端口 1 的输入反射系数，反映输入端匹配情况。
        
    -   **S21**：从端口 1 到端口 2 的正向传输系数，常用于表示增益或插入损耗。
        
    -   **S12**：从端口 2 到端口 1 的反向传输系数，常用于表示隔离度或反向增益。
        
    -   **S22**：端口 2 的输出反射系数，反映输出端的匹配情况。
        

##### 2. S21 参数（正向传输系数）

-   **定义**：  
    S21 = b2a1\dfrac{b_2}{a_1}a1​b2​​  
    表示从端口 1 输入的激励波 a1a_1a1​，在端口 2 产生的输出波 b2b_2b2​ 的比值。
    
-   **物理意义**：
    
    -   **无源器件**（滤波器）：S21 表示插入损耗，数值通常小于 0 dB。
        
    -   **有源器件**（放大器）：S21 表示增益，数值可能大于 0 dB。
        
-   **应用场景**：
    
    -   测量滤波器通带和带外抑制。
        
    -   测量功率放大器的小信号增益。
        
    -   测试电缆或连接器的插入损耗。
        

##### 3. S12 参数（反向传输系数）

-   **定义**：  
    S12 = b1a2\dfrac{b_1}{a_2}a2​b1​​  
    表示从端口 2 输入的激励波 a2a_2a2​，在端口 1 产生的输出波 b1b_1b1​ 的比值。
    
-   **物理意义**：
    
    -   对无源、对称器件（如理想电缆），S21 ≈ S12。
        
    -   对有源器件（如放大器），S12 一般远小于 S21，反映**反向隔离度**。
        
-   **应用场景**：
    
    -   放大器稳定性分析（反向耦合过大可能引发自激）。
        
    -   隔离器、环行器的反向隔离性能测试。
        
    -   滤波器的双向特性比较。
        

##### 4. 史密斯圆图（Smith Chart）介绍

###### 4.1 定义

史密斯圆图是一种射频领域常用的坐标图，用于在复平面上直观表示 **阻抗 / 导纳** 与 **反射系数** 的关系。它将复杂的阻抗匹配问题转化为几何图形问题。

###### 4.2 坐标系统

-   **横轴**：实部（阻性分量）。
    
-   **纵轴**：虚部（感性或容性分量）。
    
-   **圆心**：代表匹配点（50 Ω）。
    
-   **外圆**：代表 |Γ|=1（全反射）。
    

###### 4.3 功能

1.  **阻抗匹配**
    
    -   在圆图上可以直观地找到器件阻抗位置。
        
    -   通过移动（加电感/电容/传输线）实现到中心点的匹配。
        
2.  **稳定性与增益圆**
    
    -   绘制稳定性圆和增益圆，帮助放大器设计。
        
3.  **频率响应分析**
    
    -   扫频时，阻抗轨迹会在圆图上形成曲线，反映器件随频率变化的特性。
        

###### 4.4 在 VNA 中的使用

-   测量 **S11** 时，史密斯圆图能直观显示输入端口的阻抗情况。
    
-   学生常见现象：
    
    -   匹配良好 → 曲线靠近圆心。
        
    -   严重失配 → 曲线靠近外圆。
        
    -   感性负载 → 曲线位于上半部分。
        
    -   容性负载 → 曲线位于下半部分。
        

###### 5. 总结

-   **S21** 代表器件的正向传输性能，是滤波器和放大器测量的重点。
    
-   **S12** 代表反向传输性能，尤其在放大器稳定性和隔离器件测试中非常重要。
    
-   **史密斯圆图**是射频工程师必备工具，可以直观地分析阻抗匹配、频率响应和稳定性。


#### 19.2. 核心指标

##### 19.2.1 频率范围

网络分析仪的频率范围决定了它能测量多高的工作频率。  
低端的设备往往从几十千赫兹到几吉赫兹，适用于低频通信系统；主流的实验室网络分析仪则通常覆盖 9 kHz 到 20 GHz 的频率范围，可以满足大多数射频与微波器件的测试需求；更高端的设备则可以通过外接扩展模块，测量到 40 GHz、67 GHz、110 GHz，甚至进入毫米波与太赫兹频段。

##### 19.2.2 动态范围

动态范围是指网络分析仪能准确测量的最大信号与最小信号之间的差值。  
如果动态范围不足，滤波器等器件的带外抑制无法被准确测量。例如，一个高性能滤波器在通带外可能有 80 dB 的抑制，如果仪器的动态范围只有 70 dB，就无法完全展示其性能。  
因此，高端网络分析仪往往具备 120 dB 到 140 dB 的动态范围。

##### 19.2.3 幅度与相位精度

幅度精度通常控制在 ±0.05 到 ±0.1 dB 的范围，相位精度在 ±0.5° 左右。  
这些精度指标在阻抗匹配和相控阵天线设计中尤为关键，因为即便是微小的误差，也会在系统中累积，影响整体性能。

##### 19.2.4 输出功率范围

网络分析仪的输出功率通常可调，范围在 -90 dBm 到 +10 dBm 之间。  
对于小信号器件，需要较低的输出功率以避免非线性失真；而对于某些需要驱动的有源器件，则需要较高的功率。

##### 19.2.5 中频带宽

中频带宽越窄，测量噪声越低，动态范围越大，但扫描速度就越慢。相反，宽带宽能提高扫描速度，但会引入更大噪声。  
工程师通常根据测试需求，在精度与速度之间做权衡。

##### 19.2.6 端口数

常见的网络分析仪为 2 端口，可以测量基本的 S11、S21、S12、S22。  
对于差分器件或更复杂的网络，4 端口网络分析仪更为常见。  
在 MIMO 系统、汽车雷达阵列中，还会使用 8 端口甚至更多端口的网络分析仪。

##### 19.2.7 校准方式

为了保证测量精度，校准是不可或缺的一步。  
最常见的校准方法是 **SOLT**，即短路、开路、负载、直通。  
另一种是 **TRL**，适用于高频 PCB 与微波电路，能获得更高精度。  
现代网络分析仪还支持 **电子校准（ECal）**，用户只需连接一个专用模块，仪器即可自动完成校准，大幅提高效率，特别适合生产线使用。


#### 19.3. 各种网络分析仪的对比

首先，从测量能力来看，标量网络分析仪只能测量幅度，通常用于简单的增益或插入损耗测试，精度较低；矢量网络分析仪则能同时测量幅度与相位，得到完整的 S 参数，适用于高精度的科研和产业应用。  

- 标量网络分析仪
![AV36110标量网络分析仪-成都嘉恒科技有限责任公司][1]

- 矢量网络分析仪
![网络分析仪-网分仪-网络分析测试仪器-是德科技| Keysight][2]

其次，从使用场景来看，台式网络分析仪性能最强，动态范围大，端口数多，适合实验室和生产环境；而便携式或 USB 网络分析仪则体积小巧、成本低廉，虽然性能不及台式机，但在野外测试或快速验证中非常有用。  
- 台式网络分析仪
![网络分析仪| Anritsu 中国][3]

- 便携式网络分析仪
![P500xA 精简系列USB 矢量网络分析仪| 是德科技][4]

再次，从频率覆盖来看，低端设备适合低频通信，中高端设备覆盖微波和毫米波，部分高端型号甚至进入太赫兹波段。  
最后，从价格角度看，标量分析仪和便携式 VNA 成本较低，适合教学与初步研发；高端台式 VNA 则价格昂贵，但在科研与产业中不可替代。


#### 19.4. 示意图

##### 19.4.1 网络分析仪测试系统框图

```mermaid
flowchart TB
    SRC[信号源] --> CPL[定向耦合器]
    CPL --> PORT1[测试端口1]
    PORT1 --> DUT[被测器件]
    DUT --> PORT2[测试端口2]
    PORT2 --> RX[接收机]
    CPL --> REF[参考通道]
    RX --> DSP[矢量处理单元]
    REF --> DSP
    DSP --> DISP[显示/PC分析]
```

##### 19.4.2 S 参数示意

```mermaid
flowchart LR
    P1[Port 1] -->|S21 正向传输| DUT[被测器件 DUT]
    DUT -->|S12 反向传输| P1
    P1 -->|S11 输入反射| P1
    DUT -->|S22 输出反射| DUT
    DUT --> P2[Port 2]
    P2 --> DUT
```

#### 19.5. 矢量网络分析仪（VNA）操作简介

##### 1. 开机与预设

1.  打开电源，等待仪器自检完成。
    
2.  按下 **[Preset]** 键，恢复默认设置，避免之前的残留参数影响测量。
    
##### 2. 校准准备

1.  选择测量端口数（常见为 2 端口）。
    
2.  设置频率范围，例如 1 GHz ~ 3 GHz。
    
3.  设置输出功率，通常从 -10 dBm 到 0 dBm，避免损坏被测器件（DUT）。
    
4.  选择合适的中频带宽（IF Bandwidth），权衡速度与噪声。
    


##### 3. 校准（Calibration）

校准是保证测量精度的关键步骤。常用方法：

-   **SOLT**：Short（短路）、Open（开路）、Load（负载）、Thru（直通），适合同轴测试。
    
-   **TRL**：Thru、Reflect、Line，常用于高频 PCB 电路。
    
-   **ECal**：电子校准模块，操作最简便。
    

操作流程：

1.  按下 **[Cal] → [Calibrate]**。
    
2.  依次连接标准件（短路、开路、负载、直通），仪器会自动记录误差。
    
3.  校准完成后保存，屏幕显示 “Calibration Done”。
    


##### 4. 连接 DUT

1.  用扭矩扳手连接 DUT，避免 SMA 或 K 接口损坏。
    
2.  确认端口编号（Port1 为输入，Port2 为输出）。
    
3.  确认偏置要求（如果 DUT 为有源放大器，需要直流电源和偏置网络）。
    


##### 5. 测量与显示

1.  选择要显示的参数：
    
    -   **S11**：输入端反射，常用来判断阻抗匹配。
        
    -   **S21**：正向传输，常用来测增益或插入损耗。
        
    -   **S12 / S22**：反射与反向隔离。
        
2.  选择显示格式：
    
    -   **Log Mag（dB）**：常用于增益或损耗。
        
    -   **Smith Chart**：用于阻抗匹配分析。
        
    -   **Phase（°）**：用于相位响应分析。
        
    -   **Group Delay**：用于系统相位畸变分析。
        
3.  扫描并观察曲线，记录数据。
    


##### 6. 保存与导出

1.  保存截图或触摸屏数据。
    
2.  导出测量曲线（CSV、Touchstone S2P 文件）。
    
3.  用仿真软件（ADS、HFSS、Matlab）进一步分析。
    


##### 7. 注意事项

-   不要输入超过 +30 dBm 的高功率信号。
    
-   每次更换频率范围或端口，应重新校准。
    
-   避免弯折测试电缆，保持稳定连接。
    
-   长时间测量时，应考虑温度漂移对精度的影响。
    
##### 📌 总结：  
VNA 的操作流程可以概括为 **预设 → 设置频率功率 → 校准 → 连接 DUT → 测量与显示 → 保存结果**。熟悉这几个步骤，就能完成天线、滤波器、放大器等器件的常规测试。

```mermaid
flowchart TB
    A["开机 & 预设"] --> B["设置频率/功率/带宽"]
    B --> C["校准 (SOLT / TRL / ECal)"]
    C --> D["连接 DUT (被测器件)"]
    D --> E["选择测量参数 (S11 / S21 / S12 / S22)"]
    E --> F["选择显示格式 (dB / Smith 圆图 / 相位 / 群延迟)"]
    F --> G["观察曲线 & 记录数据"]
    G --> H["保存结果 & 导出文件"]
```

#### 19.6. 使用注意事项

1.  不要让高功率信号（通常高于 +30 dBm）直接输入仪器，否则会损坏前端。
    
2.  测量不同频段、不同接口时，必须重新校准。
    
3.  在连接 SMA 或 K 型接头时，应使用力矩扳手，避免过紧或过松。
    
4.  测试过程中保持环境温度稳定，避免因温漂影响精度。
    

#### 19.7. 总结

网络分析仪是射频测试的核心仪器。它通过 S 参数测量，使工程师能够深入理解电路器件的电磁特性。从天线到滤波器，从放大器到整机系统，几乎所有射频器件的性能评估都依赖网络分析仪。  
随着 5G、6G、毫米波和卫星通信的发展，网络分析仪正不断朝着更高频率、更大动态范围、更多端口和更强自动化的方向演进。  
掌握网络分析仪的使用，不仅是射频工程师的基本功，更是进入高频通信领域的必修课。

[4]:
data:image/jpeg;base64,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

[3]:
data:image/jpeg;base64,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

[2]:
data:image/jpeg;base64,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


[1]:
data:image/jpeg;base64,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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQwNjQwNjk1M119
-->