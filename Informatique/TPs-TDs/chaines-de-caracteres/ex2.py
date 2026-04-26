def conjuguer(verbe):
    verbe=verbe[:-2]
    pronouns_du_present =["Je", "Tu", "Il/Elle", "Nous", "Vous", "Ils/Elles"]
    terminaisons=["e", "es", "e", "ons", "ez", "ent"]
    for i in range(len(terminaisons)):
        print(f"{pronouns_du_present[i]} {verbe}{terminaisons[i]}")
print(conjuguer("parler"))