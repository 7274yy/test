from functools import lru_cache
from os import listdir, getcwd
from json import dumps

ROOT = getcwd()


@lru_cache(maxsize=10)
def getSubject(level: str):
    return dumps(sorted(listdir(f'{ROOT}/{level}')))


@lru_cache(maxsize=24)
def getYear(level: str, subject: str) -> list[str]:
    return sorted(listdir(f'{ROOT}/{level}/{subject}'))


@lru_cache(maxsize=None)
def getPaper(level: str, subject: str, year: str) -> list[str]:
    print(f'{ROOT}/{level}/{subject}/{year}')
    print(listdir(f'{ROOT}/{level}/{subject}/{year}'))
    return sorted(listdir(f'{ROOT}/{level}/{subject}/{year}'))

