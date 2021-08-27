import math


class Meter:

    @classmethod
    def is_validate(cls, kyori):
        if kyori <= 0:
            return False
        return True

    @classmethod
    def calc_price(cls, kyori):
        # 初乗りの距離
        hatunori_kyori = 1000
        # 初乗り料金
        hatunori_price = 600
        # メータが回る距離
        add_meter = 500
        # 加算値段
        meter_price = 300

        add_price = math.ceil((kyori - hatunori_kyori) / add_meter) * meter_price
        add_price = 0 if add_price < 0 else add_price
        return hatunori_price + add_price
