import numpy as np

with open("input", 'r') as dfh:

    # All of the measurements
    measurements = list(int(depth.strip()) for depth in dfh.readlines())

    # Make Sliding Window using np.convolve()
    sw_3 = np.convolve(measurements, np.ones(3), 'valid')

    increase = 0
    previous = sw_3[0]
    for window in sw_3[1:]:
            if window > previous:
                    increase += 1
            previous = window

    print(increase)
