class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        s=[]
        s.append(celsius+273.15)
        s.append((celsius*1.80)+32.00)
        return s
