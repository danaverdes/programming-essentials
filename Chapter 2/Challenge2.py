traveler_class = input("Enter traveler class([D]iplomat, [M]erchant, [C]ivilian): ")
traveler_planet = input("Enter planet of origin: ")
traveler_goods = float(input("Enter declared value of goods: "))
traveler_cyber = input("Carrying restricted cybernetics? (yes/no): ")
scan = ""
threat_score = 0
docket_notes = ""
if traveler_class == "D" and traveler_planet == "Alpha Centauri":
    scan = "Full Immunity"
elif traveler_planet == "Sirius B" and traveler_cyber == "yes":
    scan = "High Threat"
else:
    if traveler_planet == "Mars":
        threat_score += 10
        docket_notes = "* Origin flagged as historic conflict zone. \n"
    elif traveler_planet == "Sirius B":
        threat_score += 20
        docket_notes = "* Origin on bio-containment watchlist. \n"
    else:
        threat_score = threat_score
        docket_notes = ""

if not scan == "Full Immunity" or scan == "High Threat":
    if traveler_class == "M" and traveler_goods < 100:
        threat_score += 25
        docket_notes += "* Anomalously low declaration for Merchant class \n"
    elif traveler_class == "C" and traveler_goods > 25000:
        threat_score += 10
        docket_notes += "* Unusually high-value cargo for Civilian class. \n"
    else:
        threat_score = threat_score
        docket_notes += ""

if traveler_cyber == "yes" and traveler_planet!="Sirius B":
    threat_score += 20
    docket_notes += "* Declared possession of restricted cybernetics. \n"
else:
    threat_score = threat_score
    docket_notes += ""
verdict = ""
if threat_score >= 30:
    verdict = "Verdict: Level 3 Inspection & Mandatory Quarantine"
elif 15 <= threat_score <= 29:
    verdict = "Verdict: Level 2 Inspection Required"
else:
    verdict = "Verdict: Cleared for Entry."
tax = 0
if traveler_class == "M":
    tax = traveler_goods * 0.2
else:
    tax = tax
print("=========================================")
print("STARPORT ALPHA-7 CUSTOMS DOCKET")
print("=========================================")
print("Traveler Class:\t", traveler_class)
print("Planet of Origin:\t", traveler_planet)
print("Declared Goods Value:\t", traveler_goods, "Credits")
print("Tax Due:\t", tax, "Credits")
print(" --- SCANNER NOTES ---")
print(docket_notes)
print(" --- FINAL ASSESSMENT --- ")
print("Threat Score:", threat_score)
print(verdict)
print("=========================================")
