import logging
from optparse import OptionParser

logger = logging.getLogger(__name__)

def process_input_file(filename: str):
    frequency = 0
    with open(filename, 'r') as fp:
        for line in fp:
            operation = line[0]
            value = int(line[1::])
            if operation == '+':
                frequency = increase_frequency(value, frequency)
            else:
                frequency = decrease_frequency(value, frequency)
    return frequency

def increase_frequency(value: int, current_frequency: int) -> int:
    logger.info('Increasing Frequency by %s (%s)' % (value, current_frequency + value))
    return current_frequency + value

def decrease_frequency(value: int, current_frequency: int) -> int:
    logger.info('Decreasing Frequency by %s (%s)' % (value, current_frequency - value))
    return current_frequency - value

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-l', '--log-level', dest='loglevel', default='WARNING',
                      help='Set the log level to the specified value. Default is WARNING.')
    (options, args) = parser.parse_args()
    loglevel = getattr(logging, options.loglevel)
    logging.basicConfig(level=loglevel)
    print(process_input_file('input'))
