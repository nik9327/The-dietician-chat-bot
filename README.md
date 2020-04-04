# The-dietician-chat-bot
This project is to provide an bot which suggests diet plan based on user’s height, weight, age and exercise one perform.

# Objective

The system measures a user’s Basal Metabolic Rate (BMR)  using his/her height and weight, age. The system has been 
trained with large dataset of food varieties and their nutritional values. Once the system has the user’s Basal Metabolic
Rate(BMR),it needs to know eating habit of the user. The user has to provide information about the Activities Or Exercise
he/shepreform, Age, Weight, Height. Once the system has this data, it suggests the user a diet plan as per the user’s Basal 
Metabolic Rate (BMR) . If the user doesn’t like the diet plan the system modifies the diet plan keeping nutritional value 
the same and gives you a suitable diet for breakfast, lunch, snacks, dinner, and other diet . This is done to ensure that 
the user likes the diet suggested to him. Thus the need to travel to a dietician to know the diet plan can be removed. The
users can get a diet plan based on their Basal Metabolic Rate (BMR)  if they know their height and weight and age. No need 
to pay a visit to local dietician any more. 

# Methodology Used

## For the proposed project, a series of steps were followed for the system to recommend a diet plan.

#### Step 1: Input details from the user: Age (in years), Weight (in kg), Height (in cm's) and daily exercise level.

#### Step 2: Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict Equations: Men BMR= 88.362 + (13.397 * weight in kg) + (4.799 * height in cm) – (5.677 * age in years) Women BMR = 447.593 + (9.247 * weight in kg) + (3.099 * height in cm) – (4.330 * age in years)

#### Step 3: Calculate the calorie intake using the following table:

#### Exercise level Daily Calories Required (Kcal/day) Little to no exercise Daily kilocalories needed = BMR x 1.2 Light exercise(1–3 days per week) Daily kilocalories needed = BMR x 1.375 Moderate exercise (3–5 days per week) Daily kilocalories needed = BMR x 1.55 Heavy exercise (6–7 days per week) Daily kilocalories needed = BMR x 1.725 Very heavy exercise (twice per day, extra heavy workouts) Daily kilocalories needed = BMR x 1.9

#### Step 4: click on submit to view diet chart or you can clear the entry using entry button

# Conclusion

The users can get a diet plan based on their Basal Metabolic Rate (BMR)  if they know their height and weight and age. Thus the need to travel to a dietician to know the diet plan can be removed. No need to pay a visit to local dietician any more. 
