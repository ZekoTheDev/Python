# In this Program we have two functions.
# Function basePrice is used to calculate the base price of a price ticket based on the distance.
# Function finalPrice is used to calculate the final price of the train ticket by calculating discounts and checking if the trip is taking place during weekdays or the weekend

# Conditions for BasePrice():
# If distance is below or equals to 0, return €0
# If distance is below 50, charge €0.8 per kilometer
# If distance is above 50, add €15 to the base price. And charge €0.6 per kilometer.

# Conditions for finalPrice():
# If person is below 12 or 65 and older. Give them a 30% discount during weekdays and 35% during weekends.
# All the other ages will have no discount during weekdays, but will have a 40% discount during the weekends.

def basePrice(distance):
    if distance <= 0:
        return 0

    elif distance <= 50:
        return distance * 0.8

    elif distance > 50:
        return 15 + (distance * 0.60)


def finalPrice(age, weekend, distance):
    price = basePrice(distance)

    if weekend == False:
        if age < 12 or age >= 65:
            return price * 0.7
        else:
            return price

    else:
        if age < 12 or age >= 65:
            return price * 0.65

        else:
            return price * 0.60
