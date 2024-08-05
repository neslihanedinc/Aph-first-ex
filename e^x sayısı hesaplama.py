def factorial(n):
    #computes the factorial positive integers.
    if n==0:
        return 1
    else:
        return n * factorial(n-1)  


def calculate_ex(x, term_count=10):
    result =0
    for n in range(term_count):
        result+= x**n/factorial(n)
    return result

while True:
    #True: Koşul True olduğu için döngü sonsuz bir döngü oluşturur. Bu, döngünün içinde break ifadesi kullanılarak sonlandırılana kadar devam edeceği anlamına gelir.
   
        
    try:  
        user_input = input("Enter a number (type 'a' to quit): ") 
        if user_input.lower() == 'a':   #Bu blok, hata meydana gelebilecek kodu içerir. Eğer bu blok içinde bir hata oluşursa, Python bir exception (istisna) fırlatır ve kontrol except bloğuna geçer.
            break #break: Eğer koşul doğruysa (user_input.lower() == 'a'), break ifadesi döngüyü sonlandırır ve döngüden çıkar.
        x = float(user_input)   #Olası Hata: Eğer kullanıcı geçersiz bir giriş yaparsa (örneğin bir harf girerse), float fonksiyonu ValueError hatası fırlatır.
        result =(calculate_ex(x)) #calculate_ex fonksiyonunu çağırır ve x değeri ile e^x'i hesaplar. Hesaplanan sonuç result değişkenine atanır.
        print(f"e^{x} is {result}.")  #f-string: Bu ifade, değişkenlerin değerlerini string içinde dinamik olarak yerleştirmek için kullanılır. f"e^{x} is approximately {result}." ifadesi, x ve result değişkenlerinin değerlerini string içine yerleştirir.
    except ValueError:
        print("Invalid input,please enter a number.")


