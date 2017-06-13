from rider import AbcRider


class OrcRider(AbcRider):
    def __init__(self, name, max_hp=30):
        self.health_meter = max_hp
        self.name = name
        self.unit_type = 'enemy'
        self.is_enemy = True
