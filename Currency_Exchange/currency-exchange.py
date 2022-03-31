import requests
# import simplejson
# import sys


class Requests:
    def __init__(self, const_currency, currency, value):
        self.const_currency = const_currency
        self.currency = currency
        self.value = value
        self.course = []
        self.course_usd_eur = []
        self.cache_check()

    def cache_check(self):
        if self.const_currency[0] in self.course:
            self.cache_read()
        else:
            self.cache_write()

    def cache_read(self):
        print(f"""It's in cache.
You received {self.currency}""")

    def cache_write(self):
        r = requests.get(f"http://www.floatrates.com/daily/{self.const_currency[0]}.json").json()
        self.course_usd_eur.append({"usd": r.get('usd').get('rate'), "eur": r.get('eur').get('rate')})
        self.course.append({self.const_currency: self.course_usd_eur})
        self.course_usd_eur.clear()
        print(f"""It's not in cache.
You received {self.currency}""")
        print(self.course)


if __name__ == "__main__":
    cc = input("• ").lower().split()
    while True:
        c = input("• ").lower().split()
        try:
            v = float(input("• "))
            request = Requests(cc, c, v)
        except ValueError:
            print("Only numerical values")
