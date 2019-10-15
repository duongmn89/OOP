class bmi:
    height = 0.0
    weight  = 0.0
    bodybmi = 0.0
    def __init__(self):
        self.height = 0.0
        self.weight = 0.0
        self.bodybmi = 0.0
    def __init__(self, height, weight):
        if weight >= 0 and weight <= 500:
            self.weight = weight
        if height >= 0 and height <= 3:
            self.height = height
    def caculateBMI(self):
        if self.height == 0.0 or self.weight == 0.0:
            return 1
        else:
            self.bodybmi = (self.weight/(self.height*self.height))
            print("Chi so BMI la " + self.bodybmi.__str__())
    def categoryBMI(self):
        if self.caculateBMI() == 1:
            print("Ban nhap thong tin khong hop ly")
        elif self.bodybmi < 18.5:
            print("Ban thieu can")
        elif self.bodybmi >= 18.5 and self.bodybmi < 25:
            print("Ban trung binh")
        elif self.bodybmi >= 25 and self.bodybmi < 30:
            print("Ban thua can")
        elif self.bodybmi >= 30:
            print("Ban beo phi")

def main():
    user_height = input("Nhap chieu cao theo m")
    user_weight = input("Nhap can nang theo kg")
    try:
        height = float (user_height)
        weight = float (user_weight)
        p1 = bmi(height, weight)
        p1.categoryBMI()
    except ValueError:
        print("Gia chi nhap vao khong phai float")

if __name__ == '__main__':
    main()
