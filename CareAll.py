oldies=[]
youngs=[]
choices=[]
old_young_data={}
keys=[]
Choices_over=[]
Couples=[]
class CareAll():
    pass
class Elders(CareAll):
            
    def eld_detail(self):
        return '{} {} {} {}' .format(self.Name,self.Age,self.Funds,self.Rating)
    
    
    def UpdateFund(self):
        F = int(input("How much funds do you want to offer"))
        self.funds= F
    
    def AsCouple():
        AC= input("Do you have a partner [Y/N]")
        
        if AC == "Y" :
            Status = 1
        else:
            Status = 0
    
    def Rate_young(self,RATE):
        pass
        
    
    def Young_Who(self):
        pass


class Young_ones(CareAll):
        
    def YO_detail(self):
        return '{} {} {}' .format(self.Name,self.Age,self.Rating)
    
    
    def RateOld():
        Elders.Rating
    def EldersWho():
        pass


def loop1():
    eld_1 = Elders()
    n=input('Enter the name of the elder')
    eld_1.Name=n
    a=int(input('Enter the age of the elder'))
    eld_1.Age=a
    f=int(input('Enter the funds of the elder'))
    eld_1.Funds=f
    oldies.append([eld_1.Name,eld_1.Age,eld_1.Funds])
    AC=input('Are you Maried? IF yes- Is your partner being taken care too? [Y/N]')
    if AC=='Y':
        E=input('Have they been already entered?[Y/N]')
        if E=='Y':
            print(oldies)
            InD=int(input('Enter INDEX VALUE of your partner'))
            if InD == len(oldies)-1:
                print('You cannot be married to yourself')
            else:
                Couples.append([[eld_1.Name,eld_1.Age,eld_1.Funds],oldies[InD]])
            
        if E=='N':
            print('PLEASE ENTER THEM WHEN ASKED TO MAKE MORE ENTRIES')
    
    
            
    p=input('More Oldies? [Y/N]')
    
    if p =='Y' :
        loop1()
    elif p!="N":
        print('INVALID ENTRY')
        p=input('More Oldies? [Y/N]')
    
        if p =='Y' :
            loop1()
        
def loop2():
    APP=input("Now , Youngster!! Have you been approved by your elders?[Y/N]")
    if APP=="Y":
        YC_1 = Young_ones()
        n=input('Enter your name ')
        YC_1.Name=n
        a=int(input('Enter your age '))
        YC_1.Age=a
        youngs.append([YC_1.Name,YC_1.Age])
        p=(len(oldies)-len(Choices_over))
        print('No. of oldies available for care are ' + str(p))
        HM=int(input('How many Oldies do you want to take care of[Max-4]?'))
    
        
        
        if HM<p+1:
            i=0
            while i<HM:
                if len(Choices_over)==0:
                    print('None')
                else:
                    print(Choices_over)
                print('Have already been choosen')    
                choice=int(input('Choose the oldie you want to take care of[Pass INDEX VALUE] '))
                
                
                if choice not in Choices_over:
                    choices.append(choice)
                    Choices_over.append(choice)
                    i=i+1
                else:
                    print('Oldie you just choose has already been choosen , choose another ')
                    continue
            print('You choose these olides')
            for olds in choices:
                print(oldies[olds])
                # y=0
                # while y<4:
            
            # print(choices)
            for olds in choices:    
                old_young_data.update({ oldies[olds][0]: YC_1.Name})
            choices.clear()
            # for olds in choices:
            #     oldies.pop(olds)
        else:
            print("INVALID ENTRY , " + str(p) +" Oldies available only" )
            loop2()
    elif APP=='N':
        print('Please get approved')
        print('''
              
                ENTER ANOTHER YOUNGSTER IF WANTED, WHEN ASKED TO ENTER NEXT TIME
                
                ''')
    else:
        print('Invalid entry')
        loop2()
        
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = old_young_data.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

loop1()
print(oldies)
loop2()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print("The following dictionary shows which oldie is taken care by which youngster in the format 'oldie': 'youngster'")
print(old_young_data)


a=input('Do you want to make more entries? [Y/N]')
if a=='Y':
    g=input('Oldie or youngster or both?[O/Y/B]')
    if g=='O':
        loop1()
    if g=="Y":
        print(oldies)
        loop2()
        print("The following dictionary shows which oldie is taken care by which youngster in the format 'oldie': 'youngster'")
        print(old_young_data)
    if g=="B":
        loop1()
        print(oldies)
        loop2()
        print("The following dictionary shows which oldie is taken care by which youngster in the format 'oldie': 'youngster'")
        print(old_young_data)
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


def Search():    
   
        c=input('Oldie or youngster?[O/Y]')
        if c=="O":
            print(oldies)
            ind=int(input("Enter the index of the oldie to extract info."))
            print('* In the format [Name , Age , Funds they provide]*')
            print(oldies[ind] )
            
            for names in oldies[ind][0]:
                name=old_young_data[names]
                print('Also! , They are taken care by ' + name)
                
        
        elif c=="Y":
            print(youngs)
            IND=int(input("Enter the index of the youngster to extract info."))
            
            print('* In the format [Name , Age ]*')
            print(youngs[IND])
            print('And they are taking care of :-')
            ListOfKeys = getKeysByValue(old_young_data , youngs[IND][0] )
            for keys in ListOfKeys:
                print(keys)
b=input('Do you want to search an individual?[Y/N]')
if b=='Y':                
    Search()
    h=input("More Searching to do? [Y/N]")
    if h == 'Y':
        Search()

def Rate():
    
        d=input('Oldie or young? [O/Y]')
        if d=='O':
            NAME=input("Enter name of your youngster")
            if NAME in old_young_data.values():
                RATE=int(input('How much do you rate them?'))
                print("You rate them "+str(RATE))
            else:
                print('NO SUCH YOUNGSTER EXISTS')
    
        if d=="Y":
            l=0
            name=input("Enter your name")
            # print(youngs)
            while l< len(youngs):
                # print(youngs[l][0])
                if name in youngs[l][0]:
                    ListOfKeys = getKeysByValue(old_young_data , name )
                else:
                    print('You are not in our database, please register first')
                    break
                l += 1
            for key in ListOfKeys:
                if key not in keys:
                    keys.append(key) 
                    
            print(keys)     
            WO=int(input('Which one would you like to rate?[enter index value]'))
            rate=input('Ok enter rating for ' + str(keys[WO]))
            print("You rate them "+str(rate))
            
e=input('Do you want to rate?[Y/N]')        
if e=="Y":
    Rate()
    RS=input("More rating to do? [Y/N]")
    if RS == 'Y':
        Rate()

def Partner_search():
    print(youngs)
    FW=int(input('Which youngster do you want to search for if they have a couple or not?'))
    k=0
    # L=0
    # STAT=0
    print("IF NOTHING PRINTS AFTER THIS -- NO OLD COUPLES PRESENT AND VICA VERSA")
    while k < (len(Couples)):
        ListOfKeys = getKeysByValue(old_young_data , youngs[FW][0] )
       
        if Couples[k][0][0] and Couples[k][1][0] in ListOfKeys:
            print(Couples[k])
        k=k+1
   
inP=input('Do you want to search if an old couple is being taken care by a youngster[Y/N]')
if inP=='Y':
    Partner_search()

    OC=input("More couple searching to do? [Y/N]")
    if OC == 'Y':
        Partner_search()
        
    
def Final():
    
    while True:
        CHO=int(input('''Anything More to do?
          1) Make more entries?
          2) Do you want to rate?
          3) Do you want to search?
          4) Old Couple Search
          5) EXIT 
        '''))
    
        if CHO==1:
            g=input('Oldie or youngster or both?[O/Y/B]')
            if g=='O':
                loop1()
            if g=="Y":
                print(oldies)
                loop2()
                print(old_young_data)
            if g=="B":
                loop1()
                print(oldies)
                loop2()
                print(old_young_data)
        if CHO==2:
            Rate()
        if CHO==3:
            Search()
        if CHO==4:
            Partner_search()
        if CHO == 5:
            break
        else:
            Final()



Final()

