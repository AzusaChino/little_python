class Pascal:
    def gen(self, n):
        base = [1]
        for _ in range(1, n):
            base = [x + y for x, y in zip([0] + base, base + [0])]
        return base


if __name__ == "__main__":
    p = Pascal()
    print(p.gen(3))
