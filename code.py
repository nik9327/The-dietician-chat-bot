from tkinter import *
from random import randint
a = Tk()
a.title('The dietician')
a.geometry("1400x600")
a.configure(bg='#808080')
def BMR():

    protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
    ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    w = v3.get()
    h = v4.get()
    age = v5.get()
    act = str(Lb.get(ACTIVE))
    gender = Lb2.get(ACTIVE)

    if gender == 'Male':
        ncal = float()
        ncal = 88.362 + (13.397*float(w)) + (4.799*float(h)) - (5.677*float(age))
        print ("old calories",ncal)
    elif gender == 'Female':
        ncal = float()
        ncal = 447.593 + (9.247*float(w)) + (3.098*float(h)) - (4.330*float(age))


    if act == 'Sedentary (little or no exercise)':
        cal = ncal*1.2

    elif act == 'Lightly active (1-3 days/week)':
        cal = ncal*1.375

    elif act == 'Moderately active (3-5 days/week)':
        cal = ncal*1.55

    elif act == 'Very active (6-7 days/week)':
        cal = ncal*1.725

    elif act == 'Super active (twice/day)':
        cal = ncal*1.9

    print ("new calories",cal)


    if cal<1500:
        fin = StringVar()
        l10 = Label(a, textvariable=fin, relief=RAISED,fg = 'white',bg='#980000')
        fin.set("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])
        l10.grid(row=5,column=4,sticky=W)


        fin2 = StringVar()
        l11 = Label(a, textvariable=fin2, relief=RAISED ,fg = 'white',bg='#980000')
        fin2.set("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l11.grid(row=6,column=4,sticky=W)


        fin3 = StringVar()
        l12 = Label(a, textvariable=fin3, relief=RAISED,fg = 'white' ,bg='#980000')
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l12.grid(row=7,column=4,sticky=W)


        fin4 = StringVar()
        l13 = Label(a, textvariable=fin4, relief=RAISED,fg = 'white' ,bg='#980000')
        fin4.set("Dinner: "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l13.grid(row=8,column=4,sticky=W)


        fin5 = StringVar()
        l14 = Label(a, textvariable=fin5, relief=RAISED ,fg = 'white',bg='#980000')
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l14.grid(row=9,column=4,sticky=W)


    elif cal<1800:
        fin = IntVar()
        l10 = Label(a, textvariable=fin, relief=RAISED ,fg = 'white',bg='#980000')
        fin.set("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])
        l10.grid(row=5,column=4,sticky=W)


        fin2 = StringVar()
        l11 = Label(a, textvariable=fin2, relief=RAISED ,fg = 'white',bg='#980000')
        fin2.set("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l11.grid(row=6,column=4,sticky=W)


        fin3 = StringVar()
        l12 = Label(a, textvariable=fin3, relief=RAISED ,fg = 'white',bg='#980000')
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l12.grid(row=7,column=4,sticky=W)


        fin4 = StringVar()
        l13 = Label(a, textvariable=fin4, relief=RAISED ,fg = 'white',bg='#980000')
        fin4.set("Dinner: 2 "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l13.grid(row=8,column=4,sticky=W)


        fin5 = StringVar()
        l14 = Label(a, textvariable=fin5, relief=RAISED ,fg = 'white',bg='#980000')
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l14.grid(row=9,column=4,sticky=W)

    elif cal<2200:
        fin = StringVar()
        l10 = Label(a, textvariable=fin, relief=RAISED ,fg = 'white',bg='#980000')
        fin.set("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])
        l10.grid(row=5,column=4,sticky=W)


        fin2 = StringVar()
        l11 = Label(a, textvariable=fin2, relief=RAISED ,fg = 'white',bg='#980000')
        fin2.set("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l11.grid(row=6,column=4,sticky=W)


        fin3 = StringVar()
        l12 = Label(a, textvariable=fin3, relief=RAISED,fg = 'white' ,bg='#980000')
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l12.grid(row=7,column=4,sticky=W)


        fin4 = StringVar()
        l13 = Label(a, textvariable=fin4, relief=RAISED,fg = 'white',bg='#980000' )
        fin4.set("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l13.grid(row=8,column=4,sticky=W)


        fin5 = StringVar()
        l14 = Label(a, textvariable=fin5, relief=RAISED,fg = 'white' ,bg='#980000')
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l14.grid(row=9,column=4,sticky=W)


    elif cal>=2200:
        fin = StringVar()
        l10 = Label(a, textvariable=fin, relief=RAISED ,fg = 'white',bg='#980000')
        fin.set("Breakfast: 2 "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]+" + "+grains[randint(0,4)])
        l10.grid(row=5,column=4,sticky=W)


        fin2 = StringVar()
        l11 = Label(a, textvariable=fin2, relief=RAISED ,fg = 'white',bg='#980000')
        fin2.set("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l11.grid(row=6,column=4,sticky=W)


        fin3 = StringVar()
        l12 = Label(a, textvariable=fin3, relief=RAISED,fg = 'white' ,bg='#980000')
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l12.grid(row=7,column=4,sticky=W)


        fin4 = StringVar()
        l13 = Label(a, textvariable=fin4, relief=RAISED,fg = 'white' ,bg='#980000')
        fin4.set("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens + 2 "+grains[randint(0,4)]+" + 2 "+taste_en[randint(0,5)])
        l13.grid(row=8,column=4,sticky=W)


        fin5 = StringVar()
        l14 = Label(a, textvariable=fin5, relief=RAISED ,fg = 'white',bg='#980000')
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l14.grid(row=9,column=4,sticky=W)

''''def clear1():
    v3.clear()
    v4.clear()
    v5.clear()'''
def clear1():                                                                           
    v3.set("")    
    v4.set("")    
    v5.set("") 
   

'''
v1 = IntVar()
c1 = Checkbutton(a, text = 'Male', variable = v1)
c1.grid(row=0,column=1)

v2 = IntVar()
c2 = Checkbutton(a, text = 'Female', variable = v2)
c2.grid(row=0,column=2)
'''
l1 = Label(a,text="Artificial         Intelligence        Dietitian        System ",font=('60'),bg='black',fg='white',width=55,height=2)
l2 = Label(a, text='Weight',font=('10'), bg = '#980000',fg = 'white',width=15)
l3 = Label(a, text='Height(in cms)',font=('10'), bg = '#980000',fg = 'white',width=15)
l4 = Label(a, text='Age ',font=('10'), bg = '#980000',fg = 'white',width=15)
l5 = Label(a, text = 'Gender', bg = '#980000',fg = 'white',font=('10'),width=15)
l6 = Label(a, text = 'Excercise You Perform ',font=('20'), bg = '#980000',fg = 'white',width=20)
l7 = Label(a, text = '')
l8 = Label(a, text = 'Your Diet Chart Will Prepare Here',bg='black',fg='white',width=45,font=6)
l20 = Label(a,bg='#808080')
l21 = Label(a,bg='#808080')
l22 = Label(a,bg='#808080')
l23 = Label(a,bg='#808080')
l24 = Label(a,bg='#808080')
l25 = Label(a,bg='#808080')
l26 = Label(a,bg='black',fg='white',width=20,height=2,font=('60'))
l27 = Label(a,bg='black',fg='white',width=65,height=2,font=('60'))


v3=StringVar()
v4=StringVar()
v5=StringVar()


e3 = Entry(a, textvariable=v3,justify=RIGHT,bd=8, width=30)
e4 = Entry(a, textvariable=v4,justify=RIGHT,bd=8, width=30)
e5 = Entry(a, textvariable=v5,justify=RIGHT,bd=8, width=30)

Lb = Listbox(a, height=6, width=30,bd=8)
Lb.insert(1, 'Sedentary (little or no exercise)')
Lb.insert(2, 'Lightly active (1-3 days/week)')
Lb.insert(3, 'Moderately active (3-5 days/week)')
Lb.insert(4, 'Very active (6-7 days/week)')
Lb.insert(5, 'Super active (twice/day)')

Lb2 = Listbox(a, height=2, width=30,justify=RIGHT,bd=8)
Lb2.insert(1, 'Male')
Lb2.insert(2, 'Female')

var = Lb.get(ACTIVE)
print (var)


b1 = Button(a, text = 'Submit',font=('15'), width=25,height =1, command = BMR,bd=8,bg="#274e13",fg='white')
b2 = Button(a, text = 'Clear ',font=('15'), width=25,height =1, command = clear1,bd=8,bg="#274e13",fg='white')

l1.grid(row=1,column=3,sticky=W)

l2.grid(row=5,column=2,sticky=W) # Weight
e3.grid(row=5, column=3)

l3.grid(row=7,column=2,sticky=W) # Height
e4.grid(row=7, column=3)

l4.grid(row=9,column=2,sticky=W) # age
e5.grid(row=9, column=3)

l5.grid(row=3,column=2,sticky=W) #gender
Lb2.grid(row=3,column = 3)

l6.grid(row=11,column=2,sticky=W) # activity
Lb.grid(row=11,column = 3)

l8.grid(row=3,column=4,sticky=W) # output
b1.grid(row=13,columns=4) # submit button
b2.grid(row=13,columns=5) # clear button

        # free spaceing for css                
l20.grid(row=2,column=2) 
l21.grid(row=4,column=2) 
l22.grid(row=6,column=2) 
l23.grid(row=8,column=2) 
l24.grid(row=10,column=2) 
l25.grid(row=12,column=2) 
l26.grid(row=1,column=2,sticky=E) 
l27.grid(row=1,column=4,sticky=E) 

a.mainloop()
