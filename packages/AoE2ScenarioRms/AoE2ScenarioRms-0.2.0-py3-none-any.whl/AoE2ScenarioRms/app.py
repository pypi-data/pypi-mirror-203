from __future__ import annotations

import random
import sys

from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

from AoE2ScenarioRms import AoE2ScenarioRms
from AoE2ScenarioRms.debug import ApplyAllVisible, ApplyNoClutter, ApplyXsPrint, ApplyBlockedAsBlack
from AoE2ScenarioRms.debug.apply_state_as_black import ApplyAvailableAsBlack
from AoE2ScenarioRms.flags import ObjectClear, TerrainMark, ObjectMark
from AoE2ScenarioRms.local_config import folder_de
from AoE2ScenarioRms.util import GridMapFactory, ScenarioUtil
from examples.create_objects import create_objects_config, create_objects_config_shore_fish, \
    create_objects_config_deep_fish

seed = random.randrange(sys.maxsize)
seed = 7647799647017082024
random.seed(seed)
print("Seed:", seed)

filename = "defense2"
scenario = AoE2DEScenario.from_file(f"{folder_de}{filename}.aoe2scenario")
asr = AoE2ScenarioRms(scenario)

ScenarioUtil.clear(scenario, ObjectClear.ALL & ~ObjectClear.CLIFFS)

grid_map = GridMapFactory.block(
    scenario=scenario,
    terrain_marks=TerrainMark.WATER_SHORE_BEACH,
    object_marks=ObjectMark.ALL,
)
asr.create_objects(create_objects_config, grid_map)

grid_map = GridMapFactory.select(
    scenario=scenario,
    terrain_marks=TerrainMark.SHORE,
)
asr.create_objects(create_objects_config_shore_fish, grid_map)

grid_map = GridMapFactory.select(
    scenario=scenario,
    terrain_ids=[
        TerrainId.WATER_DEEP_OCEAN,
        TerrainId.WATER_DEEP,
        TerrainId.WATER_MEDIUM,
    ]
)
asr.create_objects(create_objects_config_deep_fish, grid_map)

ApplyAllVisible(asr)
ApplyNoClutter(asr)
ApplyXsPrint(asr)
# ApplyAvailableAsBlack(asr, grid_map, as_layer=False)

scenario.write_to_file(f"{folder_de}!{filename}_written.aoe2scenario")
