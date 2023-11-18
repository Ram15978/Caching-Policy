#ifndef RANDOM_H
#define RANDOM_H


#include <list>
#include <map>
#include <random>
#include "../utils/config.h"

using namespace std;

class RANDOM {
public:
    
    RANDOM(long long size=CACHE_SIZE):cache_size(size){}

    bool Cached(const long long &key)
    {
        return cache_map.count(key)!=0;
    }

    bool Get(const long long &key){
        return cache_map.at(key);
    }

    void Put(const long long &key)
    {
        cache_map[key]=0;
    }

    long long Touch(const long long &key)
    {
        long long victim = -1;
        if(cache_map.size() >= cache_size){
            victim = ReplCandidate();
            Erase(victim);
        }

        Put(key);

        return victim; 
    }

    void Erase(const long long &key) 
    {
        cache_map.erase(key);
    }


    const long long &ReplCandidate()
    {
        // ʹ�������������ѡ��һ�����������
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(0, cache_map.size() - 1);

        auto it = cache_map.begin();
        advance(it, dis(gen)); // �ƶ������������λ��
        return it->first;
    }

private:
    long long cache_size; 
    map<long long, bool> cache_map;
};

#endif // RANDOM_H
