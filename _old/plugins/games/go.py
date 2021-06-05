from copy import deepcopy


class Go:
    """
    术语参考: https://senseis.xmp.net/?ChineseGoTerms
    """
    def __init__(self, way, katago=False):
        self.way = way
        self.board = [[None for _ in range(way)] for _ in range(way)]
        self.dead = set()

    def reset_board(self):
        self.board = [[None for _ in range(self.way)] for _ in range(self.way)]

    def get_board(self):
        return self.board

    def move(self, player, x, y):              # 手
        if self.playing_stone(player, x, y):
            self.remove_from_board(player)
            return True
        else:
            return False

    def playing_stone(self, player, x, y):      # 落子
        if self.board[x][y] is None and self.has_chi(player, x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def end_game(self):
        """
        强制点目

        :return: False - 棋局继续, 0 - player0 胜利, 1 - player1 胜利, True - 和棋
        """
        _board = deepcopy(self.board)

        for _player in (1, 0):
            _board_t = [[_player for _ in range(self.way + 2)]] + \
                       [[_player] + b + [_player] for b in _board] + \
                       [[_player for _ in range(self.way + 2)]]
            for x in range(1, self.way+1):
                for y in range(1, self.way+1):
                    if _board_t[x][y] is None:
                        if _board_t[x-1][y] == _board_t[x+1][y] == _board_t[x][y-1] == _board_t[x][y+1] == _player:
                            _board[x-1][y-1] = _player

        for x in range(self.way):
            for y in range(self.way):
                if _board[x][y] is None:
                    return False

        _test = sum(sum(b) for b in _board)
        if _test > self.way ** 2:
            return 1
        elif _test < self.way ** 2:
            return 0
        else:
            return True

    def has_chi(self, player, x, y):
        """
        判断该位置是否有气

        :param player: 0 / 1
        :param x, y: 要判断的棋盘位置
        :return: True - 有气
        """

        _board = deepcopy(self.board)
        _enemy = 1 - player
        _board = [[_enemy for _ in range(self.way + 2)]] +\
                 [[_enemy] + b + [_enemy] for b in _board] +\
                 [[_enemy for _ in range(self.way + 2)]]
        _x, _y = x + 1, y + 1
        _board[_x][_y] = player

        _set = set()
        _set.add((_x, _y))
        _sta = [(_x, _y)]
        while _sta:
            x, y = _sta.pop()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if _board[x+dx][y+dy] is None:
                    return True
                elif _board[x+dx][y+dy] == player and (x+dx, y+dy) not in _set:
                    _sta.append((x+dx, y+dy))
                    _set.add((x+dx, y+dy))
        self.dead = _set
        return False

    def remove_from_board(self, player):
        for x in range(self.way):
            for y in range(self.way):
                if self.board[x][y] == player and not self.has_chi(player, x, y):
                    for _x, _y in self.dead:
                        self.board[_x][_y] = None


if __name__ == '__main__':
    go = Go(way=4)
    go.board = [
        [1, 0, 0, ],
        [1, None, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print(go.has_chi(0, 1, 1))
    # print(go.end_game())
