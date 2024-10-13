#gas usage in units
gas_usage = {
  "Week 38" : {
    "own" : 0,
    "average" : 2
  },
  "Week 39" : {
    "own" : 0,
    "average" : 3
  },
  "Week 40" : {
    "own" : 0,
    "average" : 9
  },
}

# loop all the entries in the dictionary
for week in gas_usage:
    total_units = gas_usage[week]["average"] * 22
    week_average = gas_usage[week]["own"] / (total_units / 100)
    # print results
    print(week)
    print("Percentage:" + str(round(week_average, 2)) + "%")
    print("Total units:" + str(total_units))
    print(" ")
    
# so we can see the output on the screen
input("Press enter to exit")
