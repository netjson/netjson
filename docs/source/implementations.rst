Implementations
===============

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

.. raw:: html

    <p>
        <iframe src="http://openwisp.io/github-btn.html?user=netjson&amp;repo=netjson&amp;type=watch&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
        <iframe src="http://openwisp.io/github-btn.html?user=netjson&amp;repo=netjson&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
    </p>

Configuration Management
------------------------

OpenWISP Controller
^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-controller/docs/docs/controller_demo.gif
   :target: https://github.com/openwisp/openwisp-controller/tree/docs/docs/controller_demo.gif
   :alt: OpenWISP Controller

`OpenWISP Controller <https://github.com/openwisp/openwisp-controller>`_ is an open-source `wifi controller
<http://openwisp.org/whatis.html>`_ and configuration manager for embedded devices and routers running
OpenWRT.

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

As of 15th of April 2016, a `netjson plugin is available in the master branch
<https://lists.olsr.org/pipermail/olsr-users/2016-April/006844.html>`_ of the
git repository of the OLSRd1 routing daemon.

This plugin implements the following NetJSON types:

* ``NetworkRoutes``
* ``NetworkGraph``
* ``NetworkCollection``

PopRouting (Prince)
^^^^^^^^^^^^^^^^^^^

`Prince <https://github.com/AdvancedNetworkingSystems/poprouting>`_ is an
open source implementation of the `PopRouting Algorithm
<http://ieeexplore.ieee.org/document/7524407/?reload=true>`_.
It has been developed as a `Google Summer of Code Project
<https://blog.freifunk.net/2016/implementing-poprouting-final-evaluation>`_
in collaboration with `Freifunk <https://freifunk.net/>`_ and the
`University of Trento <http://www.unitn.it/en>`_.

It fetches topology data in ``NetworkGraph`` format from the routing deamon, calculates the
betweenness centrality for every node of the network and pushes back the optimized timer's value.
Currently (as of December 2016) it only supports OLSRd2 (aka OONF).

Network Topology Visualizers
----------------------------

netjsongraph.js
^^^^^^^^^^^^^^^

.. image:: https://openwisp.io/docs/_images/netjsongraph-default.png
  :target: https://github.com/netjson/netjsongraph.js

`netjsongraph.js <https://github.com/netjson/netjsongraph.js>`_ is a javascript
library based on the popular d3.js visualization framework which can be used to
visualize NetJSON ``NetworkGraph`` objects.

MeshNetSimulator
^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/mwarning/MeshnetSimulator/master/docs/screenshot.png
  :target: https://github.com/mwarning/MeshNetSimulator

`MeshNetSimulator <https://github.com/mwarning/MeshNetSimulator>`_ is a simulator for sketching mesh routing algorithms.
Supported is the import and export of mesh network topologies via the NetJSON format. The MeshNetSimulator also serves as an editor to change loaded networks and create new network structures.

BGP aspath-graph
^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/coxley/aspath_graph/master/path.png
  :alt: link up, link down
  :target: https://github.com/coxley/aspath_graph

`aspath-graph <https://github.com/coxley/aspath_graph>`_ is a python library that
converts BGP ASPATHs and converts them to NetJSON ``NetworkGraph`` so they can
be viewed with `netjsongraph.js <https://github.com/netjson/netjsongraph.js>`_.

Network Topology Monitoring
---------------------------

OpenWISP Network Topology
^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://raw.githubusercontent.com/openwisp/openwisp-network-topology/docs/docs/demo_network_topology.gif
  :alt: OpenWISP Network Topology
  :target: https://github.com/openwisp/openwisp-network-topology

`OpenWISP Network Topology <https://github.com/openwisp/openwisp-network-topology>`_
is the module of the OpenWISP designed to collect, store and visualize network topology data.

Prominent features of this module are:

- Show information about links and nodes, allowing to add custom properties to nodes and links.
- Allows collecting information by receiving data via an HTTP API or by fetching the data from a URL.
- It allows to receive information from multiple nodes to avoid single points of failures and to
  know if the network was split in multiple parts.
- It allows to visualize previous states of the network: from days to weeks or even years.
- Detects and shows links that are failing.
- Show the last time a link changed its status (eg: down since 3 days)
- It can be extended to implement custom network topology monitoring solutions
  eg: it can be programmed to perform actions when the status of the network changes

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

OpenWISP Monitoring
^^^^^^^^^^^^^^^^^^^

.. image:: https://github.com/openwisp/openwisp-monitoring/raw/docs/docs/monitoring-demo.gif
  :align: center
  :alt: OpenWISP Monitoring
  :target: https://github.com/openwisp/openwisp-monitoring

`OpenWISP Monitoring <https://github.com/openwisp/openwisp-monitoring>`_
is the module of the OpenWISP designed to collect, store and visualize network topology data.

Prominent features of this module are:

- Collects and displays device status information like uptime, RAM status, CPU load averages,
  Interface properties and addresses, WiFi interface status and associated clients,
  Neighbors information, DHCP Leases, Disk/Flash status
- Collection of monitoring information in a timeseries database.
- Monitoring charts for uptime, packet loss, round trip time (latency), associated wifi clients, interface traffic,
  RAM usage, CPU load, flash/disk usage
- Charts can be viewed at resolutions of 1 day, 3 days, a week, a month and a year
- Configurable alerts
- CSV Export of monitoring data
- Possibility to configure additional `Metrics <https://github.com/openwisp/openwisp-monitoring/blob/master/README.rst#openwisp_monitoring_metrics>`_ and `Charts <https://github.com/openwisp/openwisp-monitoring/blob/master/README.rst#openwisp_monitoring_charts>`_
- Extensible active check system: it's possible to write additional checks that
  are run periodically using python classes
- API to retrieve the chart metrics and status information of each device. You can read more about it in `OpenWISP Monitoring docs <https://github.com/openwisp/openwisp-monitoring/tree/master#rest-api>`_.

OpenWrt netjson-monitoring Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `OpenWrt OpenWISP Monitoring package <https://github.com/openwisp/openwrt-openwisp-monitoring>`_
provides an OpenWrt package named
``netjson-monitoring`` which provides a command line utility which returns
NetJSON DeviceMonitoring information.

E.g.::

    netjson-monitoring --dump "*"

.. image:: https://raw.githubusercontent.com/netjson/netjson/master/docs/source/_static/lua-monitoring.png
  :alt: Device Monitoring data in NetJSON format
  :target: https://github.com/openwisp/openwrt-openwisp-monitoring

netengine-utils
^^^^^^^^^^^^^^^

`netengine-utils <http://netengine.readthedocs.org/en/latest/topics/netengine-utils.html#ifconfig-netjson-option>`_:
utilities for parsing the output from ``ifconfig``, ``iwconfig``.
