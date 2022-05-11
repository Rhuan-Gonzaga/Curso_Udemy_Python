#dic = {"k1": 1, "k2": 2, "k3": 3}
#d1 = dic(chave1 = 10) # 2 jeito de criar chaves

#print(dic.get("k3"))
#print("k5" in dic.keys())
#print(2 in dic.values())

dic2 = {
    "chavepai": {
        "k4": 4,
        "k5": 5,
        "k6": 6,
    },

    "chavepai2": {
        "k7": 7,
        "k8": 8,
        "k8": 9,
    }
}

print(dic2["chavepai"].values())
print(dic2["chavepai2"].items())
print(dic2["chavepai"].keys())