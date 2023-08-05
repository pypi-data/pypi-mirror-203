from pathlib import Path
from sys import stdout
from typing import List, Optional

from ..APIs import LOOKUP_NAMES, LOOKUPS
from ..bibtex.io import writer
from ..lookups.condition_mixin import FieldConditionMixin
from ..lookups.https import HTTPSLookup
from ..utils.ansi import ANSICodes, ansi_format
from ..utils.constants import (
    CONNECTION_TIMEOUT,
    FIELD_PREFIX,
    LICENSE,
    MARKED_FIELD,
    SCRIPT_NAME,
    URL,
    VERSION_DATE,
    VERSION_STR,
)
from ..utils.functions import list_sort_using, list_unduplicate
from ..utils.logger import logger
from ..utils.only_exclude import OnlyExclude
from .autocomplete import BibtexAutocomplete
from .parser import (
    HELP_TEXT,
    flatten,
    get_bibfiles,
    indent_string,
    make_output_names,
    parser,
)


def main(argv: Optional[List[str]] = None) -> None:
    """The main function of bibtexautocomplete
    Takes an argv like List as argument,
    if none, uses sys.argv
    see HELP_TEXT or main(["-h"]) for details"""
    if argv is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(argv)

    ANSICodes.use_ansi = stdout.isatty() and not args.no_color

    if args.help:
        print(
            ansi_format(
                HELP_TEXT,
                TIMEOUT=CONNECTION_TIMEOUT,
                VERSION=VERSION_STR,
                VERSION_DATE=VERSION_DATE,
                LOOKUPS=LOOKUP_NAMES,
                NAME=SCRIPT_NAME,
                URL=URL,
                LICENSE=LICENSE,
                MARKEDFIELD=MARKED_FIELD,
                PREFIX=FIELD_PREFIX,
            )
        )
        return
    if args.version:
        print(
            "{NAME} version {VERSION} ({VERSION_DATE})".format(
                NAME=SCRIPT_NAME, VERSION=VERSION_STR, VERSION_DATE=VERSION_DATE
            )
        )
        return

    if args.silent:
        args.verbose = -args.silent
    logger.set_verbosity(args.verbose)

    args.input = flatten(args.input)
    # No input -> CWD
    if args.input == []:
        args.input = [Path(".")]
    args.input = flatten(map(get_bibfiles, args.input))
    if args.inplace:
        if args.output != []:
            logger.warn("Inplace mode, ignoring specified output files")
        args.output = args.input
    else:
        args.output = make_output_names(args.input, args.output)

    writer.align_values = args.align_values
    writer.comma_first = args.comma_first
    writer.add_trailing_comma = args.no_trailing_comma
    writer.indent = indent_string(args.indent)

    HTTPSLookup.connection_timeout = args.timeout if args.timeout > 0.0 else None
    HTTPSLookup.ignore_ssl = args.ignore_ssl
    lookups = (
        OnlyExclude[str]
        .from_nonempty(args.only_query, args.dont_query)
        .filter(LOOKUPS, lambda x: x.name)
    )
    if args.only_query != []:
        # remove duplicate from list
        args.only_query, dups = list_unduplicate(args.only_query)
        if dups:
            # Print set without leading and ending brace
            logger.warn("Duplicate '-q' arguments ignored: {set}", set=str(dups)[1:-1])
        lookups = list_sort_using(lookups, args.only_query, lambda x: x.name)

    fields = OnlyExclude[str].from_nonempty(args.only_complete, args.dont_complete)
    entries = OnlyExclude[str].from_nonempty(args.only_entry, args.exclude_entry)

    FieldConditionMixin.fields_to_complete = set(
        fields.filter(FieldConditionMixin.fields_to_complete, lambda x: x)
    )

    databases = BibtexAutocomplete.read(args.input)
    completer = BibtexAutocomplete(
        databases,
        lookups,
        fields,
        entries,
        args.force_overwrite,
        mark=args.mark,
        ignore_mark=args.ignore_mark,
        prefix=args.prefix,
    )
    completer.print_filters()
    try:
        completer.autocomplete(args.verbose < 0)
        completer.print_changes()
        if args.dump_data is not None:
            completer.write_dumps(args.dump_data)
        if not args.no_output:
            completer.write(args.output)
    except KeyboardInterrupt:
        logger.warn("Interrupted")
