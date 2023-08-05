import gzip
import io
import logging
import sys
import typing
from urllib.request import urlopen

DEFAULT_LOG_FMT = '%(asctime)s %(name)-20s %(levelname)-3s : %(message)s'


def setup_logging(level: int = logging.INFO,
                  log_fmt: str = DEFAULT_LOG_FMT):
    """
        Create a basic configuration for the logging library. Set up console and file handler using provided `log_fmt`.
        :param level: verbosity to use, INFO by default
        :param log_fmt: format string for logging
        """
    # create logger
    logger = logging.getLogger()
    logger.setLevel(level)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # create formatter
    formatter = logging.Formatter(log_fmt)
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)


def looks_like_url(file: str) -> bool:
    return file.startswith('http://') or file.startswith('https://')


def looks_gzipped(file: str) -> bool:
    return file.endswith('.gz')


def open_text_io_handle(fh: typing.Union[typing.IO, str],
                        timeout: int = 30,
                        encoding: str = None) -> typing.TextIO:
    """
    Open a `io.TextIO` file handle based on `fh`.

    :param fh: a `str` or `typing.IO` to read from. If `str`, then it should be a path to a local file or a URL
    of a remote resource. Either `http` or `https` protocols are supported. The content will be uncompressed on the fly
    if the file name ends with `.gz`. If `fh` is an IO wrapper, the function ensures we get a text wrapper that uses
    given encoding.
    :param timeout: timeout in seconds used when accessing a remote resource
    :param encoding: encoding used to decode the input or the system preferred encoding if unset.
    :return: the `io.TextIO` wrapper
    """
    logger = logging.getLogger('hpotk.util')
    logger.debug(f'Opening {fh}')
    if encoding is None:
        encoding = sys.getdefaultencoding()
        logger.debug(f'Using default encoding \'{encoding}\'')
    else:
        logger.debug(f'Using provided encoding \'{encoding}\'')

    if isinstance(fh, str):
        # Can be a path to local file or URL
        if looks_like_url(fh):
            logger.debug(f'Looks like a URL: {fh}')
            if not isinstance(timeout, int) or timeout <= 0:
                raise ValueError(f'If {fh} looks like URL then timeout {timeout} must be a positive `int`')
            logger.debug(f'Downloading with timeout={timeout}s')
            handle = urlopen(fh, timeout=timeout)
        else:
            logger.debug(f'Looks like a local file: {fh}')
            handle = open(fh, 'rb')

        if looks_gzipped(fh):
            logger.debug(f'Looks like a gzipped data, uncompressing on the fly')
            return gzip.open(handle, mode='rt', newline='', encoding=encoding)
        else:
            logger.debug(f'Looks like un-compressed data')
            return io.TextIOWrapper(handle, encoding=encoding)
    elif isinstance(fh, typing.IO):
        if isinstance(fh, typing.BinaryIO):
            logger.debug(f'Looks like a binary IO')
            return io.TextIOWrapper(fh, encoding=encoding)
        elif isinstance(fh, typing.TextIO):
            return fh
        else:
            raise ValueError(f'Unexpected type {type(fh)}')
    else:
        raise ValueError(f'Unexpected type {type(fh)}')
