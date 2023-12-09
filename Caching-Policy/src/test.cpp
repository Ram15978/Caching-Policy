#include "simulator/randomSl.h"
#include "simulator/fifoSl.h"
#include "simulator/lruSl.h"
#include "simulator/lfuSl.h"
#include "simulator/lirsSl.h"
#include "simulator/arcSl.h"
#include "simulator/clockproSl.h"
#include "simulator/2qSl.h"


using namespace std;

int main(){
    // RandomSl simulator;
    // FifoSl simulator; 
    // LfuSl simulator;
    // LruSl simulator;
    // LirsSl simulator; 
    // ArcSl simulator;
    // ClockproSl simulator; 
    TqSl simulator;


    simulator.test();
    simulator.statistic();

    return 0;
}
/*
sudo mount /dev/mmcblk0p1 /mnt/eMMC
lsblk
g++ -std=c++17 -o test test.cpp
./test
*/
