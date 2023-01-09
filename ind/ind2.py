#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import json
import click


@click.group()
def cli():
    pass


@cli.command('add')
@click.argument('filename')
@click.option('-n', '--name')
@click.option('-sn', '--surname')
@click.option('-z', '--zodiak')
@click.option('-d', '--date')
def get_human(filename, name, surname, zodiak, date):
    """""
    Запросить данные о человеке.
    """""
    humans = load_humans(filename)
    humans.append(
        {
            'surname': surname,
            'name': name,
            'zodiak': zodiak,
            'date': date
        }
    )
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(humans, fout, ensure_ascii=False, indent=4)
    click.secho("Данные добавлены")


@cli.command("display")
@click.argument('filename')
@click.option('--select', '-s', type=str)
def display_human(filename, select):
    """""
    Отобразить список людей
    """""
    humans = load_humans(filename)
    # Проверить что список людей не пуст
    if select:
        select_humans(humans, select)
    elif humans:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия и имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех.
        for idx, worker in enumerate(humans, 1):
            date = worker.get('date', '')
            print(
                '| {:^4} | {:<14} {:<15} | {:<20} | {}{} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiak', ''),
                    date,
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список работников пуст.")


def select_humans(humans, addedzz):
    """""
    Выбрать людей с заданным ЗЗ
    """""
    # Инициализировать счетчик.
    count = 0
    # Сформировать список людей
    result = []
    # Проверить сведения людей из списка.
    for human in humans:
        if human.get('zodiak', '') == addedzz:
            count += 1
            result.append(human)

    return result


def load_humans(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


if __name__ == '__main__':
    cli()
