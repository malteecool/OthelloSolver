boardsize = 10


def moveNorth(board, lookFor, row, col):
    """
    Check for markers in the north direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """
    if row < 1 or board[row-1][col] != lookFor:
        return [-1, -1]

    coords = []

    i = row - 1

    while board[i][col] == lookFor:
        coords.append([i, col])
        i -= 1

    if board[i][col] != lookFor and board[i][col] != 'E':
        return coords
    else:
        return [-1, -1]


def moveEast(board, lookFor, row, col):
    """
    Check for markers in the east direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """
    if col >= boardsize or board[row][col+1] != lookFor:
        return [-1, -1]

    coords = []

    i = col + 1

    while board[row][i] == lookFor:
        coords.append([row, i])
        i += 1

    if board[row][i] != lookFor and board[row][i] != 'E':
        return coords
    else:
        return [-1, -1]


def moveSouth(board, lookFor, row, col):
    """
    Check for markers in the south direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """
    if row >= boardsize or board[row+1][col] != lookFor:
        #print("South: not what we are looking for!")
        return [-1, -1]

    coords = []

    i = row + 1

    while board[i][col] == lookFor:
        coords.append([i, col])
        i += 1

    if board[i][col] != lookFor and board[i][col] != 'E':
        return coords
    else:
        return [-1, -1]





def moveWest(board, lookFor, row, col):
    """
    Check for markers in the west direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """
    if col < 1 or board[row][col-1] != lookFor:
        return [-1, -1]

    coords = []

    i = col - 1

    while board[row][i] == lookFor:
        coords.append([row, i])
        i -= 1

    if board[row][i] != lookFor and board[row][i] != 'E':
        return coords
    else:
        return [-1, -1]


def moveNorthwest(board, lookFor, row, col):
    """
    Check for markers in the north west direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """

    if (row < 1 or col < 1) or board[row-1][col-1] != lookFor:
        return [-1, -1]

    coords = []

    i = row - 1
    j = col - 1

    while board[i][j] == lookFor:
        coords.append([i, j])
        i -= 1
        j -= 1

    if board[i][j] != lookFor and board[i][j] != 'E':
        return coords
    else:
        return [-1, -1]


def moveNortheast(board, lookFor, row, col):
    """
    Check for markers in the north east direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """
    if (row < 1 or col >= boardsize) or board[row-1][col+1] != lookFor:
        return [-1, -1]

    coords = []

    i = row - 1
    j = col + 1

    while board[i][j] == lookFor:
        coords.append([i, j])
        i -= 1
        j += 1

    if board[i][j] != lookFor and board[i][j] != 'E':
        return coords
    else:
        return [-1, -1]


def moveSouthwest(board, lookFor, row, col):
    """
    Check for markers in the south west direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """

    if (row >= boardsize or col < 1) or board[row+1][col-1] != lookFor:
        return [-1, -1]

    coords = []

    i = row + 1
    j = col - 1

    while board[i][j] == lookFor:
        coords.append([i, j])
        i += 1
        j -= 1

    if board[i][j] != lookFor and board[i][j] != 'E':
        return coords
    else:
        return [-1, -1]


def moveSoutheast(board, lookFor, row, col):
    """
    Check for markers in the south east direction to 
    flip.
    If no marker was found the that direction,
    or if the opponents markers should not be flipped,
    return array of negative values.

    :param lookFor: The color to look for.
    :param row: the starting row
    :param col: the starting col
    :return: list of the found coordinates
    """

    if (row >= boardsize or col >= boardsize) or board[row+1][col+1] != lookFor:
        return [-1, -1]

    coords = []

    i = row + 1
    j = col + 1

    while board[i][j] == lookFor:
        coords.append([i, j])
        i += 1
        j += 1

    if board[i][j] != lookFor and board[i][j] != 'E':
        return coords
    else:
        return [-1, -1]
