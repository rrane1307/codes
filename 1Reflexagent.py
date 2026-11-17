
environment = {'A': 'Dirty', 'B': 'Dirty'}

location = 'A'

while True:

    print("Current Location:", location)
    print("Environment:", environment)

    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Goal achieved! Both rooms are clean.")
        break

    if environment[location] == 'Dirty':
        print("Action: SUCK")
        environment[location] = 'Clean'

    else:

        if location == 'A':
            print("Action: MOVE RIGHT")
            location = 'B'

        else:
            print("Action: MOVE LEFT")
            location = 'A'
            
    print("-" * 40)
    print("\nRational Behaviour Analysis")
    print("1. Cleans a room immediately if dirty.")
    print("2. Moves only when current room is already clean.")
    print("3. Stops after both rooms are clean.")
    print("Hence the agent behaves rationally for this environment.")