import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from psd_tools import PSDImage

import composite
import export

file_name = 'H:/art/temp/test.psd'
image = PSDImage.open(file_name)

def get_layer_data(psd, name):
    layer = export.find_layer(psd, name)
    layer.visible = True
    return composite.get_pixel_layer_data(layer, composite.swap(psd.size), (0, 0))

res, res_a = composite.composite_group_layer(image, image.size, (0, 0))
tgt, tgt_a = get_layer_data(image, 'tgt')
src, src_a = get_layer_data(image, 'src')
dst, dst_a = get_layer_data(image, 'dst')
#dst, dst_a = composite.composite_layers([export.find_layer(image, 'dst')], image.size, (0, 0))

x = np.arange(res.shape[1]) / 255.0

def band(data, row, i):
    return data[row,:,i]

def plot(ax, data, row, dashes):
    ax.plot(x, band(data, row, 0), color=(1, 0, 0), dashes=dashes)
    ax.plot(x, band(data, row, 1), color=(0, 1, 0), dashes=dashes)
    ax.plot(x, band(data, row, 2), color=(0, 0, 1), dashes=dashes)

def plot_a(ax, data, row, dashes):
    ax.plot(x, band(data, row, 0), color=(0, 0, 0), dashes=dashes)

fig, ax = plt.subplots(1,1)
fig.subplots_adjust(bottom=0.25)
axframe = fig.add_axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(axframe, 'row', 0, image.height - 1, valinit=0, valstep=1)

def update(val):
    ax.cla()
    row = int(slider.val)
    plot(ax, res, row, (1, 0))
    plot(ax, tgt, row, (2, 2))
    plot(ax, src, row, (3, 3))
    plot_a(ax, src_a, row, (3, 3))
    plot(ax, dst, row, (4, 1))
    plot_a(ax, dst_a, row, (4, 1))
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')

slider.on_changed(update)
update(0)

plt.show()