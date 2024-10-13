# function to calculate the usage
def usage_percentage(own, avarage, week):
    # calculate total units
    total_units = avarage * 22
    # calculate avarage
    week_average = own / (total_units / 100)
    # print results
    print("Week: " + str(week))
    print("Percentage:" + str(round(week_average, 2)) + "%")
    print("Total units:" + str(total_units) + "\n")
    
# call function with week numbers    
usage_percentage(0, 2, 38)
usage_percentage(0, 3, 39)
usage_percentage(0, 9, 40)
usage_percentage(0, 16, 41)

# so we can see the output on the screen
input("Press enter to exit")
