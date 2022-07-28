weight = 4.8

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <=10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
#Ground Shipping Premium
cost_ground_premium = 125.00
#Drone Shipping
if weight <= 2:
  drone_ground = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_ground = weight * 9
elif weight > 6 and weight <=10:
  drone_ground = weight * 12
else:
  drone_ground = weight * 14.25
print(cost_ground)
print(cost_ground_premium)
print(drone_ground)