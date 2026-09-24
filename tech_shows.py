tv_shows = ["Silicon Valley", "Halt and Catch Fire", "Blackberry", "The Billion Dollar Code", "Mr. Robot", "The IT Crowd", "WeCrashed", "The Social Network", "Severence", "Pirates of Silicon Valley" ]

print (f"The first show is: {tv_shows[0]}")
print (f"The last show is: {tv_shows[-1]}")
#OR
print (f"The last show is: {tv_shows[len(tv_shows)-1]}")
tv_shows[6] = "The Dropout"
tv_shows[7] = "Black Mirror"
print(f"The 5th to ninth shows in the list are: {tv_shows[4:9]}")