import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import tqdm

data_dir = '../../data/statistic'
result_dir = '../../result/real/lineplot/cache_size_no_random_lfu'
# 读入数据
df = pd.read_excel(os.path.join(data_dir, 'statistic_real_3.xlsx'))

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'

# 设置图表的大小和风格
plt.rcParams["figure.figsize"] = (12, 6)
sns.set(style="white")  # 设置背景为全白色

# 定义不同的线条和标记样式
markers = ['o', 's', 'D']
LineStyles = ['-', '--', '-.']

trace_operation_combinations = df[
    ['Real Trace Type', 'Real Trace Name', 'IO(on/off)']].drop_duplicates()
combination_list = trace_operation_combinations.values.tolist()

# style_dict = {
#     'Random': {'marker': 'o', 'linestyle': '-'},
#     'FIFO': {'marker': 's', 'linestyle': '--'},
#     'LFU': {'marker': 'D', 'linestyle': '-.'},
#     'LRU': {'marker': '^', 'linestyle': ':'},
#     'LIRS': {'marker': 'v', 'linestyle': '-'},
#     'ARC': {'marker': '>', 'linestyle': '--'},
#     'CLOCK-Pro': {'marker': '<', 'linestyle': '-.'},
#     '2Q': {'marker': 'p', 'linestyle': '-'},
#     'TinyLFU': {'marker': 'h', 'linestyle': '--'}
# }

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

# caching_policy_list = ['Random', 'FIFO', 'LFU', 'LRU', 'LIRS', 'ARC', 'CLOCK-Pro', '2Q', 'TinyLFU']
caching_policy_list = ['FIFO', 'LRU', 'LIRS', 'ARC', 'CLOCK-Pro', '2Q', 'TinyLFU']


# 要测的y轴变量
def lineplot_real_cache_size(combination_, y_label_):
    # 创建图表
    fig, ax = plt.subplots()

    real_trace_type, real_trace_name, io_status = combination_

    save_dir = os.path.join(result_dir, real_trace_type, real_trace_name, io_status)
    os.makedirs(save_dir, exist_ok=True)

    trace_data = df[(df['Real Trace Type'] == real_trace_type) &
                               (df['Real Trace Name'] == real_trace_name) &
                               (df['IO(on/off)'] == io_status)]

    # 遍历每种 IO 类型和 Caching Policy 的组合
    for idx, caching_policy in enumerate(caching_policy_list):  # 筛选特定Caching Policy 的数据
        policy_data = trace_data[trace_data['Caching Policy'] == caching_policy]

        # 获取标记样式和线型
        mk = markers[idx % len(markers)]
        ls = LineStyles[idx // len(LineStyles)]

        # 绘制折线图
        sns.lineplot(ax=ax, data=policy_data, x='Cache Size', y=f"{y_label_}", marker=mk, linestyle=ls,
                     label=f"{caching_policy}", errorbar=None)


        # # 获取标记样式和线型
        # style = style_dict[caching_policy]
        #
        # # 绘制折线图
        # sns.lineplot(ax=ax, data=policy_data, x='Cache Size', y=f"{y_label_}", marker=style['marker'], linestyle=style['linestyle'],
        #              label=f"{caching_policy}", errorbar=None)

    # 设置坐标轴标签
    ax.set_xlabel("Cache Size")
    ax.set_ylabel(f"{y_label_}")

    # 设置x轴的间隔为0.02
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.02))

    ax.legend(loc='best', ncol=3, frameon=False, handlelength=3.5)

    if y_label_ == 'Bandwidth(MB/s)':
        y_label_ = 'Bandwidth(MBps)'

    # plt.show()

    # 保存图表到文件夹中
    save_path = os.path.join(save_dir, f"{y_label_}.svg")
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    print(save_path)


if __name__ == '__main__':
    for y_label in y_labels:
        for combination in combination_list:
            lineplot_real_cache_size(combination, y_label)
