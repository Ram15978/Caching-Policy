##### 2023.10.26
���⣺

Trace��mojitianqi��CACHE_SIZE��3

offset_cache=-1���µ���read/writeCache����ʱ�ļ���д����
������

- ���ų�odirectread/write������

- �����룬������CACHE_SIZE=3��cache����������£�������chunk_mapӦ����ʾ��3��offset_cache��-1��chunk����������ȴ��������������ͼ����ʱvictimΪkey=1835008��chunk���³�[1835008]������������offset_cacheȴΪ-1���ɴˣ��ƶ�����offset_cacheû����ȷ��ֵ��

  <img src="images/image-20231026203541899.png" alt="image-20231026203541899" style="zoom: 50%;" />

- ��ǰѰ��[1835008]��һ��offset_cache��Ϊ0��ʱ�̣���trace20������
- ͬʱѰ�ҵ�һ��cache���ҳ�������CACHE_SIZE��chunk��offset_cache��Ϊ-1��ʱ�̣���trace19������

<img src="images/image-20231026205438990.png" alt="image-20231026205438990" style="zoom:50%;" />

- �۲�ɵã�trace18ʱ��[1835008]���ڻ����У�trace19������ʱȴ�϶��䲻�ڻ����У���[1073152]��λ���滻����[1835008]��[1073152]���ź��˳�������Ϊʲô�أ�

- ����LRU����ʱδ�������ƴ�������ʱ��Ϊ��Clockpro::cache_map.Cached�����������԰ѵڶ����ж�ע�ͣ����¡������trace18�ͱ���

  ```c
  // --clockpro.hpp--
  bool Cached(const k& key){
  	if (cache_map.find(key) == cache_map.end()) return false;
  	// if (cache_map[key]->ptype == ptTest) return false;
  	return true;
  }
  ```

- ����clockpro.hpp��182�У��˴���10�У���һ��ע�͵Ĵ��룬���һ��Դ���Ƿ�ע�ͣ�Դ���ַΪhttps://github.com/maximecaron/ClockProCPP

  ```c
  // --clockpro.hpp--
  bool Set(k key, v value)
  {
  	if(cache_map.find(key) == cache_map.end()) // miss
  	{
  		// Allocate memory outside of holding cache the lock
  		auto e = new Entry<k, v>(false, key, value, ptCold);
  		// no cache entry?  add it
  		cache_map[key]=e;
  		// cache_map.insert_or_assign(key, e);
  		std::unique_lock<std::mutex> lockx(cacheMutex);
  		meta_add(e);
  		count_cold++;
  		return true;
  	}
  ......
  }
  ```

  81920 cnt==0

  