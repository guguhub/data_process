# 从头开始构建满足所有要求的代码，包括插值、颜色平滑以及保存图像
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
# 创建更平滑的数据插值函数
def smooth_data(kx_sparse, ky_sparse, E_sparse, method='cubic', grid_num=200):
    kx_fine = np.linspace(-1, 1, grid_num)
    ky_fine = np.linspace(-1, 1, grid_num)
    kx_fine, ky_fine = np.meshgrid(kx_fine, ky_fine)
    E_fine = griddata((kx_sparse, ky_sparse), E_sparse, (kx_fine, ky_fine), method=method)
    return kx_fine, ky_fine, E_fine

# 模拟稀疏数据
kx_sparse = np.random.uniform(-1, 1, 100)
ky_sparse = np.random.uniform(-1, 1, 100)
E_sparse = np.sin(np.sqrt(kx_sparse**2 + ky_sparse**2))

# 插值数据
kx_fine, ky_fine, E_fine = smooth_data(kx_sparse, ky_sparse, E_sparse)

# 绘制图像
fig, ax = plt.subplots(figsize=(7, 6))

# 绘制平滑颜色变化的等能面图
im = ax.imshow(E_fine, extent=(-1, 1, -1, 1), cmap='viridis', interpolation='bilinear', origin='lower')

# 添加颜色条
cbar = fig.colorbar(im, ax=ax, orientation='vertical')
cbar.set_label('Energy E')

# 设置标题和轴标签
ax.set_title('Interpolated Energy Contour')
ax.set_xlabel('kx')
ax.set_ylabel('ky')

# 保存图片
current_path = os.getcwd()
#parent_path = os.path.abspath(os.path.join(current_path, '..'))
folder_name = 'fig'
folder_path = os.path.join(current_path, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
time = datetime.datetime.now().strftime('%m-%d %H_%M') # 括号里('%Y-%m-%d %H_%M_%S') 年月日，时分秒
figname = '/energy_contour'
filetype = '.png'
plt.savefig(folder_path + figname + time + filetype, format='png', dpi=300)

# 显示图片
plt.show()

# 输出保存的文件路径
#print('/mnt/data/energy_contour.png')
