Implementations
===============

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

.. raw:: html

    <p>
        <iframe src="https://nodeshot.org/github-btn.html?user=interop-dev&amp;repo=netjson&amp;type=watch&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
        <iframe src="https://nodeshot.org/github-btn.html?user=interop-dev&amp;repo=netjson&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
    </p>

Configuration Management
------------------------

django-netjsonconfig
^^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/openwisp/django-netjsonconfig/master/docs/images/adhoc-interface.png
  :alt: interface2, wireless interface, adhoc, ssid, bssid
  :target: https://github.com/openwisp/django-netjsonconfig

`django-netjsonconfig <https://github.com/openwisp/django-netjsonconfig>`_ is
configuration manager for embedded devices, implemented as a reusable django-app
which can be used as a standalone web app or integrated in a larger project using
the popular `django web framework <https://www.djangoproject.com/>`_.

The app makes use of the `netjsonconfig <https://github.com/openwisp/netjsonconfig>`_
library behind the scenes and allows administrators to use its features through an easy
to use web interface.

The NetJSON ``DeviceConfiguration`` objects can also be edited in directly
using raw JSON by entering *"advanced mode"*.

netjsonconfig
^^^^^^^^^^^^^

`netjsonconfig <https://github.com/openwisp/netjsonconfig>`_ is a network
configuration management library that implements the ``DeviceConfiguration`` NetJSON type.

The library has support for `OpenWRT <https://openwrt.org/>`_, `OpenWISP Firmware
<https://github.com/openwisp/OpenWISP-Firmware>`_ and it ships interesting
features like configuration templates, variables and arbitrary file inclusion.

Routing Deamons
---------------

OLSRd2 netjsoninfo plugin
^^^^^^^^^^^^^^^^^^^^^^^^^

The `netjsoninfo plugin <http://www.olsr.org/mediawiki/index.php/NetJson_Info_Plugin>`_
for the *OLSRd2* routing daemon (also known as *OLSR.org Network Framework*)
enables OLSRd2 to produce NetJSON output.

This plugin implements the following NetJSON types:

* ``NetworkRoutes``
* ``NetworkGraph``
* ``NetworkCollection``

OLSRd1 netjson plugin
^^^^^^^^^^^^^^^^^^^^^

As of 15th of April, a `netjson plugin is available in the master branch
<https://lists.olsr.org/pipermail/olsr-users/2016-April/006844.html>`_ of the
git repository of the OLSRd1 routing daemon.

This plugin implements the following NetJSON types:

* ``NetworkRoutes``
* ``NetworkGraph``
* ``NetworkCollection``

Network Topology Visualizers
----------------------------

netjsongraph.js
^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/interop-dev/netjsongraph.js/master/docs/netjsongraph-default.png
  :target: https://github.com/interop-dev/netjsongraph.js

`netjsongraph.js <https://github.com/interop-dev/netjsongraph.js>`_ is a javascript
library based on the popular d3.js visualization framework which can be used to
visualize NetJSON ``NetworkGraph`` objects.

BGP aspath-graph
^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/coxley/aspath_graph/master/path.png
  :alt: link up, link down
  :target: https://github.com/coxley/aspath_graph

`aspath-graph <https://github.com/coxley/aspath_graph>`_ is a python library that
converts BGP ASPATHs and converts them to NetJSON ``NetworkGraph`` so they can
be viewed with `netjsongraph.js <https://github.com/interop-dev/netjsongraph.js>`_.

Network Topology Monitoring
---------------------------

django-netjsongraph
^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/interop-dev/django-netjsongraph/master/docs/images/visualizer.png
  :alt: link up, link down
  :target: https://github.com/interop-dev/django-netjsongraph

`django-netjsongraph <https://github.com/interop-dev/django-netjsongraph>`_ is a
reusable `django <https://www.djangoproject.com/>`_ app for collecting and visualizing network topology. The app is able
to store network topology, detect and show links that are failing.

It can be used as a stand alone web app or integrated in larger django projects.

This implementation has an HTTP API that is able to produce ``NetworkGraph`` and
``NetworkCollection`` objects, as well as consuming and storing incoming ``NetworkGraph``
objects sent in the payload of a POST HTTP request.

This web app uses two other NetJSON implementations behind the scenes: **netjsongraph.js**
and **netdiff**.

netdiff
^^^^^^^

`netdiff <https://github.com/ninuxorg/netdiff#netjson-output>`_ is a simple python
library that acts as an abstraction layer for parsing different network topology
formats of open source dynamic routing protocols and is also able to detect changes
topology changes (added links, removed links, change in metrics).

It is able to produce and consume the ``NetworkGraph`` NetJSON type.

Device Monitoring
-----------------

netengine-utils
^^^^^^^^^^^^^^^

`netengine-utils <http://netengine.readthedocs.org/en/latest/topics/netengine-utils.html#ifconfig-netjson-option>`_:
utilities for parsing the output from ``ifconfig``, ``iwconfig``.
