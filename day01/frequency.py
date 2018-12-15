import logging
from optparse import OptionParser

logger = logging.getLogger(__name__)

def load_operations_from_file(filename: str) -> list:
    operations = []
    with open(filename, 'r') as fp:
        for line in fp:
            operations.append(line.rstrip())
    return operations

def find_repeated_frequency(operations: list) -> int:
    """Find the first repeated frequency in a list of operations"""
    frequency = 0
    seen_frequencies = []
    number_of_iterations = 0
    while True:
        number_of_iterations += 1
        logger.info("Starting iteration %s through operations" % number_of_iterations)
        for op in operations:
            operation = op[0]
            value = int(op[1::])
            if operation == '+':
                frequency = increase_frequency(value, frequency)
            else:
                frequency = decrease_frequency(value, frequency)
            if frequency in seen_frequencies:
                logger.info("Found Repeated Frequency %s" % frequency)
                return frequency
            else:
                logger.info("Frequency %s not seen before, adding to list of "
                            "seen frequencies" % frequency)
                seen_frequencies.append(frequency)

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
    operations = load_operations_from_file('input')
    print("The First Repeated Frequency is: %s" % find_repeated_frequency(operations))
