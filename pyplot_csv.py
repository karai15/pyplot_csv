import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    # fast_plot()  # とりあえず全ファイルplot (./csv_data/)
    tuning_plot()  # 指定してplot

def tuning_plot():

    x_label = "SNR [dB]"
    y_label = r"NMSE($\mathbf{H}$) [dB]"
    save_path = "./NMSE_H_vs_SNR.pdf"

    # (csv_name, legend_name, color, marker, linestyle)
    plot_list = [
        ["CoDL.csv", "CoDL", "black", "s", "solid"],
        ["SOMP.csv", "SOMP", "red", "x", "solid"],
        ["SIGW.csv", "SIGW", "green", "o", "solid"],
        ["ML.csv", "Proposed", "blue", "^", "solid"],
    ]


    ##########################
    # plot
    dir_data = "./csv_data/"
    pp = plot_config()
    fig, ax = plt.subplots(1, 1, squeeze=False)
    for n, plot_data in enumerate(plot_list):
        data = np.loadtxt(os.path.join(dir_data, plot_data[0]), delimiter=",")
        plt.plot(data[:, 0], data[:, 1])

        ax[0, 0].plot(data[:, 0], data[:, 1],
                      label=plot_data[1], color=plot_data[2], marker=plot_data[3], linestyle=plot_data[4],
                      markerfacecolor=pp["markerfacecolor"], markeredgewidth=pp["markeredgewidth"],
                      markersize=pp["markersize"], alpha=pp["alpha"])

    ax[0, 0].set_xlabel(x_label)
    ax[0, 0].set_ylabel(y_label)
    ax[0, 0].grid(which="both")
    ax[0, 0].legend(fontsize=pp["leg_ftz"])

    # save fig
    fig.savefig(save_path, dpi=300)
    plt.show()
    ##########################



def fast_plot():
    x_label = "SNR [dB]"
    y_label = r"NMSE($\mathbf{H}$) [dB]"
    save_path = "./NMSE_H_vs_SNR.pdf"

    # plot
    dir_data = "./csv_data/"
    files = os.listdir(dir_data)
    pp = plot_config()
    fig, ax = plt.subplots(1, 1, squeeze=False)
    for n, file in enumerate(files):
        data = np.loadtxt(os.path.join(dir_data, file), delimiter=",")
        plt.plot(data[:, 0], data[:, 1])

        ax[0, 0].plot(data[:, 0], data[:, 1], label=file,
                      color=pp["color"][n], marker=pp["marker"][n], linestyle=pp["linestyle"][n],
                      markerfacecolor=pp["markerfacecolor"], markeredgewidth=pp["markeredgewidth"],
                      markersize=pp["markersize"], alpha=pp["alpha"])

    ax[0, 0].set_xlabel(x_label)
    ax[0, 0].set_ylabel(y_label)
    ax[0, 0].grid(which="both")
    ax[0, 0].legend(fontsize=pp["leg_ftz"])

    # save fig
    fig.savefig(save_path, dpi=300)
    # plt.show()


def plot_config():
    fsz = 15  # フォントサイズ
    plt.rcParams['font.family'] = 'Times New Roman'  # font familyの設定
    plt.rcParams['mathtext.fontset'] = 'stix'  # math fontの設定
    plt.rcParams["font.size"] = fsz  # 全体のフォントサイズが変更されます。
    plt.rcParams['axes.linewidth'] = 1.5  # グラフの枠線の太さ
    plt.rcParams["figure.figsize"] = (6, 4)  # 横：縦

    # 軸
    plt.rcParams['xtick.labelsize'] = fsz  # x軸のフォントサイズ
    plt.rcParams['ytick.labelsize'] = fsz  # y軸のフォントサイズ
    plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.2  # x軸目盛の太さ
    plt.rcParams['ytick.major.width'] = 1.2  # y軸目盛の太さ
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = 0.8  # gridの太さ

    # legend
    plt.rcParams["legend.fancybox"] = False  # 丸角
    plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
    plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更

    # 図のサイズ
    fig_ftz = 12
    plt.rcParams["figure.dpi"] = 300  # dpi(dots per inch)
    plt.rcParams["figure.autolayout"] = True  # レイアウトの自動調整

    # plot param
    plot_param = {
        "color": ["b", "r", "g", "k", "y", "m", "c"] * 10,
        "marker": ['s', '^', 'o', 'D', 'x', 'v', 'p', '*'] * 10,
        "linestyle": ["solid", "dashdot", "dotted", "dashed"] * 10,
        "markerfacecolor": "w",  # marker内の色
        "markersize": 9,
        "markeredgewidth": 2.0,
        "leg_ftz": 10,  # 凡例フォントサイズ  14
        "alpha": 1,  # 透明度
    }

    return plot_param


if __name__ == '__main__':
    main()
