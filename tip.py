def calculate_tip(cost, tip_fraction):
    try:
        tip_percent = float(tip_fraction)
        tip_percent >= 0
    except:
        print("The tip must be a number between 0 and 1")

    O =  cost*( 1+tip_percent );
    return O


print(calculate_tip(100, 0.18))
