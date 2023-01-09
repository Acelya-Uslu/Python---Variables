#%%
#Python 'ın temelinde 3 ç#eşit component vardır:
    #1-Variable
    #2-Function
    #3-Object
    
#Variable - (degisken)
#Python da herhangi bir şeyi tanımlamak, beyan etmek için  kullandığımız kalıplardır.

#Variable isimleri türkçe karakter olamaz.
#Variable isimleri sayıyla başlayamaz(invalid syntax), sayıyla bitebilir.
#Variable isimleri büyük harfle başlamaz.

var1=10 #integer

day="monday" #string

var3=11.3 #float-double

#%%


#String

s="Today is Wednesday."
variable_type=type(s)
#type() fonksiyonu --> İçindeki variable'ın veri tipini veren fonksiyondur.

print(s) 
#print() fonksiyonu --> İçindeki değeri ekrana basan fonksiyondur.

var1="ankara"
var2="izmir"
var3=var1+var2


var4="100"
var5="200"
var6=var4+var5


uzunluk=len(var6)
#╚len fonksiyonu içindeki stringin uzunluğunu veren fonksiyondur.

#%%

#Numbers

integer_deneme=-50

#float-double: ondalıklı sayı

float_deneme=-20.7

# float bir methodtur.variable ismi olarak kullanılamaz.

float(10)
#float methodu:içindeki değeri floata çevirir.


#%%
#Built-in Functions: Gömülü Fonksiyonlar

str1="Deneme"

float1=10.6

acem="ace"

#%% User Defined Functions :Kullanıcının ihtiyaç doğrultusunda tanımladığı Fonksiyonlar

var1=20
var2=50

output=(var1+var2*5)/10

def first_function(a,b):
#fonksiyonun içine yazacğın herşeyi tabla yazmalısın.

    """
    fonksiyon parametresi-input:car1,var2
    return:(var1+var2*5)/10
    """
    output=(a+b*5)/10
    return output
    
sonuc=first_function(5,6)
print(sonuc)


def second_function():
    print("This is my second function.")
#%% Default and Flexible Functions:
  
#Çemberim çevre uzunluğu:2*pi*r


def cember_cevre_hesapla(r,pi=3.14):
#default parametre: pi
    """
    cember cevresi hesapla
    input:r 
    output: 2*pi*r(cember çevresi)
    """
    
    output=2*pi*r
    return output

#Flexible Function


def hesapla(boy,kilo,*args):
    print(args)
    output=(boy+kilo)*args[0]
    return output

#args parametresi istersem bişi eklerim istersem eklemem.

#%% QUIZ

#int variable-yas
#string variable -name
#fonksiyon olucak
#fonksiyonda print , type,len, float fonkları olucak.
# *args soyisim
#default parametre ayakkabı numarası

def function_quiz(name,age,*args,foot_number=35):
    # default parametreler sona yazılır.
    # *args--> flexible variable,
    # foot_number=35 --> default variable
    
    print("His name:",name)     
    print("His foot_number:",foot_number)
    print("His age:",age)
    print("His surname:",surname)

    
    print(type(age))
    print(len(name))
    print(float(foot_number))
    
    output=args[0]*age
    return output



sonuc=function_quiz("Alican",32,"aslan")
print("args[0]*age:",sonuc)



#%%  Lambda Function

def hesapla_function(x):
    output=x*x
    return output
#return x*x de yapabiliriz.

sonucum=hesapla_function(3)
print(sonucum)

sonuc2=lambda x: x*x
sonuc2(3)

#%% List

liste=[1,2,3,4,5]
# liste integerlardan oluşabilir.

print(type(liste))

liste_str=["monday","tuesday","wednesday"]
#liste stringlerden oluşabilir.
print(type(liste_str))

value=liste[1]
print(value)

#liste[-1]--son değeri basar.
last_value=liste[-1]


list_divide=liste[0:3]
#0.,1.,2. elemanları  al 3 dahil değil.

#Listenin de  kendine ait built in functionları var.dir(liste) ile görüntüleriz

#append-- listenin sonuna eleman ekler.
liste.append(6)
print(liste)

liste.remove(1)
print(liste)


liste.reverse() # listeyi ters çevirir.
print(liste)

liste2=[1,8,2,9,3,4,9,4]
liste2.sort()

#%%Tuple

#Köşeli parantez yerine normal parantez kullanılır.
#Çok kullanılmaz.Listeler daha kullanışlıdır.

t=(1,2,3,5,8,6,8,9)
print(t[2])

t.count(3)
t.index(1)


#%% Dictionary- Sözlük

#Dictionary küçük bir database gibi kullanılır.Kullanışlıdır.


dictionary={"ali":12,
            "ayse":32,
            "açelya":26}

print(dictionary["ali"])
print(type(dictionary["ali"]))

#ali,ayse,acelya --->Keys
#12,32,25 --->Values


def deneme():
    dictionary={"ali":12,
            "ayse":32,
            "acelya":26}
    return dictionary

result=deneme()
print(result)
print(type(deneme()))


#%% Conditionals

#if-else statement

var1=10
var2=10

if(var1  > var2):
    print("var1 var2den büyüktür.")

elif(var1==var2):
    print("var1 ve var2 eşittir.")
    
else:
    print("var2 var1den büyüktür.")

liste=[1,2,3,4,5,6]
value=11

print("***")
if value in liste:
    print("Yes {} değeri listenin içinde".format(value))
else:
    print("No {} değeri listenin içinde değil".format(value))


keys=dictionary.keys()

if "ali" in keys:
    print("yes")
else:
    print("no")

#%% Quiz 2

#109. yıl -->2.yüzyıl
#1640.yıl --> 17. yüzyıl
#2000.yıl -->20.yüzyıl

#method yazın
   #milattan öncesi yok
   #input:integer(yıllar)
   #output:integer yüzyıl
   

#input year--> 1<= year <=2005

def year2Century(year):
    
    """
    from year to century
    """

    str_year=str(year)
    
    if(len(str_year)<3):
        return  1        #10 ,20 ise

    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #yani 100,200,300....,900 ise
            return int(str_year[0])
        else:
                                #190,250,380
            return int(str_year[0])+1
    else:                 #1750,1700,1805
        if(str_year[2:4]=="00"):
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1
            

sonuc=year2Century(202)
print(sonuc)


#%% Loops
#For loop


for each in range(1,11):
    #1dahil 11 dahil değil.
    print(each)



for each in "açelyauslu":
    print(each)


for each in "açelya uslu".split():
    #split() methodu default olarak boşluğa göre ayırır.
    print(each)


liste=[1,2,3,4,6,8,9,10]

sumation=sum(liste)
print(sumation)

print("*****")

count=0
for each in liste:
    count=count+each


print(count)    

#%% While Loop

#For loop da bir range var, while loop da bir condition var.

i=0
while i<4:
    print(i)
    i+=1

print("********")

liste=[1,5,9,7,8,6,2]
a=0
while a < len(liste):
    print(a)
    a+=1
    
print("******")

sinir=len(liste)
each=0
count=0

while (each < sinir):
    count=count+liste[each]
    each=each+1
    
print(count)

#%% QUIZ-3

#liste var.
#listenin içindeki en küçük sayıyı bul


listem=[8,2,9,3,4,9,4,96,78,35,14,56,12]
listem.sort()
print(listem)

min_deger=1000000
for each in listem:
    if(each<min_deger):
        min_deger=each
    else:
        continue
print(min_deger)
