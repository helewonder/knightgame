from rider import AbcRider


class OrcRider(AbcRider):
    def __init__(self,  max_hp=30):
        self.health_meter = max_hp
        self.unit_type = 'enemy'
        self.is_enemy = True
