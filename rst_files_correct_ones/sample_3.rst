=============================
          Title
=============================

Author: Your Name
Date: August 31, 2024

Introduction
------------

This is an example of a document written in reStructuredText (reST). 
It illustrates various features of reST.

Sections
--------

This section demonstrates how to create different levels of headings.

1. First Level Heading
   --------------------
   
   This is a paragraph under the first level heading.

2. Second Level Heading
   ~~~~~~~~~~~~~~~~~~~~~

   Another paragraph under the second level heading.

Lists
-----

### Unordered List

- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3

### Ordered List

1. First item
2. Second item
3. Third item

### Definition List

term1
  Definition of term1.

term2
  Definition of term2.

Links
-----

You can link to `Python <https://www.python.org/>`_ and `reStructuredText <https://docutils.sourceforge.io/rst.html>`_.

Images
------

Here is an example of how to include an image:

.. image:: example.jpg
   :alt: Example image
   :width: 300px
   :align: center

You can also include an image from a URL:

.. image:: https://www.example.com/image.png
   :alt: Remote image
   :width: 400px
   :align: right

Functions
---------

### Example Function

Here is an example of a simple Python function:

.. code:: python

   def add(a, b):
       """
       Add two numbers together.

       :param a: First number
       :param b: Second number
       :return: Sum of a and b
       """
       return a + b

### Function Usage

To use the function, call it as follows:

.. code:: python

   result = add(5, 3)
   print(result)  # Output: 8

Tables
------

+-----------+------------+
| Header 1  | Header 2   |
+===========+============+
| Row 1     | Data 1     |
+-----------+------------+
| Row 2     | Data 2     |
+-----------+------------+

Directives
----------

.. note::

   This is a note directive. It is used to provide additional information.

.. warning::

   This is a warning directive. It is used to highlight important information.

Conclusion
----------

This document provides an overview of the key features of reStructuredText, including images and functions. 
For more information, refer to the `official documentation <https://docutils.sourceforge.io/>`_.
