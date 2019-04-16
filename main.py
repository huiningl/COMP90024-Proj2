import harvester
import sys


def main(argv):
    if argv == 'stream':
        stream_mode = harvester.StreamRunner()
        stream_mode.run()
    elif argv == 'search':
        pass


if __name__ == '__main__':
    main(sys.argv)
