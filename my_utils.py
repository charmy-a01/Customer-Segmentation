
class DataError(Exception):
    pass

def offer(segment):
    offers = {"Champions": "Early access and loyalty points",
              "Loyal": "Bundle discount",
              "Occasional": "10% coupon",
              "Low value": "Win-back voucher"}
    return offers.get(segment, "Newsletter")

def percent(part, total):
    return round(part / total * 100, 1)
