class Solution:
    def __init__(self):
        self.mapping = {
          1000000000: 'Billion',
          1000000: 'Million',
          1000: 'Thousand',
          100: 'Hundred',
          90: 'Ninety',
          80: 'Eighty',
          70: 'Seventy',
          60: 'Sixty',
          50: 'Fifty',
          40: 'Forty',
          30: 'Thirty',
          20: 'Twenty',
          19: 'Nineteen',
          18: 'Eighteen',
          17: 'Seventeen',
          16: 'Sixteen',
          15: 'Fifteen',
          14: 'Fourteen',
          13: 'Thirteen',
          12: 'Twelve',
          11: 'Eleven',
          10: 'Ten',
          9: 'Nine',
          8: 'Eight',
          7: 'Seven',
          6: 'Six',
          5: 'Five',
          4: 'Four',
          3: 'Three',
          2: 'Two',
          1: 'One'
        }
        
    def numberToWords(self, num: int) -> str:

        if num==0:
            return "Zero"
        result=""
        
        for value, name in self.mapping.items():
            count=0
            if num>=value:
                count=num//value
                num%=value
                if count>1 or value>=100:
                    result= result+" "+self.numberToWords(count)+" "+name
                else:
                    result+=" "+name
        result=result[1:]
        return result