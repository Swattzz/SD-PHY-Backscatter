# SD-PHY Backscatter
 First backscatter tag that realizes software-defined PHY
## Overview
SD-PHY backscatter is the first backscatter tag that realizes a software-defined PHY. It means that it can communicate with different PHY protocols even without hardware modifications. Just calculating a few PHY parameter values and write to the tag, it can move to another PHY protocol in an online manner, no restart is requested. So far, it supports Wi-Fi (802.11b/g/n), BLE (Bluetooth Low Energy), LoRa (Long Range) and LTE (Long-term Evolution). Besides, it supports customized PHY protocols like OFDMA backscatter [PDF] and Distributed CSS [PDF]. It can support other protocols as long as you find appropriate PHY parameters values and write to it.
![SD-PHY tag](./images/SDPHYtag.png | width=100)
## Hardware platform
SD-PHY hardware platform is made open-source. The PCB hardware is designed using Altium Designer 19. You can download the schematics as well as the layout files in this project.
## Firmware
SD-PHY is featured by its generic baseband design. The whole baseband is realized in a low-power FPGA by GOWIN Inc. The binary file to be burnt into the FPGA can be downloaded in this project.
## Our academic paper
Our academic paper of SD-PHY backscatter is published in ACM MobiSys '22. [PDF]
To use our SD-PHY platform in your research, please cite our paper in your work. An ACM reference format should be: [to be editted].
## Main Contributors
* Fengyuan Zhu (jsqdzhufengyuan@sjtu.edu.cn)
* Ouyang Mingwei (1999mrou@sjtu.edu.cn)
* Luwei Feng (yundanfengqing@sjtu.edu.cn)
* Yaoyu Liu (lyyu19@sjtu.edu.cn)