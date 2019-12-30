def is_leap(year):
    #leap = 0
    # Write your logic here
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                print("Year is leap")
            else:
                print("Year is not leap")
        else:
            print("Year is leap")
    else:
        print("Year is not leap")

    return is_leap(year)
year = int(input())
print(is_leap(year))