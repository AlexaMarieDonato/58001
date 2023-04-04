class DistanceConversion:
    def __init__(self, distance):
        self.__dist = distance

    def MeterToCentimeter(self):
        print(self.__dist * 100, "centimeters")

    def MeterToKilometer(self):
        print(self.__dist / 1000, "kilometers")

    def MeterToInch(self):
        print(self.__dist * 39.37, "inches")

distanceInMeter = DistanceConversion(float(input("Enter the measurement in Meters: ")))
distanceInMeter.MeterToCentimeter()
distanceInMeter.MeterToKilometer()
distanceInMeter.MeterToInch()
