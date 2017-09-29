
def main():
    global States
    States = States.replace(' - ', '|')
    States = States.split('\n')
    Statez = []
    for state in States:
        Statez.append(state.split('|'))
    Statez = sorted(Statez, key=lambda x: x[1])
    Statezz = {}
    for i in range(len(Statez)):
        Statezz[i+1] = Statez[i][0]
    print(Statezz)
States = """AL - Alabama
AK - Alaska
AR - Arkansas
AZ - Arizona
CA - California
CO - Colorado
CT - Connecticut
DC - District of Columbia
DE - Delaware
FL - Florida
GA - Georgia
HA - Hawaii
IA - Iowa
ID - Idaho
IL - Illinois
IN - Indiana
KS - Kansas
KY - Kentucky
LA - Louisiana
MA - Massachussets
MD - Maryland
ME - Maine
MI - Michigan
MN - Minnesota
MO - Missouri
MS - Mississippi
MT - Montana
NC - North Carolina
ND - North Dakota
NE - Nebraska
NH - New Hampshire
NJ - New Jersey
NM - New Mexico
NV - Nevada
NY - New York
OH - Ohio
OK - Oklahoma
OR - Oregon
PA - Pennsylvania
RI - Rhode Island
SC - South Carolina
SD - South Dakota
TN - Tennessee
TX - Texas
UT - Utah
VA - Virginia
VT - Vermont
WA - Washington
WI - Wisconsin
WV - West Virginia
WY - Wyoming"""
main()
