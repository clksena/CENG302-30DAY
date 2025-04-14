def vucut_kitle_indeksi_hesapla():
    try:
        kilo = float(input("Kilonuzu girin (kg): "))
        boy = float(input("Boyunuzu girin (metre cinsinden, örn. 1.75): "))

        if boy <= 0 or kilo <= 0:
            print("Boy ve kilo pozitif sayılar olmalıdır.")
            return

        bmi = kilo / (boy ** 2)
        print(f"Vücut Kitle İndeksiniz (BMI): {bmi:.2f}")

        if bmi < 18.5:
            print("Durum: Zayıf")
        elif 18.5 <= bmi < 24.9:
            print("Durum: Normal")
        elif 25 <= bmi < 29.9:
            print("Durum: Fazla kilolu")
        else:
            print("Durum: Obez")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

vucut_kitle_indeksi_hesapla()
``