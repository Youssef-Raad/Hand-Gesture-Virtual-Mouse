import numpy as np

def get_angle(a, b, c):
    """
    Calculates the angle (in degrees) between three 2D points (a, b, c),
    where point 'b' acts as the vertex.
    
    Parameters:
        a (tuple/list): Coordinates of the first point [x, y].
        b (tuple/list): Coordinates of the vertex point [x, y].
        c (tuple/list): Coordinates of the end point [x, y].
        
    Returns:
        float: Absolute angle in degrees formed at point b.
    """
    # Calculate angle difference in radians using arctan2
    rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    
    # Convert radians to degrees and take the absolute value
    angle = np.abs(np.degrees(rad))
    return angle


def get_distance(landmark_list):
    """
    Calculates the Euclidean distance between two landmark points and maps
    the distance to a normalized range [0, 1000].
    
    Parameters:
        landmark_list (list): List containing at least two 2D coordinate pairs [(x1, y1), (x2, y2)].
        
    Returns:
        float: Mapped distance value in the range [0, 1000].
    """
    if len(landmark_list) < 2:
        return 0

    # Unpack the x, y coordinates for the two landmark points
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]

    # Compute Euclidean distance using hypotenuse formula
    L = np.hypot(x2 - x1, y2 - y1)
    
    # Interpolate distance from normalized scale [0, 1] to target range [0, 1000]
    return np.interp(L, [0, 1], [0, 1000])