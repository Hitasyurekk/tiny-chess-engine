# tiny-chess-engine

A chess engine in under 4 KB of Python 3.13 (standard library only), entered in
make.fun's [tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty.

- 10x12 mailbox board, flipped after every move so the side to move is upper case
- piece-square tables, with an endgame king table and passed-pawn bonus
- alpha-beta with quiescence, transposition table, null move and late move reductions
- fixed node budget per move: deterministic, never reads a clock

```sh
MAKEFUN_ENV_URL=http://<env> python3 main.py
```

MIT licensed.
