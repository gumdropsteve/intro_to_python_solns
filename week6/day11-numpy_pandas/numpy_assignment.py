import numpy as np

def normalize_1d(np_array):
    """Normalize the inputted 1D ndarray.

    Here we're going to subtract off the mean of the array
    and divide by the standard deviation.

    Args:
        np_array: ndarray
    """

    normalized_array = (np_array - np_array.mean()) / np_array.std()
    return normalized_array

def normalize_2d(np_array):
    """Normalize the inputted 2D ndarray along the columns.

    For each column, we're going to subtract off its mean and divide
    by its standard deviation.

    Args:
        np_array: ndarray
    """

    normalized_array = (np_array - np_array.mean(axis=0)) / np_array.std(axis=0)
    return normalized_array

def np_array_creation(num_cols, num_rows, fill_value):
    """Create a numpy array of the inputted shape filled with the inputted value.

    Args:
        num_cols: int
        num_rows: int
        fill_value: int
    """

    return_array = np.ones((num_rows, num_cols)) * fill_value
    return return_array

def perform_math(np_array, my_int, math_operator):
    """Perform the inputted operation using the inputted int on an ndarray.

    Take the inputted mathematical operator, and then perform that operation
    with the inputted integer, on the inputted numpy array. For example, if
    2 and + are inputted, then add 2 to each element of the array.

    Args:
        np_array: ndarray
        my_int: int
        math_operator: str
    """


    if math_operator == "+":
        np_array += my_int
    elif math_operator == "-":
        np_array -= my_int
    elif math_operator == "/":
        np_array = np_array / my_int
    elif math_operator == "*":
        np_array *= my_int

    return np_array

def create_random_float_array(num_elements):
    """Return an array num_elements long with random floating point nums from 0-1

    Args:
        num_elements: int
    """

    random_array = np.random.random(num_elements)
    return random_array

def create_shaped_float_array(num_rows, num_cols):
    """Return an array of the specified shape, full with random
    floating point nums from 0-1

    Args:
        num_rows: int
        num_cols: int
    """

    random_array = np.random.random(num_rows * num_cols).reshape(num_rows, num_cols)
    return random_array

def random_sample(np_array, num_elements):
    """Randomly sample num_elements from np_array.

    Args:
        np_array: ndarray
        num_elements: int
    """

    sampled_elements = np.random.choice(np_array, size=num_elements)
    return sampled_elements

def replace_max(np_array):
    """Replace the maximum element in the array with 0.

    Args:
        np_array: ndarray
    """

    np_array[np_array.argmax()] = 0
    return np_array

def return_cum_sum(num_elements):
    """Return the cumulative sum of all numbers up to the inputted number,
    but using a numpy array.

    Args:
        num_elements: int
    """

    np_array = np.arange(num_elements + 1)
    cum_sum = np_array.cumsum()
    return cum_sum[-1]

def return_mat_multiplication(np_array1, np_array2):
    """Return the matrix multiplication of the inputted arrays.

    Args:
        np_array1: ndarray
        np_arary2: ndarray
    """

    return np.dot(np_array1, np_array2)

def return_elementwise_multiplication(np_array1, np_array2):
    """Return the element-wise multiplication of the inputted arrays.

    Args:
        np_array1: ndarray
        np_array2: ndarray
    """

    return np_array1 * np_array2

def return_top_5(np_array):
    """Return the top 5 elements of the inputted array"""

    np_array.sort()
    return np_array[-5:]

def return_smallest_5(np_array):
    """Return the smallest 5 elements in each column."""

    np_array.sort(axis=0)
    return np_array[:5, :]

def extra_credit_1(inputted_int):
    """Return the cumulative sum of a square matrix of elements from 0 up to
    inputted_int

    This function involves three steps:
        1. Create an array of numbers from 0 up to the inputted_int
        2. Reshape it to the largest n * n array that it can be, discarding
        extra elements
        3. Returns the cumulative sum of the column means

    Args:
        inputted_int: int
    """

    arr = np.arange(inputted_int)
    n_shape = int(inputted_int ** 0.5)

    reshaped_arr = arr[:n_shape ** 2].reshape(n_shape, n_shape)
    cum_sum= reshaped_arr.mean(axis=0).cumsum(axis=0)

    return cum_sum[-1]
