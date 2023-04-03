class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #{card: count}
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)

        counter = Counter(deck)
        count = min(list(counter.values()))
        for card in counter:
            g = gcd(counter[card], count)
            count = g
            
        return True if g > 1 else False