striptiz = "Александр"
glasnie = "аяуюоеёэиы"
vowel_count = 0

for i in striptiz:
    if i in glasnie:
        glasnie.count("аяуюоеёэиы")
        vowel_count += 1
    print(vowel_count)