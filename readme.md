## Prerequisites

You should have the below ready to go.

* MCEdit with `skygrid.py` in the `filters` folder.
* An NBT editor.
* Minecraft Indev.
* A proxy to supply the required resources to Minecraft Indev.

I use [MCEdit version 0.1.8](https://github.com/mcedit/mcedit/releases), [NBTExplorer](https://github.com/jaquadro/NBTExplorer/releases/tag/v2.8.0-win), [Omniarchive](https://vault.omniarchive.uk/archive/java/client-indev/index.html), [MultiMC](https://multimc.org/), and the [Betacraft proxy](https://betacraft.uk).

## Basic Generation

These are the steps I follow to create a basic Sky Grid map without any chests.

1. Create a copy of `skygrid template.dat` and rename it to something else with the file extension `.mclevel`. Open the copy in MCEdit.
2. Hit ctrl+A and use the filter, which is named "Sethbling's Sky Grid." Set "Grid Width" and "Length" to `3`, and "Grid Height" to `4`. Leave "Generate Chests" unchecked.
3. Save the world and reload, before flying around a little just to look at the map.
4. Change the file extension back to `.dat` and open the folder it and the template are in using NBTExplorer. Delete all entities that may be in the world save and copy the one from the template file in.
5. Save and exit NBTExplorer and then change the file extension of the skygrid map back to `.mclevel`. The map is ready to be played.

## Chest Generation

Due to some issues with every version of MCEdit I can find that's compatible with editing mclevel files, you need to do some extra steps to include chests in your map.

1. Have a copy of `skygrid chest template` in the .minecraft saves folder and open it in MCEdit under "Load World."
2. Hit ctrl+A and use the filter. Set "Grid Width" and "Length" to `3`, and "Grid Height" to `4`. Check the box beside "Generate Chests."
3. Use the selection tool to export the world as a `.schematic` file.
4. Exit MCEdit without saving
5. Make a copy of `skygrid template.dat` and rename it, keeping the file extension as `.dat`. Copy the schematic file into the same folder.
6. Open the folder in NBTExplorer, and delete the elements, "Blocks" and "TileEntities," from the template copy. Then copy the "TileEntites" and "Blocks" elements from the schematic into their respective places.
7. Save and exit NBTExplorer and then change the file extension of the skygrid map to `.mclevel`. The map is ready to be played.

Do note that, for whatever reason, the filter will sometimes save the integer formatted position as a short, which completely misaligns the chest tile entities. You may want to check the positions of the chest tile entities before playing. There are two ways to check. One way is to open the map in MCEdit and fly around to see if the tile entity outlines match chest positions. Another way to check is to look at the properties of one or two of the chest entities in NBTExplorer and see if `(z * 1024 + y) * 1024 + x` equals the `Pos` tag. 