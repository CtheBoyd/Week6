fore = ["Kiki", "Krystal", "Pavel", "Marykay", "Annie", "Koala"]
surname = "Kardashian"


def add_surname():
    k_fore = [i + " " + surname for i in fore if i[0] == "K"]
    return k_fore


print(add_surname())
