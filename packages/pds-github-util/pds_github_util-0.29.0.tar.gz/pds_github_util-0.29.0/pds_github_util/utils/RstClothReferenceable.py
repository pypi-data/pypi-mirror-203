import os
import logging
import rstcloth

logger = logging.getLogger(__name__)


def _indent_ok_for_table(content, indent):
    """

    :param content:
    :param indent:
    :return:
    """
    if indent == 0:
        return content
    else:
        indent = " " * indent
        if isinstance(content, list):
            return ["".join([indent, line]) for line in content]
        elif '\n' in content:
            content_lines = content.split('\n')
            return f"\n{indent}".join(content_lines)
        else:
            return "".join([indent, content])

# hacky rewirting of the function used in the rstpackage
# should do a pull request eventually
rstcloth.rstcloth._indent = _indent_ok_for_table
_indent = _indent_ok_for_table


class RstClothReferenceable(rstcloth.RstCloth):
    def __init__(self, line_width=160):
        super().__init__(line_width=line_width)
        self._deferred_directives = []

    def hyperlink(self, ref, url):
        self._deferred_directives.append(f".. _{ref}: {url}")

    def deferred_directive(self, name, arg=None, fields=None, content=None, indent=0, wrap=True, reference=None):
        """
        :param name: the directive itself to use
        :param arg: the argument to pass into the directive
        :param fields: fields to append as children underneath the directive
        :param content: the text to write into this element
        :param indent: (optional default=0) number of characters to indent this element
        :param wrap: (optional, default=True) Whether or not to wrap lines to the line_width
        :param reference: (optional, default=None) Reference to call the directive elswhere
        :return:
        """
        logger.debug("Ignoring wrap parameter, presumably for api consistency. wrap=%s", wrap)
        o = list()
        if reference:
            o.append(".. |{0}| {1}::".format(reference, name))
        else:
            o.append(".. {0}::".format(name))

        if arg is not None:
            o[0] += " " + arg

        if fields is not None:
            for k, v in fields:
                o.append(_indent(":" + k + ": " + str(v), 3))

        if content is not None:
            o.append("")

            if isinstance(content, list):
                o.extend(_indent(content, 3))
            else:
                o.append(_indent(content, 3))

        self._deferred_directives.extend(_indent(o, indent))

    def write(self, filename):
        """
            :param filename:
            :return:
            """
        dirpath = os.path.dirname(filename)
        if os.path.isdir(dirpath) is False:
          try:
              os.makedirs(dirpath)
          except OSError:
              logger.info("{0} exists. ignoring.".format(dirpath))

        with open(filename, "w") as f:
            f.write("\n".join(self._data))
            f.write("\n")
            f.write("\n".join(self._deferred_directives))
            f.write("\n")

