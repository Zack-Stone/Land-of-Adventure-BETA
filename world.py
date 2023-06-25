import map_tile, items

class World():
  def __init__(self, name, tile_map):
    #set x, y for each room
    self.name = name
    self.tile_map = tile_map

  def getTile(self, x, y):
    return self.tile_map[x][y]

  def tile_exists(self, x, y): 
    if x <= 4 and x >= 0 and y <= 3 and y >= 0:
      return self.tile_map[x][y] != None
    else:
      return False

  def getTileMap(self):
    return self.tile_map

class EasyKingdom(World):
  def __init__(self):
    #[[None,          FindDaggerRoom, BossRoom,       LeaveCaveRoom], 
    #[FindGoldRoom,   GiantSpiderRoom,None,           None], 
    #[PuzzleRoom,     None,           None,           None], 
    #[ShopRoom,       GiantSpiderRoom,FindSwordRoom,  MedicalRoom], 
    #[StartingRoom,   FindIceBoltRoom,None,           ManaRoom]]
    name = "Kingdom of Easy"
    self.StartingXY = (4, 0)
    tile_map = [[None,map_tile.FindDaggerRoom(0,1,"LOT"),map_tile.QueenSpiderRoom(0,2, "ENM"),map_tile.LeaveCaveRoom(0,3, "END")],[map_tile.FindGoldRoom(1,0,100, "GLD"),map_tile.GiantSpiderRoom(1,1, "ENM"),None,None],[map_tile.PuzzleRoom(2,0, "PZL"),None,None,None],[map_tile.ShopRoom(3,0, [items.Sword(), items.Shield(), items.TestWeapon(), items.LeaveItem()],"SHR"),map_tile.GiantSpiderRoom(3,1, "EMN"),map_tile.FindSwordRoom(3,2, "LOT"),map_tile.MedicalRoom(3,3,50, "MED")],[map_tile.StartingRoom(4,0, "STR"),map_tile.FindIceBolt(4, 1, "ICE"),None,map_tile.ManaRoom(4, 3, 0, "MAN")]]

    super().__init__(name, tile_map)

class HardTown(World):
  def __init__(self):
    name = "Hard Town"
    self.StartingXY = (0, 0)
    tile_map = [[map_tile.StartingRoom(0,0, "STR"),map_tile.GoblinRoom(0,1, "GOB"),map_tile.EmptyCavePath(0,2, "ECP"),None,None,None,None,map_tile.GoblinRoom(0,7, "GOB"),map_tile.PuzzleRoom(0,8, "BPZ"),map_tile.FindOldLongSwordRoom(0,9, "OLS")],[map_tile.GoblinRoom(1,0, "GOB"),None,map_tile.GoblinRoom(1,2, "GOB"),map_tile.EmptyCavePath(1,3, "ECP"),map_tile.GoblinRoom(1,4, "GOB"),map_tile.PuzzleRoom(1,5, "BPZ"),map_tile.EmptyCavePath(1,6, "ECP"),map_tile.GoblinRoom(1,7, "GOB"),None,map_tile.PuzzleRoom(1,9, "APZ")],[map_tile.EmptyCavePath(2,0, "ECP"),map_tile.GoblinRoom(2,1, "GOB"),None,map_tile.ManaRoom(2,3,0,"MAN"),None,map_tile.GoblinRoom(2,5,"GOB"),None,None,map_tile.EmptyCavePath(2,8, "ECP"),map_tile.PuzzleRoom(2,9, "APZ")],[None,map_tile.EmptyCavePath(3,1, "ECP"),map_tile.MedicalRoom(3,2,50,"MED"),None,None,map_tile.PuzzleRoom(3,5, "BPZ"),None,None,map_tile.PuzzleRoom(3,8,"APZ"),None],[None,map_tile.GoblinRoom(4,1,"GOB"),None,None,map_tile.FindOldSwordRoom(4,4,"OSR"),map_tile.FindShortSwordRoom(4,5,"SSR"),map_tile.GoblinRoom(4,6,"GOB"),map_tile.PuzzleRoom(4,7,"BPZ"),map_tile.EmptyCavePath(4,8,"ECP"),None],[None,map_tile.PuzzleRoom(5,1,"BPZ"),map_tile.GoblinRoom(5,2,"GOB"),map_tile.PuzzleRoom(5,3,"BPZ"),map_tile.FindSwordRoom(5,4,"FSR"),map_tile.FindOldShortSwordRoom(5,5,"OSS"),None,None,map_tile.GoblinRoom(5,8,"GOB"),None],[None,map_tile.EmptyCavePath(6,1,"ECP"),None,None,map_tile.GoblinRoom(6,4,"GOB"),None,None,map_tile.MedicalRoom(6,7,35,"MED"),map_tile.EmptyCavePath(6,8,"ECP"),None],[map_tile.EmptyCavePath(7,0,"ECP"),map_tile.GoblinRoom(7,1,"GOB"),None,None,map_tile.PuzzleRoom(7,4,"BPZ"),None,map_tile.ManaRoom(7,6,0,"MAN"),None,map_tile.ShopRoom(7,8, [items.Longsword(), items.Oldlongsword(), items.TestWeapon(), items.LeaveItem()],"SHR"),map_tile.PuzzleRoom(7,9,"APZ")],[map_tile.PuzzleRoom(8,0,"BPZ"),None,map_tile.GoblinRoom(8,2,"GOB"),map_tile.PuzzleRoom(8,3,"APZ"),map_tile.EmptyCavePath(8,4,"ECP"),map_tile.GoblinRoom(8,5,"GOB"),map_tile.EmptyCavePath(8,6,"ECP"),map_tile.ShopRoom(8,7, [items.Longsword(), items.Oldlongsword(), items.TestWeapon(), items.LeaveItem()],"SHR"),None,map_tile.KingoftheDungeonRoom(8,9,"KDR")],[map_tile.FindLongSwordRoom(9,0,"FLS"),map_tile.PuzzleRoom(9,1,"APZ"),map_tile.PuzzleRoom(9,2,"APZ"),None,None,None,None,map_tile.PuzzleRoom(9,7,"APZ"),map_tile.KingoftheDungeonRoom(9,8,"KDR"),map_tile.LeaveCaveRoom(9,9,"END")]]

    super().__init__(name, tile_map)


class AdeptVille(World):
  def __init__(self):
#    [None,                            None,                              None,                                map_tile.EmptyCavePath(0, 3),   
#     None,                            map_tile.FindGoldRoom(0, 5),  map_tile.FindSwordRoom(0, 6),        None],
#    [map_tile.FindGoldRoom(1, 0),map_tile.PuzzleRoom(1, 1),         map_tile.FindOldLongSwordRoom(1, 2), map_tile.GiantSpiderRoom(1, 3),
#     None,                            map_tile.PuzzleRoom(1, 5),         None,                                None],
#   [None,                            None,                              map_tile.StartingRoom(2, 2),         None,
#    map_tile.PuzzleRoom(2, 4),       map_tile.MedicalRoom(2, 5, amt=50),map_tile.OgreRoom(2, 6),             None], 
#[None,                            map_tile.PuzzleRoom(3, 1),         map_tile.OgreRoom(3, 2),             map_tile.PuzzleRoom(3, 3), map_tile.EmptyCavePath(3, 4),     None,                              map_tile.MedicalRoom(3, 6, amt=50),  None], 
#    [None,                            map_tile.FindSwordRoom(4, 1),      None,                                None,
#     None,                            None,                              map_tile.BossRoom(4, 6),             map_tile.LeaveCaveRoom(4, 7)]
#    [None,                            map_tile.PuzzleRoom(5,1),          map_tile.FindShieldRoom(5,2),        None,
#     None,                            None,                              map_tile.PuzzleRoom(5, 6),           None], 
#    [map_tile.FindGoldRoom(6, 0),map_tile.PuzzleRoom(6, 1),         None,                                None,
#     map_tile.FindOldLongSwordRoom(6, 4),map_tile.PuzzleRoom(6, 5),      None,                                map_tile.FindGoldRoom(6, 7)], 
#    [None,                            map_tile.BossRoom(7, 1),           map_tile.LeaveCaveRoom(7, 2),        None,
#     None,                            map_tile.FindLongSwordRoom(7, 5),  map_tile.PuzzleRoom(7, 6),           None]]

    name = "Adeptville"
    self.StartingXY = (2, 2)
    tile_map = [[None,None,None,map_tile.EmptyCavePath(0, 3, "ECP"),None,map_tile.FindGoldRoom(0, 5, 100, "GLD"),map_tile.FindSwordRoom(0, 6,"LOT"),None],[map_tile.FindGoldRoom(1, 0,100,"GLD"),map_tile.PuzzleRoom(1, 1,"PZL"),map_tile.FindOldLongSwordRoom(1, 2,"LOT"),map_tile.GiantSpiderRoom(1, 3,"ENM"),None,map_tile.PuzzleRoom(1, 5,"PZL"),None,None],[None,None,map_tile.StartingRoom(2, 2,"STR"),None,map_tile.PuzzleRoom(2, 4,"PZL"),map_tile.MedicalRoom(2, 5, 50,"MED"),map_tile.OgreRoom(2, 6,"ENM"),None],[None,map_tile.PuzzleRoom(3, 1, "PZL"),map_tile.OgreRoom(3, 2, "EMN"),map_tile.PuzzleRoom(3,3, "PZL"),map_tile.EmptyCavePath(3, 4, "ECP"),None,map_tile.MedicalRoom(3, 6,50, "MED"),None],[None,map_tile.FindSwordRoom(4, 1, "LOT"),None,None,None,None,map_tile.QueenSpiderRoom(4,2,"ENM"),map_tile.LeaveCaveRoom(4, 7,"END")],[None,map_tile.PuzzleRoom(5,1,"PZL"),map_tile.FindShieldRoom(5,2,"LOT"),None,None,None,map_tile.PuzzleRoom(5, 6,"PZL"),None],[map_tile.FindGoldRoom(6, 0,100,"GLD"),map_tile.PuzzleRoom(6, 1,"PZL"),None,None,map_tile.FindOldLongSwordRoom(6, 4,"LOT"),map_tile.PuzzleRoom(6, 5,"PZL"), map_tile.EmptyCavePath(6, 6, "ECP"),map_tile.FindGoldRoom(6, 7, 100, "GLD")],[None,map_tile.OgreLordRoom(7, 1,"ENM"),map_tile.LeaveCaveRoom(7, 2,"END"),None,None,map_tile.FindLongSwordRoom(7, 5,"LOT"), map_tile.PuzzleRoom(7, 6,"PZL"),None]]
    super().__init__(name, tile_map)