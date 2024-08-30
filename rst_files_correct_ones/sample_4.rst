=============================
       Document Title
=============================

Author: Your Name
Date: August 31, 2024

Overview
--------

This document serves as a comprehensive guide to the key features of reStructuredText (reST). 
It covers various elements such as headings, lists, links, images, functions, tables, and directives.

Headings
--------

The following shows how to create different levels of headings.

========================
First Level Heading
========================

-------------------------
Second Level Heading
-------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~
Third Level Heading
~~~~~~~~~~~~~~~~~~~~~~~~~

Lists
-----

### Bulleted List

- Item A
- Item B
  - Subitem B1
  - Subitem B2
- Item C

### Numbered List

1. First point
2. Second point
3. Third point

### Definition List

term1
  Description of term1.

term2
  Description of term2.

Links
-----

For more information, visit `Python's official website <https://www.python.org/>`_ 
or check the `reStructuredText documentation <https://docutils.sourceforge.io/rst.html>`_.

Images
------

To include an image from a local file:

.. image:: local_image.png
   :alt: Local image example
   :width: 500px
   :align: center

To include an image from an external source:

.. image:: https://www.example.com/external_image.png
   :alt: External image example
   :height: 300px
   :align: left

Functions
---------

### Example Function Definition

Here’s an example of a function in Python:

.. code:: python

   def multiply(x, y):
       """
       Multiply two numbers.

       :param x: First number
       :param y: Second number
       :return: Product of x and y
       """
       return x * y

### Example Function Call

You can call the function like this:

.. code:: python

   product = multiply(4, 5)
   print(product)  # Output: 20

Tables
------

This table presents information in a structured format:

+------------+-----------+
| Column 1   | Column 2  |
+============+===========+
| Row 1      | Value 1   |
+------------+-----------+
| Row 2      | Value 2   |
+------------+-----------+

Directives
----------

Use directives to highlight important notes or warnings:

.. note::

   This is a note that provides additional context.

.. caution::

   This is a caution that warns about potential issues.

Conclusion
----------

This document summarizes the essential features of reStructuredText, including how to use images, functions, and various formatting options. 
For further details, refer to the `official documentation <https://docutils.sourceforge.io/>`_.
