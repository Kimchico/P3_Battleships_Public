def coordinates(blobs):
    coordinates = []
    for blob in blobs:
        x = []
        y = []
        for pixel in blob:
            x.append(pixel[-1])
            y.append(pixel[0])
        x.sort(); y.sort()

        coordinates.append(((x[0], y[0]), (x[-1], y[-1])))
    return coordinates