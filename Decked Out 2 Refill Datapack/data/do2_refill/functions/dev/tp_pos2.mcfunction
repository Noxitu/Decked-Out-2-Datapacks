schedule function do2_refill:dev/tp_pos2 5t
execute store result score current_slot do2_refill run data get entity @p recipeBook.isGuiOpen
execute if score last_slot do2_refill = current_slot do2_refill run return 0
execute store result score last_slot do2_refill run data get entity @p recipeBook.isGuiOpen
say [DEV] TP to next position
execute if score next_index do2_refill matches 0 run say item -622 -51 1889 An Old Friend's Pickaxe (38)
execute if score next_index do2_refill matches 0 run tp @p -622 -51 1889
execute if score next_index do2_refill matches 1 run say item -637 -51 1888 An Old Friend's Pickaxe (38)
execute if score next_index do2_refill matches 1 run tp @p -637 -51 1888
execute if score next_index do2_refill matches 2 run say item -659 -14 1922 An Old Friend's Pickaxe (38)
execute if score next_index do2_refill matches 2 run tp @p -659 -14 1922
execute if score next_index do2_refill matches 3 run say item -548 51 1972 Axe of the Screamin' Void (7)
execute if score next_index do2_refill matches 3 run tp @p -548 51 1972
execute if score next_index do2_refill matches 4 run say item -573 55 1944 Axe of the Screamin' Void (7)
execute if score next_index do2_refill matches 4 run tp @p -573 55 1944
execute if score next_index do2_refill matches 5 run say item -593 49 1967 Axe of the Screamin' Void (7)
execute if score next_index do2_refill matches 5 run tp @p -593 49 1967
execute if score next_index do2_refill matches 6 run say item -588 -9 1917 Bionic Eye of Doom (24)
execute if score next_index do2_refill matches 6 run tp @p -588 -9 1917
execute if score next_index do2_refill matches 7 run say item -598 1 1890 Bionic Eye of Doom (24)
execute if score next_index do2_refill matches 7 run tp @p -598 1 1890
execute if score next_index do2_refill matches 8 run say item -623 1 1892 Bionic Eye of Doom (24)
execute if score next_index do2_refill matches 8 run tp @p -623 1 1892
execute if score next_index do2_refill matches 9 run say item -519 12 1943 Butcher's Apron (20)
execute if score next_index do2_refill matches 9 run tp @p -519 12 1943
execute if score next_index do2_refill matches 10 run say item -519 12 1982 Butcher's Apron (20)
execute if score next_index do2_refill matches 10 run tp @p -519 12 1982
execute if score next_index do2_refill matches 11 run say item -534 12 1939 Butcher's Apron (20)
execute if score next_index do2_refill matches 11 run tp @p -534 12 1939
execute if score next_index do2_refill matches 12 run say item -574 -48 1910 CF-135 (46)
execute if score next_index do2_refill matches 12 run tp @p -574 -48 1910
execute if score next_index do2_refill matches 13 run say item -601 -49 1911 CF-135 (46)
execute if score next_index do2_refill matches 13 run tp @p -601 -49 1911
execute if score next_index do2_refill matches 14 run say item -607 -51 1863 CF-135 (46)
execute if score next_index do2_refill matches 14 run tp @p -607 -51 1863
execute if score next_index do2_refill matches 15 run say item -623 -52 1856 CF-135 (46)
execute if score next_index do2_refill matches 15 run tp @p -623 -52 1856
execute if score next_index do2_refill matches 16 run say item -490 15 2002 Chisel of the Undead Sculptress (19)
execute if score next_index do2_refill matches 16 run tp @p -490 15 2002
execute if score next_index do2_refill matches 17 run say item -537 16 2003 Chisel of the Undead Sculptress (19)
execute if score next_index do2_refill matches 17 run tp @p -537 16 2003
execute if score next_index do2_refill matches 18 run say item -554 10 2024 Chisel of the Undead Sculptress (19)
execute if score next_index do2_refill matches 18 run tp @p -554 10 2024
execute if score next_index do2_refill matches 19 run say item -480 27 1992 Death Loop (13)
execute if score next_index do2_refill matches 19 run tp @p -480 27 1992
execute if score next_index do2_refill matches 20 run say item -505 51 1962 Death Loop (13)
execute if score next_index do2_refill matches 20 run tp @p -505 51 1962
execute if score next_index do2_refill matches 21 run say item -511 52 1958 Death Loop (13)
execute if score next_index do2_refill matches 21 run tp @p -511 52 1958
execute if score next_index do2_refill matches 22 run say item -590 -51 1899 Gem of Greatness (40)
execute if score next_index do2_refill matches 22 run tp @p -590 -51 1899
execute if score next_index do2_refill matches 23 run say item -601 -50 1890 Gem of Greatness (40)
execute if score next_index do2_refill matches 23 run tp @p -601 -50 1890
execute if score next_index do2_refill matches 24 run say item -580 -11 1892 Golden Eye (34)
execute if score next_index do2_refill matches 24 run tp @p -580 -11 1892
execute if score next_index do2_refill matches 25 run say item -582 -19 1896 Golden Eye (34)
execute if score next_index do2_refill matches 25 run tp @p -582 -19 1896
execute if score next_index do2_refill matches 26 run say item -589 -26 1898 Golden Eye (34)
execute if score next_index do2_refill matches 26 run tp @p -589 -26 1898
execute if score next_index do2_refill matches 27 run say item -513 46 2030 Hood of Aw'Yah (6)
execute if score next_index do2_refill matches 27 run tp @p -513 46 2030
execute if score next_index do2_refill matches 28 run say item -536 46 2035 Hood of Aw'Yah (6)
execute if score next_index do2_refill matches 28 run tp @p -536 46 2035
execute if score next_index do2_refill matches 29 run say item -556 51 2006 Hood of Aw'Yah (6)
execute if score next_index do2_refill matches 29 run tp @p -556 51 2006
execute if score next_index do2_refill matches 30 run say item -562 48 2033 Hood of Aw'Yah (6)
execute if score next_index do2_refill matches 30 run tp @p -562 48 2033
execute if score next_index do2_refill matches 31 run say item -487 20 2008 Horn of the G.O.A.T. (18)
execute if score next_index do2_refill matches 31 run tp @p -487 20 2008
execute if score next_index do2_refill matches 32 run say item -503 15 2033 Horn of the G.O.A.T. (18)
execute if score next_index do2_refill matches 32 run tp @p -503 15 2033
execute if score next_index do2_refill matches 33 run say item -520 12 2025 Horn of the G.O.A.T. (18)
execute if score next_index do2_refill matches 33 run tp @p -520 12 2025
execute if score next_index do2_refill matches 34 run say item -572 9 1944 Hypnotic Bandana (21)
execute if score next_index do2_refill matches 34 run tp @p -572 9 1944
execute if score next_index do2_refill matches 35 run say item -573 8 1966 Hypnotic Bandana (21)
execute if score next_index do2_refill matches 35 run tp @p -573 8 1966
execute if score next_index do2_refill matches 36 run say item -588 13 1987 Hypnotic Bandana (21)
execute if score next_index do2_refill matches 36 run tp @p -588 13 1987
execute if score next_index do2_refill matches 37 run say item -517 52 2006 Jar of Speedy Slime (11)
execute if score next_index do2_refill matches 37 run tp @p -517 52 2006
execute if score next_index do2_refill matches 38 run say item -525 51 1969 Jar of Speedy Slime (11)
execute if score next_index do2_refill matches 38 run tp @p -525 51 1969
execute if score next_index do2_refill matches 39 run say item -543 44 1940 Jar of Speedy Slime (11)
execute if score next_index do2_refill matches 39 run tp @p -543 44 1940
execute if score next_index do2_refill matches 40 run say item -571 12 2026 Knight's Helm (23)
execute if score next_index do2_refill matches 40 run tp @p -571 12 2026
execute if score next_index do2_refill matches 41 run say item -574 15 2014 Knight's Helm (23)
execute if score next_index do2_refill matches 41 run tp @p -574 15 2014
execute if score next_index do2_refill matches 42 run say item -599 12 2031 Knight's Helm (23)
execute if score next_index do2_refill matches 42 run tp @p -599 12 2031
execute if score next_index do2_refill matches 43 run say item -570 -51 1853 Mug of the Dungeon Master (54)
execute if score next_index do2_refill matches 43 run tp @p -570 -51 1853
execute if score next_index do2_refill matches 44 run say item -490 50 2020 Multi-Grain Waffle (8)
execute if score next_index do2_refill matches 44 run tp @p -490 50 2020
execute if score next_index do2_refill matches 45 run say item -499 44 2013 Multi-Grain Waffle (8)
execute if score next_index do2_refill matches 45 run tp @p -499 44 2013
execute if score next_index do2_refill matches 46 run say item -546 38 1995 Multi-Grain Waffle (8)
execute if score next_index do2_refill matches 46 run tp @p -546 38 1995
execute if score next_index do2_refill matches 47 run say item -528 45 1956 Papa's Slippers (10)
execute if score next_index do2_refill matches 47 run tp @p -528 45 1956
execute if score next_index do2_refill matches 48 run say item -536 44 1966 Papa's Slippers (10)
execute if score next_index do2_refill matches 48 run tp @p -536 44 1966
execute if score next_index do2_refill matches 49 run say item -552 45 1955 Papa's Slippers (10)
execute if score next_index do2_refill matches 49 run tp @p -552 45 1955
execute if score next_index do2_refill matches 50 run say item -452 18 1979 Pearl of Cleansing (14)
execute if score next_index do2_refill matches 50 run tp @p -452 18 1979
execute if score next_index do2_refill matches 51 run say item -475 16 1962 Pearl of Cleansing (14)
execute if score next_index do2_refill matches 51 run tp @p -475 16 1962
execute if score next_index do2_refill matches 52 run say item -484 18 2037 Pearl of Cleansing (14)
execute if score next_index do2_refill matches 52 run tp @p -484 18 2037
execute if score next_index do2_refill matches 53 run say item -598 -7 1881 Pocket Watch of Shreeping (36)
execute if score next_index do2_refill matches 53 run tp @p -598 -7 1881
execute if score next_index do2_refill matches 54 run say item -623 -19 1890 Pocket Watch of Shreeping (36)
execute if score next_index do2_refill matches 54 run tp @p -623 -19 1890
execute if score next_index do2_refill matches 55 run say item -648 -19 1893 Pocket Watch of Shreeping (36)
execute if score next_index do2_refill matches 55 run tp @p -648 -19 1893
execute if score next_index do2_refill matches 56 run say item -517 35 1984 Shades of the Dog (9)
execute if score next_index do2_refill matches 56 run tp @p -517 35 1984
execute if score next_index do2_refill matches 57 run say item -520 35 2000 Shades of the Dog (9)
execute if score next_index do2_refill matches 57 run tp @p -520 35 2000
execute if score next_index do2_refill matches 58 run say item -550 38 1984 Shades of the Dog (9)
execute if score next_index do2_refill matches 58 run tp @p -550 38 1984
execute if score next_index do2_refill matches 59 run say item -599 -51 1842 Staff of the Pink Shepherd (48)
execute if score next_index do2_refill matches 59 run tp @p -599 -51 1842
execute if score next_index do2_refill matches 60 run say item -600 -51 1851 Staff of the Pink Shepherd (48)
execute if score next_index do2_refill matches 60 run tp @p -600 -51 1851
execute if score next_index do2_refill matches 61 run say item -623 -54 1842 Staff of the Pink Shepherd (48)
execute if score next_index do2_refill matches 61 run tp @p -623 -54 1842
execute if score next_index do2_refill matches 62 run say item -604 -9 1914 The Hidden Stache (30)
execute if score next_index do2_refill matches 62 run tp @p -604 -9 1914
execute if score next_index do2_refill matches 63 run say item -635 -9 1890 The Hidden Stache (30)
execute if score next_index do2_refill matches 63 run tp @p -635 -9 1890
execute if score next_index do2_refill matches 64 run say item -651 1 1916 The Hidden Stache (30)
execute if score next_index do2_refill matches 64 run tp @p -651 1 1916
execute if score next_index do2_refill matches 65 run say item -603 -60 1886 The Master's Key (60)
execute if score next_index do2_refill matches 65 run tp @p -603 -60 1886
execute if score next_index do2_refill matches 66 run say item -590 -51 1864 The Skadoodler (52)
execute if score next_index do2_refill matches 66 run tp @p -590 -51 1864
execute if score next_index do2_refill matches 67 run say item -635 -51 1877 The Skadoodler (52)
execute if score next_index do2_refill matches 67 run tp @p -635 -51 1877
execute if score next_index do2_refill matches 68 run say item -636 -56 1842 The Skadoodler (52)
execute if score next_index do2_refill matches 68 run tp @p -636 -56 1842
execute if score next_index do2_refill matches 69 run say item -568 -51 1878 The Slab (50)
execute if score next_index do2_refill matches 69 run tp @p -568 -51 1878
execute if score next_index do2_refill matches 70 run say item -569 -51 1884 The Slab (50)
execute if score next_index do2_refill matches 70 run tp @p -569 -51 1884
execute if score next_index do2_refill matches 71 run say item -591 -51 1870 The Slab (50)
execute if score next_index do2_refill matches 71 run tp @p -591 -51 1870
execute if score next_index do2_refill matches 72 run say item -497 51 1995 Tome of the Hills (12)
execute if score next_index do2_refill matches 72 run tp @p -497 51 1995
execute if score next_index do2_refill matches 73 run say item -505 51 1981 Tome of the Hills (12)
execute if score next_index do2_refill matches 73 run tp @p -505 51 1981
execute if score next_index do2_refill matches 74 run say item -543 51 2016 Tome of the Hills (12)
execute if score next_index do2_refill matches 74 run tp @p -543 51 2016
execute if score next_index do2_refill matches 75 run say item -505 23 1958 Wand of Gorgeousness (22)
execute if score next_index do2_refill matches 75 run tp @p -505 23 1958
execute if score next_index do2_refill matches 76 run say item -549 10 1969 Wand of Gorgeousness (22)
execute if score next_index do2_refill matches 76 run tp @p -549 10 1969
execute if score next_index do2_refill matches 77 run say item -575 13 1994 Wand of Gorgeousness (22)
execute if score next_index do2_refill matches 77 run tp @p -575 13 1994
execute if score next_index do2_refill matches 78 run say item -641 -23 1958 An Old Friend's Pickaxe
execute if score next_index do2_refill matches 78 run tp @p -641 -23 1958
execute if score next_index do2_refill matches 79 run say item -641 -23 1977 Axe of the Screamin' Void
execute if score next_index do2_refill matches 79 run tp @p -641 -23 1977
execute if score next_index do2_refill matches 80 run say item -641 -23 1963 Bionic Eye of Doom
execute if score next_index do2_refill matches 80 run tp @p -641 -23 1963
execute if score next_index do2_refill matches 81 run say item -641 -23 1967 Butcher's Apron
execute if score next_index do2_refill matches 81 run tp @p -641 -23 1967
execute if score next_index do2_refill matches 82 run say item -641 -23 1956 CF-135
execute if score next_index do2_refill matches 82 run tp @p -641 -23 1956
execute if score next_index do2_refill matches 83 run say item -641 -23 1968 Chisel of the Undead Sculptress
execute if score next_index do2_refill matches 83 run tp @p -641 -23 1968
execute if score next_index do2_refill matches 84 run say item -641 -23 1971 Death Loop
execute if score next_index do2_refill matches 84 run tp @p -641 -23 1971
execute if score next_index do2_refill matches 85 run say item -641 -23 1957 Gem of Greatness
execute if score next_index do2_refill matches 85 run tp @p -641 -23 1957
execute if score next_index do2_refill matches 86 run say item -641 -23 1961 Goggles of Symmetry
execute if score next_index do2_refill matches 86 run tp @p -641 -23 1961
execute if score next_index do2_refill matches 87 run say item -641 -23 1960 Golden Eye
execute if score next_index do2_refill matches 87 run tp @p -641 -23 1960
execute if score next_index do2_refill matches 88 run say item -641 -23 1978 Hood of Aw'Yah
execute if score next_index do2_refill matches 88 run tp @p -641 -23 1978
execute if score next_index do2_refill matches 89 run say item -641 -23 1969 Horn of the G.O.A.T.
execute if score next_index do2_refill matches 89 run tp @p -641 -23 1969
execute if score next_index do2_refill matches 90 run say item -641 -23 1966 Hypnotic Bandana
execute if score next_index do2_refill matches 90 run tp @p -641 -23 1966
execute if score next_index do2_refill matches 91 run say item -641 -23 1973 Jar of Speedy Slime
execute if score next_index do2_refill matches 91 run tp @p -641 -23 1973
execute if score next_index do2_refill matches 92 run say item -641 -23 1964 Knight's Helm
execute if score next_index do2_refill matches 92 run tp @p -641 -23 1964
execute if score next_index do2_refill matches 93 run say item -641 -23 1952 Mug of the Dungeon Master
execute if score next_index do2_refill matches 93 run tp @p -641 -23 1952
execute if score next_index do2_refill matches 94 run say item -641 -23 1976 Multi-Grain Waffle
execute if score next_index do2_refill matches 94 run tp @p -641 -23 1976
execute if score next_index do2_refill matches 95 run say item -641 -23 1974 Papa's Slippers
execute if score next_index do2_refill matches 95 run tp @p -641 -23 1974
execute if score next_index do2_refill matches 96 run say item -641 -23 1970 Pearl of Cleansing
execute if score next_index do2_refill matches 96 run tp @p -641 -23 1970
execute if score next_index do2_refill matches 97 run say item -641 -23 1959 Pocket Watch of Shreeping
execute if score next_index do2_refill matches 97 run tp @p -641 -23 1959
execute if score next_index do2_refill matches 98 run say item -641 -23 1975 Shades of the Dog
execute if score next_index do2_refill matches 98 run tp @p -641 -23 1975
execute if score next_index do2_refill matches 99 run say item -641 -23 1955 Staff of the Pink Shepherd
execute if score next_index do2_refill matches 99 run tp @p -641 -23 1955
execute if score next_index do2_refill matches 100 run say item -641 -23 1962 The Hidden Stache
execute if score next_index do2_refill matches 100 run tp @p -641 -23 1962
execute if score next_index do2_refill matches 101 run say item -641 -23 1951 The Master's Key
execute if score next_index do2_refill matches 101 run tp @p -641 -23 1951
execute if score next_index do2_refill matches 102 run say item -641 -23 1953 The Skadoodler
execute if score next_index do2_refill matches 102 run tp @p -641 -23 1953
execute if score next_index do2_refill matches 103 run say item -641 -23 1954 The Slab
execute if score next_index do2_refill matches 103 run tp @p -641 -23 1954
execute if score next_index do2_refill matches 104 run say item -641 -23 1972 Tome of the Hills
execute if score next_index do2_refill matches 104 run tp @p -641 -23 1972
execute if score next_index do2_refill matches 105 run say item -641 -23 1965 Wand of Gorgeousness
execute if score next_index do2_refill matches 105 run tp @p -641 -23 1965
execute if score next_index do2_refill matches 106 run say item -630 -20 2014 Adrenaline Rush
execute if score next_index do2_refill matches 106 run tp @p -630 -20 2014
execute if score next_index do2_refill matches 107 run say item -630 -20 2004 Beast Sense
execute if score next_index do2_refill matches 107 run tp @p -630 -20 2004
execute if score next_index do2_refill matches 108 run say item -630 -20 2005 Bounding Strides
execute if score next_index do2_refill matches 108 run tp @p -630 -20 2005
execute if score next_index do2_refill matches 109 run say item -630 -20 1995 Ember Seeker
execute if score next_index do2_refill matches 109 run tp @p -630 -20 1995
execute if score next_index do2_refill matches 110 run say item -630 -20 1998 Evasion
execute if score next_index do2_refill matches 110 run tp @p -630 -20 1998
execute if score next_index do2_refill matches 111 run say item -630 -20 2001 Frost Focus
execute if score next_index do2_refill matches 111 run tp @p -630 -20 2001
execute if score next_index do2_refill matches 112 run say item -630 -20 2000 Loot and Scoot
execute if score next_index do2_refill matches 112 run tp @p -630 -20 2000
execute if score next_index do2_refill matches 113 run say item -630 -20 1996 Moment of Clarity
execute if score next_index do2_refill matches 113 run tp @p -630 -20 1996
execute if score next_index do2_refill matches 114 run say item -630 -20 2010 Nimble Looting
execute if score next_index do2_refill matches 114 run tp @p -630 -20 2010
execute if score next_index do2_refill matches 115 run say item -630 -20 2012 Quickstep
execute if score next_index do2_refill matches 115 run tp @p -630 -20 2012
execute if score next_index do2_refill matches 116 run say item -630 -20 2007 Reckless Charge
execute if score next_index do2_refill matches 116 run tp @p -630 -20 2007
execute if score next_index do2_refill matches 117 run say item -630 -20 2003 Second Wind
execute if score next_index do2_refill matches 117 run tp @p -630 -20 2003
execute if score next_index do2_refill matches 118 run say item -630 -20 2011 Smash and Grab
execute if score next_index do2_refill matches 118 run tp @p -630 -20 2011
execute if score next_index do2_refill matches 119 run say item -630 -20 1992 Sneak
execute if score next_index do2_refill matches 119 run tp @p -630 -20 1992
execute if score next_index do2_refill matches 120 run say item -630 -20 2008 Sprint
execute if score next_index do2_refill matches 120 run tp @p -630 -20 2008
execute if score next_index do2_refill matches 121 run say item -630 -20 1993 Stability
execute if score next_index do2_refill matches 121 run tp @p -630 -20 1993
execute if score next_index do2_refill matches 122 run say item -630 -20 2013 Suit Up
execute if score next_index do2_refill matches 122 run tp @p -630 -20 2013
execute if score next_index do2_refill matches 123 run say item -630 -20 1999 Tread Lightly
execute if score next_index do2_refill matches 123 run tp @p -630 -20 1999
execute if score next_index do2_refill matches 124 run say item -630 -20 1994 Treasure Hunter
execute if score next_index do2_refill matches 124 run tp @p -630 -20 1994
execute if score next_index do2_refill matches 125 run say item -557 109 1982 Compass Level Token
execute if score next_index do2_refill matches 125 run tp @p -557 109 1982
execute if score next_index do2_refill matches 126 run say item -558 109 1982 Compass Level Token
execute if score next_index do2_refill matches 126 run tp @p -558 109 1982
execute if score next_index do2_refill matches 127 run say item -559 109 1982 Compass Level Token
execute if score next_index do2_refill matches 127 run tp @p -559 109 1982
execute if score next_index do2_refill matches 128 run say item -560 109 1982 Compass Level Token
execute if score next_index do2_refill matches 128 run tp @p -560 109 1982
execute if score next_index do2_refill matches 129 run say item -561 109 1982 Compass Level Token
execute if score next_index do2_refill matches 129 run tp @p -561 109 1982
execute if score next_index do2_refill matches 130 run say item -549 106 1970 Manual Compass
execute if score next_index do2_refill matches 130 run tp @p -549 106 1970
execute if score next_index do2_refill matches 131 run say item -549 106 1971 Manual Compass
execute if score next_index do2_refill matches 131 run tp @p -549 106 1971
execute if score next_index do2_refill matches 132 run say item -549 106 1972 Manual Compass
execute if score next_index do2_refill matches 132 run tp @p -549 106 1972
execute if score next_index do2_refill matches 133 run say item -549 106 1973 Manual Compass
execute if score next_index do2_refill matches 133 run tp @p -549 106 1973
execute if score next_index do2_refill matches 134 run say item -549 106 1974 Manual Compass
execute if score next_index do2_refill matches 134 run tp @p -549 106 1974
execute if score next_index do2_refill matches 135 run say item -549 106 1975 Manual Compass
execute if score next_index do2_refill matches 135 run tp @p -549 106 1975
execute if score next_index do2_refill matches 136 run say item -549 106 1976 Manual Compass
execute if score next_index do2_refill matches 136 run tp @p -549 106 1976
execute if score next_index do2_refill matches 137 run say item -549 106 1977 Manual Compass
execute if score next_index do2_refill matches 137 run tp @p -549 106 1977
execute if score next_index do2_refill matches 138 run say item -549 106 1978 Manual Compass
execute if score next_index do2_refill matches 138 run tp @p -549 106 1978
execute if score next_index do2_refill matches 139 run say item -549 106 1979 Manual Compass
execute if score next_index do2_refill matches 139 run tp @p -549 106 1979
execute if score next_index do2_refill matches 140 run say item -478 19 2009 Decked Out Frost Ember
execute if score next_index do2_refill matches 140 run tp @p -478 19 2009
execute if score next_index do2_refill matches 141 run say item -484 53 1988 Decked Out Frost Ember
execute if score next_index do2_refill matches 141 run tp @p -484 53 1988
execute if score next_index do2_refill matches 142 run say item -485 31 1962 Decked Out Frost Ember
execute if score next_index do2_refill matches 142 run tp @p -485 31 1962
execute if score next_index do2_refill matches 143 run say item -489 11 2007 Decked Out Frost Ember
execute if score next_index do2_refill matches 143 run tp @p -489 11 2007
execute if score next_index do2_refill matches 144 run say item -490 50 2016 Decked Out Frost Ember
execute if score next_index do2_refill matches 144 run tp @p -490 50 2016
execute if score next_index do2_refill matches 145 run say item -496 15 1999 Decked Out Frost Ember
execute if score next_index do2_refill matches 145 run tp @p -496 15 1999
execute if score next_index do2_refill matches 146 run say item -498 51 1980 Decked Out Frost Ember
execute if score next_index do2_refill matches 146 run tp @p -498 51 1980
execute if score next_index do2_refill matches 147 run say item -501 16 1972 Decked Out Frost Ember
execute if score next_index do2_refill matches 147 run tp @p -501 16 1972
execute if score next_index do2_refill matches 148 run say item -502 31 1975 Decked Out Frost Ember
execute if score next_index do2_refill matches 148 run tp @p -502 31 1975
execute if score next_index do2_refill matches 149 run say item -508 9 1951 Decked Out Frost Ember
execute if score next_index do2_refill matches 149 run tp @p -508 9 1951
execute if score next_index do2_refill matches 150 run say item -509 14 2033 Decked Out Frost Ember
execute if score next_index do2_refill matches 150 run tp @p -509 14 2033
execute if score next_index do2_refill matches 151 run say item -513 51 1962 Decked Out Frost Ember
execute if score next_index do2_refill matches 151 run tp @p -513 51 1962
execute if score next_index do2_refill matches 152 run say item -515 46 2031 Decked Out Frost Ember
execute if score next_index do2_refill matches 152 run tp @p -515 46 2031
execute if score next_index do2_refill matches 153 run say item -518 2 2007 Decked Out Frost Ember
execute if score next_index do2_refill matches 153 run tp @p -518 2 2007
execute if score next_index do2_refill matches 154 run say item -518 53 2011 Decked Out Frost Ember
execute if score next_index do2_refill matches 154 run tp @p -518 53 2011
execute if score next_index do2_refill matches 155 run say item -518 53 2011 Decked Out Frost Ember
execute if score next_index do2_refill matches 155 run tp @p -518 53 2011
execute if score next_index do2_refill matches 156 run say item -519 35 2002 Decked Out Frost Ember
execute if score next_index do2_refill matches 156 run tp @p -519 35 2002
execute if score next_index do2_refill matches 157 run say item -521 35 1981 Decked Out Frost Ember
execute if score next_index do2_refill matches 157 run tp @p -521 35 1981
execute if score next_index do2_refill matches 158 run say item -526 12 1941 Decked Out Frost Ember
execute if score next_index do2_refill matches 158 run tp @p -526 12 1941
execute if score next_index do2_refill matches 159 run say item -527 51 1974 Decked Out Frost Ember
execute if score next_index do2_refill matches 159 run tp @p -527 51 1974
execute if score next_index do2_refill matches 160 run say item -528 12 2032 Decked Out Frost Ember
execute if score next_index do2_refill matches 160 run tp @p -528 12 2032
execute if score next_index do2_refill matches 161 run say item -531 16 1989 Decked Out Frost Ember
execute if score next_index do2_refill matches 161 run tp @p -531 16 1989
execute if score next_index do2_refill matches 162 run say item -533 44 2024 Decked Out Frost Ember
execute if score next_index do2_refill matches 162 run tp @p -533 44 2024
execute if score next_index do2_refill matches 163 run say item -537 45 1948 Decked Out Frost Ember
execute if score next_index do2_refill matches 163 run tp @p -537 45 1948
execute if score next_index do2_refill matches 164 run say item -542 11 1998 Decked Out Frost Ember
execute if score next_index do2_refill matches 164 run tp @p -542 11 1998
execute if score next_index do2_refill matches 165 run say item -545 51 2008 Decked Out Frost Ember
execute if score next_index do2_refill matches 165 run tp @p -545 51 2008
execute if score next_index do2_refill matches 166 run say item -548 11 1976 Decked Out Frost Ember
execute if score next_index do2_refill matches 166 run tp @p -548 11 1976
execute if score next_index do2_refill matches 167 run say item -553 10 2037 Decked Out Frost Ember
execute if score next_index do2_refill matches 167 run tp @p -553 10 2037
execute if score next_index do2_refill matches 168 run say item -554 51 2008 Decked Out Frost Ember
execute if score next_index do2_refill matches 168 run tp @p -554 51 2008
execute if score next_index do2_refill matches 169 run say item -558 45 1976 Decked Out Frost Ember
execute if score next_index do2_refill matches 169 run tp @p -558 45 1976
execute if score next_index do2_refill matches 170 run say item -558 46 2022 Decked Out Frost Ember
execute if score next_index do2_refill matches 170 run tp @p -558 46 2022
execute if score next_index do2_refill matches 171 run say item -560 47 1942 Decked Out Frost Ember
execute if score next_index do2_refill matches 171 run tp @p -560 47 1942
execute if score next_index do2_refill matches 172 run say item -565 36 1999 Decked Out Frost Ember
execute if score next_index do2_refill matches 172 run tp @p -565 36 1999
execute if score next_index do2_refill matches 173 run say item -569 8 1964 Decked Out Frost Ember
execute if score next_index do2_refill matches 173 run tp @p -569 8 1964
execute if score next_index do2_refill matches 174 run say item -573 11 2007 Decked Out Frost Ember
execute if score next_index do2_refill matches 174 run tp @p -573 11 2007
execute if score next_index do2_refill matches 175 run say item -573 36 1998 Decked Out Frost Ember
execute if score next_index do2_refill matches 175 run tp @p -573 36 1998
execute if score next_index do2_refill matches 176 run say item -579 -37 1835 Decked Out Frost Ember
execute if score next_index do2_refill matches 176 run tp @p -579 -37 1835
execute if score next_index do2_refill matches 177 run say item -582 13 1934 Decked Out Frost Ember
execute if score next_index do2_refill matches 177 run tp @p -582 13 1934
execute if score next_index do2_refill matches 178 run say item -582 13 1935 Decked Out Frost Ember
execute if score next_index do2_refill matches 178 run tp @p -582 13 1935
execute if score next_index do2_refill matches 179 run say item -582 13 1936 Decked Out Frost Ember
execute if score next_index do2_refill matches 179 run tp @p -582 13 1936
execute if score next_index do2_refill matches 180 run say item -582 13 1937 Decked Out Frost Ember
execute if score next_index do2_refill matches 180 run tp @p -582 13 1937
execute if score next_index do2_refill matches 181 run say item -582 9 1955 Decked Out Frost Ember
execute if score next_index do2_refill matches 181 run tp @p -582 9 1955
execute if score next_index do2_refill matches 182 run say item -583 45 2013 Decked Out Frost Ember
execute if score next_index do2_refill matches 182 run tp @p -583 45 2013
execute if score next_index do2_refill matches 183 run say item -584 -17 1927 Decked Out Frost Ember
execute if score next_index do2_refill matches 183 run tp @p -584 -17 1927
execute if score next_index do2_refill matches 184 run say item -584 13 1934 Decked Out Frost Ember
execute if score next_index do2_refill matches 184 run tp @p -584 13 1934
execute if score next_index do2_refill matches 185 run say item -584 13 1935 Decked Out Frost Ember
execute if score next_index do2_refill matches 185 run tp @p -584 13 1935
execute if score next_index do2_refill matches 186 run say item -584 13 1936 Decked Out Frost Ember
execute if score next_index do2_refill matches 186 run tp @p -584 13 1936
execute if score next_index do2_refill matches 187 run say item -584 13 1937 Decked Out Frost Ember
execute if score next_index do2_refill matches 187 run tp @p -584 13 1937
execute if score next_index do2_refill matches 188 run say item -585 -9 1920 Decked Out Frost Ember
execute if score next_index do2_refill matches 188 run tp @p -585 -9 1920
execute if score next_index do2_refill matches 189 run say item -586 1 1888 Decked Out Frost Ember
execute if score next_index do2_refill matches 189 run tp @p -586 1 1888
execute if score next_index do2_refill matches 190 run say item -587 52 1951 Decked Out Frost Ember
execute if score next_index do2_refill matches 190 run tp @p -587 52 1951
execute if score next_index do2_refill matches 191 run say item -589 11 2032 Decked Out Frost Ember
execute if score next_index do2_refill matches 191 run tp @p -589 11 2032
execute if score next_index do2_refill matches 192 run say item -589 46 1978 Decked Out Frost Ember
execute if score next_index do2_refill matches 192 run tp @p -589 46 1978
execute if score next_index do2_refill matches 193 run say item -591 1 1901 Decked Out Frost Ember
execute if score next_index do2_refill matches 193 run tp @p -591 1 1901
execute if score next_index do2_refill matches 194 run say item -598 11 1989 Decked Out Frost Ember
execute if score next_index do2_refill matches 194 run tp @p -598 11 1989
execute if score next_index do2_refill matches 195 run say item -599 12 2009 Decked Out Frost Ember
execute if score next_index do2_refill matches 195 run tp @p -599 12 2009
execute if score next_index do2_refill matches 196 run say item -602 -9 1885 Decked Out Frost Ember
execute if score next_index do2_refill matches 196 run tp @p -602 -9 1885
execute if score next_index do2_refill matches 197 run say item -606 1 1921 Decked Out Frost Ember
execute if score next_index do2_refill matches 197 run tp @p -606 1 1921
execute if score next_index do2_refill matches 198 run say item -606 43 2023 Decked Out Frost Ember
execute if score next_index do2_refill matches 198 run tp @p -606 43 2023
execute if score next_index do2_refill matches 199 run say item -609 -19 1919 Decked Out Frost Ember
execute if score next_index do2_refill matches 199 run tp @p -609 -19 1919
execute if score next_index do2_refill matches 200 run say item -619 43 2026 Decked Out Frost Ember
execute if score next_index do2_refill matches 200 run tp @p -619 43 2026
execute if score next_index do2_refill matches 201 run say item -623 -9 1924 Decked Out Frost Ember
execute if score next_index do2_refill matches 201 run tp @p -623 -9 1924
execute if score next_index do2_refill matches 202 run say item -628 1 1921 Decked Out Frost Ember
execute if score next_index do2_refill matches 202 run tp @p -628 1 1921
execute if score next_index do2_refill matches 203 run say item -633 -20 1952 Decked Out Frost Ember
execute if score next_index do2_refill matches 203 run tp @p -633 -20 1952
execute if score next_index do2_refill matches 204 run say item -633 -20 1953 Decked Out Frost Ember
execute if score next_index do2_refill matches 204 run tp @p -633 -20 1953
execute if score next_index do2_refill matches 205 run say item -633 -20 1954 Decked Out Frost Ember
execute if score next_index do2_refill matches 205 run tp @p -633 -20 1954
execute if score next_index do2_refill matches 206 run say item -633 -20 1955 Decked Out Frost Ember
execute if score next_index do2_refill matches 206 run tp @p -633 -20 1955
execute if score next_index do2_refill matches 207 run say item -633 -20 1956 Decked Out Frost Ember
execute if score next_index do2_refill matches 207 run tp @p -633 -20 1956
execute if score next_index do2_refill matches 208 run say item -633 -20 1957 Decked Out Frost Ember
execute if score next_index do2_refill matches 208 run tp @p -633 -20 1957
execute if score next_index do2_refill matches 209 run say item -633 -20 1958 Decked Out Frost Ember
execute if score next_index do2_refill matches 209 run tp @p -633 -20 1958
execute if score next_index do2_refill matches 210 run say item -633 -20 1959 Decked Out Frost Ember
execute if score next_index do2_refill matches 210 run tp @p -633 -20 1959
execute if score next_index do2_refill matches 211 run say item -633 -20 1960 Decked Out Frost Ember
execute if score next_index do2_refill matches 211 run tp @p -633 -20 1960
execute if score next_index do2_refill matches 212 run say item -633 -20 1961 Decked Out Frost Ember
execute if score next_index do2_refill matches 212 run tp @p -633 -20 1961
execute if score next_index do2_refill matches 213 run say item -633 -20 1962 Decked Out Frost Ember
execute if score next_index do2_refill matches 213 run tp @p -633 -20 1962
execute if score next_index do2_refill matches 214 run say item -633 -20 1963 Decked Out Frost Ember
execute if score next_index do2_refill matches 214 run tp @p -633 -20 1963
execute if score next_index do2_refill matches 215 run say item -633 -20 1964 Decked Out Frost Ember
execute if score next_index do2_refill matches 215 run tp @p -633 -20 1964
execute if score next_index do2_refill matches 216 run say item -633 -20 1965 Decked Out Frost Ember
execute if score next_index do2_refill matches 216 run tp @p -633 -20 1965
execute if score next_index do2_refill matches 217 run say item -633 -20 1966 Decked Out Frost Ember
execute if score next_index do2_refill matches 217 run tp @p -633 -20 1966
execute if score next_index do2_refill matches 218 run say item -633 -20 1967 Decked Out Frost Ember
execute if score next_index do2_refill matches 218 run tp @p -633 -20 1967
execute if score next_index do2_refill matches 219 run say item -633 -20 1968 Decked Out Frost Ember
execute if score next_index do2_refill matches 219 run tp @p -633 -20 1968
execute if score next_index do2_refill matches 220 run say item -633 -20 1969 Decked Out Frost Ember
execute if score next_index do2_refill matches 220 run tp @p -633 -20 1969
execute if score next_index do2_refill matches 221 run say item -633 -20 1970 Decked Out Frost Ember
execute if score next_index do2_refill matches 221 run tp @p -633 -20 1970
execute if score next_index do2_refill matches 222 run say item -633 -20 1971 Decked Out Frost Ember
execute if score next_index do2_refill matches 222 run tp @p -633 -20 1971
execute if score next_index do2_refill matches 223 run say item -633 -20 1972 Decked Out Frost Ember
execute if score next_index do2_refill matches 223 run tp @p -633 -20 1972
execute if score next_index do2_refill matches 224 run say item -633 -20 1973 Decked Out Frost Ember
execute if score next_index do2_refill matches 224 run tp @p -633 -20 1973
execute if score next_index do2_refill matches 225 run say item -633 -20 1974 Decked Out Frost Ember
execute if score next_index do2_refill matches 225 run tp @p -633 -20 1974
execute if score next_index do2_refill matches 226 run say item -633 -20 1975 Decked Out Frost Ember
execute if score next_index do2_refill matches 226 run tp @p -633 -20 1975
execute if score next_index do2_refill matches 227 run say item -633 -20 1976 Decked Out Frost Ember
execute if score next_index do2_refill matches 227 run tp @p -633 -20 1976
execute if score next_index do2_refill matches 228 run say item -633 -20 1977 Decked Out Frost Ember
execute if score next_index do2_refill matches 228 run tp @p -633 -20 1977
execute if score next_index do2_refill matches 229 run say item -633 -20 1978 Decked Out Frost Ember
execute if score next_index do2_refill matches 229 run tp @p -633 -20 1978
execute if score next_index do2_refill matches 230 run say item -633 -20 1979 Decked Out Frost Ember
execute if score next_index do2_refill matches 230 run tp @p -633 -20 1979
execute if score next_index do2_refill matches 231 run say item -640 -19 1889 Decked Out Frost Ember
execute if score next_index do2_refill matches 231 run tp @p -640 -19 1889
execute if score next_index do2_refill matches 232 run say item -642 -19 1921 Decked Out Frost Ember
execute if score next_index do2_refill matches 232 run tp @p -642 -19 1921
execute if score next_index do2_refill matches 233 run say item -644 1 1921 Decked Out Frost Ember
execute if score next_index do2_refill matches 233 run tp @p -644 1 1921
execute if score next_index do2_refill matches 234 run say item -652 1 1892 Decked Out Frost Ember
execute if score next_index do2_refill matches 234 run tp @p -652 1 1892
execute if score next_index do2_refill matches 235 run say item -654 -9 1892 Decked Out Frost Ember
execute if score next_index do2_refill matches 235 run tp @p -654 -9 1892
execute if score next_index do2_refill matches 236 run say item -569 -48 1909 The Bomb
execute if score next_index do2_refill matches 236 run tp @p -569 -48 1909
execute if score next_index do2_refill matches 237 run say item -598 -51 1876 The Bomb
execute if score next_index do2_refill matches 237 run tp @p -598 -51 1876
execute if score next_index do2_refill matches 238 run say item -602 -51 1843 The Bomb
execute if score next_index do2_refill matches 238 run tp @p -602 -51 1843
execute if score next_index do2_refill matches 239 run say item -605 -49 1910 The Bomb
execute if score next_index do2_refill matches 239 run tp @p -605 -49 1910
execute if score next_index do2_refill matches 240 run say item -637 -51 1872 The Bomb
execute if score next_index do2_refill matches 240 run tp @p -637 -51 1872
execute if score next_index do2_refill matches 241 run say item -644 -20 1992 Victory Tome
execute if score next_index do2_refill matches 241 run tp @p -644 -20 1992
execute if score next_index do2_refill matches 242 run say item -644 -20 1994 Victory Tome
execute if score next_index do2_refill matches 242 run tp @p -644 -20 1994
execute if score next_index do2_refill matches 243 run say item -644 -20 1996 Victory Tome
execute if score next_index do2_refill matches 243 run tp @p -644 -20 1996
execute if score next_index do2_refill matches 244 run say item -627 59 1945 minecraft:cooked_porkchop
execute if score next_index do2_refill matches 244 run tp @p -627 59 1945
execute if score next_index do2_refill matches 245 run say item -629 59 1945 minecraft:diamond_chestplate
execute if score next_index do2_refill matches 245 run tp @p -629 59 1945
execute if score next_index do2_refill matches 246 run say item -630 59 1945 minecraft:diamond_leggings
execute if score next_index do2_refill matches 246 run tp @p -630 59 1945
execute if score next_index do2_refill matches 247 run say item -625 59 1945 minecraft:filled_map
execute if score next_index do2_refill matches 247 run tp @p -625 59 1945
execute if score next_index do2_refill matches 248 run say item -579 -39 1843 minecraft:tnt
execute if score next_index do2_refill matches 248 run tp @p -579 -39 1843
execute if score next_index do2_refill matches 249 run say item -640 17 1904 minecraft:tnt
execute if score next_index do2_refill matches 249 run tp @p -640 17 1904
execute if score next_index do2_refill matches 250 run say item -629 59 1945 minecraft:diamond_chestplate
execute if score next_index do2_refill matches 250 run tp @p -629 59 1945
execute if score next_index do2_refill matches 251 run say item -630 59 1945 minecraft:diamond_leggings
execute if score next_index do2_refill matches 251 run tp @p -630 59 1945
execute if score next_index do2_refill matches 252 run say item -479 19 2009 Decked Out Coin
execute if score next_index do2_refill matches 252 run tp @p -479 19 2009
execute if score next_index do2_refill matches 253 run say item -484 53 1989 Decked Out Coin
execute if score next_index do2_refill matches 253 run tp @p -484 53 1989
execute if score next_index do2_refill matches 254 run say item -485 31 1963 Decked Out Coin
execute if score next_index do2_refill matches 254 run tp @p -485 31 1963
execute if score next_index do2_refill matches 255 run say item -490 11 2007 Decked Out Coin
execute if score next_index do2_refill matches 255 run tp @p -490 11 2007
execute if score next_index do2_refill matches 256 run say item -490 50 2017 Decked Out Coin
execute if score next_index do2_refill matches 256 run tp @p -490 50 2017
execute if score next_index do2_refill matches 257 run say item -497 51 1980 Decked Out Coin
execute if score next_index do2_refill matches 257 run tp @p -497 51 1980
execute if score next_index do2_refill matches 258 run say item -502 16 1972 Decked Out Coin
execute if score next_index do2_refill matches 258 run tp @p -502 16 1972
execute if score next_index do2_refill matches 259 run say item -507 9 1951 Decked Out Coin
execute if score next_index do2_refill matches 259 run tp @p -507 9 1951
execute if score next_index do2_refill matches 260 run say item -509 14 2034 Decked Out Coin
execute if score next_index do2_refill matches 260 run tp @p -509 14 2034
execute if score next_index do2_refill matches 261 run say item -514 51 1962 Decked Out Coin
execute if score next_index do2_refill matches 261 run tp @p -514 51 1962
execute if score next_index do2_refill matches 262 run say item -516 46 2031 Decked Out Coin
execute if score next_index do2_refill matches 262 run tp @p -516 46 2031
execute if score next_index do2_refill matches 263 run say item -521 35 1982 Decked Out Coin
execute if score next_index do2_refill matches 263 run tp @p -521 35 1982
execute if score next_index do2_refill matches 264 run say item -527 51 1973 Decked Out Coin
execute if score next_index do2_refill matches 264 run tp @p -527 51 1973
execute if score next_index do2_refill matches 265 run say item -531 16 1990 Decked Out Coin
execute if score next_index do2_refill matches 265 run tp @p -531 16 1990
execute if score next_index do2_refill matches 266 run say item -532 44 2024 Decked Out Coin
execute if score next_index do2_refill matches 266 run tp @p -532 44 2024
execute if score next_index do2_refill matches 267 run say item -536 45 1948 Decked Out Coin
execute if score next_index do2_refill matches 267 run tp @p -536 45 1948
execute if score next_index do2_refill matches 268 run say item -546 51 2008 Decked Out Coin
execute if score next_index do2_refill matches 268 run tp @p -546 51 2008
execute if score next_index do2_refill matches 269 run say item -554 51 2007 Decked Out Coin
execute if score next_index do2_refill matches 269 run tp @p -554 51 2007
execute if score next_index do2_refill matches 270 run say item -557 45 1976 Decked Out Coin
execute if score next_index do2_refill matches 270 run tp @p -557 45 1976
execute if score next_index do2_refill matches 271 run say item -559 46 2022 Decked Out Coin
execute if score next_index do2_refill matches 271 run tp @p -559 46 2022
execute if score next_index do2_refill matches 272 run say item -561 47 1942 Decked Out Coin
execute if score next_index do2_refill matches 272 run tp @p -561 47 1942
execute if score next_index do2_refill matches 273 run say item -563 36 1999 Decked Out Coin
execute if score next_index do2_refill matches 273 run tp @p -563 36 1999
execute if score next_index do2_refill matches 274 run say item -578 15 1968 Decked Out Coin
execute if score next_index do2_refill matches 274 run tp @p -578 15 1968
execute if score next_index do2_refill matches 275 run say item -583 45 2012 Decked Out Coin
execute if score next_index do2_refill matches 275 run tp @p -583 45 2012
execute if score next_index do2_refill matches 276 run say item -588 52 1951 Decked Out Coin
execute if score next_index do2_refill matches 276 run tp @p -588 52 1951
execute if score next_index do2_refill matches 277 run say item -590 11 2032 Decked Out Coin
execute if score next_index do2_refill matches 277 run tp @p -590 11 2032
execute if score next_index do2_refill matches 278 run say item -590 46 1978 Decked Out Coin
execute if score next_index do2_refill matches 278 run tp @p -590 46 1978
execute if score next_index do2_refill matches 279 run say item -594 12 1954 Decked Out Coin
execute if score next_index do2_refill matches 279 run tp @p -594 12 1954
execute if score next_index do2_refill matches 280 run say item -597 12 2009 Decked Out Coin
execute if score next_index do2_refill matches 280 run tp @p -597 12 2009
execute if score next_index do2_refill matches 281 run say item -598 11 1988 Decked Out Coin
execute if score next_index do2_refill matches 281 run tp @p -598 11 1988
execute if score next_index do2_refill matches 282 run say item -606 43 2024 Decked Out Coin
execute if score next_index do2_refill matches 282 run tp @p -606 43 2024
execute if score next_index do2_refill matches 283 run say item -619 43 2027 Decked Out Coin
execute if score next_index do2_refill matches 283 run tp @p -619 43 2027
execute if score next_index do2_refill matches 284 run say item -628 1 1920 Decked Out Coin
execute if score next_index do2_refill matches 284 run tp @p -628 1 1920
execute if score next_index do2_refill matches 285 run say item -640 -19 1888 Decked Out Coin
execute if score next_index do2_refill matches 285 run tp @p -640 -19 1888
execute if score next_index do2_refill matches 286 run say item -496 15 2000 Decked Out Crown
execute if score next_index do2_refill matches 286 run tp @p -496 15 2000
execute if score next_index do2_refill matches 287 run say item -523 12 2042 Decked Out Crown
execute if score next_index do2_refill matches 287 run tp @p -523 12 2042
execute if score next_index do2_refill matches 288 run say item -526 12 1942 Decked Out Crown
execute if score next_index do2_refill matches 288 run tp @p -526 12 1942
execute if score next_index do2_refill matches 289 run say item -528 12 2031 Decked Out Crown
execute if score next_index do2_refill matches 289 run tp @p -528 12 2031
execute if score next_index do2_refill matches 290 run say item -541 11 1998 Decked Out Crown
execute if score next_index do2_refill matches 290 run tp @p -541 11 1998
execute if score next_index do2_refill matches 291 run say item -548 11 1975 Decked Out Crown
execute if score next_index do2_refill matches 291 run tp @p -548 11 1975
execute if score next_index do2_refill matches 292 run say item -568 8 1964 Decked Out Crown
execute if score next_index do2_refill matches 292 run tp @p -568 8 1964
execute if score next_index do2_refill matches 293 run say item -574 11 2007 Decked Out Crown
execute if score next_index do2_refill matches 293 run tp @p -574 11 2007
execute if score next_index do2_refill matches 294 run say item -575 36 1998 Decked Out Crown
execute if score next_index do2_refill matches 294 run tp @p -575 36 1998
execute if score next_index do2_refill matches 295 run say item -577 -37 1837 Decked Out Crown
execute if score next_index do2_refill matches 295 run tp @p -577 -37 1837
execute if score next_index do2_refill matches 296 run say item -578 15 1970 Decked Out Crown
execute if score next_index do2_refill matches 296 run tp @p -578 15 1970
execute if score next_index do2_refill matches 297 run say item -581 9 1955 Decked Out Crown
execute if score next_index do2_refill matches 297 run tp @p -581 9 1955
execute if score next_index do2_refill matches 298 run say item -583 -17 1927 Decked Out Crown
execute if score next_index do2_refill matches 298 run tp @p -583 -17 1927
execute if score next_index do2_refill matches 299 run say item -585 -9 1919 Decked Out Crown
execute if score next_index do2_refill matches 299 run tp @p -585 -9 1919
execute if score next_index do2_refill matches 300 run say item -586 1 1887 Decked Out Crown
execute if score next_index do2_refill matches 300 run tp @p -586 1 1887
execute if score next_index do2_refill matches 301 run say item -590 1 1901 Decked Out Crown
execute if score next_index do2_refill matches 301 run tp @p -590 1 1901
execute if score next_index do2_refill matches 302 run say item -603 -9 1885 Decked Out Crown
execute if score next_index do2_refill matches 302 run tp @p -603 -9 1885
execute if score next_index do2_refill matches 303 run say item -606 1 1920 Decked Out Crown
execute if score next_index do2_refill matches 303 run tp @p -606 1 1920
execute if score next_index do2_refill matches 304 run say item -608 -19 1919 Decked Out Crown
execute if score next_index do2_refill matches 304 run tp @p -608 -19 1919
execute if score next_index do2_refill matches 305 run say item -632 -12 1990 Decked Out Crown
execute if score next_index do2_refill matches 305 run tp @p -632 -12 1990
execute if score next_index do2_refill matches 306 run say item -654 -9 1891 Decked Out Crown
execute if score next_index do2_refill matches 306 run tp @p -654 -9 1891
execute if score next_index do2_refill matches 307 run say item -503 31 1975 The Black Mines Key
execute if score next_index do2_refill matches 307 run tp @p -503 31 1975
execute if score next_index do2_refill matches 308 run say item -553 10 2036 The Black Mines Key
execute if score next_index do2_refill matches 308 run tp @p -553 10 2036
execute if score next_index do2_refill matches 309 run say item -624 -9 1924 The Burning Dark Key
execute if score next_index do2_refill matches 309 run tp @p -624 -9 1924
execute if score next_index do2_refill matches 310 run say item -641 -19 1921 The Burning Dark Key
execute if score next_index do2_refill matches 310 run tp @p -641 -19 1921
execute if score next_index do2_refill matches 311 run say item -644 1 1920 The Burning Dark Key
execute if score next_index do2_refill matches 311 run tp @p -644 1 1920
execute if score next_index do2_refill matches 312 run say item -652 1 1893 The Burning Dark Key
execute if score next_index do2_refill matches 312 run tp @p -652 1 1893
execute if score next_index do2_refill matches 313 run say item -513 37 1992 The Caves of Carnage Key
execute if score next_index do2_refill matches 313 run tp @p -513 37 1992
execute if score next_index do2_refill matches 314 run say item -518 35 2002 The Caves of Carnage Key
execute if score next_index do2_refill matches 314 run tp @p -518 35 2002
execute if score next_index do2_refill matches 315 run say item -519 53 2011 The Caves of Carnage Key
execute if score next_index do2_refill matches 315 run tp @p -519 53 2011
scoreboard players add next_index do2_refill 1

