from building.core import CoreBuilding
from building.drill import DrillBuilding
from content.blocks import CORE_SHARD, MECHANICAL_DRILL
from content.items import COPPER
from settings import TEST_WORLD_HEIGHT, TEST_WORLD_WIDTH
from world.terrain import COPPER_ORE, STONE
from world.world import World


PLAYER_TEAM = 0


class Game:
    def __init__(self):
        self.world = World(
            TEST_WORLD_WIDTH,
            TEST_WORLD_HEIGHT,
            STONE,
        )

        self._build_test_world()

    def _build_test_world(self):
        # 2x2 copper patch
        for y in range(2, 4):
            for x in range(2, 4):
                self.world.get_tile(x, y).ore = COPPER_ORE

        self.drill = DrillBuilding(
            MECHANICAL_DRILL,
            tile_x=2,
            tile_y=2,
            team=PLAYER_TEAM,
        )
        assert self.world.place_building(self.drill)

        self.core = CoreBuilding(
            CORE_SHARD,
            tile_x=7,
            tile_y=3,
            team=PLAYER_TEAM,
        )
        assert self.world.place_building(self.core)

    def update(self, dt: float):
        for building in list(self.world.buildings):
            if not building.destroyed:
                building.update(self, dt)

        self._cleanup_destroyed_buildings()

    def _cleanup_destroyed_buildings(self):
        for building in list(self.world.buildings):
            if building.destroyed:
                self.world.remove_building(building)

    def run_logic_test(self, seconds: float = 5.0, step: float = 0.1):
        elapsed = 0.0

        while elapsed < seconds:
            self.update(step)
            elapsed += step

        copper = self.drill.inventory.amount(COPPER)

        print("=== Phase 1 Logic Test ===")
        print(f"Simulated time: {seconds:.1f}s")
        print(f"Drill Copper: {copper}")
        print(f"Drill progress: {self.drill.progress:.2f}")
        print(f"Core Copper: {self.core.inventory.amount(COPPER)}")
