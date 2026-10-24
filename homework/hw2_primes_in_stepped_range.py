"""List numbers in a stepped range, validate input, and mark which ones are prime."""

from math import floor, sqrt

sta = input("Start number: ")
end = input("End number: ")
stp = input("Step number: ")

count = 0
prime = 0
num = ""

if sta.isnumeric() == True and end.isnumeric() == True and stp.isnumeric() == True:
    sta = float(sta)
    end = float(end)
    stp = float(stp)

    if sta == floor(sta) and end == floor(end) and stp == floor(stp) and sta >= 1 and end >= 1 and stp >= 1 and end > sta:
        sta = int(sta)
        end = int(end)
        stp = int(stp)

        for i in range(sta, end+1, stp):

            if i % 2 == 1 and i != 1 and i != 3:

                if floor(sqrt(i)) >= 3:
                    subcount = 0

                    for j in range(3, floor(sqrt(i))+1, 2):

                        if i % j != 0 and subcount == 0:
                            pass
                        else:
                            subcount = subcount + 1

                    if subcount == 0:
                        num = num + "%s" % i + "*"
                        count = count + 1
                        prime = prime + 1

                    else:
                        num = num + "%s" % i
                        count = count + 1

                else:
                    num = num + "%s" % i + "*"
                    count = count + 1
                    prime = prime + 1
            elif i == 2 or i == 3:
                num = num + "%s" % i + "*"
                count = count + 1
                prime = prime + 1

            else:
                num = num + "%s" % i
                count = count + 1

            if i != (end-((end-sta) % stp)):
                num = num + ", "
            else:
                pass
        print("Starting from %d and ending at %d with a step of %d, there are a total of %d numbers." % (sta, end, stp, count))
        print("Among them, %d are prime." % prime)
        print("Numbers:", num)
    else:
        print("Input ERROR!!")

else:
    print("Input ERROR!!")
