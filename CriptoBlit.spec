# # -*- mode: python ; coding: utf-8 -*-
#
# import sys
# import os
#
# from kivy_deps import sdl2, glew
# from kivymd import hooks_path as kivymd_hooks_path
#
# path = os.path.abspath("D:\gitub\gen_metamask")
#
# a = Analysis(
#     ["main.py"],
#     pathex=[path],
#     datas=[('View//MainScreen//main_screen.kv', '.')],
#     binaries=[],
#     hookspath=[kivymd_hooks_path],
#     hiddenimports=[],
#     win_no_prefer_redirects=False,
#     win_private_assemblies=False,
#     cipher=None,
#     noarchive=False,
# )
#
# pyz = PYZ(a.pure, a.zipped_data, cipher=None)
#
# exe = EXE(
#     a.scripts,
#     exclude_binaries=True,
#     name="CriptoBlit",
#     ebug=True,
#     strip=False,
#     upx=True,
#     console=True
# )
#
# coll = COLLECT(exe,
#   a.binaries,
#   a.zipfiles,
#   a.datas,
#   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins )],
#   strip=False,
#   upx=True,
#   name="CriptoBlit")



# -*- mode: python ; coding: utf-8 -*-

import sys
import os

from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

path = os.path.abspath("D:\gitub\gen_metamask")
wordlist_path = ('D://gitub//gen_metamask//CriptoBlit//venv//lib//site-packages//eth_account//hdaccount//wordlist//*.txt', 'eth_account//hdaccount//wordlist')
a = Analysis(
    ["main.py"],
    pathex=[path],
    datas=[('View//MainScreen//*.kv', 'View//MainScreen'),
           ('View//CreatWalletScreen//*.kv', 'View//CreatWalletScreen'),
           wordlist_path],
    binaries=[],
    hookspath=[kivymd_hooks_path],
    hiddenimports=['eth_account', 'mnemonic'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="CriptoBlit",
    console=False,
)

