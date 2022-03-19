dict_traductor = {
    "a": "un/una",
    "be": "ser/estar",
    "city": "ciudad",
    "decay": "decaer",
    "equal": "igual",
    "nothing": "FUCK",
}

print("\n", type(dict_traductor), "\n")
print(dict_traductor, "\n")
dict_traductor["nothing"] = "nada"
print(dict_traductor, "\n")
del dict_traductor["decay"]
print(dict_traductor, "\n")
