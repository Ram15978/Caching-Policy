import pandas as pd
import matplotlib.pyplot as plt
import os

data_dir = '../../../../data/statistic'
result_dir = '../../../../result/change_font_size/ycsb/block_size/barplot'
statistic_name = 'statistic_ycsb_125MB_all.xlsx'

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 16

# 设置图表的大小和风格
plt.rcParams["figure.figsize"] = (10, 6)

# 定义颜色和样式
# 配色1：先白、灰、黑
colors = ['#FFFFFF', '#CCCCCC', '#666666', '#FFFFFF', '#CCCCCC', '#666666', '#FFFFFF', '#CCCCCC', '#666666']
hatches = ['', '', '', '/', '/', '/', '\\\\', '\\\\', '\\\\']

# 配色2：配色1+先空、单斜线、反双斜线
# colors = ['#FFFFFF', '#FFFFFF',  '#FFFFFF', '#CCCCCC', '#CCCCCC', '#CCCCCC', '#666666','#666666', '#666666']
# hatches = ['', '/', '\\\\','', '/', '\\\\','', '/', '\\\\']

# 配色3：配色1+改蓝
# colors = ['#FFFFFF', '#87CEEB', '#4682B4', '#FFFFFF', '#87CEEB', '#4682B4', '#FFFFFF', '#87CEEB', '#4682B4']
# hatches = ['', '', '', '/', '/', '/', '\\\\', '\\\\', '\\\\']


# 读取Excel文件
original_data = pd.read_excel(os.path.join(data_dir, statistic_name))

# 获取 Workload Type 和 Operation Read Ratio 的组合
trace_operation_combinations = original_data[
    ['Workload Type', 'Operation Read Ratio', 'Cache Size', 'IO(on/off)']].drop_duplicates()
combination_list = trace_operation_combinations.values.tolist()  # 转换为列表

# 不同的y坐标
y_labels = ['Hit Ratio', 'Average Latency(ms)', 'P99 Latency(ms)', 'Total Time(s)', 'Bandwidth(MB/s)',
            'Average CPU Usage(%)', 'Average Memory Used(MB)',
            'Average Power(W)', 'Energy(J)',
            'eMMC Read Size(KB)', 'eMMC Write Size(KB)',
            'SD Read Size(KB)', 'SD Write Size(KB)',
            'Average Power(W)', 'Energy(J)',
            'eMMC Read Numbers', 'eMMC Read Average Latency(ms)', 'eMMC Read P99 Latency(ms)',
            'eMMC Write Numbers', 'eMMC Write Average Latency(ms)', 'eMMC Write P99 Latency(ms)',
            'SD Read Numbers', 'SD Read Average Latency(ms)', 'SD Read P99 Latency(ms)',
            'SD Write Numbers', 'SD Write Average Latency(ms)', 'SD Write P99 Latency(ms)']


def barplots_ycsb_block_size(combination_, y_label_):
    workload_type, operation_read_ratio, block_size, io_status = combination_
    if y_label_ == 'Bandwidth(MB/s)':
        file_name = 'Bandwidth(MBps)'
    else:
        # file_name = y_label_.replace(' ', '_')
        file_name = y_label_
    save_dir = os.path.join(result_dir, workload_type, str(operation_read_ratio), str(block_size), io_status)

    os.makedirs(save_dir, exist_ok=True)  # 先创建目录
    save_path = os.path.join(save_dir, f"{file_name}.png")

    # 初始化画布和子图
    fig, ax = plt.subplots()
    trace_data = original_data[(original_data['Workload Type'] == workload_type) &
                               (original_data['Operation Read Ratio'] == operation_read_ratio) &
                               (original_data['Cache Size'] == block_size) &
                               (original_data['IO(on/off)'] == io_status)]

    caching_policy_list = ['Random', 'FIFO', 'LFU', 'LRU', 'LIRS', 'ARC', 'CLOCK-Pro', '2Q', 'TinyLFU']
    block_size_list = trace_data['Block Size(KB)'].unique()

    # 遍历每种 Cache Size
    for idx, block_size in enumerate(sorted(block_size_list)):
        for policy_idx, caching_policy in enumerate(caching_policy_list):
            y_axis = trace_data[(trace_data['Caching Policy'] == caching_policy) &
                                (trace_data['Block Size(KB)'] == block_size)][y_label_]

            # 画柱状图
            if not y_axis.empty:
                ax.bar(idx * 10 + policy_idx, y_axis, color=colors[policy_idx], edgecolor='black', 
                       hatch=hatches[policy_idx], width=0.8, label=f"{caching_policy}" if idx == 0 else "")

    # 设置刻度线格式
    ax.tick_params(axis='both', which='both', bottom=False, labelsize=16)

    # 设置横纵坐标标签和标题
    ax.set_xlabel('Block Size(KB)', weight='bold', fontsize=16)
    ax.set_ylabel(y_label_, weight='bold', fontsize=16)
    ax.set_xticks([idx * 10 + 4 for idx in range(len(block_size_list))])
    ax.set_xticklabels(sorted(block_size_list))
    # # 设置图例
    # if idx == 0:
    #     ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False)

    # 设置图例
    ax.legend(caching_policy_list, loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, shadow=False, ncol=5, frameon=False, fontsize=14)
    # plt.show()

    # 保存图形
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

    plt.close(fig)

    print(save_path)


if __name__ == '__main__':
    for y_label in y_labels:
        for combination in combination_list:
            barplots_ycsb_block_size(combination, y_label)
