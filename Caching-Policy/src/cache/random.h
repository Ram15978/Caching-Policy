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

    ll getVictim(){
        return victim;
    }

    void Touch(const long long &key)
    {
        long long curVictim = -1;
        if(cache_map.size() >= cache_size){
            curVictim = ReplCandidate();
            Erase(curVictim);
            victim = curVictim;
        }

        Put(key);
        // return victim; 
    }

    void Erase(const long long &key) 
    {
        auto it = cache_map.find(key);
        if (it != cache_map.end())
            cache_map.erase(it); // map.erase(e->key);
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
    ll victim;
};

#endif // RANDOM_H
