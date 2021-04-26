class Taxation:
    def __init__(self,commodity):
        self.commodity=commodity
        
    
    def taxables(self):

        imported=False
        exempt=False
        
        count=int(self.commodity[0])
        price=float(self.commodity[len(self.commodity)-1])
        value=' '.join(self.commodity[1:(len(self.commodity)-2)])

        exempted=['book','chocolate','pills']

        for i in exempted:
            if i in value:
                exempt=True
        
        if 'imported' in value:
            imported=True
     
        ans=self.solve(price,count,value,imported,exempt)
        print(f'{count} {value}: {self.round_off(ans[0])}')
        return ans


    def solve(self,price,count,value,imported,exempt):
        sales_tax=price*(0.1 if not exempt else 0)+price*(0.05 if imported else 0)
        total=(price+sales_tax)*count
        tot_sales_tax=sales_tax*count
                
        return total,tot_sales_tax

   
    def round_off(self,n):
        x= n*100
        x=round(x)
        r=x%10
        if r>5:
            return round((x/100),2)
        else:
            return round(((x+(5-r))/100),2)


total=0
total_sales_tax=0

while True:

    commodity=list(input().split())
    if commodity==[]:
        break
    val=Taxation(commodity)
    returns=val.taxables()
    
# To call the round_off() function outside the class component
    x=Taxation(returns)
    total+= x.round_off(returns[0])
    total_sales_tax+= x.round_off(returns[1])


    
print('Total:',x.round_off(total))
print('Sales Taxes:',x.round_off(total_sales_tax))
