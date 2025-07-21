the_weather = input("What's the weather like today? (sunny/rainy/cold): ") 
if the_weather == "sunny":
    print("Wear a t-shirt and sunglasses", the_weather)
elif the_weather == "rainy":
    print("Don't forget your umbrella and a raincoat", the_weather)
elif the_weather == "cold":
    print("Make sure to wear a warm coat and a scarf", the_weather)
else:
    print("Sorry, I don't have recommendations for this weather")