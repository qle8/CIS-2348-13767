# Name: Quang Le
# Student ID: 1768324


if __name__ == "__main__":
    print("Davy's auto shop services")
    services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12, "-": 0}
    print("Oil change -- ${}".format(services["Oil change"]))
    print("Tire rotation -- ${}".format(services["Tire rotation"]))
    print("Car wash -- ${}".format(services["Car wash"]))
    print("Car wax -- ${}".format(services["Car wax"]))
    print()
    services_1 = input("Select first service:\n")
    services_2 = input("Select second service:\n")
    total = services[services_1] + services[services_2]
    print()
    print("Davy's auto shop invoice")
    print()
    if services_1 == "-":
        print("Service 1: No service")
    else:
        print("Service 1: {}, ${}".format(services_1, services[services_1]))
    if services_2 == "-":
        print("Service 2: No service")
    else:
        print("Service 2: {}, ${}".format(services_2, services[services_2]))
    print()
    print("Total: ${}".format(total))
