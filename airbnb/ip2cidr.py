import unittest


class IpToCidr:

    def ip_to_int(self, ip):
        ip = ip.split(".")
        res = 0
        for val in ip:
            res = (res << 8) + int(val)
        return res

    def convert(self, val, n):
        res = ["0"] * 4
        for i in range(3, -1, -1):
            res[i] = str(val & 255)
            val = val >> 8
        n = 33 - n.bit_length()
        return ".".join(res) + "/" + str(n)

    def ip_to_cidr(self, ip, n):
        val = self.ip_to_int(ip)
        res = []
        while n > 0:
            temp = val & -val
            if temp == 0:
                temp = 32
            while temp > n:
                temp = temp // 2

            res.append(self.convert(val, temp))
            n -= temp
            val += temp
        return res


class Test(unittest.TestCase):
    def test(self):
        solution = IpToCidr()
        self.assertEqual(["1.1.1.0/30"], solution.ip_to_cidr("1.1.1.0", 4))
        self.assertEqual(["1.1.1.1/32", "1.1.1.2/31", "1.1.1.4/32"], solution.ip_to_cidr("1.1.1.1", 4))
        self.assertEqual(["1.1.1.255/32", "1.1.2.0/31", "1.1.2.2/32"], solution.ip_to_cidr("1.1.1.255", 4))
        self.assertEqual(["0.0.0.0/31"], solution.ip_to_cidr("0.0.0.0", 2))
