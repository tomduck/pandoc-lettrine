

--------------------------------------------------------------------

**NOTICE:** This project is deprecated in favour of [pandoc-latex-extensions](https://github.com/tomduck/pandoc-latex-extensions).

--------------------------------------------------------------------


pandoc-lettrine 0.1.1
=====================

*Lettrine* (noun, french): An (ornamental) initial letter larger than the size of the text it accompanies, usually used at the beginning of a section or chapter of a book.  Known in english typesetting as a "drop cap".

*pandoc-lettrine* is a [pandoc] filter that adds a syntax extension to markdown for drop caps styling.  Python  is required.  You can install the filter using `pip install pandoc-lettrine`.

In your markdown, wrap the first character of a paragraph in square brackets to mark it for drop caps.  For TeX/pdf output you should also put `\usepackage{lettrine}` in the `header-includes` field of your file metadata.  See [demo.md] for an example.

Processing [demo.md] with `pandoc -s --filter lettrine` gives output in [pdf], [tex], and [html] formats.  Other output formats can be supported given suitable markup examples.

If you find pandoc-lettrine useful, then please kindly give it a star [on GitHub].

[pandoc]: http://pandoc.org/
[demo.md]: https://raw.githubusercontent.com/tomduck/pandoc-lettrine/master/demos/demo.md
[pdf]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.pdf
[tex]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.tex
[html]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.html
[on GitHub]:  https://github.com/tomduck/pandoc-lettrine
