"""
### Perform convolutions on arrays.  ###
"""

# Standard Library
from typing import List, Tuple, Optional

# Internal
from buteo.utils import core_utils
from buteo.raster.convolution_funcs import *

# External
import numpy as np
from numba import jit, prange


def weight_distance(
    arr: np.ndarray,
    method: Optional[str] = None,
    decay: float = 0.2,
    sigma: float = 1.0,
    center: float = 0.0,
    spherical: bool = False,
    radius: float = 3.0,
) -> float:
    """
    Weights the kernel by distance using various methods.

    Args:
        arr (numpy.ndarray): The input array.
        method (str, default=None): The weighting method to use.
            "none": No weighting (default).
            "linear": Linear decay.
            "sqrt": Square root decay.
            "power": Power decay.
            "log": Logarithmic decay.
            "gaussian": Gaussian decay.
        decay (float, default=0.2): The decay rate for the `linear`, `sqrt`, and `power` methods.
        sigma (float, default=1.0): The standard deviation for the Gaussian method.
        center (float, default=0.0): The center of the array.
        spherical (bool, default=False): If True, adjust weights based on the radius.
        radius (float, default=3.0): The radius for spherical adjustments.

    Returns:
        float: The computed weight.
    """

    if center == 0.0:
        normed = np.linalg.norm(arr)
    else:
        normed = np.linalg.norm(arr - np.array([0, 0, center]))

    if normed == 0.0:
        weights = 1.0

    if method is None or method == "none" or method == "":
        weights = 1.0
    elif method == "linear":
        weights = np.power((1 - decay), normed)
    elif method == "sqrt":
        weights = np.power(np.sqrt((1 - decay)), normed)
    elif method == "power":
        weights = np.power(np.power((1 - decay), 2), normed)
    elif method == "log":
        weights = np.log(normed + 2) # +2 to avoid log(0)
    elif method == "gaussian":
        weights = np.exp(-(np.power(normed, 2)) / (2 * np.power(sigma, 2)))
    else:
        raise ValueError("Unable to parse parameters for weight_distance.")

    if spherical:
        sqrt_2 = np.sqrt(2)
        half_sqrt_2 = np.divide(sqrt_2, 2)

        if normed > radius + half_sqrt_2:
            return 0.0
        elif normed < radius - half_sqrt_2:
            return 1.0

        dist_min = radius - half_sqrt_2
        dist_max = radius + half_sqrt_2

        normed = 1 - np.interp(normed, [dist_min, dist_max], [0, 1])
        return weights * normed

    return weights


def rotate_kernel(bottom_right: np.ndarray) -> np.ndarray:
    """
    Creates a whole kernel from a quadrant.

    Args:
        bottom_right (numpy.ndarray): The bottom-right quadrant of the kernel.

    Returns:
        numpy.ndarray: The complete kernel generated from the given quadrant.
    """
    size = ((bottom_right.shape[0] - 1) * 2) + 1
    depth = bottom_right.shape[2]
    kernel = np.zeros((size, size, depth), dtype="float32")

    top_right = np.flipud(bottom_right)
    lower_left = np.fliplr(bottom_right)
    top_left = np.flipud(lower_left)

    kernel[size // 2:, size // 2:, :] = bottom_right
    kernel[:1 + -size // 2, :1 + -size // 2, :] = top_left
    kernel[1 + size // 2:, :size // 2, :] = lower_left[1:, :-1, :]
    kernel[:size // 2, 1 + size // 2:, :] = top_right[:-1, 1:, :]

    return kernel


def get_kernel(
    size: int,
    depth: int = 1,
    hole: bool = False,
    inverted: bool = False,
    normalise: bool = True,
    multi_dimensional: bool = False,
    multi_dimensional_center: int = 0,
    spherical: bool = False,
    distance_weight: Optional[str] = None,
    distance_decay: float = 0.2,
    distance_sigma: float = 1,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generates a square kernel for convolutions.

    Args:
        size (int): Size of the kernel (must be odd).
        depth (int, default=1): Depth of the kernel.
        hole (bool, default=False): Create a hole in the center of the kernel.
        inverted (bool, default=False): Invert the kernel values.
        normalise (bool, default=True): Normalize the kernel values.
        multi_dimensional (bool, default=False): Consider the kernel multi-dimensional.
        multi_dimensional_center (int, default=0): Center of the
            multi-dimensional kernel.
        spherical (bool, default=False): Consider the kernel spherical.
        distance_weight (str or None, default=None): Distance weighting method.
        distance_decay (float, default=0.2): Distance decay factor.
        distance_sigma (float, default=1): Distance sigma for Gaussian distance weighting.

    Returns:
        tuple: A tuple containing the kernel, weights, and offsets.
    """
    assert size >= 3, "Kernel must have atleast size 3."
    assert size % 2 != 0, "Kernel must be an uneven size."
    assert isinstance(size, int), "Kernel must be an integer."
    assert depth >= 1, "Depth must be a positive integer"
    assert isinstance(depth, int), "Depth must be an integer."

    if distance_weight is False:
        distance_weight = None

    quadrant = np.zeros((1 + size // 2, 1 + size // 2, depth), dtype="float32")

    for idx_x in range(0, quadrant.shape[0]):
        for idx_y in range(0, quadrant.shape[1]):
            for idx_z in range(0, quadrant.shape[2]):

                z_value = idx_z if multi_dimensional else 0

                weighted = weight_distance(
                    np.array([idx_x, idx_y, z_value], dtype="float32"),
                    method=distance_weight,
                    decay=distance_decay,
                    sigma=distance_sigma,
                    center=multi_dimensional_center,
                    spherical=spherical,
                    radius=size / 2,
                )

                quadrant[idx_x, idx_y, idx_z] = weighted

    if hole:
        for idx_z in range(0, quadrant.shape[2]):
            quadrant[0, 0, idx_z] = 0

    kernel = rotate_kernel(quadrant)

    if distance_weight == "log":
        kernel = kernel.max() - kernel

    if inverted:
        kernel = 1 - kernel

    if normalise:
        if multi_dimensional:
            summed = kernel.sum()
            if summed != 0.0:
                kernel = kernel / summed
        else:
            summed = kernel.sum(axis=(0, 1))

            for dim in range(0, depth):
                kernel[:, :, dim] = kernel[:, :, dim] / summed[dim]

    weights = []
    offsets = []

    for idx_x in range(0, kernel.shape[0]):
        for idx_y in range(0, kernel.shape[1]):
            for idx_z in range(0, kernel.shape[2]):
                current_weight = kernel[idx_x][idx_y][idx_z]

                if current_weight <= 0.0:
                    continue

                offsets.append(
                    [
                        idx_x - (kernel.shape[0] // 2),
                        idx_y - (kernel.shape[1] // 2),
                        idx_z
                    ]
                )

                weights.append(current_weight)

    return kernel, np.array(weights, dtype="float32"), np.array(offsets, dtype=int)


def pad_array(
    arr: np.ndarray,
    pad_size: int = 1,
    method: str = "same",
    constant_value: Union[float, int] = 0.0,
) -> np.ndarray:
    """
    Create a padded view of an array using SAME padding.

    Args:
        arr (numpy.ndarray): The input array to be padded.

    Keyword Args:
        pad_size (int, default=1): The number of padding elements to add
            to each side of the array. Default is 1.
        method (str, default="same"): The padding method to use. Default
            is "same". Other options are "edge" and "constant".
        constant_value (int, default=None): The constant value to use
            when padding with "constant". Default is 0.

    Returns:
        numpy.ndarray: A padded view of the input array.
    """
    core_utils.type_check(arr, [np.ndarray], "arr")
    core_utils.type_check(pad_size, [int], "pad_size")
    core_utils.type_check(method, [str], "method")

    assert pad_size >= 0, "pad_size must be a non-negative integer"
    assert method in ["same", "SAME", "edge", "EDGE"], "method must be one of ['same', 'SAME', 'constant', 'CONSTANT']"

    if method in ["same", "SAME"]:
        padded_view = np.pad(
            arr,
            pad_width=((pad_size, pad_size), (pad_size, pad_size), (0, 0)),
            mode='edge',
        )
    elif method in ["constant", "CONSTANT"]:
        padded_view = np.pad(
            arr,
            pad_width=((pad_size, pad_size), (pad_size, pad_size), (0, 0)),
            mode='constant',
            constant_values=constant_value,
        )

    return padded_view

METHOD_ENUMS = {
    "sum": 1,
    "mode": 2,
    "max": 3,
    "dilate": 3,
    "min": 4,
    "erode": 4,
    "contrast": 5,
    "median": 6,
    "std": 7,
    "mad": 8,
    "z_score": 9,
    "z_score_mad": 10,
    "sigma_lee": 11,
    "quantile": 12,
    "occurrances": 13,
    "feather": 14,
}


@jit(nopython=True, nogil=False, fastmath=True, cache=True)
def hood_to_value(method, values, weights, nodata_value=-9999.9, center_value=0, value=0.5):
    """ Convert a array of values and weights to a single value using a given method. """
    if method == 1:
        return hood_sum(values, weights)
    elif method == 2:
        return hood_mode(values, weights)
    elif method == 3:
        return hood_max(values, weights)
    elif method == 4:
        return hood_min(values, weights)
    elif method == 5:
        return hood_contrast(values, weights)
    elif method == 6:
        return hood_quantile(values, weights, 0.5)
    elif method == 7:
        return hood_standard_deviation(values, weights)
    elif method == 8:
        return hood_median_absolute_deviation(values, weights)
    elif method == 9:
        return hood_z_score(values, weights, center_value)
    elif method == 10:
        return hood_z_score_mad(values, weights, center_value)
    elif method == 11:
        return hood_sigma_lee(values, weights)
    elif method == 12:
        return hood_quantile(values, weights, value)
    elif method == 13:
        return hood_count_occurances(values, weights, value, normalise=False)
    elif method == 14:
        return hood_count_occurances(values, weights, value, normalise=True)
    else:
        return nodata_value



@jit(nopython=True, parallel=True, nogil=False, fastmath=True, cache=True)
def _convolve_array_collapse(
    arr: np.ndarray,
    offsets: List[Tuple[int, int, int]],
    weights: List[float],
    method: int = 1,
    nodata: bool = False,
    nodata_value: float = -9999.9,
    normalise_edges: bool = True,
    value: Union[int, float] = 0.5,
) -> np.ndarray:
    """
    Internal. Convolve an array using a set of offsets and weights.
    """
    result = np.zeros((arr.shape[0], arr.shape[1], 1), dtype="float32")
    hood_size = len(offsets)

    if arr.shape[2] == 1:
        idx_center = 0
    else:
        idx_center = int(np.ceil((arr.shape[2] / 2) - 1))

    for idx_y in prange(0, arr.shape[0]):
        for idx_x in range(0, arr.shape[1]):

            center_value = arr[idx_y, idx_x, idx_center]

            if nodata and arr[idx_y, idx_x] == nodata_value:
                result[idx_y, idx_x] = nodata_value
                continue

            hood_normalise = False
            hood_values = np.zeros(hood_size, dtype="float32")
            hood_weights = np.zeros(hood_size, dtype="float32")
            hood_count = 0

            for idx_h in range(0, hood_size):
                hood_x = idx_x + offsets[idx_h][0]
                hood_y = idx_y + offsets[idx_h][1]
                hood_z = offsets[idx_h][2]

                if hood_x < 0 or hood_x >= arr.shape[1]:
                    if normalise_edges:
                        hood_normalise = True
                    continue

                if hood_y < 0 or hood_y >= arr.shape[0]:
                    if normalise_edges:
                        hood_normalise = True
                    continue

                if hood_z < 0 or hood_z >= arr.shape[2]:
                    if normalise_edges:
                        hood_normalise = True
                    continue

                if nodata and arr[hood_y, hood_x, hood_z] == nodata_value:
                    if normalise_edges:
                        hood_normalise = True
                    continue

                hood_values[hood_count] = arr[hood_y, hood_x, hood_z]
                hood_weights[hood_count] = weights[idx_h]
                hood_count += 1

            if hood_count == 0:
                result[idx_y, idx_x] = nodata_value
                continue

            hood_values = hood_values[:hood_count]
            hood_weights = hood_weights[:hood_count]

            if hood_normalise:
                hood_weights /= np.sum(hood_weights)

            result[idx_y, idx_x, 0] = hood_to_value(method, hood_values, hood_weights, nodata_value, center_value, value)

    return result


@jit(nopython=True, parallel=True, nogil=False, fastmath=True, cache=True)
def _convolve_array(
    arr: np.ndarray,
    offsets: List[Tuple[int, int, int]],
    weights: List[float],
    method: int = 1,
    nodata: bool = False,
    nodata_value: float = -9999.9,
    normalise_edges: bool = True,
    value: Union[int, float, None] = None,
) -> np.ndarray:
    """
    Internal. Convolve an array using a set of offsets and weights.
    """
    result = np.zeros((arr.shape[0], arr.shape[1], arr.shape[2]), dtype="float32")
    hood_size = len(offsets)

    for idx_y in prange(0, arr.shape[0]):
        for idx_x in range(0, arr.shape[1]):
            for idx_z in range(0, arr.shape[2]):

                center_value = arr[idx_y, idx_x, idx_z]
                hood_normalise = False
                hood_values = np.zeros(hood_size, dtype="float32")
                hood_weights = np.zeros(hood_size, dtype="float32")
                hood_count = 0

                if nodata and arr[idx_y, idx_x, idx_z] == nodata_value:
                    result[idx_y, idx_x, idx_z] = nodata_value
                    continue

                for idx_h in range(0, hood_size):
                    hood_x = idx_x + offsets[idx_h][0]
                    hood_y = idx_y + offsets[idx_h][1]
                    hood_z = idx_z + offsets[idx_h][2]

                    if hood_x < 0 or hood_x >= arr.shape[1]:
                        if normalise_edges:
                            hood_normalise = True
                        continue

                    if hood_y < 0 or hood_y >= arr.shape[0]:
                        if normalise_edges:
                            hood_normalise = True
                        continue

                    if hood_z < 0 or hood_z >= arr.shape[2]:
                        if normalise_edges:
                            hood_normalise = True
                        continue

                    if nodata and arr[hood_y, hood_x, hood_z] == nodata_value:
                        if normalise_edges:
                            hood_normalise = True
                        continue

                    hood_values[hood_count] = arr[hood_y, hood_x, hood_z]
                    hood_weights[hood_count] = weights[idx_h]
                    hood_count += 1

                if hood_count == 0:
                    result[idx_y, idx_x, idx_z] = nodata_value
                    continue

                hood_values = hood_values[:hood_count]
                hood_weights = hood_weights[:hood_count]

                if hood_normalise:
                    hood_weights /= np.sum(hood_weights)

                result[idx_y, idx_x, idx_z] = hood_to_value(method, hood_values, hood_weights, nodata_value, center_value, value)

    return result


def convolve_array(
    arr: np.ndarray,
    offsets: np.ndarray,
    weights: np.ndarray,
    method: int = 1,
    nodata: bool = False,
    nodata_value: float = -9999.9,
    normalise_edges: bool = True,
    collapse: bool = False,
    value: Union[int, float, None] = None,
) -> np.ndarray:
    """
    Convolve an image with a function.

    Args:
        arr (numpy.ndarray): The input array to convolve.
        offsets (list of tuples): The list of offsets for the neighborhood
            used in the convolution.
        weights (list): The list of weights used in the convolution.

    Keyword Args:
        method (int=1): The method to use for the convolution.
            1: hood_sum
            2: hood_mode
            3: hood_max
            4: hood_min
            5: hood_contrast
            6: hood_quantile
            7: hood_standard_deviation
            8: hood_median_absolute_deviation
            9: hood_z_score
            10: hood_z_score_mad
            11: hood_sigma_lee
        nodata (bool=False): If True, nodata values are considered
            in the convolution.
        nodata_value (float=-9999.9): The value representing nodata.
        normalise_edges (bool=True): If True, the weights at the edges
            are normalised to sum to one. Only relavant for border pixels.
            Use false, if you are interested in the sum, otherwise you likely
            want to use True.
        collapse (bool=False): If True, the convolution results in a (height, width, 1)
            array. Otherwise, the convolution results in a (height, width, depth) applied
            channelwise.
        value (Union[int, float, None]=None): If not None, the value to use for the convolution.
            depending on the method specified.


    Returns:
        numpy.ndarray: The convolved array.
    """
    core_utils.type_check(arr, [np.ndarray], "arr")
    core_utils.type_check(offsets, [np.ndarray], "offsets")
    core_utils.type_check(weights, [np.ndarray], "weights")
    core_utils.type_check(method, [int], "method")
    core_utils.type_check(nodata, [bool], "nodata")
    core_utils.type_check(nodata_value, [float], "nodata_value")
    core_utils.type_check(normalise_edges, [bool], "normalise_edges")
    core_utils.type_check(collapse, [bool], "collapse")
    core_utils.type_check(value, [int, float, type(None)], "value")

    assert len(offsets) == len(weights), "offsets and weights must be the same length"
    assert method in range(1, len(METHOD_ENUMS)), "method must be between 1 and 11"
    assert arr.ndim in [2, 3], "arr must be 2 or 3 dimensional"

    if value is None:
        value = 0.5

    if arr.ndim == 2:
        arr = arr[:, :, np.newaxis]

    if collapse:
        return _convolve_array_collapse(
            arr,
            offsets,
            weights,
            method=method,
            nodata=nodata,
            nodata_value=nodata_value,
            normalise_edges=normalise_edges,
            value=value,
        )

    return _convolve_array(
        arr,
        offsets,
        weights,
        method=method,
        nodata=nodata,
        nodata_value=nodata_value,
        normalise_edges=normalise_edges,
        value=value,
    )
