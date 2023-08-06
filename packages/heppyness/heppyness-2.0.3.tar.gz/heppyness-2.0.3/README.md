# Heppy

Heppy provides pythonic data structures and a few high-level tools for high-energy physics. In particular, it provides very useful histogram classes that neatly integrate systematic variations (which, to my knowledge, no other histogram class that's widely used in HEP does) and support common operations such as addition, division, rebinning, slicing, projecting, integrating. It also provides flexible matplotlib-based plotting.

The documentation can be found [here](https://heppy.readthedocs.io).

This package provides object conversion from and to ROOT histograms, which is handled by [uproot](https://github.com/scikit-hep/uproot).
As such, it does not depend on ROOT per se. It does, however, contain some functionality (mostly clearly marked as "legacy") that does require (py)ROOT and the deprecated (but still to some degree functioning) root-numpy to be installed if you want to use it. All of that will also be ported to uproot at some point.
