import numba
from numba.typed import Dict
import numpy as np

@numba.njit
def get_gaussian_kernel(size, kernels):
    kernel = kernels.get(size)
    if kernel is not None:
        return kernel
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(size))
    kernel = np.outer(gauss, gauss)
    kernel /= np.sum(kernel)
    kernels[size] = kernel
    return kernel

@numba.njit(inline='always')
def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

@numba.njit
def get_clamped(data, y, x):
    h, w = data.shape[:2]
    y = clamp(y, 0, h - 1)
    x = clamp(x, 0, w - 1)
    return data[y, x]

@numba.njit
def convolve(data, y, x, kernel, result):
    kh, kw = kernel.shape
    total = kh * kw
    kh2, kw2 = kh // 2, kw // 2
    dy = y - kh2
    for ky in range(kh):
        dx = x - kw2
        for kx in range(kw):
            result[y, x] += get_clamped(data, dy, dx) * kernel[ky, kx]
            dx += 1
        dy += 1

@numba.njit()
def variable_blur(color, alpha, size, kernels):
    alpha_k = (alpha * size).astype(np.int16).reshape(alpha.shape[:2])
    h, w = color.shape[:2]
    result = np.empty_like(color)
    for y in range(h):
        for x in range(w):
            k = alpha_k[y, x]
            if k > 0:
                convolve(color, y, x, get_gaussian_kernel(k, kernels), result)
    return result

kernel_cache = Dict.empty(
    key_type=numba.int16,
    value_type=numba.float64[:,:],
)

def variable_blur_op(color, alpha, size=50, *_):
    size = int(size)
    color = variable_blur(color, alpha, size, kernel_cache)
    return color, alpha