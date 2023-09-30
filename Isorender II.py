def NAME():
    FILE = open("FirstNames.txt", "r", encoding = "utf-8")
    LIST = FILE.read()
    FILE.close()
    LIST = LIST.split("\n")
    NAME = ""
    NAME += LIST[random.randint(0, len(LIST)-1)]
    FILE = open("LastNames.txt", "r", encoding = "utf-8")
    LIST = FILE.read()
    FILE.close()
    LIST = LIST.split("\n")
    NAME += " " + LIST[random.randint(0, len(LIST)-1)]
    LIST = ""
    return NAME
    
class NPC():
    def __init__(self):
        self.NAME = NAME()
        self.POS = [random.randint(95, 105), 100, random.randint(95, 105)]
        AGES = []
        self.DIR = random.randint(0, 7)
        for I in range(30):
            AGES.append(random.randint(0, 13))
        for I in range(8):
            AGES.append(random.randint(14, 17))
        for I in range(15):
            AGES.append(random.randint(18, 25))
        for I in range(9):
            AGES.append(random.randint(26, 30))
        for I in range(15):
            AGES.append(random.randint(31, 40))
        for I in range(13):
            AGES.append(random.randint(41, 50))
        for I in range(10):
            AGES.append(random.randint(51, 60))
        for I in range(6):
            AGES.append(random.randint(61, 70))
        for I in range(3):
            AGES.append(random.randint(71, 80))
        for I in range(2):
            AGES.append(random.randint(81, 100))
        for I in range(1):
            AGES.append(random.randint(101, 120))
        for I in range(5):
            random.shuffle(AGES)
        self.AGE = AGES[random.randint(0, len(AGES)-1)]
        PSKILLS = ["Artist", "Farrier", "Gardener", "Glazier", "Candlemaker", "Engraver", "Barrister",
                   "Embroiderer", "Musician", "Locksmith", "Servant", "Archer", "Animal-Handeler",
                   "Sailer", "Explorer"]
        LSKILLS = ["Farmer", "Fisherman", "Forester", "Laborer", "Soldier", "Miner", "Master-Of-None"]
        CSKILLS = ["Salesman", "Beekeeper", "Miller", "Bucher", "Woodcutter", "Knight", "Blacksmith",
                   "Carpenter", "Armourer", "Baker", "Chef", "Artisan", "Stonemason"]
        MSKILLS = ["Swordsman", "Stealth", "Tank", "Craftsman", "Barber-Surgeon", "Architect", "Clergy", "Mage", "Brewer",
                   "Monk"]
        HSKILLS = ["Survivor", "Lucky", "Summoner", "Sorcerer", "Alchemist", "Necromancer", "Inventor"]
        self.SKILLS = []
        if random.randint(1, 10) == 1:
            if random.randint(1, 20) == 1:
                NUM = random.randint(4, 6)
            else:
                NUM = random.randint(2, 3)
        else:
            NUM = 1
        #L 60%
        #C 20%
        #M 10%
        #H/P 5%
        SKILL = []
        for I in range(60):
            if random.randint(1, 3) == 1:
                SKILL.append([0, random.randint(1, len(LSKILLS)-1)])
            SKILL.append([0, 0])
        for I in range(20):
            SKILL.append([1, random.randint(0, len(CSKILLS)-1)])
        for I in range(10):
            SKILL.append([2, random.randint(0, len(MSKILLS)-1)])
        for I in range(5):
            SKILL.append([3, random.randint(0, len(HSKILLS)-1)])
        for I in range(5):
            SKILL.append([4, random.randint(0, len(PSKILLS)-1)])
        for I in range(5):
            random.shuffle(SKILL)
        #1-3 40%
        #4-6 40%
        #7-9 10%
        #10-13 5%
        #14-16 5%
        LVS = []
        for I in range(40):
            LVS.append(random.randint(1, 3))
        for I in range(40):
            LVS.append(random.randint(4, 6))
        for I in range(10):
            LVS.append(random.randint(7, 9))
        for I in range(5):
            LVS.append(random.randint(10, 13))
        for I in range(5):
            LVS.append(random.randint(14, 16))
        for I in range(5):
            random.shuffle(LVS)
        for I in range(NUM):
            LV = LVS[random.randint(0, len(LVS)-1)]
            PK = random.randint(0, len(SKILL)-1)
            if SKILL[PK][0] == 0:
                pass
        #Sanity:
        #Immunity:
        #Perseption:
        #Gullibility:
        #Forgiveness:
        #Resistance:
        #Vulgarity:
        #Strength:
        #Speed:
        #Endurance:
        #Agility:
        #Head Torso Left-Arm Right-Arm Left-Leg Right-Leg Hands Eyes
        self.CONDITION = []
        #Illness: NAME SEVERITY EFFECT(S) CURES TREATMENTS PROGRESSION (L, M, S used to descride phases a phase is two days)
        self.ILLNESS = []
        #Organs
        #Lung: Controlls O2 which effects other organs effectiveness
        #
    def get_pos(self):
        return self.POS
    def display(self, scrn = [0,0,0]):
        global WLK
        CORDS = [[135, 8], [353, 8], [23, 8], [245, 8], [408, 8], [79, 8], [301, 8], [190, 8]]
        FRM = WLK.get(0, CORD=CORDS[self.DIR])
        DX, DY = PlaceCube(scrn[0], scrn[1], scrn[2], RETR = True)
        screen.blit(FRM, [DX, DY])
def change(surface, KEEP = [1, 1, 1, 1], BW = False):
    EDI = surface.copy()
    w, h = EDI.get_size()
    for x in range(w):
        for y in range(h):
            r = EDI.get_at((x, y))[0]
            g = EDI.get_at((x, y))[1]
            b = EDI.get_at((x, y))[2]
            a = EDI.get_at((x, y))[3]
            if BW:
                VAL = round(((r + g + b)/3)*KEEP[0])
                if VAL > 255:
                    VAL = 255
                elif VAL < 0:
                    VAL = 0
                EDI.set_at((x, y), pygame.Color(VAL, 0, 0, round(a*KEEP[3])))
            else:
                EDI.set_at((x, y), pygame.Color(round(r*KEEP[0]), round(g*KEEP[1]), round(b*KEEP[2]), round(a*KEEP[3])))
    return EDI
def SetOff():
    global OFFX
    global OFFY
    PX = 0
    PY = 0
    PZ = 0
    X = (SW/2) + ((PX+PZ)*(14*SCALE)) - PZ*(29*SCALE) + PZ*(3*SCALE) + OFFX
    Y = (SH/2) + ((PX+PZ)*(7*SCALE)) - PY*(18*SCALE) + PZ*(-1*SCALE) + OFFY
    X = round(X)
    Y = round(Y)
    if PX == 0 and PY == 0 and PZ == 0:
        print(X, Y, screen.get_width(), screen.get_height())
        if X > round(screen.get_width()/2):
            OFFX -= abs(round(screen.get_width()/2)-X)
        elif X < round(screen.get_width()/2):
            OFFX += abs(X-round(screen.get_width()/2))
        if Y > round(screen.get_height()/2):
            OFFY -= abs(round(screen.get_height()/2)-Y)
        elif Y < round(screen.get_height()/2):
            OFFY += abs(Y-round(screen.get_height()/2))
def PlaceCube(PX = 0, PY = 0, PZ = 0, TYP = 0, COL = 0, IMG = None, SURF = "WORK", REC = False, RETR = False):
    global COLOR
    global BASE
    global SW
    global SH
    global SCALE
    global GRID
    global OFFX
    global OFFY
    global X
    global Y
    if REC:
        try:
            GRID[PY+100][PX+100][PZ+100] = [TYP, COL]
        except:
            pass
    #OG
    X = (SW/2) + ((PX+PZ)*(14*SCALE)) - PZ*(29*SCALE) + PZ*(3*SCALE) + OFFX
    Y = (SH/2) + ((PX+PZ)*(7*SCALE)) - PY*(9*SCALE) + PZ*(-1*SCALE) + OFFY
    #9 in PY*() was originally 18
    X = round(X)
    Y = round(Y)
    if RETR:
        return X, Y
    else:
        try:
            if IMG != None:
                exec(SURF + ".blit(" + IMG + ", [X, Y])", globals())
            else:
                exec(SURF + ".blit(" + BASE[TYP] + COLOR[COL] + ", [X, Y])", globals())
        except:
            print(TYP, COL)
def RendMap(SEED = None, TN = 0, LVS = 20):
    global GRID
    if SEED == None:
        SEED = random.randint(1, 99999999)
    GRID = []
    PLT = []
    ROW = []
    for I in range(200):
        ROW.append([None])
    for I in range(200):
        PLT.append(ROW.copy())
    ROW = []
    for I in range(200):
        GRID.append(PLT.copy())
    print(GRID[0][0][0])
    PLT = []
    noise1 = PerlinNoise(octaves=3, seed=SEED+TN+3)
    noise2 = PerlinNoise(octaves=6, seed=SEED+TN+3)
    noise3 = PerlinNoise(octaves=12, seed=SEED+TN+3)
    noise4 = PerlinNoise(octaves=24, seed=SEED+TN+3)
    noise5 = PerlinNoise(octaves=48, seed=SEED+TN+3)
    noise6 = PerlinNoise(octaves=96, seed=SEED+TN+3)
    for X in range(200):
        for Z in range(200):
            NVAL = noise1([X/200, Y/200])
            NVAL += 0.5 * noise2([X/200, Y/200])
            NVAL += 0.25 * noise3([X/200, Y/200])
            NVAL += 0.125 * noise4([X/200, Y/200])
            NVAL += 0.0625 * noise5([X/200, Y/200])
            NVAL += 0.03125 * noise5([X/200, Y/200])
            NVAL = abs(NVAL)
            NVAL = round(LVS*NVAL)
            GRID[X][NVAL+95][Z] = [29, 0]
            for I in range(NVAL+95):
                if I == NVAL+94:
                    GRID[X][I][Z] = [29, 0]
                else:
                    GRID[X][I][Z] = [0, random.randint(0, 20)]
        pygame.event.get()
            
    
def NameGen(lengmin = 4, lengmax = 7, area = None, The = None, Type = 1):
    if Type == 1:
        AREA = ["City State Of ", "Nation Of ", "Republic Of ", "Democracy Of ", "Kingdom Of ", "Empire Of ", "Union Of ", "Confederacy Of ",
                "Territory Of ", "Unclaimed Lands Of ", "Continent Of ", "Region Of "]
    elif Type == 2:
        AREA = ["Guild Of ", "Den Of ", "Hidout Of ", "Hollow Of ", "Lair Of ", "Covert Of ", "Burrow Of ", "Lodge Of ", "Sanctuary Of ",
                "Refuge Of ", "Sanctum Of "]
    else:
        AREA = [""]
    if area == None:
        area = random.randint(0, len(AREA)-1)
    if The == None:
        The = random.randint(0, 1)
    VOWEL = "aeiou"
    CONSA = "cdfhlmnrst"
    RARCO = "jqxzvkbywgp"
    RAND = random.randint(lengmin, lengmax)
    VC = random.randint(0, 1)
    if VC == 1:
        VC = True
    else:
        VC = False
    NM = ""
    for I in range(RAND):
        if VC:
            if random.randint(1, 9) != 1:
                VC = False
            if I == 0:
                NM += VOWEL[random.randint(0, len(VOWEL)-1)].upper()
            else:
                NM += VOWEL[random.randint(0, len(VOWEL)-1)]
        else:
            if random.randint(1, 8) != 1:
                VC = True
            if I == 0:
                if random.randint(1, 6) != 1:
                    NM += CONSA[random.randint(0, len(CONSA)-1)].upper()
                else:
                    NM += RARCO[random.randint(0, len(RARCO)-1)].upper()
            else:
                if random.randint(1, 6) != 1:
                    NM += CONSA[random.randint(0, len(CONSA)-1)]
                else:
                    NM += RARCO[random.randint(0, len(RARCO)-1)]
    THE = ["", "The "]
    return THE[The] + AREA[area] + NM

def CALENDAR():
    MINUTE = round(59*FRM/9999)
    if FRM >= 9999:
        FRM = 0
        HOUR += 1
        if HOUR >= 24:
            HOUR = 0
            DAY += 1
            if DAY > 400:
                DAY = 1
                YEAR += 1
    else:
        FRM += 1
    if len(str(HOUR)) == 1:
        DHOUR = "0" + str(HOUR)
    else:
        DHOUR = HOUR
    if len(str(MINUTE)) == 1:
        DMINUTE = "0" + str(MINUTE)
    else:
        DMINUTE = MINUTE
class GIF():
    def __init__(self, FILE, SCALE = 1, SUB = None):
        img = Image.open(FILE)
        I = 0
        RUN = True
        if SUB != None:
            self.SUB = [round(SUB[0]*SCALE), round(SUB[1]*SCALE)]
        self.SCALE = SCALE
        self.FRM = 0
        while RUN:
            try:
                img.seek(I)
                img.convert("RGBA")
                img.save('RAM.png')
                exec("self.FRM" + str(I) + " = pygame.image.load('RAM.png').convert_alpha()")
                if SCALE != 1:
                    exec("self.FRM" + str(I) + " = pygame.transform.scale(self.FRM" + str(I) + ", [round(self.FRM" + str(I) + ".get_width()*SCALE), round(self.FRM" + str(I) + ".get_height()*SCALE)])")
                I += 1
            except:
                RUN = False
                self.MFRM = I-1
    def reset(self):
        self.FRM = 0
    def get(self, FRM = None, CORD = None, SUB = None):
        if FRM != None:
            exec("self.DATA = self.FRM" + str(FRM) + ".copy()")
        else:
            self.FRM += 1
            if self.FRM > self.MFRM:
                self.FRM = 0
            exec("self.DATA = self.FRM" + str(self.FRM) + ".copy()")
        if SUB != None:
            SUB[0][0] = round(SUB[0][0] * self.SCALE)
            SUB[0][1] = round(SUB[0][1] * self.SCALE)
            SUB[1][0] = round(SUB[1][0] * self.SCALE)
            SUB[1][1] = round(SUB[1][1] * self.SCALE)
            self.DATA = pygame.Surface.subsurface(self.DATA, (SUB[0], SUB[1]))
        elif CORD != None:
            CORD = CORD.copy()
            CORD[0] = round(CORD[0] * self.SCALE)
            CORD[1] = round(CORD[1] * self.SCALE)
            self.DATA = pygame.Surface.subsurface(self.DATA, (CORD, self.SUB))
        return self.DATA
def TEST():
    global GRID
    global OFFX
    global OFFY
    global WORK
    global COLOR
    global WLK
    OFFY = -3760
    OFFX = 1840
    UPDATE = True
    REN = 10
    POS = [0,0,0]
    WLK = GIF("SSF-WALK.gif", 2, [60, 100])
    DIR = 0
    TFRM = 50
    WALK = True
    CORDS = [[135, 8], [353, 8], [23, 8], [245, 8], [408, 8], [79, 8], [301, 8], [190, 8]]
    WORK = pygame.Surface([screen.get_width(), screen.get_height()])
    SetOff()
    RendMap()
    SHX = 0
    SHY = 0
    NPCS = [0]
    NPCS[0] = NPC() 
    while True:
        screen.fill([0,0,0])
        if TFRM >= 10 and WALK:
            TFRM = 0
            FRM = WLK.get(CORD = CORDS[DIR])
        else:
            TFRM += 1
        if UPDATE:
            UPDATE = False
            WORK.fill([0,0,0])
            NPCP = []
            for I in range(len(NPCS)):
                NPCP.append(NPCS[I].get_pos())
            for DX in range(REN):
                for DZ in range(REN):
                    for DY in range(round(REN/2)+20):
                        LK = round((POS[0]-REN/2)+DX)+100, round((POS[1]-REN/2)+DY)+100, round((POS[2]-REN/2)+DZ)+100
                        DT = GRID[LK[0]][LK[1]][LK[2]]
                        for I in range(len(NPCP)):
                            if LK == NPCP[I]:
                                NPCS[I].display([round(DX-REN/2), round(DY-REN/4), round(DZ-REN/2)])
                        if DT != [None]:
                            PlaceCube(round(DX-REN/2), round(DY-REN/4), round(DZ-REN/2), DT[0], DT[1], SURF = "WORK", REC = False)
        screen.blit(WORK, [SHX,SHY])
        screen.blit(FRM, [screen.get_width()/2-FRM.get_width()/2, screen.get_height()/2-FRM.get_height()/2])
        TXT = MFONT.render(str(POS), False, [117, 0, 0])
        screen.blit(TXT, [4, 11])
        pygame.event.get()
        pygame.display.update()
        keys = pygame.key.get_pressed()
        WALK = True
        OPOS = POS.copy()
        OPOS[0] = round(OPOS[0])
        OPOS[2] = round(OPOS[2])
        if keys[pygame.K_u]:
            OFFY -= 10
        elif keys[pygame.K_j]:
            OFFY += 10
        elif keys[pygame.K_h]:
            OFFX -= 10
        elif keys[pygame.K_k]:
            OFFX += 10
        elif keys[pygame.K_e]:
            POS[1] -= 1
            time.sleep(0.1)
        elif keys[pygame.K_q]:
            POS[1] += 1
            time.sleep(0.1)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            DIR = 6
            POS[2] -= 0.005
            POS[0] += 0.005
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            DIR = 7
            POS[2] += 0.005
            POS[0] += 0.005
        elif keys[pygame.K_a] and keys[pygame.K_w]:
            DIR = 4
            POS[2] -= 0.005
            POS[0] -= 0.005
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            DIR = 5
            POS[2] += 0.005
            POS[0] -= 0.005
        elif keys[pygame.K_w]:
            DIR = 1
            POS[2] -= 0.01
        elif keys[pygame.K_s]:
            DIR = 0
            POS[2] += 0.01
        elif keys[pygame.K_a]:
            DIR = 2
            POS[0] -= 0.01
        elif keys[pygame.K_d]:
            DIR = 3
            POS[0] += 0.01
        else:
            WALK = False
            WLK.reset()
            FRM = WLK.get(CORD = CORDS[DIR])
            UPDATE = False
        NPOS = POS.copy()
        NPOS[0] = round(NPOS[0])
        NPOS[2] = round(NPOS[2])
        if NPOS != OPOS:
            UPDATE = True
            SetOff()
        pygame.event.get()
        time.sleep(0.01)
import pygame
import os
import random
import time
import math
import ctypes
from perlin_noise import PerlinNoise
from PIL import Image
pygame.init()
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screen = pygame.display.set_mode((2000, 1000), pygame.FULLSCREEN)# pygame.RESIZABLE)
WORK = pygame.Surface((4000, 4000))
SW = WORK.get_width()
SH = WORK.get_height()
BKG = pygame.image.load("StarStruckFantasy.png").convert_alpha()
LBKG1 = pygame.image.load("SSF-LBKG1.png").convert_alpha()
LBKG2 = pygame.image.load("SSF-LBKG2.png").convert_alpha()
LBKG3 = pygame.image.load("SSF-LBKG3.png").convert_alpha()
X = round(700*(screen.get_width()/700))
Y = round(700*(screen.get_height()/700))
if X > Y:
    X = Y
else:
    Y = X
for I in range(30):
    print(NameGen())
GRID = []
BKG = pygame.transform.scale(BKG, [X, X])
LBKG1 = pygame.transform.scale(LBKG1, [X, X])
LBKG2 = pygame.transform.scale(LBKG2, [X, X])
LBKG3 = pygame.transform.scale(LBKG3, [X, X])
SCL = X/700
TFONT = pygame.font.Font("W95FA.OTF", round(5*SCL))
SFONT = pygame.font.Font("W95FA.OTF", round(10*SCL))
FONT = pygame.font.Font("W95FA.OTF", round(13*SCL))
MFONT = pygame.font.Font("W95FA.OTF", round(26*SCL))
LFONT = pygame.font.Font("W95FA.OTF", round(39*SCL))
SLC = 0
MENU = True
while MENU:
    X = round(screen.get_width()/2 - BKG.get_width()/2)
    Y = round(screen.get_height()/2 - BKG.get_height()/2)
    screen.blit(BKG, [X, Y])
    if SLC == 0:
        TXT = MFONT.render("> New Stranded Life <", False, [117, 0, 0])
    else:
        TXT = MFONT.render("  New Stranded Life  ", False, [117, 0, 0])
    screen.blit(TXT, [X + (27*SCL), Y + (314*SCL)])
    if SLC == 1:
        TXT = MFONT.render("> Continue Existing <", False, [117, 0, 0])
    else:
        TXT = MFONT.render("  Continue Existing  ", False, [117, 0, 0])
    screen.blit(TXT, [X + (29*SCL), Y + (340*SCL)])
    if SLC == 2:
        TXT = MFONT.render("> About Software <", False, [117, 0, 0])
    else:
        TXT = MFONT.render("  About Software  ", False, [117, 0, 0])
    screen.blit(TXT, [X + (41*SCL), Y + (366*SCL)])
    if SLC == 3:
        TXT = MFONT.render("> Settings <", False, [117, 0, 0])
    else:
        TXT = MFONT.render("  Settings  ", False, [117, 0, 0])
    screen.blit(TXT, [X + (79*SCL), Y + (392*SCL)])
    if SLC == 4:
        TXT = MFONT.render("> Quit <", False, [117, 0, 0])
    else:
        TXT = MFONT.render("  Quit  ", False, [117, 0, 0])
    screen.blit(TXT, [X + (100*SCL), Y + (418*SCL)])
    pygame.event.get()
    pygame.display.update()
    time.sleep(0.11)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        SLC -= 1
        if SLC < 0:
            SLC = 4
        time.sleep(0.1)
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        SLC += 1
        if SLC > 4:
            SLC = 0
        time.sleep(0.1)
    elif keys[pygame.K_RETURN]:
        if SLC == 0:
            MENU = False
BX, BY = X, Y     
TXT = MFONT.render("Loading...", False, [200, 100, 33])
screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
pygame.display.update()
#WORK.fill([255, 255, 255])

FILES = ["CUBE.png", "CHAR.png", "UCHR.png", "USLB.png", "SLAB.png", "LSLB.png", "NAT1.png", "NAT2.png", "NAT3.png",
         "GLAS.png", "RAMP.png", "RMP1.png", "RMp2.png", "LRMP.png", "LRM1.png", "LRM2.png", "CORN.png", "CRN1.png",
         "DOTE.png", "COLC.png", "TORC.png", "PILL.png", "SELC.png", "QBRT.png", "QBT1.png", "QBT2.png", "QBT3.png",
         "Torso.png", "Head.png", "GRASS.png", "CHR1.png", "CHAI.png", "CHA1.png", "CHA2.png", "CHA3.png", "BRIK.png",
         "BRK1.png", "GCHA.png", "GCH1.png", "GCH2.png", "GCH3.png", "LAMP.png", "TRAM1.png", "TRAM2.png", "WATR.png"]
#           1       2       3      4       5       6       7       8       9       10      11      12      13 
NAMES = ['CUBE', 'DCHR', 'UCHR', 'USLB', 'SLAB', 'LSLB', 'NAT1', 'NAT2', 'NAT3', 'GLAS', 'RAMP', 'RAM1', 'RAM2',
         'LRAM', 'LRM1', 'LRM2', 'CORN', 'CRN1', 'DOTE', 'COLC', 'TORC', 'PILL', 'SELC', 'QBRT', 'QBT1', 'QBT2',
         'QBT3', 'TORS', 'HEAD', 'GRAS', 'CHR1', "CHAI", "CHA1", "CHA2", "CHA3", "BRIK", "BRK1", "GCHA", "GCH1",
         "GCH2", "GCH3", "LAMP", "TRAM1", "TRAM2", "WATR"]
SCALE = 4
PIK = random.randint(1, 3)
for I in range(len(FILES)):
    screen.fill([0,0,0])
    if PIK == 1:
        screen.blit(LBKG1, [BX, BY])
    elif PIK == 2:
        screen.blit(LBKG2, [BX, BY])
    else:
        screen.blit(LBKG3, [BX, BY])
    TXT = MFONT.render("Loading... Textures [" + str(I+1) + "/" + str(len(FILES)) + "]", False, [117, 0, 0])
    screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
    pygame.display.update()
    pygame.event.get()
    time.sleep(0.11)
    exec(str(NAMES[I]) + " = pygame.image.load('" + str(FILES[I]) + "').convert_alpha()", globals())
    exec(str(NAMES[I]) + " = pygame.transform.scale(" + str(NAMES[I]) + ", [" + str(NAMES[I]) + ".get_width()*SCALE, " + str(NAMES[I]) + ".get_height()*SCALE])", globals())
X = 0
Y = 0
BASE = ["CUBE", "DCHR", "UCHR", "USLB", "SLAB", "LSLB", "NAT1", "NAT2", "NAT3", "GLAS", "RAMP", "RAM1", "RAM2", "LRAM", "LRM1", "LRM2", "CORN",
        "CRN1", "DOTE", "COLC", "TORC", "PILL", "QBRT", "QBT1", "QBT2", "QBT3", "HEAD", "TORS", "CHR1", "GRAS", "CHAI", "CHA1", "CHA2",
        "CHA3", "BRIK", "BRK1", "GCHA", "GCH1", "GCH2", "GCH3", "LAMP", "TRAM1", "TRAM2", "WATR"]

COLOR = ["WHT", "RED", "RD1", "RD2", "RD3", "RD4", "RD5", "RD6", "RD7", "RD8", "GRN", "GR1", "GR2", "GR3", "GR4", "GR5", "GR6", "GR7", "GR8", "BLU",
         "BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7", "BL8", "YEL", "MAG", "CYN", "BRW", "DBR", "BLK", "GY0", "GY1", "GY2", "GY3",
         "GY4", "GY5", "GY6", "GY7", "GY8", "GL1", "GL2", "GL3", "GL4", "GL5", "GL6", "GL7", "GL8", "GL9", "GL0", "GLS", "BBR"]
LONG = False
LRG = " 0 1 2 3 4 5 9 10 11 12 13 14 15 16"
PIK = random.randint(1, 3)
for I in range(len(BASE)):
    screen.fill([0,0,0])
    if PIK == 1:
        screen.blit(LBKG1, [BX, BY])
    elif PIK == 2:
        screen.blit(LBKG2, [BX, BY])
    else:
        screen.blit(LBKG3, [BX, BY])
    TXT = MFONT.render("Loading... Dyeing Blocks [" + str(I+1) + "/" + str(len(BASE)) + "]", False, [117, 0, 0])
    screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
    pygame.display.update()
    pygame.event.get()
    if " " + str(I) + " " in LRG:
        if LONG:
            exec(BASE[I] + "RED = change(" + BASE[I] + ", [1, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD1 = change(" + BASE[I] + ", [0.9, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD2 = change(" + BASE[I] + ", [0.8, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD3 = change(" + BASE[I] + ", [0.7, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD4 = change(" + BASE[I] + ", [0.6, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD5 = change(" + BASE[I] + ", [0.5, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD6 = change(" + BASE[I] + ", [0.4, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD7 = change(" + BASE[I] + ", [0.3, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "RD8 = change(" + BASE[I] + ", [0.2, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "GRN = change(" + BASE[I] + ", [0.1, 1, 0.1, 1])", globals())
            exec(BASE[I] + "GR1 = change(" + BASE[I] + ", [0.1, 0.9, 0.1, 1])", globals())
            exec(BASE[I] + "GR2 = change(" + BASE[I] + ", [0.1, 0.8, 0.1, 1])", globals())
            exec(BASE[I] + "GR3 = change(" + BASE[I] + ", [0.1, 0.7, 0.1, 1])", globals())
            exec(BASE[I] + "GR4 = change(" + BASE[I] + ", [0.1, 0.6, 0.1, 1])", globals())
            exec(BASE[I] + "GR5 = change(" + BASE[I] + ", [0.1, 0.5, 0.1, 1])", globals())
            exec(BASE[I] + "GR6 = change(" + BASE[I] + ", [0.1, 0.4, 0.1, 1])", globals())
            exec(BASE[I] + "GR7 = change(" + BASE[I] + ", [0.1, 0.3, 0.1, 1])", globals())
            exec(BASE[I] + "GR8 = change(" + BASE[I] + ", [0.1, 0.2, 0.1, 1])", globals())
            exec(BASE[I] + "BLU = change(" + BASE[I] + ", [0.1, 0.1, 1, 1])", globals())
            exec(BASE[I] + "BL1 = change(" + BASE[I] + ", [0.1, 0.1, 0.9, 1])", globals())
            exec(BASE[I] + "BL2 = change(" + BASE[I] + ", [0.1, 0.1, 0.8, 1])", globals())
            exec(BASE[I] + "BL3 = change(" + BASE[I] + ", [0.1, 0.1, 0.7, 1])", globals())
            exec(BASE[I] + "BL4 = change(" + BASE[I] + ", [0.1, 0.1, 0.6, 1])", globals())
            exec(BASE[I] + "BL5 = change(" + BASE[I] + ", [0.1, 0.1, 0.5, 1])", globals())
            exec(BASE[I] + "BL6 = change(" + BASE[I] + ", [0.1, 0.1, 0.4, 1])", globals())
            exec(BASE[I] + "BL7 = change(" + BASE[I] + ", [0.1, 0.1, 0.3, 1])", globals())
            exec(BASE[I] + "BL8 = change(" + BASE[I] + ", [0.1, 0.1, 0.2, 1])", globals())
            exec(BASE[I] + "YEL = change(" + BASE[I] + ", [1, 1, 0.1, 1])", globals())
            exec(BASE[I] + "MAG = change(" + BASE[I] + ", [0.6, 0.2, 0.6, 1])", globals())
            exec(BASE[I] + "CYN = change(" + BASE[I] + ", [0.4, 1, 1, 1])", globals())
            exec(BASE[I] + "BBR = change(" + BASE[I] + ", [0.219, 0.119, 0, 1])", globals())
            exec(BASE[I] + "DBR = change(" + BASE[I] + ", [0.5, 0.3, 0.1, 1])", globals())
            exec(BASE[I] + "BRW = change(" + BASE[I] + ", [0.6, 0.4, 0.2, 1])", globals())
            exec(BASE[I] + "BLK = change(" + BASE[I] + ", [0.01, 0.01, 0.01, 1])", globals())
            exec(BASE[I] + "GY0 = change(" + BASE[I] + ", [0.1, 0.1, 0.1, 1])", globals())
            exec(BASE[I] + "GY1 = change(" + BASE[I] + ", [0.2, 0.2, 0.2, 1])", globals())
            exec(BASE[I] + "GY2 = change(" + BASE[I] + ", [0.3, 0.3, 0.3, 1])", globals())
            exec(BASE[I] + "GY3 = change(" + BASE[I] + ", [0.4, 0.4, 0.4, 1])", globals())
            exec(BASE[I] + "GY4 = change(" + BASE[I] + ", [0.5, 0.5, 0.5, 1])", globals())
            exec(BASE[I] + "GY5 = change(" + BASE[I] + ", [0.6, 0.6, 0.6, 1])", globals())
            exec(BASE[I] + "GY6 = change(" + BASE[I] + ", [0.7, 0.7, 0.7, 1])", globals())
            exec(BASE[I] + "GY7 = change(" + BASE[I] + ", [0.8, 0.8, 0.8, 1])", globals())
            exec(BASE[I] + "GY8 = change(" + BASE[I] + ", [0.9, 0.9, 0.9, 1])", globals())
            exec(BASE[I] + "WHT = change(" + BASE[I] + ", [1, 1, 1, 1])", globals())
            exec(BASE[I] + "GL1 = change(" + BASE[I] + ", [1, 1, 1, 0.4])", globals())
            exec(BASE[I] + "GL2 = change(" + BASE[I] + ", [1, 0.1, 0.1, 0.4])", globals())
            exec(BASE[I] + "GL3 = change(" + BASE[I] + ", [0.1, 1, 0.1, 0.4])", globals())
            exec(BASE[I] + "GL4 = change(" + BASE[I] + ", [0.1, 0.5, 0.1, 0.4])", globals())
            exec(BASE[I] + "GL5 = change(" + BASE[I] + ", [0.1, 0.1, 1, 0.4])", globals())
            exec(BASE[I] + "GL6 = change(" + BASE[I] + ", [1, 1, 0.1, 0.4])", globals())
            exec(BASE[I] + "GL7 = change(" + BASE[I] + ", [0.6, 0.2, 0.6, 0.4])", globals())
            exec(BASE[I] + "GL8 = change(" + BASE[I] + ", [0.4, 1, 1, 0.4])", globals())
            exec(BASE[I] + "GL9 = change(" + BASE[I] + ", [0.6, 0.4, 0.2, 0.4])", globals())
            exec(BASE[I] + "GL0 = change(" + BASE[I] + ", [0.01, 0.01, 0.01, 0.4])", globals())
            exec(BASE[I] + "GLS = change(" + BASE[I] + ", [0.1, 0.1, 0.1, 0.4])", globals())
        else:
            exec("BB = change(" + BASE[I] + ", [0, 0, 0, 1], True)", globals())
            exec("G1 = change(" + BASE[I] + ", [0.1, 0.1, 0.1, 1], True)", globals())
            exec("G2 = change(" + BASE[I] + ", [0.2, 0.2, 0.2, 1], True)", globals())
            exec("G3 = change(" + BASE[I] + ", [0.3, 0.3, 0.3, 1], True)", globals())
            exec("G4 = change(" + BASE[I] + ", [0.4, 0.4, 0.4, 1], True)", globals())
            exec("G5 = change(" + BASE[I] + ", [0.5, 0.5, 0.5, 1], True)", globals())
            exec("G6 = change(" + BASE[I] + ", [0.6, 0.6, 0.6, 1], True)", globals())
            exec("G7 = change(" + BASE[I] + ", [0.7, 0.7, 0.7, 1], True)", globals())
            exec("G8 = change(" + BASE[I] + ", [0.8, 0.8, 0.8, 1], True)", globals())
            exec("G9 = change(" + BASE[I] + ", [0.9, 0.9, 0.9, 1], True)", globals())
            exec("WW = change(" + BASE[I] + ", [1, 1, 1, 1], True)", globals())
            
            exec(BASE[I] + "RED = WW", globals())
            exec(BASE[I] + "RD1 = G9", globals())
            exec(BASE[I] + "RD2 = G8", globals())
            exec(BASE[I] + "RD3 = G7", globals())
            exec(BASE[I] + "RD4 = G6", globals())
            exec(BASE[I] + "RD5 = G5", globals())
            exec(BASE[I] + "RD6 = G4", globals())
            exec(BASE[I] + "RD7 = G3", globals())
            exec(BASE[I] + "RD8 = G2", globals())
            exec(BASE[I] + "GRN = WW", globals())
            exec(BASE[I] + "GR1 = G9", globals())
            exec(BASE[I] + "GR2 = G8", globals())
            exec(BASE[I] + "GR3 = G7", globals())
            exec(BASE[I] + "GR4 = G6", globals())
            exec(BASE[I] + "GR5 = G5", globals())
            exec(BASE[I] + "GR6 = G4", globals())
            exec(BASE[I] + "GR7 = G3", globals())
            exec(BASE[I] + "GR8 = G2", globals())
            exec(BASE[I] + "BLU = WW", globals())
            exec(BASE[I] + "BL1 = G9", globals())
            exec(BASE[I] + "BL2 = G8", globals())
            exec(BASE[I] + "BL3 = G7", globals())
            exec(BASE[I] + "BL4 = G6", globals())
            exec(BASE[I] + "BL5 = G5", globals())
            exec(BASE[I] + "BL6 = G4", globals())
            exec(BASE[I] + "BL7 = G3", globals())
            exec(BASE[I] + "BL8 = G2", globals())
            exec(BASE[I] + "YEL = G9", globals())
            exec(BASE[I] + "MAG = G5", globals())
            exec(BASE[I] + "CYN = G6", globals())
            exec(BASE[I] + "BBR = G2", globals())
            exec(BASE[I] + "DBR = G4", globals())
            exec(BASE[I] + "BRW = G5", globals())
            exec(BASE[I] + "BLK = BB", globals())
            exec(BASE[I] + "GY0 = G1", globals())
            exec(BASE[I] + "GY1 = G2", globals())
            exec(BASE[I] + "GY2 = G3", globals())
            exec(BASE[I] + "GY3 = G4", globals())
            exec(BASE[I] + "GY4 = G5", globals())
            exec(BASE[I] + "GY5 = G6", globals())
            exec(BASE[I] + "GY6 = G7", globals())
            exec(BASE[I] + "GY7 = G8", globals())
            exec(BASE[I] + "GY8 = G9", globals())
            exec(BASE[I] + "WHT = WW", globals())
            exec(BASE[I] + "GL1 = G1", globals())
            exec(BASE[I] + "GL2 = G1", globals())
            exec(BASE[I] + "GL3 = G1", globals())
            exec(BASE[I] + "GL4 = G1", globals())
            exec(BASE[I] + "GL5 = G1", globals())
            exec(BASE[I] + "GL6 = G1", globals())
            exec(BASE[I] + "GL7 = G1", globals())
            exec(BASE[I] + "GL8 = G1", globals())
            exec(BASE[I] + "GL9 = G1", globals())
            exec(BASE[I] + "GL0 = G1", globals())
            exec(BASE[I] + "GLS = G1", globals())
    else:
        exec(BASE[I] + "RED = " + BASE[I], globals())
        exec(BASE[I] + "RD1 = " + BASE[I], globals())
        exec(BASE[I] + "RD2 = " + BASE[I], globals())
        exec(BASE[I] + "RD3 = " + BASE[I], globals())
        exec(BASE[I] + "RD4 = " + BASE[I], globals())
        exec(BASE[I] + "RD5 = " + BASE[I], globals())
        exec(BASE[I] + "RD6 = " + BASE[I], globals())
        exec(BASE[I] + "RD7 = " + BASE[I], globals())
        exec(BASE[I] + "RD8 = " + BASE[I], globals())
        exec(BASE[I] + "GRN = " + BASE[I], globals())
        exec(BASE[I] + "GR1 = " + BASE[I], globals())
        exec(BASE[I] + "GR2 = " + BASE[I], globals())
        exec(BASE[I] + "GR3 = " + BASE[I], globals())
        exec(BASE[I] + "GR4 = " + BASE[I], globals())
        exec(BASE[I] + "GR5 = " + BASE[I], globals())
        exec(BASE[I] + "GR6 = " + BASE[I], globals())
        exec(BASE[I] + "GR7 = " + BASE[I], globals())
        exec(BASE[I] + "GR8 = " + BASE[I], globals())
        exec(BASE[I] + "BLU = " + BASE[I], globals())
        exec(BASE[I] + "BL1 = " + BASE[I], globals())
        exec(BASE[I] + "BL2 = " + BASE[I], globals())
        exec(BASE[I] + "BL3 = " + BASE[I], globals())
        exec(BASE[I] + "BL4 = " + BASE[I], globals())
        exec(BASE[I] + "BL5 = " + BASE[I], globals())
        exec(BASE[I] + "BL6 = " + BASE[I], globals())
        exec(BASE[I] + "BL7 = " + BASE[I], globals())
        exec(BASE[I] + "BL8 = " + BASE[I], globals())
        exec(BASE[I] + "YEL = " + BASE[I], globals())
        exec(BASE[I] + "MAG = " + BASE[I], globals())
        exec(BASE[I] + "CYN = " + BASE[I], globals())
        exec(BASE[I] + "BBR = " + BASE[I], globals())
        exec(BASE[I] + "DBR = " + BASE[I], globals())
        exec(BASE[I] + "BRW = " + BASE[I], globals())
        exec(BASE[I] + "BLK = " + BASE[I], globals())
        exec(BASE[I] + "GY0 = " + BASE[I], globals())
        exec(BASE[I] + "GY1 = " + BASE[I], globals())
        exec(BASE[I] + "GY2 = " + BASE[I], globals())
        exec(BASE[I] + "GY3 = " + BASE[I], globals())
        exec(BASE[I] + "GY4 = " + BASE[I], globals())
        exec(BASE[I] + "GY5 = " + BASE[I], globals())
        exec(BASE[I] + "GY6 = " + BASE[I], globals())
        exec(BASE[I] + "GY7 = " + BASE[I], globals())
        exec(BASE[I] + "GY8 = " + BASE[I], globals())
        exec(BASE[I] + "WHT = " + BASE[I], globals())
        exec(BASE[I] + "GL1 = " + BASE[I], globals())
        exec(BASE[I] + "GL2 = " + BASE[I], globals())
        exec(BASE[I] + "GL3 = " + BASE[I], globals())
        exec(BASE[I] + "GL4 = " + BASE[I], globals())
        exec(BASE[I] + "GL5 = " + BASE[I], globals())
        exec(BASE[I] + "GL6 = " + BASE[I], globals())
        exec(BASE[I] + "GL7 = " + BASE[I], globals())
        exec(BASE[I] + "GL8 = " + BASE[I], globals())
        exec(BASE[I] + "GL9 = " + BASE[I], globals())
        exec(BASE[I] + "GL0 = " + BASE[I], globals())
        exec(BASE[I] + "GLS = " + BASE[I], globals())       
TEST()
SEED = random.randint(1, 9999999)
LAND = [[28,61,87], [39,102,150], [58,150,221], [196,164,120], [123,149,60], [123,149,60], [80,112,3], [80,112,3], [36,72,12], [82,82,82],
        [90,90,90], [104,104,104], [104,104,104], [205,205,205], [205,205,205]]
TEMP = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [255,255,255,20], [255,255,255,40], [255,255,255,80], [255,255,255,160], [255,255,255,220], [255,255,255,220]]
MANA = [[0,0,0,0], [202,34,163,20], [202,34,163,40], [202,34,163,80], [202,34,163,90], [202,34,163,160], [202,34,163,170], [202,34,163,180], [202,34,163,190], [202,34,163,220]]
#    0           1           2         3     4-5      6-7      8-9          10-12    13-14
#Deep-Ocean Medium-Ocean Coast-Ocean Beach Medows    Plains  Foothills   Mountains   Peaks
#0     1-4    5-6     7-10
#Hot Normal Medium  Low Cold 
#    0        1-3      4-6           7
#Dead-Zone Low-Mana Medium-Mana High-Mana
screen.fill([0,0,0])
noise1 = PerlinNoise(octaves=3, seed=SEED)
noise2 = PerlinNoise(octaves=6, seed=SEED)
noise3 = PerlinNoise(octaves=12, seed=SEED)
noise4 = PerlinNoise(octaves=24, seed=SEED)
noise5 = PerlinNoise(octaves=48, seed=SEED)
TER = []
IMP = []
LYON = pygame.Surface((400, 400))
BORD = pygame.Surface((400, 400), pygame.SRCALPHA)
LYTW = pygame.Surface((400, 400), pygame.SRCALPHA)
LYTH = pygame.Surface((400, 400), pygame.SRCALPHA)
SCLX = round(400*(screen.get_width()/400))
SCLY = round(400*(screen.get_height()/400))
if SCLX > SCLY:
    SCLX = SCLY
else:
    SCLY = SCLX
SCLF = SCLX/400
POSX = round(screen.get_width()/2 - (SCLX/2))
POSY = round(screen.get_height()/2 - (SCLX/2))
TXT = MFONT.render("Drawing Terrain...", False, [117, 0, 0])
screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
for CY in range(400):
    row = []
    for CX in range(400):
        NVAL = noise1([CX/400, CY/400])
        NVAL += 0.5 * noise2([CX/400, CY/400])
        NVAL += 0.25 * noise3([CX/400, CY/400])
        NVAL += 0.125 * noise4([CX/400, CY/400])
        NVAL += 0.0625 * noise5([CX/400, CY/400])
        if NVAL < 0:
            NVAL = -(NVAL)
        NVAL = round(14*NVAL)
        if NVAL >= 3 and random.randint(1, 400) == 1:
            #Name, X, Y, Democracy-Dictatorship, LeiseFair-Command, Tolerant-Persecutive, TotalFreedom-TotalOrder, Likes, Dislikes
            IMP.append([NameGen(The = 0), CX+1, CY+1, random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)])
        pygame.draw.rect(LYON, LAND[NVAL], pygame.Rect(CX+1, CY+1, 1, 1))
        row.append(NVAL)
    TER.append(row)
    D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
    D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
    D3 = pygame.transform.scale(LYTH, [SCLX, SCLX])
    screen.blit(D1, [POSX, POSY])
    screen.blit(D2, [POSX, POSY])
    screen.blit(D3, [POSX, POSY])
    pygame.event.get()
    pygame.display.update()

screen.fill([0,0,0])
screen.blit(D1, [POSX, POSY])
screen.blit(D2, [POSX, POSY])
screen.blit(D3, [POSX, POSY])
TXT = MFONT.render("Collinising World...", False, [117, 0, 0])
screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
pygame.event.get()
pygame.display.update()
points = []
size = [400, 400]
COLS = " "
for I in range(len(IMP)):
    COL = random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), 70
    TST = str(COL[0]) + " " + str(COL[1]) + " " + str(COL[2])
    if " " + TST + " " in COLS:
        while " " + TST + " " in COLS:
            COL = random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), 70
            TST = str(COL[0]) + " " + str(COL[1]) + " " + str(COL[2])
    else:
        COLS += TST + " "
    points.append([[IMP[I][1], IMP[I][2]], COL, IMP[I][0]])
for x, y in [(x, y) for x in range(size[0]) for y in range(size[1])]:
    if BORD.get_at((x, y))[:-1] != (255, 255, 255):
        if TER[y-1][x-1] >= 3:
            BORD.set_at((x, y), min([(math.sqrt((x - i[0][0])**2 + (y - i[0][1])**2), i[1]) for i in points])[1])
    pygame.event.get()
BD = pygame.transform.scale(BORD, [SCLX, SCLX])
D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
D3 = pygame.transform.scale(LYTH, [SCLX, SCLX])
screen.blit(D1, [POSX, POSY])
screen.blit(D2, [POSX, POSY])
screen.blit(BD, [POSX, POSY])
screen.blit(D3, [POSX, POSY])
noise1 = PerlinNoise(octaves=3, seed=SEED+1)
noise2 = PerlinNoise(octaves=6, seed=SEED+1)
noise3 = PerlinNoise(octaves=12, seed=SEED+1)
TEM = []
screen.fill([0,0,0])
TXT = MFONT.render("Creating Global Climate...", False, [117, 0, 0])
screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
for CY in range(400):
    row = []
    for CX in range(400):
        NVAL = noise1([CX/400, CY/400])
        NVAL += 0.125 * TER[CY][CX]
        NVAL += 0.25 * noise2([CX/400, CY/400])
        NVAL += 0.125 * noise3([CX/400, CY/400])
        if NVAL < 0:
            NVAL = -(NVAL)
        NVAL = round(10*NVAL)
        if NVAL > 10:
            NVAL = 10
        if TER[CY][CX] >= 3:
            LYTW.set_at((CX+1, CY+1), pygame.Color(TEMP[NVAL][0], TEMP[NVAL][1], TEMP[NVAL][2], TEMP[NVAL][3]))
            #pygame.draw.rect(DIS, TEMP[NVAL], pygame.Rect(CX+1, CY+1, 1, 1))
        row.append(NVAL)
    TEMP.append(row)
    D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
    D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
    D3 = pygame.transform.scale(LYTH, [SCLX, SCLX])
    screen.blit(D1, [POSX, POSY])
    screen.blit(D2, [POSX, POSY])
    screen.blit(BD, [POSX, POSY])
    screen.blit(D3, [POSX, POSY])
    for I in range(len(IMP)):
        TXT = TFONT.render(IMP[I][0], False, [117, 0, 0])
        screen.blit(TXT, [POSX + SCLF*IMP[I][1] - TXT.get_width()/2, POSY + SCLF*IMP[I][2] - TXT.get_height()/2])
        #print([SCLX + SCLF*IMP[I][1], SCLX + SCLF*IMP[I][2]], [screen.get_width(), screen.get_height()])
    pygame.event.get()
    pygame.display.update()
D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
D3 =pygame.transform.scale(LYTH, [SCLX, SCLX])
screen.blit(D1, [POSX, POSY])
screen.blit(D2, [POSX, POSY])
screen.blit(BD, [POSX, POSY])
screen.blit(D3, [POSX, POSY])
for I in range(len(IMP)):
    TXT = TFONT.render(IMP[I][0], False, [117, 0, 0])
    screen.blit(TXT, [POSX + SCLF*IMP[I][1] - TXT.get_width()/2, POSY + SCLF*IMP[I][2] - TXT.get_height()/2])
noise1 = PerlinNoise(octaves=3, seed=SEED+2)
noise2 = PerlinNoise(octaves=6, seed=SEED+2)
MAN = []
screen.fill([0,0,0])
TXT = MFONT.render("Adding Ambient Mana...", False, [117, 0, 0])
screen.blit(TXT, [4, screen.get_height()-TXT.get_height()])
for CY in range(400):
    row = []
    for CX in range(400):
        NVAL = noise1([CX/400, CY/400])
        NVAL += 0.5 * noise2([CX/400, CY/400])
        if NVAL < 0:
            NVAL = -(NVAL)
        NVAL = round(9*NVAL)
        LYTH.set_at((CX+1, CY+1), pygame.Color(MANA[NVAL][0], MANA[NVAL][1], MANA[NVAL][2], MANA[NVAL][3]))
        #pygame.draw.rect(DIS, MANA[NVAL], pygame.Rect(CX+1, CY+1, 1, 1))
        row.append(NVAL)
    MAN.append(row)
    D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
    D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
    D3 =pygame.transform.scale(LYTH, [SCLX, SCLX])
    screen.blit(D1, [POSX, POSY])
    screen.blit(D2, [POSX, POSY])
    screen.blit(BD, [POSX, POSY])
    screen.blit(D3, [POSX, POSY])
    for I in range(len(IMP)):
        TXT = TFONT.render(IMP[I][0], False, [117, 0, 0])
        screen.blit(TXT, [POSX + SCLF*IMP[I][1] - TXT.get_width()/2, POSY + SCLF*IMP[I][2] - TXT.get_height()/2])
    
    pygame.event.get()
    pygame.display.update()
D1 = pygame.transform.scale(LYON, [SCLX, SCLX])
D2 = pygame.transform.scale(LYTW, [SCLX, SCLX])
D3 =pygame.transform.scale(LYTH, [SCLX, SCLX])
screen.blit(D1, [POSX, POSY])
screen.blit(D2, [POSX, POSY])
screen.blit(BD, [POSX, POSY])
screen.blit(D3, [POSX, POSY])
for I in range(len(IMP)):
    TXT = TFONT.render(IMP[I][0], False, [117, 0, 0])
    screen.blit(TXT, [POSX + SCLF*IMP[I][1] - TXT.get_width()/2, POSY + SCLF*IMP[I][2] - TXT.get_height()/2])
PRX, PRY = 200, 200
STATS = ["Move To Update"]
REJN = ""
keys = pygame.key.get_pressed()
while not keys[pygame.K_RETURN]:
    keys = pygame.key.get_pressed()
    screen.fill([0,0,0])
    screen.blit(D1, [POSX, POSY])
    screen.blit(D2, [POSX, POSY])
    screen.blit(BD, [POSX, POSY])
    screen.blit(D3, [POSX, POSY])
    for I in range(len(IMP)):
        if IMP[I][0] == REJN:
            TXT = TFONT.render(IMP[I][0], False, [255, 191, 0])
        else:
            TXT = TFONT.render(IMP[I][0], False, [117, 0, 0])
        screen.blit(TXT, [POSX + SCLF*IMP[I][1] - TXT.get_width()/2, POSY + SCLF*IMP[I][2] - TXT.get_height()/2])
    RX, RY = pygame.mouse.get_pos()
    if RX == PRX and RY == PRY:
        for I in range(len(STATS)):
            TXT = FONT.render(STATS[I], False, [117, 0, 0])
            screen.blit(TXT, [POSX + D1.get_width() + 10, POSY+(TXT.get_height()*I)])
    else:
        PRX, PRY = RX, RY
        try:
            DT = BD.get_at((RX-POSX, RY-POSY))
        except:
            pass
        RX = round((RX-POSX)/SCLF)
        RY = round((RY-POSY)/SCLF)
        STATS = []
        STATS.append("XY: (" + str(RX) + ", " + str(RY) + ")")
        try:
            FND = 0
            for CHK in range(len(points)):
                if DT == points[CHK][1]:
                    FND = CHK
            STATS.append("Region: " + str(points[FND][2]))
            REJN = str(points[FND][2])
        except:
            pass
        DISC = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        try:
            DISC[IMP[FND][3]] = "|"
            DISC = "".join(DISC)
            STATS.append("Democratic" + DISC + "Dictatorial")
        except:
            pass
        DISC = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        try:
            DISC[IMP[FND][4]] = "|"
            DISC = "".join(DISC)
            STATS.append("Unregulated" + DISC + "Command")
        except:
            pass
        DISC = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        try:
            DISC[IMP[FND][5]] = "|"
            DISC = "".join(DISC)
            STATS.append("Tolorant" + DISC + "Persecutive")
        except:
            pass
        DISC = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        try:
            DISC[IMP[FND][6]] = "|"
            DISC = "".join(DISC)
            STATS.append("Freedom" + DISC + "Order")
        except:
            pass
        DISC = ["Deep-Ocean", "Medium-Ocean", "Coast-Ocean", "Beach", "Medows", "High-Medows", "Plains", "High-Plains", "Hills", "Foothills", "Low-Mountains", "Medium-Mountains", "High-Mountains", "Low-Peaks", "High-Peaks"]
        try:
            STATS.append("Terrain: " + str(DISC[TER[RY][RX]]))
        except:
            pass
        DISC = ["Very Hot", "Hot", "Tropical", "Normal", "Normal", "Normal", "Temped", "Temped", "Cold", "Very Cold", "Freezing"]
        try:
            STATS.append("Climate: " + str(DISC[TEMP[RY][RX]]))
        except:
            pass
        DISC = ["Dead-Zone", "Very-Little", "Little", "Small-Amount", "Normal", "Medium-Amount", "High", "Extremely-High"]
        try:
            STATS.append("Ambient Mana: " + str(DISC[MAN[RY][RX]]))
        except:
            pass
    pygame.event.get()
    pygame.display.update()
    time.sleep(0.011)
time.sleep(2)
#    0           1           2         3     4-5      6-7      8-9          10-12    13-14
#Deep-Ocean Medium-Ocean Coast-Ocean Beach Medows    Plains  Foothills   Mountains   Peaks
#RendMap(SEED)
TEST()
while True:
    screen.fill([0,0,0])
    
    if keys[pygame.K_a]:
        if MODE == 1:
            PPOS[2] += 1
        else:
            time.sleep(0.1)
        SLC[2] += 1
        CXY = PlaceCube(PPOS[0], PPOS[1], PPOS[2], REC = False, RETR = True)
        OFFX = screen.get_width()/2-CXY[0]
        OFFY = screen.get_height()/2-CXY[1]
        PUPD = True
    elif keys[pygame.K_w]:
        if MODE == 1:
            PPOS[2] -= 1
        else:
            time.sleep(0.1)
        SLC[2] -= 1
        CXY = PlaceCube(PPOS[0], PPOS[1], PPOS[2], REC = False, RETR = True)
        OFFX = screen.get_width()/2-CXY[0]
        OFFY = screen.get_height()/2-CXY[1]
        PUPD = True
    if keys[pygame.K_s]:
        if MODE == 1:
            PPOS[0] += 1
        else:
            time.sleep(0.1)
        SLC[0] += 1
        CXY = PlaceCube(PPOS[0], PPOS[1], PPOS[2], REC = False, RETR = True)
        OFFX = screen.get_width()/2-CXY[0]
        OFFY = screen.get_height()/2-CXY[1]
        PUPD = True
    elif keys[pygame.K_q]:
        if MODE == 1:
            PPOS[0] -= 1
        else:
            time.sleep(0.1)
        SLC[0] -= 1
        CXY = PlaceCube(PPOS[0], PPOS[1], PPOS[2], REC = False, RETR = True)
        OFFX = screen.get_width()/2-CXY[0]
        OFFY = screen.get_height()/2-CXY[1]
        PUPD = True
