from hw_2.interfaices import IGameItem, ItemFabric


class FerrumReward(IGameItem):
    def open(self):
        print('Ferrum')


class FerrumGenerator(ItemFabric):
    def create_item(self):
        return FerrumReward()
