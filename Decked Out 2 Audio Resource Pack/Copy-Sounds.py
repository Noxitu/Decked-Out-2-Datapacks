from pathlib import Path
import shutil
import json


OGG_DATA = (
    Path.home()
    / "AppData/Roaming/.minecraft/profiles/h9/saves/hc9/audio_player_data_ogg"
)

ASSETS_ROOT = Path(__file__).parent / "assets"


IDS = {
    "": "7323bc71-0053-4679-966d-1a4099eb8f1c", # Generic difficulty setting? # DO_Shulker_Loaded_1 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.1": "34e9c2c9-c961-48e4-80d1-c182d13f42a8",  # DO_Atmospherics_CaveGust_1 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.2": "57711562-505e-4f31-82b1-01fd462734a0",  # DO_Atmospherics_CaveGust_2 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.3": "c345eccc-046f-4eeb-a782-7eb8ca14b938",  # DO_Atmospherics_CaveGust_3 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.4": "4b42a8b1-3a7d-43d3-9b03-e9fc55c39002",  # DO_Atmospherics_CaveGust_4 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.5": "c05eed60-ea9d-4af2-8e8a-93f456c77e56",  # DO_Atmospherics_CaveGust_5 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.6": "dc1b5992-d862-4542-b28f-9647a72cfea7",  # DO_Atmospherics_CaveGust_6 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.7": "f32d95aa-7532-4a13-944f-a1f9859b21f5",  # DO_Atmospherics_CaveGust_7 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.8": "d78183dd-4b1a-4f3a-918e-cc8b12d0ad78",  # DO_Atmospherics_CaveGust_8 BY Del Chupenebray/Joel Bickford
    "ambient.cave_gust.9": "4351ada5-2fe1-4dd1-b739-ff0bc2d6211c",  # DO_Atmospherics_CaveGust_9 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.1": "f33500b4-325e-489c-ad05-b21e2131b077",  # DO_Ambient_Drone_DeepFrost_1 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.10": "da214c03-1077-44d4-92e0-b80d64c4aa3f",  # DO_Ambient_Drone_DeepFrost_10 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.11": "3bbbec08-c4c5-4dc8-ad6c-09818a8ef1c0",  # DO_Ambient_Drone_DeepFrost_11 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.12": "90e3c4a5-5c02-4a50-ab29-ef48f3085f8d",  # DO_Ambient_Drone_DeepFrost_12 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.13": "96a041fe-e707-46fd-8f19-6257070855b6",  # DO_Ambient_Drone_DeepFrost_13 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.14": "6a5fdfe5-517a-44c9-970c-2c63e943f10a",  # DO_Ambient_Drone_DeepFrost_14 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.15": "7a9ded95-2b70-46fa-b62a-c0200a3d6837",  # DO_Ambient_Drone_DeepFrost_15 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.16": "e6507218-95f6-4459-b7f0-91e88bd5b3e6",  # DO_Ambient_Drone_DeepFrost_16 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.17": "5cccaa4f-d4aa-4095-8e2a-406e0f88a191",  # DO_Ambient_Drone_DeepFrost_17 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.18": "1030f3cc-d8b6-497b-9a8b-21e409f4761f",  # DO_Ambient_Drone_DeepFrost_18 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.2": "ac3075a5-351a-4cb4-ba7c-837b1716d53c",  # DO_Ambient_Drone_DeepFrost_2 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.3": "1f75dbb7-117a-40d9-813c-049838e7987d",  # DO_Ambient_Drone_DeepFrost_3 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.4": "328d2142-e139-4177-9a5e-6a223367da9a",  # DO_Ambient_Drone_DeepFrost_4 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.5": "103b9608-8d37-4894-96a7-53cdacf6a158",  # DO_Ambient_Drone_DeepFrost_5 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.6": "f39e5048-42b1-4d17-9dda-cf3c7ebbcdcc",  # DO_Ambient_Drone_DeepFrost_6 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.7": "c4b97458-87d1-4cce-940e-4c22ec9385ca",  # DO_Ambient_Drone_DeepFrost_7 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.8": "a2a79a50-07b6-4573-a16f-bb7629ab162a",  # DO_Ambient_Drone_DeepFrost_8 BY Del Chupenebray/Joel Bickford
    "ambient.drone_deepfrost.9": "ad066a0e-13f7-46b0-b75f-ab62eda6275b",  # DO_Ambient_Drone_DeepFrost_9 BY Del Chupenebray/Joel Bickford
    "ambient.drone.1": "77ced0ba-20bb-4bbf-a35d-1b787b57459f",  # DO_Ambient_Drone_Set1_1 BY Del Chupenebray/Joel Bickford
    "ambient.drone.2": "553f395f-f8c1-4bec-9ab1-6b180db1ae4d",  # DO_Ambient_Drone_Set1_2 BY Del Chupenebray/Joel Bickford
    "ambient.drone.3": "8eb9f97f-f825-49b6-a544-6928a395f294",  # DO_Ambient_Drone_Set1_3 BY Del Chupenebray/Joel Bickford
    "ambient.drone.4": "44da4c88-c857-4e1b-84d5-32cff4fe11b0",  # DO_Ambient_Drone_Set1_4 BY Del Chupenebray/Joel Bickford
    "ambient.drone.5": "1f96ee69-5c48-402d-97bf-07569cc87dd9",  # DO_Ambient_Drone_Set1_5 BY Del Chupenebray/Joel Bickford
    "ambient.drone.6": "af1f3552-b249-43d8-85e6-cb68c88c934b",  # DO_Ambient_Drone_Set1_6 BY Del Chupenebray/Joel Bickford
    "ambient.drone.7": "52e70667-5c2e-44da-8167-ca9d30470c2a",  # DO_Ambient_Drone_Set1_7 BY Del Chupenebray/Joel Bickford
    "ambient.drone.8": "72e21207-4074-477b-9d5d-4a90f53d3c6d",  # DO_Ambient_Drone_Set1_8 BY Del Chupenebray/Joel Bickford
    "ambient.drone.9": "efbc63f4-1ca4-4bd1-ab4d-e4e54bd4c114",  # DO_Ambient_Drone_Set1_9 BY Del Chupenebray/Joel Bickford
    "ambient.ghostly_whisper.1": "474bff59-1af9-410b-95a9-63142a6794c5",  # DO_Atmospherics_GhostlyWhisper BY Del Chupenebray/Joel Bickford
    "ambient.ghostly_whisper.2": "eb56e58d-f5e8-4a6c-a224-62d6ca0632c2",  # DO_Atmospherics_GhostlyWhisper BY Del Chupenebray/Joel Bickford
    "ambient.hi_cleo": "5849d869-53a9-41b2-8ce9-824f3db15c2b", # BY
    "ambient.ice.1": "a870fc9b-625a-4318-847c-bceb5fa269ab",  # DO_Atmospherics_IceCracks_1 BY Del Chupenebray/Joel Bickford
    "ambient.ice.10": "ae6d3490-c442-4130-b982-57d0e0a401ae",  # DO_Atmospherics_IceCracks_1 BY Del Chupenebray/Joel Bickford
    "ambient.ice.2": "3bd48f07-0030-441b-be9e-e9191ed946c8",  # DO_Atmospherics_IceCracks_2 BY Del Chupenebray/Joel Bickford
    "ambient.ice.3": "7317aaf5-0282-43e5-81c8-a3bfcd85769c",  # DO_Atmospherics_IceCracks_3 BY Del Chupenebray/Joel Bickford
    "ambient.ice.4": "e245bd20-f67c-4444-b7a9-dfad5783bb3d",  # DO_Atmospherics_IceCracks_4 BY Del Chupenebray/Joel Bickford
    "ambient.ice.5": "6249f397-2afa-4d0b-9954-5279492da85a",  # DO_Atmospherics_IceCracks_5 BY Del Chupenebray/Joel Bickford
    "ambient.ice.6": "2f2b79fb-b270-418a-b363-8c2be0a838b9",  # DO_Atmospherics_IceCracks_6 BY Del Chupenebray/Joel Bickford
    "ambient.ice.7": "27c3b301-dd4d-41fb-a892-11ed459a5069",  # DO_Atmospherics_IceCracks_7 BY Del Chupenebray/Joel Bickford
    "ambient.ice.8": "e8d83d77-bdfc-47fa-b784-799fe8186a15",  # DO_Atmospherics_IceCracks_8 BY Del Chupenebray/Joel Bickford
    "ambient.ice.9": "b2dfb727-5d6d-4df5-acd1-0c6f7b8f7de4",  # DO_Atmospherics_IceCracks_9 BY Del Chupenebray/Joel Bickford
    "ambient.metal.1": "cb68b96e-1383-46c1-82ac-ac6c1adc410f",  # DO_Atmospherics_MetalCreak_1 BY Del Chupenebray/Joel Bickford
    "ambient.metal.2": "3296d2d7-d6e2-48e7-b678-8ad6a782c0e0",  # DO_Atmospherics_MetalCreak_2 BY Del Chupenebray/Joel Bickford
    "ambient.metal.3": "84e7259a-e9a7-477e-8e10-d44c625cefb7",  # DO_Atmospherics_MetalCreak_3 BY Del Chupenebray/Joel Bickford
    "ambient.metal.4": "b12b5ac9-8a18-40ca-b606-bd7b2344da7d",  # DO_Atmospherics_MetalCreak_4 BY Del Chupenebray/Joel Bickford
    "ambient.metal.5": "f9cfeaea-f7cb-4af3-b979-95b53512efb9",  # DO_Atmospherics_MetalCreak_5 BY Del Chupenebray/Joel Bickford
    "ambient.metal.6": "fe991fe2-9f34-4da7-af02-720b6f7647c1",  # DO_Atmospherics_MetalCreak_6 BY Del Chupenebray/Joel Bickford
    "ambient.metal.7": "2492615d-e277-4c74-9824-6f89a6a79eee",  # DO_Atmospherics_MetalCreak_7 BY Del Chupenebray/Joel Bickford
    "ambient.metal.8": "f879fd15-3ca9-41c2-97ec-e088d22ff0f5",  # DO_Atmospherics_MetalCreak_8 BY Del Chupenebray/Joel Bickford
    "ambient.metal.9": "4da80035-5a28-44b5-9840-6d38536bc5d3",  # DO_Atmospherics_MetalCreak_9 BY Del Chupenebray/Joel Bickford
    "ambient.warden_emerge": "30a64aef-5d3b-4db0-999b-af8d65ea775d", # BY
    "ambient.warden_roar": "bc158cd2-d153-4854-a94e-b46007eb2e1a", # BY
    "ambient.wood.1": "fc9e0d1e-87d4-4432-a166-94ed0a4afd62",  # DO_Atmospherics_WoodCreak_1 BY Del Chupenebray/Joel Bickford
    "ambient.wood.2": "07516356-a3bf-4340-abf0-2f406fde65da",  # DO_Atmospherics_WoodCreak_2 BY Del Chupenebray/Joel Bickford
    "ambient.wood.3": "dd87911c-4e42-41d5-a519-809d9ee96b38",  # DO_Atmospherics_WoodCreak_3 BY Del Chupenebray/Joel Bickford
    "ambient.wood.4": "725d5316-ffc2-4ca7-a590-0d0a5a507b7a",  # DO_Atmospherics_WoodCreak_4 BY Del Chupenebray/Joel Bickford
    "ambient.wood.5": "3c10036e-1f7c-4163-903c-1f512807e3ee",  # DO_Atmospherics_WoodCreak_5 BY Del Chupenebray/Joel Bickford
    "ambient.wood.6": "b703e297-fd17-424d-8964-7ac3543de7a1",  # DO_Atmospherics_WoodCreak_6 BY Del Chupenebray/Joel Bickford
    "ambient.wood.7": "c110e7ec-2dd9-4a79-8218-a653f7546976",  # DO_Atmospherics_WoodCreak_7 BY Del Chupenebray/Joel Bickford
    "ambient.wood.8": "55581da0-0038-41cc-bb8c-9859c8873866",  # DO_Atmospherics_WoodCreak_8 BY Del Chupenebray/Joel Bickford
    "ambient.wood.9": "8374ba7e-89aa-48d0-8050-714ca13d5b7f",  # DO_Atmospherics_WoodCreak_9 BY Del Chupenebray/Joel Bickford
    "cards.adrenaline_rush": "7cb66fe6-f320-4e14-895b-cbdd0a458414",  # adrenaline_rush BY Del Chupenebray/Joel Bickford
    "cards.avalanche": "4e2c7daf-a972-4922-9b53-4eb37a1372b0",  # avalanche BY Del Chupenebray/Joel Bickford
    "cards.beast_sense": "26e1f9a1-311a-46e9-aba0-b5f7613b03e7",  # beast_sense BY Del Chupenebray/Joel Bickford
    "cards.bounding_strides": "19f2790c-176c-45f1-9323-1dcba732dce0",  # bounding_strides BY Del Chupenebray/Joel Bickford
    "cards.brilliance": "81ce29f4-2dfa-4c43-9b2a-23d57d7da0cf",  # brilliance BY Del Chupenebray/Joel Bickford
    "cards.cash_cow": "ea8c472a-7688-4576-9bc4-9791082be299",  # cash_cow BY Del Chupenebray/Joel Bickford
    "cards.chill_step": "495f2916-f8fb-42cd-9321-a8fe3a44d53a",  # chill_step BY Del Chupenebray/Joel Bickford
    "cards.cold_snap": "8be0f393-ae01-465d-a203-141bac3f2b97",  # cold_snap BY Del Chupenebray/Joel Bickford
    "cards.deep_frost": "f6974c53-5133-4e32-b122-0202ccc7885d",  # deep_frost BY Del Chupenebray/Joel Bickford
    "cards.dungeon_repairs": "2605e385-7ecd-48f4-9d6d-702289e93586",  # dungeon_repairs BY Del Chupenebray/Joel Bickford
    "cards.eerie_silence": "6242f646-3229-4390-bc80-0c4da6d8e789",  # eerie_silence BY Del Chupenebray/Joel Bickford
    "cards.ember_seeker": "666b14dc-b35a-4c7d-bddc-96f56d09b7d9",  # ember_seeker BY Del Chupenebray/Joel Bickford
    "cards.evasion": "1fc5ac7c-11c0-4209-82d7-9082025f1da0",  # evasion BY Del Chupenebray/Joel Bickford
    "cards.eyes_on_the_prize": "8410391e-3ab5-4a3a-9ff0-5131e2dd3907",  # eyes_on_the_prize BY Del Chupenebray/Joel Bickford
    "cards.frost_focus": "9367209c-901e-4600-a1c1-183d0e1bcd53",  # frost_focus BY Del Chupenebray/Joel Bickford
    "cards.haste": "910008df-9798-4b6c-a1fc-040a48ce52a4",  # haste BY Del Chupenebray/Joel Bickford
    "cards.loot_and_scoot": "6580e672-a123-40f8-b250-79fce86ecae6",  # loot_and_scoot BY Del Chupenebray/Joel Bickford
    "cards.moment_of_clarity": "eead6655-b4bd-47ea-aa7f-1dce62bd1187",  # moment_of_clarity BY Del Chupenebray/Joel Bickford
    "cards.nimble_looting": "9f3cd5ef-7bc3-4bfb-828f-b6f7d366e8f0",  # nimble_looting BY Del Chupenebray/Joel Bickford
    "cards.pay_to_win": "fbcf4874-fe5a-4f54-bac6-1da36378f905",  # pay_to_win BY Del Chupenebray/Joel Bickford
    "cards.pirates_booty": "86f714e8-51a8-4efd-9570-309edb4ac856", # BY
    "cards.quickstep": "eca0b667-66b4-4c49-aedb-966d9c7c2221",  # quickstep BY Del Chupenebray/Joel Bickford
    "cards.reckless_charge ##": "# Card announcement only, without end marker. 672983f0-7a95-4c00-88e1-28b395b5085d",  # reckless_charge BY Del Chupenebray/Joel Bickford
    "cards.reckless_charge": "ede9d11b-de87-4ecf-8bec-c04804fc111c", # BY
    "cards.second_wind": "71c67618-3b64-4f90-b882-c932402f0bc9",  # second_wind BY Del Chupenebray/Joel Bickford
    "cards.smash_and_grab": "15d55192-91f0-493a-a253-9c2231dd47ae",  # smash_and_grab BY Del Chupenebray/Joel Bickford
    "cards.sneak": "4e6821e1-17e5-4fd4-a557-7a1764494a52",  # sneak BY Del Chupenebray/Joel Bickford
    "cards.sprint": "7bd58ea9-fcd8-4afb-9356-218f7b448c02",  # sprint BY Del Chupenebray/Joel Bickford
    "cards.stability": "81cc1aa4-9e52-4b8b-a408-abe42ecf9b44",  # stability BY Del Chupenebray/Joel Bickford
    "cards.stumble": "10da0e8d-ef22-426b-9b13-e54830ef70c9",  # stumble BY Del Chupenebray/Joel Bickford
    "cards.swagger": "0069c699-d054-49ab-a03a-babe772a3c79",  # swagger BY Del Chupenebray/Joel Bickford
    "cards.tread_lightly": "cc564ea6-c739-4332-a8a8-cb41ca45e0c1",  # tread_lightly BY Del Chupenebray/Joel Bickford
    "cards.treasure_hunter": "2f919cf2-5285-4368-b68b-a8bc3c88b30f",  # treasure_hunter BY Del Chupenebray/Joel Bickford
    "events.artifact_retrived": "5f173907-b11a-44d7-91f9-2d22f89a831b",  # DO_Artefact_ArtefactRetrieval_ BY Del Chupenebray/Joel Bickford
    "events.card_reveal": "e0d77739-2673-4d28-9cfa-c797490311d6", # BY
    "events.clank_blocked.1": "77feaace-6c3e-4bb9-865d-63609973d49e",  # DO_Clank_ClankBlocked_Set1_1 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.2": "d0478208-652f-4b3b-ad0f-9ad588fa667f",  # DO_Clank_ClankBlocked_Set1_2 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.3": "fd81ca58-68f1-4314-bc6d-5b29ffc7f34d",  # DO_Clank_ClankBlocked_Set1_3 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.4": "a25959d2-41e9-41ed-9b86-be2983508786",  # DO_Clank_ClankBlocked_Set1_4 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.5": "b959ac4e-372c-43b5-ad4d-befb65114bdb",  # DO_Clank_ClankBlocked_Set1_5 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.6": "afcbdaad-5423-4fc5-bccd-4d142bdde9b5",  # DO_Clank_ClankBlocked_Set1_6 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.7": "1fd58575-6e8b-4726-9f2b-8d30d6a7f718",  # DO_Clank_ClankBlocked_Set1_7 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.8": "f8f2a6e8-f35b-47eb-888f-1b858e3d23a2",  # DO_Clank_ClankBlocked_Set1_8 BY Del Chupenebray/Joel Bickford
    "events.clank_blocked.9": "7021b624-ae1a-4ce0-a333-b00ffebc6913",  # DO_Clank_ClankBlocked_Set1_9 BY Del Chupenebray/Joel Bickford
    "events.deepfrost_tnt": "335714a7-36d1-4c21-9c2b-38317f00d6d4",  # DO_Deepfrost_OpeningExplosion BY Del Chupenebray/Joel Bickford
    "events.dungeon_is_ready": "d44645a9-25ba-4188-99c2-253a61bcab4e", # BY
    "events.game_over": "faaa1c3b-61c6-4704-a9c3-5beadd2bae55",  # DO_GameOver_DungeonReset BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.1": "7aedee54-0c58-4a9c-8d5e-db5b1a904590",  # DO_Hazard_HazardBlocked_Set1_1 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.2": "63d590ad-fc52-4b57-91e9-2424ea6c2c9a",  # DO_Hazard_HazardBlocked_Set1_2 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.3": "0b8c1ee3-ccda-4e1b-b1d0-df252904eab8",  # DO_Hazard_HazardBlocked_Set1_3 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.4": "99a2e49c-6270-462d-ab94-2bca5bcc07dd",  # DO_Hazard_HazardBlocked_Set1_4 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.5": "afdcacdd-9363-46b6-af7d-0cde17eb8811",  # DO_Hazard_HazardBlocked_Set1_5 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.6": "e7568f4d-48fd-46be-92bf-9ab34e3f8373",  # DO_Hazard_HazardBlocked_Set1_6 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.7": "4138d535-a5ed-4e18-85a4-95160c0d54cc",  # DO_Hazard_HazardBlocked_Set1_7 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.8": "8ab227c4-c406-4968-b40d-6f2b58d1de11",  # DO_Hazard_HazardBlocked_Set1_8 BY Del Chupenebray/Joel Bickford
    "events.hazard_blocked.9": "351d61e3-ad2c-474b-b942-7f14934e560d",  # DO_Hazard_HazardBlocked_Set1_9 BY Del Chupenebray/Joel Bickford
    "events.hazard.1": "94d68cf8-8572-46e1-a11e-173fae446566",  # DO_Hazard_HazardTrigger_Set1_1 BY Del Chupenebray/Joel Bickford
    "events.hazard.2": "23f8a7d3-49b3-4ac0-9a20-297c0ec2a007",  # DO_Hazard_HazardTrigger_Set1_1 BY Del Chupenebray/Joel Bickford
    "events.hazard.3": "69eb7d29-14f7-461d-a176-176d81335b99",  # DO_Hazard_HazardTrigger_Set1_3 BY Del Chupenebray/Joel Bickford
    "events.hazard.4": "324dfa4c-b4d3-4467-877b-a79d7427a91a",  # DO_Hazard_HazardTrigger_Set1_4 BY Del Chupenebray/Joel Bickford
    "events.hazard.5": "dbff3a00-431b-48aa-b133-a1e8a8fcd173",  # DO_Hazard_HazardTrigger_Set1_5 BY Del Chupenebray/Joel Bickford
    "events.hazard.6": "6b6c2912-7e69-4af7-88d4-2fd12ee371d7",  # DO_Hazard_HazardTrigger_Set1_6 BY Del Chupenebray/Joel Bickford
    "events.hazard.7": "ff93f2fd-911b-4613-ad00-087f879753f6",  # DO_Hazard_HazardTrigger_Set1_7 BY Del Chupenebray/Joel Bickford
    "events.hazard.8": "e3687d32-9e1c-46ce-a2ab-4b3a39f94e7f",  # DO_Hazard_HazardTrigger_Set1_8 BY Del Chupenebray/Joel Bickford
    "events.hazard.9": "7609093d-8351-4c36-a098-509ae09c5641",  # DO_Hazard_HazardTrigger_Set1_9 BY Del Chupenebray/Joel Bickford
    "events.heartbeat": "b6095a48-7166-4e96-85ea-c4f9898accee",  # DO_HeartBeat_1 BY Del Chupenebray/Joel Bickford
    "events.recycle.1": "a4af0760-e902-4f79-90fa-4c42eb4cd876",  # DO_Card_Recycle_1 BY Del Chupenebray/Joel Bickford
    "events.recycle.2": "a3c20c44-a819-4398-bfb3-b945166e3c1d",  # DO_Card_Recycle_2 BY Del Chupenebray/Joel Bickford
    "events.recycle.3": "96cef58f-74c5-42f5-9d4f-812f6a41a253",  # DO_Card_Recycle_3 BY Del Chupenebray/Joel Bickford
    "events.recycle.4": "9fad09b1-8ad8-4c3b-9737-3b4cc60b8aca",  # DO_Card_Recycle_4 BY Del Chupenebray/Joel Bickford
    "events.recycle.5": "a2fa3b30-23ea-4436-bc50-ac4fc9d6a788",  # DO_Card_Recycle_5 BY Del Chupenebray/Joel Bickford
    "events.recycle.6": "1473a3ea-45ec-47ca-b8c4-f93254467be4",  # DO_Card_Recycle_6 BY Del Chupenebray/Joel Bickford
    "events.recycle.7": "40356557-dcc1-4ef5-a830-089493d7fbab",  # DO_Card_Recycle_7 BY Del Chupenebray/Joel Bickford
    "events.recycle.8": "773c56cd-e551-4a11-a050-f17310678f86",  # DO_Card_Recycle_8 BY Del Chupenebray/Joel Bickford
    "holloween.enterance.1": "cda7ec93-5454-4f64-a6c6-5b431a29b63f",  # DO_Holloween_EntranceTune_1 BY Del Chupenebray/Joel Bickford
    "holloween.enterance.2": "602f6a24-2e3b-4e13-a211-c814f452c390",  # DO_Holloween_EntranceTune_2 BY Del Chupenebray/Joel Bickford
    "holloween.enterance.3": "5bf4c518-2e69-47d4-9559-5756cc5e2343",  # DO_Holloween_EntranceTune_3 BY Del Chupenebray/Joel Bickford
    "holloween.failure.1": "32e5657f-9d7b-494e-b38d-aaca1f522d2a",  # DO_Holloween_Failure_1 BY Del Chupenebray/Joel Bickford
    "holloween.failure.2": "edd55cdd-45a7-41ce-bbfd-ec3f9c59c02a",  # DO_Holloween_Failure_2 BY Del Chupenebray/Joel Bickford
    "holloween.failure.3": "f204d832-bdd9-489e-a6aa-b8c11128949b",  # DO_Holloween_Failure_3 BY Del Chupenebray/Joel Bickford
    "holloween.success": "3477400c-a6c4-4be1-9248-8c54533f2a42",  # DO_Holloween_Success_1 BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.1": "002ca7c8-4c26-47f2-9323-a50889979936",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.2": "093c7b0e-f806-4ce9-9760-d1e9f4e700c0",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.3": "0f4d4df2-9e0f-446e-940b-cc3c1b712255",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.4": "80edeb34-a951-48b0-9950-62f2cf7f8602",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.5": "ccfcf29a-dd69-49dd-9c75-3158626e26ea",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.6": "dac165e6-b856-46a0-bc97-cf13eaace090",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.crown_conversion.7": "dbc5a4fb-1e13-4446-9f52-08ff3b9cd838",  # DO_Currency_CrownConversion_Se BY Del Chupenebray/Joel Bickford
    "interactions.difficulty.deadly": "05e5e60e-fd50-4808-9285-9f29bb2aeda7",  # DO_Difficulty_Deadly BY Del Chupenebray/Joel Bickford
    "interactions.difficulty.deepfrost": "ada9b925-673b-422a-a645-12264ad66daf",  # DO_Difficulty_Deepfrost BY Del Chupenebray/Joel Bickford
    "interactions.difficulty.easy": "5f2e0834-9202-49b3-9030-b8bf8a7229a0",  # DO_Difficulty_Easy BY Del Chupenebray/Joel Bickford
    "interactions.difficulty.hard": "4c89661b-f8a4-4481-af44-89473328b1de",  # DO_Difficulty_Hard BY Del Chupenebray/Joel Bickford
    "interactions.difficulty.medium": "773f411f-fa81-4b5d-b3f8-8b28ced53cea",  # DO_Difficulty_Medium BY Del Chupenebray/Joel Bickford
    "interactions.dungeon_door_open": "f25b0520-a30c-49d8-a714-3ded7888f22a", # BY
    "interactions.dungeon_taunt": "b44472ef-710c-4c63-85df-076331418917",  # DO_DungeonTaunt_1 BY Del Chupenebray/Joel Bickford
    "interactions.ember_shop_open": "59c6b097-0583-4367-beb8-2f349ba808e9", # BY
    "interactions.ember_shop_opening": "62a3d798-895c-40ba-af65-573d8b89cfbe", # BY
    "interactions.install_deck": "9685bf60-bdee-4fc9-91a6-d8918278429c",  # DO_Shulker_Loaded_Tick+Thud BY Del Chupenebray/Joel Bickford
    "interactions.open_main_door": "60896fe1-c47f-41e6-bc90-2305e7b98b0c",  # DO_Entrance_DoorDrone_Set1_4 BY Del Chupenebray/Joel Bickford
    "interactions.purchase.1": "0bd04a3b-5cf5-47ff-9147-84290bf14974",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.purchase.2": "21375280-9a6a-4193-affc-6d45c48e8037",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.purchase.3": "88062bea-cd7a-4293-8bda-5f4897dfabb8",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.purchase.4": "8a660ef1-1a77-4996-a6b7-6b01d1299b8b",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.purchase.5": "d174f0c5-7454-4a7e-af29-145df82025c4",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.purchase.6": "f4838028-a9c0-462e-bf85-7eae2ee3322d",  # DO_Currency_FrostEmberPurchase BY Del Chupenebray/Joel Bickford
    "interactions.take_your_items": "096aa40b-5441-401f-8add-abafe6d2b4ce", # BY
    # "": "003ad6c6-15bd-415c-a4c2-eab91f8123fe", # BY
    # "": "00fd5909-e821-4c88-943c-a2222e952249", # Blank Project BY
    # "": "030e10c0-ebfb-4343-9274-4a88ad76d0b0", # BY
    # "": "059de0d3-571b-41af-b2ec-cc66276971c5", # BY
    # "": "0745338d-0eb6-48bb-8d6b-b30988d4f5dd", # BY
    # "": "081c4e74-44a3-4932-acf2-f6425afd65a3", # BY
    # "": "097e888f-476e-4697-995c-9015d436d6bf", # BY
    # "": "0b31db81-d552-4e03-8d4c-4a607452aa89", # BY
    # "": "0c318954-cd2d-4079-a39b-03be5cac8ba0", # BY
    # "": "0dc075d3-b995-4e50-9dde-edba02d4c052", # BY
    # "": "0ec34d19-3d37-4e10-8ff5-60a68a1bdac9", # MonoTEST_3 BY
    # "": "100214a0-f58c-4de4-8a81-88caa0a09f69", # BY
    # "": "10f6d5f5-2e21-48a8-bf5c-d56e2ce3ed69", # BY
    # "": "13e96e3b-d962-4c26-8bb6-b02f6a711fb4", # Blank Project BY
    # "": "1603cf57-d6b2-4088-81ba-e6f085fa8f1d", # Shoreline Gulls BY
    # "": "174086ad-3d99-407d-8027-101a3b5f6067", # Birds Peaceful 2 BY
    # "": "17618ce1-aec1-4ecf-a8df-152c60466b9c", # BY
    # "": "190d316b-c8f4-4bc3-b7ab-6f859e0cc76b", # Bell Store Clerk 1 BY SFX Producer
    # "": "1d27deeb-6c68-4913-8c85-d9d7f4a82b09", # BY
    # "": "1e2f5c15-5daa-4504-a9bb-ae464317b2fb", # BY
    # "": "2033fc4f-e8be-4f98-ae0d-3050d909b8df", # BY
    # "": "2180dc9e-8f80-43f5-b94a-447b7b240d1b", # BY
    # "": "22e6dabf-a100-445b-ba64-25b240ec69d2", # BY
    # "": "23816786-9ea3-4a44-a7f6-82e394536194", # BY
    # "": "23f59096-a1f1-4beb-952f-8867332d61bf", # BY
    # "": "24859950-6d1b-4a54-8f87-26e0a58ce650", # BY
    # "": "24b56bc1-accf-4a04-8700-6209950ae5cd", # BY
    # "": "260ec4e4-d8ff-4088-ae7d-d2235f05936c", # BY
    # "": "2998128e-1c0a-4bb2-a2c5-2a5266783a32", # BY
    # "": "29ebc75e-9a35-440c-8b90-21026a7fd235", # BY
    # "": "2cb9fe09-3863-4ecd-b094-b61404cc46d1", # BY
    # "": "2f8a81f6-cbb6-475a-ba9b-8409da4518cd", # BY
    # "": "314372f7-feb9-4fc4-961f-698d73649c64", # Birds Peaceful 2 BY
    # "": "33a91108-bcca-4f96-ac4c-3347c5a93c9b", # BY
    # "": "345cd84b-6779-4357-9dbc-c5eecea57f4b", # BY
    # "": "34879e77-38d6-40e3-b0b0-20cc2d391ade", # Shoreline Gulls BY
    # "": "3565759b-b6bd-4614-9aca-c856b17b7676", # Blank Project BY
    # "": "3642a49a-8d5b-46ed-9d48-dd371c918d92", # BY
    # "": "370cab98-bdbd-43de-b9de-1e7c43573584", # BY
    # "": "377ba400-d096-406e-a181-85bc62452347", # BY
    # "": "3af19923-ca3c-4a87-b141-05fbd64cb7b7", # Blank Project BY
    # "": "3f725b51-c15f-4d90-9702-cba127f1d344", # BY
    # "": "419eaf62-f557-4f95-923e-c71313c0e8f0", # StereoTEST_1 BY
    # "": "4604fd75-c9c1-4d7c-9e70-502e256881dd", # BY
    # "": "4670a8b9-e3d1-49db-854e-31710b3c8df1", # BY
    # "": "46a567cb-ce79-4ecb-881d-a77953eb64c0", # BY
    # "": "4abc2d08-6059-4b82-bddc-6c21893610de", # BY
    # "": "4d56d0b3-025b-4c67-b055-30cfedf9d467", # BY
    # "": "4da6ca13-2e1d-4dd8-8076-2117aecab530", # BY
    # "": "4db0e46d-2948-4952-b98f-4280faafc146", # BY
    # "": "4f824c85-f003-49e1-8377-3a8f54f31162", # BY
    # "": "514dc56e-3d90-4d2a-9964-b12a57887d4c", # BY
    # "": "537a2a6d-39b9-442a-8988-f5496aec78a3", # BY
    # "": "53d30e71-fc55-439c-ba59-b130a484ef59", # BY
    # "": "566c33a2-daf9-4719-9459-b5886bfe8566", # BY
    # "": "56c7ecb8-623f-4e6b-8798-642889f8bb40", # BY
    # "": "56fa4425-870e-462b-8d16-fb8e74f5c1fe", # BY
    # "": "58897024-956a-4783-b632-5e9ea181eb2b", # BY
    # "": "5c393bcb-cdaa-42ed-9481-e17180c2784d", # BY
    # "": "5e844d52-cb7c-4f58-9161-e372019f6358", # Blank Project BY
    # "": "5fd8dfa8-2e61-4dc9-a0e0-7a80b5c8dd41", # Shopping for Christmas BY Home for the Holidays
    # "": "608dbecd-c74c-48b4-bc28-a117c8fb62a5", # BY
    # "": "645707cf-3428-42a7-b7f7-4e9c149d195e", # BY
    # "": "65104c88-dbf5-446f-bc03-66014bffb7f4", # BY
    # "": "657834a2-4277-4620-9420-e1754b6b7277", # BY
    # "": "665003c4-1db2-41ec-a240-375120cb5fb1", # BY
    # "": "676d9195-c4b4-4bbd-b689-f6176ab48b60", # BY
    # "": "68b03ade-c5b3-44f3-9c33-e501b08f3102", # BY
    # "": "68c9eb19-53d8-44b4-a20b-b5878adfeecc", # BY
    # "": "695f63c9-daba-493d-97e6-1a26358da0fb", # BY
    # "": "6b397114-821d-4a43-b97b-12a70801a9ce", # BY
    # "": "6baa7354-11e3-4389-8fd6-c5144346c260", # BY
    # "": "6f07046c-d56a-439a-a8e1-e415492e7021", # BY
    # "": "71e50d8e-bcc1-484d-9c53-85296d34903b", # BY
    # "": "72d46f4a-c17d-49d7-b898-542a4874f4a8", # BY
    # "": "74fd1023-125e-4e9e-8574-304fcffee854", # BY
    # "": "78a01128-0673-41eb-94ce-1f266b78631f", # BY
    # "": "7a76ea84-c4ac-4801-b97a-8fd629b4221c", # BY
    # "": "7dfab916-e03d-4937-8316-016ca66241c0", # BY
    # "": "7e4ceb1d-0d5c-4c7a-a553-f77cfc6b99a9", # BY
    # "": "7f24d052-76ad-4132-8ecf-a30fb4a1f566", # BY
    # "": "80300994-1fe6-463f-8d44-fd799c0caf9b", # BY
    # "": "819de2a5-e4f6-4346-837f-27204e4b9124", # BY
    # "": "81e3bf81-dea3-4c87-9586-eddf5483b9f1", # BY
    # "": "832458f4-28f2-45c7-bb0d-9118c0cd4136", # BY
    # "": "840ee3d8-a9e5-4b40-8e3d-4a58157f3881", # BY
    # "": "8457982d-6c1a-4e8a-84ed-2fd8ae91a1b5", # BY
    # "": "845de880-194b-46da-8864-7f6308206531", # Blank Project BY
    # "": "87076c6d-5937-4fdc-a373-ea148a5b0981", # BY
    # "": "875b3ba6-6377-4d0c-8ae1-9310bdf21f07", # BY
    # "": "8abf53de-b823-4d8c-9361-5c44fb01421c", # BY
    # "": "8cb12699-5cb7-478f-b5fa-f94714701d11", # Forest Ambience BY SFX Producer
    # "": "8d52924c-e640-47cc-b932-af8c29ada1ab", # BY
    # "": "90673ece-e5bf-4bd4-a589-ce3ea91a8ace", # BY
    # "": "9354d797-810d-4a6e-9a11-313d7990bc41", # BY
    # "": "95f49de9-8f8d-4b16-afa2-9b119db9de79", # BY
    # "": "96eb1bd4-1c38-48ec-9dcc-3acf26b7f225", # BY
    # "": "98b6766b-e614-47d6-b2ef-4c0da6f014ff", # BY
    # "": "9a0a3925-53da-4516-b352-32df9074f0c4", # BY
    # "": "9c24a49f-68a8-4933-9fda-3057a24b55fb", # BY
    # "": "9c34916b-4f52-4b4a-b62c-052bbb6533ef", # BY
    # "": "a339d65a-2360-415e-bedf-4b95655a0e57", # BY
    # "": "a93a566f-af11-48c6-b819-5fba5fa4ac88", # BY
    # "": "aa36a082-9789-4b71-aaed-5d06d32e63c3", # BY
    # "": "ad5e3c19-62c5-4861-8d27-10d537a3545b", # BY
    # "": "adf2f6bf-14df-492e-b2a2-67efe15d2f76", # BY
    # "": "aea15811-cf06-4713-a41d-1bb6cbf7baaf", # BY
    # "": "aeaa3489-dda2-41d6-b6ea-738bd494985b", # BY
    # "": "aef5d543-0be8-4efe-b153-a8fa1addb518", # Blank Project BY
    # "": "b2588a66-e467-4a47-8eb0-25502d7a565f", # BY
    # "": "b8b330a7-ab4f-48e9-b93b-c3d1540a98f2", # BY
    # "": "ba40b923-c2aa-4613-98f3-76cb67a95d8a", # BY
    # "": "baa703e6-055a-40e4-8140-f36321268883", # BY
    # "": "bdb71416-79fa-4e6e-b725-c53ecc34525d", # BY
    # "": "bfd4e3c0-bb14-41a5-be27-f74730948ab4", # BY
    # "": "c0308a5f-a654-4638-ad5a-5aa11b915335", # BY
    # "": "c03f307e-8a40-4387-bdbf-2be6b73aa79a",  # Button Beep 5 BY SFX Producer
    # "": "c0d6c3a3-a74e-45ac-ac18-b42495483ba9",  # Birds Peaceful 2 BY
    # "": "c19c1c6b-9ddd-4e72-9a45-0ee110ebde5f", # BY
    # "": "c405dd51-6d6d-4175-b982-414e4314f878", # BY
    # "": "c61a6af0-20bd-4607-84cc-e66fcd585467", # BY
    # "": "ca8a4cf1-d35a-4418-8f1a-21edf07b1d37", # BY
    # "": "caaa1d1f-51e2-4dfd-b0ec-d85ea562030e",  # Chime Musical 23 BY SFX Producer
    # "": "d570ba74-ed2c-47b9-b151-f7d11f0a85a9", # BY
    # "": "d58e2ac4-9042-4092-88e9-e62c6bbad6d5", # BY
    # "": "db32fd03-3e37-4aea-a509-b1923ee50961", # BY
    # "": "db53e96f-d301-41a0-9b66-7797960d87bc", # BY
    # "": "de046f40-a3b2-42ab-8aa0-d27ae4093a44", # BY
    # "": "de0c5d56-2241-41eb-af5a-b871876c799d", # BY
    # "": "df5e7134-cc93-4e80-897c-4aab76852c36", # BY
    # "": "dff7e5ea-6e5c-4b14-944e-b09a281a180b", # BY
    # "": "e34f8d2d-f68e-4879-8b5d-9e162e91b254", # BY
    # "": "eb4416b3-a75d-4db6-bbba-45270025910c", # Birds Peaceful 2 BY
    # "": "f75b8fb6-b0d2-4616-85bc-43ba63bf4af8", # BY
    # "": "fb82b406-6f08-490e-8081-6c6063c97672", # BY
    # "": "fc6743d3-36de-42ad-b4e6-84934c72ac18", # BY
    # "": "fde15666-26e5-4be7-b1b7-450627242be5", # Sci Fi Voice Clip 14 BY SFX Producer
    # "": "fef86c77-92e4-44c9-b15f-780a163eb84d", # BY
    # "": "ff5e9ade-a521-4178-ae29-0194cbb330b8", # BY
}

GROUPS = {
    "ambient.cave_gust": ...,
    "ambient.drone_deepfrost": ...,
    "ambient.drone": ...,
    "ambient.ghostly_whisper": ...,
    "ambient.ice": ...,
    "ambient.metal": ...,
    "ambient.wood": ...,
    "events.clank_blocked": ...,
    "events.hazard_blocked": ...,
    "events.hazard": ...,
    "events.recycle": ...,
    "holloween.enterance": ...,
    "holloween.failure": ...,
    "interactions.crown_conversion": ...,
    "interactions.frost_purchase": ...,
    "ambient.warden_roar_with_cleo": ["ambient.warden_roar"]* 7 + ["ambient.hi_cleo"]
}

SUBTITLES = {
    "events.clank_blocked": "Clank gets blocked",
    "events.hazard_blocked": "Hazard gets blocked",
    "events.hazard": "Hazard triggers",
}

SOUNDS = {}

for sound_id, sound_hash in IDS.items():
    if sound_id == "" or sound_id.endswith("#"):
        continue

    sound_path = ASSETS_ROOT / "do2/sounds" / (sound_id.replace(".", "/") + ".ogg")

    force_save = False

    # if sound_id == "cards.reckless_charge":
    #     force_save = True

    if force_save or not sound_path.exists():
        sound_path.parent.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(OGG_DATA / f"{sound_hash}.ogg", sound_path)

    sound = {"replace": False, "sounds": [{"name": f"do2:{sound_id.replace('.', '/')}"}]}

    if sound_id in SUBTITLES:
        sound["subtitle"] = SUBTITLES[sound_id]

    SOUNDS[sound_id] = sound


for group_id, sounds in GROUPS.items():
    sound = {"replace": False, "sounds": []}

    if group_id in SUBTITLES:
        sound["subtitle"] = SUBTITLES[group_id]

    if sounds is ...:
        sounds = []
        for sound_id in SOUNDS:
            if sound_id.startswith(f"{group_id}."):
                sounds.append(sound_id)
                SOUNDS[sound_id]["erased"] = True


    for sound_id in sounds:
        sound["sounds"].extend(SOUNDS[sound_id]["sounds"])

    SOUNDS[group_id] = sound


for sound_id in list(SOUNDS):
    if SOUNDS[sound_id].get("erased", False):
        del SOUNDS[sound_id]


with open(ASSETS_ROOT / "do2/sounds.json", "wt", encoding="utf-8") as fd:
    json.dump(SOUNDS, fd, indent=4)
