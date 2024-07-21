# SkyGrid Filter by SethBling
# Feel free to modify and reuse, but credit to SethBling would be nice.
# Indev edits by Vallee152

from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_Int
import random

displayName = "SethBling's Sky Grid"
inputs = (
    ("Grid Length", (1, 1, 100)),
    ("Grid Width", (1, 1, 100)),
    ("Grid Height", (1, 1, 100)),
    ("Generate Chests", False)
)

def perform(level, box, options):
    gridlength = options["Grid Length"]
    gridwidth = options["Grid Width"]
    gridheight = options["Grid Height"]
    generatechests = options["Generate Chests"]


    total = 0
    cump = {}

    p = normalp(generatechests)

    # generate the cumulative distribution
    for key, value in p.iteritems():
        cump[key] = (total, total + value)
        total += value
            
    for x in xrange(box.minx, box.maxx, gridlength):
        for y in xrange(box.miny, box.maxy, gridheight):
            for z in xrange(box.minz, box.maxz, gridwidth):
                blockid = pickblock(cump, total)

                if(blockid == 6 or blockid == 37 or blockid == 38 or
                   blockid == 39 or blockid == 40):
                    level.setBlockAt(x, y, z, 3) #dirt
                    if(y < box.maxy):
                        level.setBlockAt(x, y+1, z, blockid)
                    if(y < box.maxy):
                        level.setBlockAt(x, y+1, z, blockid)
                else:
                    level.setBlockAt(x, y, z, blockid)

                if(blockid == 54):
                    fillChestAt(level, x, y, z)



# returns an unnormalized probability distribution for blocks in the
# overworld
def normalp(generatechests):
    p = {}
    p[1] = 120                  #stone
    p[2] = 80                   #grass
    p[3] = 20                   #dirt
    p[6] = 20                   #sapling
    p[9] = 10                   #still water
    p[11] = 5                   #still lava
    p[12] = 30                  #sand
    p[13] = 15                  #gravel
    p[14] = 10                  #gold ore
    p[15] = 20                  #iron ore
    p[16] = 40                  #coal ore
    p[17] = 100                 #log
    p[21] = 1                   #red cloth
    p[22] = 1                   #orange cloth
    p[23] = 1                   #yellow cloth
    p[24] = 1                   #chartreuse cloth
    p[25] = 1                   #green cloth
    p[26] = 1                   #spring green cloth
    p[27] = 1                   #cyan cloth
    p[28] = 1                   #capri cloth
    p[29] = 1                   #ultramarine cloth
    p[30] = 1                   #violet cloth
    p[31] = 1                   #purple cloth
    p[32] = 1                   #magenta cloth
    p[33] = 1                   #rose cloth
    p[34] = 1                   #dark grey cloth
    p[35] = 1                   #light grey cloth
    p[36] = 1                   #white cloth
    p[37] = 2                   #flower
    p[38] = 2                   #red flower
    p[39] = 4                   #brown mushroom
    p[40] = 4                   #red mushroom
    p[45] = 2                   #bricks
    p[47] = 3                   #bookshelves
    p[48] = 5                   #mossy cobblestone
    p[54] = 1 * generatechests  #chest
    p[56] = 1                   #diamond ore

    return p

# picks a random block from a cumulative distribution
def pickblock(cump, size):
    r = random.random() * size
    
    for key, value in cump.iteritems():
        low, high = value
        if r >= low and r < high:
            return key

# fills a chest with random goodies
def fillChestAt(level, x, y, z):
    chunk = level.getChunk(x / 16, z / 16)

    chest = TileEntity.Create("Chest")
    
    # Indev uses a different position format than later versions for tile entities
    chest["Pos"] = TAG_Int((z * 1024 + y) * 1024 + x)

    TileEntity.setpos(chest, (x, y, z))

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(256, 294)) #various weapons/random

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(298, 317)) #various armor

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(318, 321)) #various food/tools
    
    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(296, 297)) #various food/tools

    if(random.random() < 0.7):
        itemid = randomInRange(1, 5)
        count = randomInRange(10, 64)
        slot = randomInRange(0, 26)
        blocks = createItem(itemid, count, 0, slot)
        chest["Items"].append(blocks)

    if(random.random() < 0.4):
        chest["Items"].append(createItem(6, 1, 0, randomInRange(0, 26))) #sapling

    if(random.random() < 0.05):
        chest["Items"].append(createItem(49, 32, 0, randomInRange(0, 26))) #obsidian

    chunk.TileEntities.append(chest)

# creates a random item in an item id range    
def createItemInRange(minid, maxid, count=1):
    itemid = randomInRange(minid, maxid)
    slot = randomInRange(0, 26)

    return createItem(itemid, count, 0, slot)

# creates an item with a randomized damage value
def createItemWithRandomDamage(itemid, mindmg, maxdmg, count=1):
    dmg = randomInRange(mindmg, maxdmg)
    slot = randomInRange(0, 26)
    
    return createItem(itemid, count, dmg, slot)

# creates an item
def createItem(itemid, count=1, damage=0, slot=0):
    item = TAG_Compound()

    item["id"] = TAG_Short(itemid)
    item["Damage"] = TAG_Short(damage)
    item["Count"] = TAG_Byte(count)
    item["Slot"] = TAG_Byte(slot)

    return item

# returns a random integer between minr and maxr, inclusive
def randomInRange(minr, maxr):
    return int(random.random() * (maxr - minr + 1)) + minr
