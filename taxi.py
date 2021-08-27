from Meter import Meter

if __name__ == "__main__":
    print("距離を(km)で記載してください。")
    kyori = float(input()) * 1000
    if Meter.is_validate(kyori):
        price = Meter.calc_price(kyori)
        print(price)
    else:
        print("不正な距離です")
