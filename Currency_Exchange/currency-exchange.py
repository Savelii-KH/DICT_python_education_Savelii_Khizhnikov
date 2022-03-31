import requests
import sys
import simplejson


class Requests:
    def __init__(self, const_currency):
        self.const_currency = const_currency
        self.currency = input("• ").lower().strip()
        if self.currency == "exit":
            sys.exit()
        try:
            self.value = float(input("• "))
        except ValueError:
            print("Only numerical values")
        try:
            self.r = requests.get(f"http://www.floatrates.com/daily/{self.const_currency}.json").json()
        except simplejson.errors.JSONDecodeError:
            print("Incorrect currency!")
        if self.const_currency == "usd":
            self.course = {"usd": 1, "eur": self.r["eur"]["rate"]}
        elif self.const_currency == "eur":
            self.course = {"usd": self.r["usd"]["rate"], "eur": 1}
        else:
            try:
                self.course = {"usd": self.r["usd"]["rate"], "eur": self.r["eur"]["rate"]}
            except KeyError:
                pass
            except AttributeError:
                pass

    def cache_check(self):
        print("Checking the cache...")
        if self.currency in self.course.keys():
            self.cache_read()
        else:
            self.cache_write()

    def cache_write(self):
        try:
            while True:
                print(f"""Sorry, but it is not in the cache!
You received {round(self.r[self.currency]["rate"] * self.value, 2)} {"".join(self.currency).upper()}.
""")
                self.course.update({self.currency: self.r[self.currency]["rate"]})
                break
        except AttributeError:
            print("Incorrect attribute")
        except KeyError:
            print("Incorrect attribute")

    def cache_read(self):
        print(f"""It is in the cache!
You received {round(self.course[self.currency] * self.value, 2)} {"".join(self.currency).upper()}.\n""")

    def main(self):
        self.cache_check()
        while True:
            self.currency = input("• ").lower().strip()
            try:
                self.value = float(input("• "))
                self.cache_check()
            except ValueError:
                print("Only numerical values")


if __name__ == "__main__":
    cc = input("• ").lower().strip()
    Requests(cc).main()
