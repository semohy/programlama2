#Urun görüntüleme sayısı app
urunler = {
"a":{"goruntuleme":0},
"b":{"goruntuleme":0},
    }
def goruntuleme(key):
    urunler[key]["goruntuleme"] += 1

    print("goruntuleme:")
    
    for key in urunler:
        print ("Urun:",key ,"goruntuleme: ", urunler[key]["goruntuleme"])
    
def main():
    for x in urunler:
        print(x)

while True:
    main()

    x=input("urun seçin:")
    goruntuleme(x)


#______end _urun goruntuleme sayısı_____
