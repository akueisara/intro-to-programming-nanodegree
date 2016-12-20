# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
# 1. Wait for 10 seconds
# 2. Play a youtube video on the browser
# 3. Repeat step 1 and 2 three times

# Your code here.
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1
