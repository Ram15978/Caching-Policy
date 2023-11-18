# Cache-Policy

## Environment 
����ϵͳ��Ubuntu 20.04.4 LTS
��������Cortex-A55
�ڴ棺3.6 GiB


## caching policy
password: odroid

fifo-lfu-lru
https://github.com/vpetrigo/caches

fifo-lfu
https://github.com/solangii/caches

LIRS
https://github.com/374576114/cache
https://blog.csdn.net/z69183787/article/details/105534151

ARC
https://github.com/Xiaoccer/ARC_Cache
https://github.com/anuj-rai-23/Adaptive-Replacement-Cache-ARC-Algorithm

Clock-Pro
https://github.com/maximecaron/ClockProCPP

## Trace
### [Nexus5_Kernel_BIOTracer_traces - Nexus 5 Smartphone Traces](http://iotta.snia.org/traces/block-io)
sample: log106_Messaging.txt
- ��0: access��ʼ��ַ����λΪ����
- ��1: ˵����СӦ����ʱ��Ϊ8����Ϊ�������С��4kb��8����������mmc������������˶����������һЩ��С���������Ҫ��������
- ��2: ���ʴ�С�����ֽ�Ϊ��λ��
- ��3: ��������&�Ƿ�ȴ�:���λ��ʾ����д(0��ʾ����1��ʾд)������λ��ʾ�����Ƿ�ȴ�(4��ʾû�еȴ���0��ʾ�Ѿ��ȴ���һ��ʱ��)
  ���磬5��ʾ������һ��д���������ڴ���֮ǰû�еȴ�����������󵽴�ʱ�����ǿյġ�
- ��4: ��������ʱ��(�������ɲ����뵽�������)��
- ��5: ������ʼʱ��(MMC����������������ȡ�����󲢿�ʼ����)
- ��6: ��Ӳ���ύ�����ʱ��(����������Ӳ�����������ʱ��)
- ��7: �������ʱ��(������ɺ���ûص�������ʱ��)

### [Traces �C Smartphone](http://visa.lab.asu.edu/web/resources/traces/)
http://visa.lab.asu.edu/web/resources/traces/traces-smartphone/

sample: mobi.trace.1

ref: Q. Yang, R. Jin, and M. Zhao, ��SmartDedup: Optimizing Deduplication for Resource-constrained Devices,�� Proceedings of USENIX Annual Technical Conference (USENIX ATC ��19), July 2019.

### [MobileAppTraces](https://astl.xmu.edu.cn/appdedupe.html)
The trace file-names are indicating different mobile applications and some file-names also include the running hours. Each record in the trace files is as follows: 
[Time in s] [R or W] [LBA] [size in 512 Bytes blocks] [pid] [process] [MD5 per 4096 Bytes]
sample:
7.430000743 	R	     1548752	        24	       744	       Binder_5	fb0ece031db8f58df6849c2211df8c5a-35598db6787678b2acf4d0fc056f3b1d-9fc4e51c5541ecaeefc9da9e7cc55587

ref: Bo Mao, Suzhen Wu, Hong Jiang, Xiao Chen, and Weijian Yang. Content-aware Trace Collection and I/O Deduplication for Smartphones. In Proceedings of the 33rd International Conference on Massive Storage Systems and Technology (MSST'17), Santa Clara, CA, USA, May 15-19, 2017.
### config
> ��С��Ŀ¼�ṹ����
> - Caching-Policy
>   - src
>   - storage
>   - trace

#### ��Windowsϵͳ����
1. ��`trace`�ļ��з����Ӧ��trace�ļ�����`trace.txt`�����޸�`src/utils/config.h`�е�`TRACE_PATH`��`DISK_SIZE`��`CHUNK_NUM`
2. ��`storage`�ļ��з����Ӧ��storage�ļ�����5����`disk.bin`, `cache_0.02.bin`, `cache_0.04.bin`, `cache_0.06.bin`, `cache_0.08.bin`, `cache_0.1.bin`

## create disk patition
fdisk -l
fdisk /dev/mmcblk0
```
n
p
1
2048
w
```
mkfs -t ext4 /dev/mmcblk0p1
sudo mount /dev/mmcblk0p1 /mnt/eMMC 
sudo chmod 777 /mnt/eMMC/*
## How to run

1. fdisk -l �鿴ϵͳ����ʶ�𵽵Ĵ���
2. sudo mount /dev/mmcblk0p1 /mnt/eMMC ��ʱ����
3. lsblk �鿴���̹������
6. sudo chmod 777 /mnt/eMMC/cache* ��Ȩ
7. cd /home/odroid/R/Caching-Policy/cache/src
8. chmod 777 ../storage  # Ŀ¼ ��д�ɶ���ִ��
8. g++ -std=c++17 -o test test.cpp # -std=c++17  for clock-pro
9. ./test
10. ls -lht document size
## Test

1. bash cp.sh ����CPUʹ����

## trace

## statistic

1. *+ Latency = the time process a trace
2. *+ average time
3. *+ band width = total size / total time
4. *+ average size = total size / request number
5. *+ hit ratio
6. *+ trace hit ratio
7. power/energy
9. *+ cpu usage

o-direct

## problem

1. how to cetegory different caching policy
2. relationship between hit ratio, power, latency
3. caching policy on resouce-limited edge
4. analizy data and conclude from which
5. o-direct
6. c.sh output formalated txt: cpu usage
7. test add start/end time

8. debug c.sh sleep: missing operand
9. power

## ͳ�ƴ�����
```shell
find . -type f -print | xargs wc -l
```
������: 3309

ʹ�ô�����ͳ������`cloc`
```shell
cloc .
```
