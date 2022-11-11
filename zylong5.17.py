while True:
    highwaynum = int(input("Please enter a US Interstate Highway route number: "))
    if (0 > highwaynum) or (999 <= highwaynum):
        continue
    elif highwaynum == 0:
        break
    else:  
        if highwaynum // 100 == 0:
            highwaytype = 'primary' 
        else: 
            highwaytype = 'auxiliary' 

        if highwaytype == 'primary':
            if highwaynum % 5 == 0:
                highwaysize = 'a long-distance arterial highway '
            else: 
                highwaysize = ''
            if highwaynum % 2 == 0:
                highwayorientation = 'east-west'
            else: 
                highwayorientation = 'north-south'
            print(f"Interstate {highwaynum} is {highwaysize}oriented {highwayorientation}.")

        if highwaytype == 'auxiliary':
            firstdigit = highwaynum // 100
            if firstdigit % 2 == 0:
                highwaytype1 = 'loop'
            else:
                highwaytype1 = 'spur'
            lasttwodigits = (highwaynum - ((highwaynum//100)*100))
            parenthighway = lasttwodigits
            print(f"Interstate {highwaynum} is a {highwaytype1} highway of Interstate {parenthighway}.")

