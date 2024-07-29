import matplotlib.pyplot as plt
import os

timestamp = []
dim_E = []
dim_N = []
dim_Z = []

dir = "location to get data"
save_dir = "location to store graphs"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def plot_data(ax, timestamps, dim_E, dim_N, dim_Z, title):
    ax.plot(timestamps, dim_E, marker='o', color='#DC143C', label='East-West component of signal (cm/s/s)')
    ax.plot(timestamps, dim_N, marker='o', color='#6495ED', label='North-South component of signal (cm/s/s)')
    ax.plot(timestamps, dim_Z, marker='o', color='#B8860B', label='Up-Down component of signal (cm/s/s)')
    ax.set_title(title)

for filename in os.listdir(dir):
    timestamp.clear()
    dim_E.clear()
    dim_N.clear()
    dim_Z.clear()
    f = os.path.join(dir, filename)
    lst = os.listdir(f)  # directory path

    if len(lst) >= 20:
        plot_counter = 0
        fig_counter = 1
        fig = None
        axs = None

        for subfolder in os.listdir(f):
            sub = os.path.join(f, subfolder)
            for file in os.listdir(sub):
                data = open(os.path.join(sub, file))  # file path
                for line in data:
                    p = line.split()
                    timestamp.append(p[10])
                    dim_E.append(float(p[11]))
                    dim_N.append(float(p[12]))
                    dim_Z.append(float(p[13]))
            
            if plot_counter % 16 == 0:
                if fig is not None:
                    handles, labels = axs[0, 0].get_legend_handles_labels()
                    fig.legend(handles, labels, loc='upper right')
                    plt.tight_layout()
                    fig.savefig(os.path.join(save_dir, f'Fig {fig_counter-1} {filename}.png'))
                    plt.close(fig)
                fig, axs = plt.subplots(4, 4, figsize=(10, 10), sharex=True)
                fig.suptitle(f'Figure {fig_counter} for {filename}', fontsize=16)
                fig_counter += 1
            
            row = (plot_counter % 16) // 4
            col = (plot_counter % 16) % 4
            plot_data(axs[row, col], timestamp, dim_E, dim_N, dim_Z, subfolder)

            plot_counter += 1

        if fig is not None:
            handles, labels = axs[0, 0].get_legend_handles_labels()
            fig.legend(handles, labels, loc='upper right')
            plt.tight_layout()
            fig.savefig(os.path.join(save_dir, f'Fig {fig_counter-1} {filename}.png'))
            plt.close(fig)
