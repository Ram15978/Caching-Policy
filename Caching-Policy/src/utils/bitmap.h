#ifndef _BITMAP_HPP_INCLUDED_
#define _BITMAP_HPP_INCLUDED_
#include<iostream>
#include<vector>
using namespace std;

class BitMap{
public:
	//λͼ���ڴ��С�����ݷ�Χ�й�
	BitMap(size_t range)
		:_bit(range / 32 + 1)
	{}

	void set(const size_t num)
	{
		//���������е��±�
		int idx = num / 32;
		//����num�ڶ�Ӧ�±������е��±�λ��
		int bitIdx = num % 32;
		//����Ӧ�ı���λ��1
		_bit[idx] |= 1 << bitIdx;
	}

	bool find(const size_t num)
	{
		int idx = num / 32;
		int bitIdx = num % 32;
		return (_bit[idx] >> bitIdx) & 1;
	}

	void reset(const size_t num)
	{
		int idx = num / 32;
		int bitIdx = num % 32;
		_bit[idx] &= ~(1 << bitIdx);
	}
private:
	vector<int> _bit;
};

#endif	/* _BITMAP_HPP_INCLUDED_ */
