# IEEE 802.11 Wireless 
> Keysight Technologies LAN PHY Layer (RF) Operation and Measurement
## Introduction
This application note is written for those who desire an understanding of
the test system configuration and testing of Wireless LAN (WLAN) devices
and some of the issues that arise in connection with it. Further detail on
many of the topics covered herein may be found in the Appendices.

The use of wired Local Area Networks has become ever more commonplace, even in situations where only a few computers need to be connected together. Price reductions have helped stimulate use and so have easier system configuration and increasing robustness.

A number of applications can benefit from the removal of the cable connections needed by a fixed LAN. Remote database access is a good example – from warehouses to retail stores to college campuses. WLAN cards will also be used soon for public Internet access in certain "hotspots," such as airports and hotels, where users are largely stationary and need access to a variety of medium- and high-speed digital services.

The IEEE 802.11 Wireless LAN specification was written to extend the functionality provided by the IEEE 802.3 Wired LAN standard. A radio interface
adds considerable complexity; however, advances in highly integrated radio circuitry have made it possible to bring the cost of wireless devices down to affordable levels.

The ETSI BRAN HiperLAN/2 is an alternative specification for WLAN, with more extensive services, but diminishing commercial support. Its radio frequency (RF) operates in a similar way to 802.11a, although the allocation of transmission time-slots is quite different. Increasing collaboration is now taking place between those involved in the two standards.

While wired LAN already uses numerous techniques to deal with multiple users who must access a central server, additional steps must be taken to deal with the vagaries of WLAN links. A WLAN link has many less-than-ideal transmission characteristics, such as the dependency of signal errors on physical position and the ability of nearby RF devices to "eavesdrop" or interfere.

Security is always an important issue in radio transmissions. Considerable effort is being made to ensure that security for WLAN is both adequate and straightforward to apply.

This application note begins with a brief description of an IEEE 802.11 Wireless LAN system, emphasizing the radio or physical layer. Consistency at this level provides the basis for widespread device interoperability.

Comparisons are made to cellular radio systems to highlight the significant differences in the operation of the two links. Transmitter and receiver measurements needed to verify conformance with the IEEE specification are described, along with information on how to set up the Device Under Test (DUT) and the test equipment. Appropriate equipment from Keysight Technologies, Inc. is highlighted in Appendix A. Finally, Appendices B and E provide a wide range of reference and learning material.

## 1. Basic Concepts Of IEEE 802.11 Wireless Lan
As the name implies, Wireless LAN was designed to extend the data transfer function of a Wired LAN. The heritage is important—standards which define how it works continue to evolve, but at its heart, WLAN is a system for transferring packets of digital data wirelessly and without error whenever an originating computer can send them. In this respect, it is like an asynchronous Bluetooth link but unlike a synchronous cellular voice connection, which is based on analog transmission. Transmissions take place after a device has first listened to make sure the channel is clear, a method called Carrier Sense Multiple Access/with Collision Avoidance (CSMA/CA). It is fundamentally different from the rigorous timeslot allocations used in cellular and cordless phones. This may cause confusion for engineers migrating from other technologies. 

Software is used to adapt LAN packets for transmission over the radio path, which, of course, is far less predictable than a wired path. This protocol is called Logical Link Control (LLC) and Medium Access Control (MAC). User data is encoded, headers are added, and longer packets are broken up (fragmented) before transmission.

The most widely used WLAN systems involve Network Interface Cards (NICs, also referred to as STAtions), and Access Points (APs). These allow the users to create individual wireless-to-wired LAN links, called Infrastructure Basic Service Sets, or BSS. An Extended Service Set (ESS) entails the construction of a complete network. The access point acts not only to transfer data from wired to wireless devices, but is also responsible for allocation of the radio channel to the clients it serves.

In the absence of other users in the license-exempt bands used by WLAN, a BSS can be configured to make efficient use of the radio spectrum. Even in this situation, throughput for individual users is usually only a fraction of the peak data rates which WLAN systems are known by. Typically, the maximum throughput is half the nominal peak rate and drops even more as clients are added (there may be no predetermined limit), or as the NIC moves away from the Access Point. Coverage depends on both the physical environment and the frequency band; however, in many cases the transfer time for a file over WLAN will be as low as that of a wired LAN because of bottlenecks occurring elsewhere.

Two other WLAN schemes exist. A Peer-Peer (ad hoc) Independent Basic Service Set, or IBSS, involves the use of two NICs. Interoperability between such cards may be limited due to different vendor designs, but otherwise this can be one of the most straightforward ways of effecting wireless data transfer between mutually friendly devices. Extenders are more specialized system components which deal with radio propagation problems while not acting as specific network end-points.

### 1.1 Use of Radio Carriers and Modulation
Radio is not the only medium addressed by the 802.11 specification, but it will be the focus of this application note.

Data must be applied to a radio carrier before transmission. The carrier can be used in several ways:

#### 1.1.1 Modes of Carrier Operation

– FHSS – Frequency Hopping Spread Spectrum

>A single carrier switches frequency to reduce the likelihood that it will interfere with, or be interfered by, other carriers.

– DSSS – Direct Sequence Spread Spectrum
> The energy in a single carrier is spread over a wider spectrum by multiplying data bit(s) with a special 11-bit pattern, called a Barker key. This is done at a chip rate of 11 MHz. This technique can help reduce interference from narrow-band sources. The IEEE 802.11b-1999 specification uses an 8-bit key.
Two schemes are used by 802.11b to spread the spectrum of a single carrier. CCK (Complementary Code Keying) is mandatory, while PBCC (Packet Binary Convolu-tional Coding) may be added. Channel agility may also be added as an option.

– CCK – Complementary Code Keying
> This is used to increase IEEE 802.11b's peak data rate from 2 to 11 Mbps, while still using QPSK (Quadrature Phase Shift Keying) modulation. It does this by first increas-ing the data clock rate (symbol rate) from 1 Mbps to 1.375 Mbps, then taking data in 8-bit blocks (8*1.375 = 11). Six of the 8 bits are used to choose 1 of 64 complemen-tary codes, which are 8 chips long and clocked out at 11 MHz. Thus all 8 chips are "used up" in (1/1.375) µs – the time before another byte is ready. The other 2 bits are combined with the code in the QPSK modulator.

– PBCC – Packet Binary Convolutional Coding
> This scheme is optional for IEEE 802.11b and g. It makes use of Forward Error Correction to improve the link performance when noise is the limitation. Scrambled data is fed into a convolutional encoder. The encoder consists of a 6-stage memory, with specific taps combined to give two outputs. The four possible output states (00,01,10,11) are mapped into two possible QPSK states (11 Mbps). A codeword controls how the chosen state alternates over time. The RF modulator is driven from this point. IEEE 802.11a, HiperLAN/2 and HiSWAN use OFDM.

– OFDM – Orthogonal Frequency Division Multiplexing
> OFDM uses multiple carriers, of which there are 52, spaced 312.5 kHz apart. Data is sent on 48 carriers simultaneously, with 4 used as pilots. The time to transmit each bit increases in proportion to the number of carriers. This makes the system less sensitive to multi-path interference, a major source of distortion. This note concentrates only on DSSS and OFDM systems. Some systems, such as 802.11g, may use both methods during the same RF burst, making them more compatible with 802.11b systems.

– Modulation

> The RF carrier(s) must be modulated. All the WLAN systems described in this note use a form of phase-shift keying for the preamble. More complex schemes, such as 64QAM (Quadrature Amplitude Modulation) give faster bit rates for user data, but06 | Keysight | IEEE 802.11 Wireless LAN PHY Layer (RF) Operation and Measurement – Application Note require better radio performance and less noise to work to their full potential. BPSK (Phase Shift Keying), QPSK, and QAM are described in standard RF texts.
Often, the modulation format changes during the transmission. This is because the early part of the burst contains important information about the burst, includ­ ing analog characteristics such as frequency, and digital information such as burst length. Simpler modulation formats are less prone to bit errors, and thus are more suitable to use early in a burst.

#### 1.1.2 Frequency Bands and Power Levels

WLAN systems operate in one of the frequency bands shown in Figure 1 below. The maximum transmit powers are also shown. Transmit Power Control and Dynamic Frequency Selection, part of the HiperLAN/2 specification, will be added to 802.11a operation to satisfy Euro­ pean regulatory requirements.

![2.4G](https://d2cpnw0u24fjm4.cloudfront.net/wp-content/uploads/2020/04/29163126/2.4GHz-Unlicensed-Spectrum.png)

![5G](https://d2cpnw0u24fjm4.cloudfront.net/wp-content/uploads/2020/04/29163246/5GHz-Unlicensed-Spectrum.png)

### 1.2 Anatomy of a WLAN device

Physically, the most common format of a WLAN device is that of a PC Card (PCMCIA), suitable for direct connection to a laptop computer. Access points may simply have a PC Card mounted on a motherboard.

Electrically, the WLAN card is split into two major sections: the analog RF (PHY layer) and digital Baseband (MAC, or Medium Access Control) processing. The connection to the host computer is generally through the PC Card or Compact Flash interface. In an access point, additional digital circuitry is used for the interface with a wired LAN (i.e., via Cat 5/Cat 6 cabling). Some designs provide power from the LAN wiring rather than from a separate power supply.

#### 1.2.1 Description of Operation

Figure 2 below is a generic block diagram of a radio system. As with most electronic systems, newer radio designs have higher levels of integration, although performance trade-offs must be made. This applies particularly to the receiver. Some systems will not use, or provide access to, the intermediate signals discussed in this note. Readers are advised to carefully study the block diagram of the system they must test.

The Local Oscillators (LOs) share both transmit and receive functions. Frequency doubling or tripling is used (although not shown in the diagram) to give better Voltage Controlled Oscillator (VCO) performance and to isolate the RF output from other signals.

#### 1.2.2 Data Reception

Diversity reception is used to reduce the effect of nulls on signal levels. A Receive Signal Strength Indication (RSSI) test, made during the short training sequence, determines which path is switched in for a particular burst. The chosen signal is fed through an amplifier/downconversion chain before being mixed into a pair of quadrature signals which are digitized. Analog gain control means that 6 to 8 bits is usually sufficient for the A/D conversion. Some hybrid schemes use DSP (Digital Signal Processing) for the IQ (In-phase Quadrature) separation and therefore need only a single connection from the analog circuit

![](https://www.analog.com/en/_/media/analog/en/landing-pages/technical-articles/simple-baseband-processor-for-rf-transceivers/figure1.jpg?la=en&rev=20d4609132dc40f1a8383024d63f7c8a&sc_lang=en)

An equalizer and other components of digital circuits are able to reduce the effect of distortions such as frequency error or amplitude variations, but the design itself must ensure that others errors—such as high-frequency local oscillator phase noise—are low enough to guarantee the needed link performance.

The RF portion of 802.11b, which is difficult to make small and inexpensive, is not so challenging in terms of Bits/Hz. However, the higher data rates of 802.11a and the doubling of channel frequency make it far more difficult to design and manufacture.

Receiver sensitivity is important because it determines the maximum range over which a WLAN link can operate. There are secondary system benefits as well. If one link completes a transmission faster than another because the Packet Error Rate is lower, battery consumption will be reduced and less interference will occur to other users. In a real-world Industrial, Scientific and Medical (ISM) or Unlicensed Nation­ al Information Infrastructure (UNII) environment, interference suppression and linearity will directly affect the performance of the radio. They are therefore important test parameters. It may be more difficult to distinguish between causes of poor performance as hardware becomes more and more integrated and if special test modes are not available.

#### 1.2.3 Data Transmission

Transmitter performance requirements usually necessitate an external power amplifier (PA). Cost, current consumption, and linearity combine to demand considerable attention to detail in this choice. Pre-distortion of the signal from Baseband processing may allow less stringent PA design, but it may also limit the choice of devices used if it relies heavily on a particular performance characteristic. Diversity transmission may also be applied (the switching in Figure 2 does not allow for this).

Designs with SAW (Surface Acoustic Wave) or Dielectric Bandpass filtering in the IF (Intermediate Fre­ quency) are suited to normal TDD (Time Division Duplex) operation, but also have fewer options for internal loop-back paths for testing and self-calibration. Self-calibration becomes important when the performance of the analog circuit is affected by temperature.

Differential signal paths are becoming more common as power supply and signal voltages decrease and background noise becomes more prominent. Balun transformers can be used when single-ended signals are needed.

Although the analog hardware can be tested in isolation, it needs to be combined with DSP (Digital Signal Processing) of the Baseband circuit in order to comprise a complete transceiver. Care is needed when modeling total system performance because a number of error contributions may not be just simple arithmetic additions, but result from analog and other phenomena.

Algorithms within the DSP play an essential role in both transmission and reception. Figure 3 shows an example of the main processing blocks needed for 802.11a/ OFDM system.

### 1.3 Time Division Duplex and Frame Structure

A WLAN device can only transmit or receive at a single time. Trans­ missions occur as bursts (frames) which vary in length and spacing, usually in the range of a few hundred microseconds to one milli­ second. The 802.11b CCA (Clear Chan­ nel Assessment) receiver test specifies the longest possible 5.5 Mbps frame—3.65 ms.

The basic structure of the frames is shown in Figures 4 and 5. The preamble is used by the receiver to adapt to the input signal. This may involve frequency and phase error equalizing, as well as time alignment. The header contains a wealth of information, including the destination address and the format of the remainder of the burst. User data is transferred from the original packets, which are fed into the MAC layer. Long packets may be fragmented (broken up) if the radio determines that this will improve link performance.

Five time periods in the 802.11 specification determine the spacing between transmissions. The physical values vary according to the standard used and are shown in Table 2.

The combined effect of using CSMA/ CA, data which is sent when ready and different time intervals between frames, is to produce seem­ ingly random spacing between bursts.

### 1.4 The Medium Access Control Layer

The Medium Access Control (MAC) layer provides an asynchronous data packet delivery service to the LLC software that uses it. This means that it is impossible to predict exactly when transmissions will take place. The MAC software takes the data and, identifying the PHY layer with which it is working, transports the data to the MAC layer software in the client’s receiver. Three types of MAC Frames are used to provide this service:

– Management Frames

> Eleven sub-frame types are used for link management. They provide the means for establishing and terminating a link—beacon transmission and probe requests, authentication, and association.

– Control Frames

> Six sub-frame types are used to make sure the link functions correctly: Request To Send, Clear To Send, ACKnowledged, Power Save, Contention Free, and $CF – End + CF–Ack$.

– Data Exchange Frames

> Eight sub-frame types are used and all except one contain user data. Most of them make the link more efficient by adding link control information. Figure 6a (below) shows how these frames are used (not to scale). Figure 6b shows the major frame timing options.


### 1.5 Establishing Contact

Starting when a device is powered up, software above the MAC layer must stimulate the device to establish contact. Either active or passive scanning is used. The IEEE specification allows for different implementations, so characteristics may differ between devices.

#### 1.5.1 Active Scanning

Active Scanning is the fastest way to establish contact, but consumes more battery power. Listening for a clear channel, the device which seeks to establish contact sends a Probe Request. If the Service Set IDentity matches, the recipient then sends a Probe Response. The scanning device uses this information to decide whether or not it will join the (I)BSS, but there is no further transmission at this point.

#### 1.5.2 Passive Scanning

In Passive Scanning, Beacons and Probe Requests are used. After selecting a channel, the scanning device listens for Beacons or Probe Requests from other devices. A Beacon is transmitted from an Access Point in a BSS or ESS. It contains information about the AP and a timing reference. Beacon transmissions occur on a 1024µs time grid, spaced roughly every 100ms. Like other transmissions, they are subject to a clear channel test and so may be delayed.

#### 1.5.3 Authentication

Before any user data is transferred, the Sender and Receiver must agree that they are ready to talk. These are processes of authentication (which happens first) and association. There are several others (e.g., random exponential transmission back-off) which can be used if a device finds that the channel is not clear when it is ready to transmit.

Earlier, a list of modulation rates was shown for the different 802.11 standards. The specifications do not define exactly how these are selected. Different designs will employ different proprietary algorithms. Currently, there is no "qual­ ity of service" standard in the MAC frames. However, the transmitting device is able to gauge the fidelity of the link based on the regularity of ACK frames coming back from the device it is seeking to contact.

### 1.6 Exchanging Data: Two Methods

When two WLAN devices are ready to exchange data, they must choose one of two methods. The decision depends on the expected performance of the radio link.

#### 1.6.1 Two-step Exchange

Two-step data exchange is simply the sequence:

– Send
– Acknowledge

This is good for short packets or a sparsely-used RF environment.

#### 1.6.2 Four-step Exchange

More typically, however, exchange is a four-step process:

– Request To Send (RTS)
– Clear To Send (CTS)
– Send
– Acknowledge

This is used for long frames, where there is a higher likelihood of interference with, or from, an RF-noisy environment. A special MAC signal (dot11RTSThreshold) is used to choose between frame lengths.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjUyOTU0MDgyXX0=
-->