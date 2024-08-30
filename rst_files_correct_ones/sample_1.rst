==============
reStructuredText
==============

**reStructuredText (reST)** is a lightweight markup language. Here’s a demonstration of various reST features:

Sections and Subsections
-------------------------

You can create sections and subsections using different underlines:

Introduction
~~~~~~~~~~~~

This is the introduction section.

Lists
-----

- Bullet List Item 1
- Bullet List Item 2
  - Nested Bullet List Item
  - Another Nested Item

1. Numbered List Item 1
2. Numbered List Item 2
   1. Nested Numbered Item 1
   2. Nested Numbered Item 2

Links and References
--------------------

- `reStructuredText Documentation <https://docutils.sourceforge.io/rst.html>`_
- Internal reference to the `Lists`_ section.

Inline Markup
-------------

This is **bold text**, *italic text*, and ``inline literal text``. Here’s a `link <https://www.example.com>`_.

Images
------

.. image:: https://via.placeholder.com/150
   :alt: Placeholder Image
   :width: 100px

Block Quotes
------------

Here’s a block quote:

   "To be, or not to be, that is the question." -- William Shakespeare

Literal Blocks
--------------

You can include literal blocks by indenting:

::

   def hello_world():
       print("Hello, World!")

Tables
------

Here’s a simple table:

+-----------------+-----------------+
| Header 1        | Header 2        |
+=================+=================+
| Row 1, Column 1 | Row 1, Column 2 |
+-----------------+-----------------+
| Row 2, Column 1 | Row 2, Column 2 |
+-----------------+-----------------+

Directives
----------

.. note::

   This is a note directive.

.. warning::

   This is a warning directive.

.. code-block:: python

   def hello_world():
       print("Hello, World!")

Admonitions
-----------

.. admonition:: Hint

   reStructuredText is powerful yet simple!

Footnotes
---------

You can add footnotes like this: [#]_.

.. [#] This is the footnote.

Definition Lists
----------------

Python
  A high-level programming language.

reStructuredText
  A lightweight markup language.

Sphinx Domains
--------------

Sphinx domains are used for documenting code:

.. py:function:: my_function(arg1, arg2)

   This is a Python function.

.. c:function:: int my_c_function(int arg1, int arg2)

   This is a C function.

Conclusion
----------

This reStructuredText document showcases various features you can use to create structured and well-formatted documentation.




