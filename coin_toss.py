import random

print('gues how many times heads out of 1000 coin toss: ?')
print()
input()
flips=0
heads=0
while flips<=1000:
    if random.randint(0,1)==1:
        heads=heads+1
    flips=flips+1
print('heads times: ',heads)
print(flips)
tails=flips-heads
print('tails times = ',tails)
print()
print('out of 1000 coin tosses, heads came up '+str(heads)+' times')
