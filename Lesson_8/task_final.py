from random import randint


def unique_numbers_generator(count):
    num_list = []
    while len(num_list) < count:
        new = randint(1, 91)
        if new not in num_list:
            num_list.append(new)
    return num_list


class LotoCard:
    __rows = 3
    __columns = 9
    __numbers_in_row = 5
    __data = None
    __emptynum = 0
    __crossednum = -1

    def __init__(self, title):
        uniques_count = self.__numbers_in_row * self.__rows
        uniques = unique_numbers_generator(uniques_count)
        self.title = title

        self.__data = []
        for i in range(0, self.__rows):
            row = sorted(uniques[self.__numbers_in_row * i: self.__numbers_in_row * (i + 1)])
            empty_nums_count = self.__columns - self.__numbers_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(row))
                row.insert(index, self.__emptynum)
            self.__data += row

    def __str__(self):
        line = '--------------------------'
        keep = line + '\n'
        for index, number in enumerate(self.__data):
            if number == self.__emptynum:
                keep += '  '
            elif number == self.__crossednum:
                keep += ' -'
            elif number < 10:
                keep += f' {str(number)}'
            else:
                keep += str(number)

            if (index + 1) % self.__columns == 0:
                keep += '\n'
            else:
                keep += ' '

        return keep + line

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossednum
                return
        raise ValueError(f'Числа нет в карточке: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynum, self.__crossednum}


class Game:
    __kegs_quantity = 90
    __kegs = []

    def __init__(self, human, computer):
        self.player_card = human
        self.computer_card = computer
        self.kegs = unique_numbers_generator(self.__kegs_quantity)

    def play_round(self):

        keg = self.kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.kegs)})')
        print(f'--------- Игрок ----------\n{self.player_card}')
        print(f'-- Карточка компьютера ---\n{self.computer_card}')

        player_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if player_answer == 'y' and keg not in self.player_card or \
                player_answer == 'n' and keg in self.player_card:
            return 2

        if keg in self.player_card:
            self.player_card.cross_num(keg)
            if self.player_card.closed():
                return 1
        if keg in self.computer_card:
            self.computer_card.cross_num(keg)
            if self.computer_card.closed():
                return 2

        return 0

    def start(self):
        while True:
            score = game.play_round()
            if score == 1:
                print('Вы выиграли')
                break
            elif score == 2:
                print('Вы проиграли')
                break


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = Game(human_player, computer_player)
game.start()
