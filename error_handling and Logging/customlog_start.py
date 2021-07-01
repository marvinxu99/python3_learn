# Demonstrate how to customize logging output
"""
basicConfig(
    format = formatstr
    datrfmt = date_format_str
)
%(asctime)s
%(filename)s
%(funcName)s
%(levelname)s
%(levelno)d
%(lineno)d
%(message)s
%(module)s

"""

import logging


extraData = {
    'user': 'wesley@winter.com'
}

# TODO: add another function to log from
def anotherFunc():
    logging.debug('This is a debug-level message', extra=extraData)


def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s %(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode='w',
                        format=fmtstr, 
                        datefmt=datestr
                        )

    logging.info("This is an info-level log message", extra=extraData)
    logging.warning("This is a warning-level message", extra=extraData)

    anotherFunc()


if __name__ == "__main__":
    main()
