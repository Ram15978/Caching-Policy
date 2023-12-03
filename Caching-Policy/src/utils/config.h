#ifndef _CONFIG_HPP_INCLUDED_
#define	_CONFIG_HPP_INCLUDED_

/* O_DIRECT �ƹ����������ٻ��棬ֱ��IO������Ϊʹ�����ƣ�
    0.���С(block size)ָ�豸��������С��ͨ��Ϊ512�ֽ�
    1.���ڴ������ݵĻ����������ڴ�߽�������Ϊ���С��������
    2.���ݴ���Ŀ�ʼ�㣬���ļ����豸��ƫ�����������ǿ��С��������
    3.���������ݵĳ��ȱ����ǿ��С����������
    ������������һ���ƾ�������EINVAL����
*/

typedef long long ll;

const long long CHUNK_SIZE = 4*1024; //4kB
// nexus5_4.txt: 19112; nexus5_10.txt: 19280; 20019
const long long DISK_SIZE=500 ; //disk_capacity=DISK_SIZE*CHUNK_SIZE
// const long long DISK_SIZE=1024;
// const double p=0.02;
const long long CHUNK_NUM=500 ;
// const long long CACHE_SIZE=CHUNK_NUM*0.1;
const long long CACHE_SIZE = 3;
// const char* TRACE_PATH="/home/odroid/R/Caching-Policy/Caching-Policy/trace/zipfian/1.15_1000000_150000_1_false/trace.txt";
// const char* TRACE_PATH = "/mnt/d/Projects/Caching-Policy/Caching-Policy/trace/latest/1000000_150000_1_false/trace.txt";
// const char* TRACE_PATH = "/home/odroid/R/Caching-Policy/Caching-Policy/trace/real/MobileAPPTraces/mojitianqi/mojitianqi.txt";
const char* TRACE_PATH = "../trace/real/MobileAPPTraces/mojitianqi/mojitianqi.txt";
//const char* TRACE_PATH = "/home/odroid/R/Caching-Policy/Caching-Policy/trace/real/MobileAPPTraces/qq/qq.txt";
// const char* TRACE_PATH = "/home/odroid/R/Caching-Policy/Caching-Policy/trace/test.txt";
// const char* TRACE_PATH = "../trace/test.txt";

//const char* TRACE_PATH = "/home/odroid/R/Caching-Policy/Caching-Policy/trace/test_trace.txt";
const char* CACHE_PATH = "../trace/real/MobileAPPTraces/mojitianqi/storage_655_655/cache_0.02.bin";
// const char* CACHE_PATH="../storage/cache_0.02.bin";
// const char* CACHE_PATH="/mnt/eMMC/cache_0.02.bin";
//const char* CACHE_PATH="/dev/mmcblk0";
const char* DISK_PATH="../storage/disk.bin";
//const char* DISK_PATH="/dev/mmcblk0";
// const char* CACHE_PATH="/mnt/d/Projects/Caching-Policy/Caching-Policy/storage/cache.bin";
// const char* DISK_PATH="/mnt/d/Projects/Caching-Policy/Caching-Policy/storage/disk.bin";

const bool O_DIRECT_ON = true;
const bool RANDOM_ON = false;
const int RANDOM_THRESHOLD = 0;// 10 -> 0.1�ĸ���д�뻺��

#endif /*_CONFIG_INCLUDED_*/
