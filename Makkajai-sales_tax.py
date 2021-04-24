

def taxables(line):
    exempted=['book','chocolate','pills']
    imported=False
    exempt=False
    count=int(line[0])
    price=float(line[len(line)-1])
    value=' '.join(line[1:(len(line)-2)])

    for i in exempted:
        if i in value:
            exempt=True
            
            

    if 'imported' in value:
            imported=True
    ans=solve(price,count,value,imported,exempt)
    print(f'{count} {value}: {round_off(ans[0])}')
    return ans

def solve(price,count,value,imported,exempt):
    sales_tax=price*(0.1 if not exempt else 0)+price*(0.05 if imported else 0)
    total=(price+sales_tax)*count
    tot_sales_tax=sales_tax*count
               
    return total,tot_sales_tax

def round_off(n):
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

    line=list(input().split())
    if line==[]:
        break
    val=taxables(line)
    total+= round_off(val[0])
    total_sales_tax+= round_off(val[1])


    
print('Total:',round_off(total))
print('Sales Taxes:',round_off(total_sales_tax))
