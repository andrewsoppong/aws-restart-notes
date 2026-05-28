#import the OS module 
import os 

#You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes
import subprocess

#This show the directory contents
os.system("ls")

#Exercise 2: Using subprocess.run 
subprocess.run(["ls"])

#Exercise 3: Using subprocess.run with two arguments
subprocess.run(["ls","-l"])

#Exercise 4: Using subprocess.run with three arguments
subprocess.run(["ls","-l","car_fleet.csv"])

#Exercise 5: Retrieving system information 
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Exercise 6: Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])