import sys
import csv

childcost = 25
adultcost = 100
seniorcost = 75
tickets = []

def BuyTickets():
    while (True):

        print("How many Childnern?")
        try:

            child = int(input())
            break
        except:
            print("not a number")

    while (True):

        print("How many Adults?")
        try:
            global globaladults
            adult = int(input())
            break
        except:
            print("not a number")

    while (True):

        print("How many Seniors?")
        try:

            senior = int(input())
            break
        except:
            print("not a number")





    totalsum = (child * childcost) + (adult * adultcost) + (senior * seniorcost)
    while(True):

        print("Total sum is: ",format(totalsum)+"\nDo you want to buy y/n")
        strin = input()
        if(strin == "y"):

            ts = [child,adult,senior]
            tickets.append(ts)
            FileHandler("write")

            break


        elif(strin =="n"):

            print("Order canceled")
            break

        else:

            print("you made an oppsy")


def FileHandler(ToDo):



    if(ToDo == "read"):
        with open("data.csv", "r") as csv_file:

            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                return row



    if (ToDo == "write"):
        with open("data.csv", "w") as csv_file:

            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(tickets)


def Info():
    childsum = 0
    adultsum = 0
    seniorsum = 0
    j = []

    info = FileHandler("read")
    for x in info:
        l = format(x).replace(",", "")
        childsum = childsum + int(l[1])
        adultsum = adultsum + int(l[3])
        seniorsum = seniorsum + int(l[5])

    totalchild = childsum * childcost
    totaladult = adultsum * adultcost
    totalsenior = seniorsum * seniorcost
    totalsum = totalchild + totaladult + totalsenior
    ticketamount = childsum + adultsum + seniorsum
    print(format(totalsum) + "kr profit")
    print("from " + format(ticketamount) + " tickets sold")
    print("childre tickets: " + format(childsum) + " adult tickets: " + format(adultsum) + " senior tickets: " + format(seniorsum))



print("Welcome to ticket sales")
while(True):

    tickets = FileHandler("read")
    if(tickets == None):
        tickets = []
    print("input a command")
    inStr = input().lower()

    if (inStr == "buy"):

        BuyTickets()

    elif(inStr == "refund"):
        i = 0
        info = FileHandler("read")
        for x in info:
            l = x
            print("ID: " + format(i) + " " + format(l))
            i = i + 1
        print("please choose id of the ticket you bought")
        while(True):
            try:
                ind = int(input())
                tickets.pop(ind)
                FileHandler("write")
                break
            except:
                print("not a number")



    elif(inStr == "info"):
        Info()

    elif(inStr == "quite"):

        sys.exit(0)

    elif(inStr == "help"):

        print("\"buy\" - Lets you buy tickets\n"
              "\"refund\" - lets you refund you ticket/s\n"
              "\"info\" - show the data of the sales\n"
              "\"help\" - show all the commands\n"
              "\"quite\" - exits you from the program\n")

    else:

        print("not a know command")



