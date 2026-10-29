class Statistics():
    def __init__(self,data):
        self.data=data
    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()
    def median(self):
        s=sorted(self.data)
        n=len(s)
        if n%2!=0:
            return s[n//2]
        else:      
            return (s[n//2]+s[n//2-1])/2
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26,1]

ages=Statistics(ages)

print(ages.median())