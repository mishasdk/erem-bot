from app import App
from argparse import ArgumentParser


def main(args):
    App(args.tg_token).run()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--tg_token')
    main(parser.parse_args())
