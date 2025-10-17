class Solution:
    A = 26

    def maxPartitionsAfterOperations(self, s, k):
        if k == self.A:
            return 1

        n = len(s)
        ar = [0] * n
        ur = [0] * n
        u = 0
        cu = 0
        a = 1

        # проход справа налево
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - 97
            if (u & (1 << c)) == 0:
                if cu == k:
                    cu = 0
                    u = 0
                    a += 1
                u |= (1 << c)
                cu += 1
            ar[i] = a
            ur[i] = u

        al = 0
        a = ar[0]
        l = 0

        while l < n:
            u = 0
            cu = 0
            ub = 0
            ut = 0
            last = -1
            r = l

            while r < n:
                c = ord(s[r]) - 97
                if (u & (1 << c)) == 0:
                    if cu == k:
                        break
                    ub = u
                    last = r
                    u |= (1 << c)
                    cu += 1
                elif cu < k:
                    ut |= (1 << c)
                r += 1

            if cu == k:
                if last - l > bin(ub).count('1'):
                    a = max(a, al + 1 + ar[last])
                if last + 1 < r:
                    if last + 2 >= n:
                        a = max(a, al + 2)
                    else:
                        if bin(ur[last + 2]).count('1') == k:
                            can = ((1 << self.A) - 1) & ~u & ~ur[last + 2]
                            if can > 0:
                                a = max(a, al + 1 + 1 + ar[last + 2])
                            else:
                                a = max(a, al + 1 + ar[last + 2])
                            c1 = ord(s[last + 1]) - 97
                            if (ut & (1 << c1)) == 0:
                                a = max(a, al + 1 + ar[last + 1])
                        else:
                            a = max(a, al + 1 + ar[last + 2])

            l = r
            al += 1

        return a
