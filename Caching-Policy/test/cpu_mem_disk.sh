#!/bin/sh

rm cpu_usage.log
rm mem_used.log
rm top_output.txt
rm disk_read_wrtn.log

eMMC_name="mmcblk0"
sd_name="mmcblk1"

while true; do
    # ��¼��ǰʱ��
    time=$(date "+%Y-%m-%d %H:%M:%S")

    # ��¼memory used
    mem_used=$(free -m | grep "Mem:" | awk '{print $3}')

    # ����top������������ģʽ���������ʱ�ļ�
    top -b -n 1 > top_output.txt

    # ���� iostat ����������
    iostat_output=$(iostat -d)

    # ʹ��grep������ȡ����"us"��"sy"���У�����������浽������
    us_sy_lines=$(grep -E "^\s*%Cpu\(s\):.*us|sy" top_output.txt)

    # ʹ��awk������ȡ�û�ʱ���ϵͳʱ�䣬�����浽������
    user_usage=$(echo "$us_sy_lines" | awk '{print $2}' | tr -d 'us,')
    sys_usage=$(echo "$us_sy_lines" | awk '{print $4}' | tr -d 'sy,')

    # cpuʹ��ʱ�� = �û�ʱ�� + ϵͳʱ��
    cpu_usage=`echo ${user_usage} ${sys_usage} | awk '{print $1+$2}'`

    # ���������ȡ kB_read �� kB_wrtn ����
    read_data1=$(echo "$iostat_output" | grep -E "$eMMC_name" | awk 'NR==1 {print $6}')
    write_data1=$(echo "$iostat_output" | grep -E "$eMMC_name" | awk 'NR==1 {print $7}')
    read_data2=$(echo "$iostat_output" | grep -E "$sd_name" | awk 'NR==1 {print $6}')
    write_data2=$(echo "$iostat_output" | grep -E "$sd_name" | awk 'NR==1 {print $7}')

    # ��ӡͳ�ƽ��
    # echo "User Usage: $user_usage%; System Usage: $sys_usage%"
    # echo "Cpu Usage: $cpu_usage%"
    # echo "${eMMC_name}: kB_read = $read_data1, kB_wrtn = $write_data1"
    # echo "${sd_name}: kB_read = $read_data2, kB_wrtn = $write_data2"

    # ������
    echo "${mem_used} $time" >> mem_used.log
    echo "${cpu_usage}% $time" >> cpu_usage.log
    echo "${eMMC_name}: kB_read = $read_data1, kB_wrtn = $write_data1; ${sd_name}: kB_read = ${read_data2}, kB_wrtn = ${write_data2}; $time" >> disk_read_wrtn.log

    # ������ʱ�ļ�
    rm top_output.txt

    sleep 1
done
