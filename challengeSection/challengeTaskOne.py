def temperatureConverter():
    tempCelc = float(input("Input the temperature value in celcius: "))
    celcToFahr = tempCelc * 9/5 + 32
    print(f'{tempCelc} celcius is {celcToFahr} fahrenheit')

    tempFahr = float(input("Input the temperature value in fahrenheit: "))
    fahrToCelc = (tempFahr - 32) * 5/9