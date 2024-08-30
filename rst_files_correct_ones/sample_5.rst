=============================
       Sample Document
=============================

Author: Your Name
Date: August 31, 2024

Abstract
--------

This document provides an overview of reStructuredText (reST) syntax and features, including headings, lists, links, images, functions, tables, and directives.

Headings
--------

The following shows the structure of headings in reST.

========================
Main Title
========================

-------------------------
Section Title
-------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~
Subsection Title
~~~~~~~~~~~~~~~~~~~~~~~~~

Lists
-----

### Unordered List Example

- Bullet 1
- Bullet 2
  - Nested Bullet 2.1
  - Nested Bullet 2.2
- Bullet 3

### Ordered List Example

1. First item
2. Second item
3. Third item

### Definition List Example

Key Term 1
  Explanation of key term 1.

Key Term 2
  Explanation of key term 2.

Links
-----

You can find more information at `Python's website <https://www.python.org/>`_ and the `reStructuredText documentation <https://docutils.sourceforge.io/rst.html>`_.

Images
------

To include a local image:

.. image:: local_image.png
   :alt: Local Image
   :width: 400px
   :align: center

To include an external image:

.. image:: https://www.example.com/image.png
   :alt: External Image
   :height: 200px
   :align: right

Functions
---------

### Defining a Function

Here’s how to define a function in Python:

.. code:: python

   def subtract(a, b):
       """
       Subtracts the second number from the first.

       :param a: Minuend
       :param b: Subtrahend
       :return: Result of subtraction
       """
       return a - b

### Using the Function

You can use the function as shown below:

.. code:: python

   result = subtract(10, 4)
   print(result)  # Output: 6

Tables
------

Tables can be used to present data clearly:

+------------+------------+
| Header 1   | Header 2   |
+============+============+
| Row A      | Value A    |
+------------+------------+
| Row B      | Value B    |
+------------+------------+

Directives
----------

Directives are useful for highlighting specific information:

.. tip::

   This is a helpful tip to remember.

.. danger::

   This is a danger directive that highlights important warnings.

Conclusion
----------

This document serves as an introduction to reStructuredText, covering its essential features like headings, lists, images, functions, and more. 
For further exploration, visit the `official documentation <https://docutils.sourceforge.io/>`_.
