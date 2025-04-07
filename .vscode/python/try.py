while True:
    try:
        weight = float(input("請輸入體重（kg）："))
        height = float(input("請輸入身高（cm）："))
        height /= 100
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            print("您的BMI為 {:.2f}，為體重過輕。".format(bmi))
        elif 18.5 <= bmi < 24:
            print("您的BMI為 {:.2f}，為體重正常。".format(bmi))
        elif 24 <= bmi < 27:
            print("您的BMI為 {:.2f}，為過重。".format(bmi))
        elif 27 <= bmi < 30:
            print("您的BMI為 {:.2f}，為輕度肥胖。".format(bmi))
        elif 30 <= bmi < 35:
            print("您的BMI為 {:.2f}，為中度肥胖。".format(bmi))
        else:
            print("您的BMI為 {:.2f}，為重度肥胖。".format(bmi))
        break
    except:
        print("輸入有誤，請重新輸入。")
