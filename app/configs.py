import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import DT_FORMAT, LOG_DIR, LOG_FILE, LOG_FORMAT, SIZE_LOG


def configure_parser():
    parser = argparse.ArgumentParser(
        allow_abbrev=False, description="Вывод погоды для определенного города"
    )
    parser.add_argument(
        "city",
        nargs='+',
        help="Город, для которого нужна температура",
    )
    parser.add_argument(
        '-c', '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )
    return parser


def configure_logging():
    LOG_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=SIZE_LOG, backupCount=5
    )
    logging.basicConfig(
        level=logging.INFO,
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        encoding="utf-8",
        handlers=(rotating_handler, logging.StreamHandler()),
    )
