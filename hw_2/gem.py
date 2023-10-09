from hw_2.interfaices import IGameItem, ItemFabric

# Класс 'Сундук с изумрудом', наследуется от модели
class GemReward(IGameItem):
    def open(self):
        print('Gem')


# Класс основанный на модели класса Фабрика
class GemGenerator(ItemFabric):
    def create_item(self):
        return GemReward()

