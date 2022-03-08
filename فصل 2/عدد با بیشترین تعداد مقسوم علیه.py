tedad_maghsom_asl = 0

for i in range(20):
    adad = int(input())
    def tedad_maghsomelayh(adad):
        tedad_mghsom = 0
        global tedad_maghsom_asl
        global adad_pormaghsom
        for i in range(1, adad):
            if adad % i == 0:
                tedad_mghsom +=1
                # print(tedad_mghsom)
        if tedad_mghsom > tedad_maghsom_asl:
            tedad_maghsom_asl = tedad_mghsom
            adad_pormaghsom = adad
        return adad_pormaghsom
    tedad_maghsomelayh(adad)
maghsom_adad_pormaghsom=1
for i in range(1, adad_pormaghsom):
    if adad_pormaghsom % i == 0:
        maghsom_adad_pormaghsom += 1
print(adad_pormaghsom," ",maghsom_adad_pormaghsom)
