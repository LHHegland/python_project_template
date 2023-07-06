"""
one-line summary (e.g. "[Do...] and return [item].")

detailed description, including use, input, and output information

should be usable as its “usage” message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a “-h” option, for “help”). Such a docstring should document the script’s function and command line syntax, environment variables, and files. Usage messages can be fairly elaborate (several screens full) and should be sufficient for a new user to use the command properly, as well as a complete quick reference to all options and arguments for the sophisticated user.

The docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each. (These summaries generally give less detail than the summary line in the object’s docstring.) The docstring for a package (i.e., the docstring of the package’s __init__.py module) should also list the modules and subpackages exported by the package.

The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.

The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its __init__ method. Individual methods should be documented by their own docstring.

If a class subclasses another class and its behavior is mostly inherited from that class, its docstring should mention this and summarize the differences. Use the verb “override” to indicate that a subclass method replaces a superclass method and does not call the superclass method; use the verb “extend” to indicate that a subclass method calls the superclass method (in addition to its own behavior).

REFERENCES:
  - logging -- See https://docs.python.org/3/library/logging.html
  - argparse -- used for command line only, not required for import use.
                See https://docs.python.org/3/library/argparse.html
"""


import logging
import argparse
from config_log import setup


def get_cli_help():
    """
    Setup configuration of command line interface parameters

    PURPOSE: Improve command line interface usability of module.

    USAGE: 
     - At command line: py module_template.py -h

    INPUT: None

    OUTPUT:
     - displays command line help and usage instructions (i.e. prints to stdout)

    REFERENCES:
  - argparse -- See https://docs.python.org/3/library/argparse.html
    """
    # Create argument parser instance with module information.
    parser = argparse.ArgumentParser(
        prog='module_template',
        description='Simply a draft template for new Python modules.',
        epilog='For questions or concerns, please contact'
               ' lance.hegland@civic-innovations.com'
    )

    # Add module argument information.
    parser.add_argument('--tes', '--testexceptionspecified',
                        action='store_true',
                        dest='is_test_exception_specified',
                        help='optional flag to test specified exception handling'
    )
    parser.add_argument('--teu', '--testexceptionunspecified',
                        action='store_true',
                        dest='is_test_exception_unspecified',
                        help='optional flag to test unspecified exception handling'
    )
    parser.add_argument('--lfpn', '--logfilepathname',
                        required=False, action='store', type=str,
                        dest='logfile_path_name',
                        help='optional logging file\'s path and name (e.g. \'D:\\path\\file.log\')'
    )
    
    # Return parser instance.
    return parser.parse_args()


def some_function(some_variable1: float, some_variable2: int = 23, some_variable3: str | None = None) -> list:
    """
    one-line summary (e.g. "[Do...] and return [item].")

    detailed description, including use, input, and output information

    The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.

    The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its __init__ method. Individual methods should be documented by their own docstring.

    If a class subclasses another class and its behavior is mostly inherited from that class, its docstring should mention this and summarize the differences. Use the verb “override” to indicate that a subclass method replaces a superclass method and does not call the superclass method; use the verb “extend” to indicate that a subclass method calls the superclass method (in addition to its own behavior).
    """
    return None


# Usage Example
if __name__ == '__main__':
    # Configure command line interface arguments plus help and usage messages
    args = get_cli_help()
    
    # Configure logging per command line options
    if args.logfile_path_name == None:
        logger = setup(__name__)
    else:
        logger = setup(__name__, args.logfile_path_name)

    try: # Code to execute, at least until an exception occurs

        # Create logging messages for testing.
        print('\n'
              '\n'
              '----- STARTING EXECUTION module_template.py -----\n'
              'One moment please.')

        if args.is_test_exception_specified:
            # test specified ZeroDivisionError exception handling
            some_variable = 1 / 0

        if args.is_test_exception_unspecified:
            # Test unspecified exception handling
            raise Exception(
                'Oh, golly. Something really bad'
                ' unexpectedly happened.'
            )
        
        logger.info(
            'TEST INFO: Message to confirm execution is working as'
            ' expected. Generally, displayed only in DEVELOPMENT'
            ' environment; typically, suppressed in TEST and PRODUCTION'
            ' environments.'
        )
        logger.debug(
            'TEST DEBUG: Message with critical details to help identify'
            ' and resolve problems. Generally, displayed only in'
            ' DEVELOPMENT environment; typically, suppressed in TEST and'
            ' PRODUCTION environments.'
        )
        logger.warning(
            'TEST WARNING: Message indicating that an unexpected minor problem'
            ' happened, or will likely happen in the near future (e.g.'
            ' disk space low), even though execution is currently working'
            ' as expected.',
            exc_info = True
        )
        logger.error(
            'TEST ERROR: Message indicating that an unexpected serious problem'
            ' has occurred, which prevented some code or function to finish'
            ' executing as expected. State that results are likely invalid'
            ' or unreliable. Suggest 2 or 3 of the most common causes and'
            ' related corrective actions. Refer to a specific, credible'
            ' help article title and URL. Recommend contacting the help'
            ' desk if errors continue. Offer several contact response'
            ' levels depending on the user\'s urgency. Provide help desk'
            ' contact information; e.g. online form, email address, chat'
            ' URL, phone number.',
            exc_info = True
        )
        logger.critical(
            'TEST CRITICAL: Message indicating that an unexpected near-fatal'
            ' or fatal problem has occurred, which will very likely'
            ' prevent any further execution to occur. State that results'
            ' are very likely invalid or unreliable. Suggest 2 or 3 of the'
            ' most common causes and related corrective actions. Refer to'
            ' a specific, credible help article title and URL. Recommend'
            ' contacting the help desk if errors continue. Offer several'
            ' contact response levels depending on the user\'s urgency.'
            ' Provide help desk contact information; e.g. online form,'
            ' email address, chat URL, phone number.',
            exc_info = True
        )
        # Notify user that successful execution has completed.
        if args.logfile_path_name == None:
            print('\n\nSUCCESSFUL EXECUTION: module_template.py. See output displayed above.')
        else:
            print('\n\nSUCCESSFUL EXECUTION: module_template.py. See output in', args.logfile_path_name, '.')


    except ZeroDivisionError: # Code to handle specific exception
        logger.exception(
            'Oops! Something went wrong. The application tried to do a'
            ' math problem where it tried to divide a number by zero,'
            ' but that is impossible to do. So the program stopped to'
            ' make sure it doesn\'t give you any wrong or unreliable'
            ' information.\n'
            '\n'
            'But, don\'t worry! Let\'s figure out what went wrong and'
            ' get you back on track. First, please double-check the'
            ' information you entered. Make sure everything is correct'
            ' and matches what you intended. If there\'s anything that'
            ' needs to be changed, go ahead and fix it.\n'
            '\n'
            'If you\'re still having trouble, we\'re here to help! You'
            ' can reach out to our support team in a way that\'s most'
            ' convenient for you.\n'
            '\n'
            '[TODO: Add technical support contact options.]\n'
            '\n'
            'We\'re here to make sure everything runs smoothly for'
            ' you, so don\'t hesitate to get in touch.\n'
            '\n'
            'Technical Error Details to Share with Our Support Team:',
            exc_info = True
        )
    except Exception as e: # Code to handle unspecified exception
        logger.exception(
            'Oops! Something unexpectedly went wrong. The application'
            ' stopped to make sure it doesn\'t give you any wrong or'
            ' unreliable information.\n'
            '\n'
            'But, don\'t worry! Let\'s figure out what went wrong and'
            ' get you back on track. First, please double-check the'
            ' information you entered. Make sure everything is correct'
            ' and matches what you intended. If there\'s anything that'
            ' needs to be changed, go ahead and fix it.\n'
            '\n'
            'If you\'re still having trouble, we\'re here to help! You'
            ' can reach out to our support team in a way that\'s most'
            ' convenient for you.\n'
            '\n'
            '[TODO: Add technical support contact options.]\n'
            '\n'
            'We\'re here to make sure everything runs smoothly for'
            ' you, so don\'t hesitate to get in touch.\n'
            '\n'
            'Technical Error Details to Share with Our Support Team:',
            exc_info = True
        )


    finally: # Code to always execute, even if an exception occurs
        logger.info('EXITING: module_template.py')