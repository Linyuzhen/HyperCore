import importlib
import sys

modules = [
    "hypercore",
    "hypercore.data",
    "hypercore.datasets",
    "hypercore.manifolds",
    "hypercore.models",
    "hypercore.nn",
    "hypercore.optimizers",
    "hypercore.utils",
]

submodules = [
    "hypercore.data.airport",
    "hypercore.data.bio-wormnet",
    "hypercore.data.chameleon",
    "hypercore.data.cora",
    "hypercore.data.disease_lp",
    "hypercore.data.disease_nc",
    "hypercore.data.film",
    "hypercore.data.geom-gcn",
    "hypercore.data.power",
    "hypercore.data.pubmed",
    "hypercore.data.squirrel",
    "hypercore.data.web-edu",
    "hypercore.data.wiki_new",
    "hypercore.nn.attention",
    "hypercore.nn.conv",
    "hypercore.nn.graph_conv",
    "hypercore.nn.linear",
    "hypercore.nn.peft",
]

all_modules = modules + submodules

for mod in all_modules:
    try:
        importlib.import_module(mod)
        print(f"[OK] {mod}")
    except Exception as e:
        print(f"[FAIL] {mod}: {e}")
