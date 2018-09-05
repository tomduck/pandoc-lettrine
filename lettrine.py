#!/usr/bin/env python3

"""lettrine.py - A pandoc filter for lettrine (drop caps) styling"""


import sys

from pandocfilters import toJSONFilter
from pandocfilters import RawInline, Para


TEX = r'\lettrine[lines=2]{%s}{%s}'

HTML = '<span class="lettrine"><span style="float: left; font-size: 2.3em; '\
  'line-height: 1; font-weight: bold; margin-right: 0.3em;">%s</span>'\
  '<span class="smallcaps" style="margin-left: -0.6em">%s</span></span>'


# pylint: disable=unused-argument
def action(k, v, fmt, meta):
    """Processes pandoc AST element with given key (k), value (v), output
    format (fmt) and document metadata (meta)."""

    if k == 'Para':

        # Use a lettrine/drop caps if the first letter of a paragraph is
        # marked with square brackets
        if v[0]['t'] == 'Str' and len(v[0]['c']) >= 3 and \
          v[0]['c'][0] == '[' and v[0]['c'][2] == ']':

            # Strip the brackets
            v[0]['c'] = v[0]['c'][1] + v[0]['c'][3:]

            # For latex output, use the lettrine package
            if fmt == 'latex':
                el = RawInline('latex', TEX % (v[0]['c'][0], v[0]['c'][1:]))
                return Para([el] + v[1:])

            # For html output, use css styling
            elif fmt in ['html', 'html5']:
                el = RawInline('html', HTML % (v[0]['c'][0], v[0]['c'][1:]))
                return Para([el] + v[1:])

            # Otherwise ignore
            return Para(v)

    return None


def main():
    """Main program."""
    toJSONFilter(action)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
