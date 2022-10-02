import os
import datetime

def runnerRegistration (name):
    # Make a string that is modified based on the name of the runner and on which time the runner arrives at the finish
    today = datetime.datetime.today()
    notation = today.strftime(f"%a %d %b %Y, %H:%M:%S, {name}" )

    # Receive Boolean value. True = file exists. False = file does not exist
    file = 'RunnerRegistatration.txt'
    fileExists = os.path.exists(file)

    # Check if the file exists, if it exists move the cursor to a new line and write the new data
    if fileExists:
        with open("RunnerRegistatration.txt", "a+") as file:
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file.write("\n")
                file.write(notation)

                # Create a new file and write the down the time if the previous if condition was not met
    else:
        newfile = open("RunnerRegistatration.txt","w+")
        newfile.write(notation)
        newfile.close()

# Call function with "Usain Bolt" as argument
print(runnerRegistration("Usain Bolt"))



