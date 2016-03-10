NetJSON: data interchange format for networks
=============================================

.. image:: https://raw.githubusercontent.com/interop-dev/netjson/master/static/netjson-logo.png
  :alt: NetJSON

------------

`NetJSON RFC`_ | `Mailing List`_ | `Archives`_ | `Issue tracker`_

------------

.. _NetJSON RFC: http://netjson.org/rfc.html
.. _Mailing List: https://lists.funkfeuer.at/mailman/listinfo/interop-dev
.. _Archives: https://lists.funkfeuer.at/pipermail/interop-dev/
.. _Issue tracker: https://github.com/interop-dev/netjson/issues

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

Introduction
============

NetJSON is a data interchange format based on JavaScript Object Notation (JSON)
designed to describe the basic building blocks of layer2 and layer3 networks.

It defines several types of JSON objects and the manner in which they are combined
to represent a network: configuration of devices, monitoring data, network
topology and routing information.

Goals
-----

Define simple JSON data structures that contain the lowest common denominator of:

* network device configurations
* monitoring data extracted from devices
* routes of a routing protocol

Once we get to a first version, we should implement these formats in software like:

* Firwmares and linux modules
* Routing protocols
* Monitoring agents
* Node databases
* Monitoring tools

Design principles
-----------------

The resulting JSON structures should follow these general principles:

* `KISS`_: keep it simple, proceed one step at time
* `Principle of least astonishment`_: use accepted terminology
* **Explicit names**: prefer verbose explicit names, eg: "operating_system"
  is better than "os"

.. _KISS: http://en.wikipedia.org/wiki/KISS_principle
.. _Principle of least astonishment: http://en.wikipedia.org/wiki/Principle_of_least_astonishment

Motivations
-----------

Developing software that deals with networks is harder than it should be.

Developers have to take into account all the differences between vendors,
operating systems, routing protocols, hardware and (when working with
community networks) with the different approaches of each community.

Very often, each vendor develops an entire stack that works exclusively with its
own hardware and software.

There exist many libraries and web apps for networking, but it is very hard to
make them interoperable, that is, making them talk and understand one another
with minimum effort.

Instead of creating an ecosystem, we have been creating silos that hardly talk
to each other.

This is an attempt to invert this trend, following the successful example
of the `GeoJSON`_ open standard.

By defining common data structures we can allow developers to focus on their goals
instead of having to struggle with the differences of each vendor, firmware,
routing protocol or community.

Moreover, we will lay the groundwork for an **ecosystem** to grow organically:
once the standard JSON structures are defined and adopted it will be easier to
write systems that work together, instead of creating silos.

.. _GeoJSON: http://en.wikipedia.org/wiki/GeoJSON

Specification
=============

For a detailed specification, please read the `NetJSON RFC`_.

Implementations
===============

* `OLSR.org Network Framework <http://www.olsr.org/mediawiki/index.php/NetJson_Info_Plugin>`__ (OLSRd v2)
* `netjsongraph.js <https://github.com/interop-dev/netjsongraph.js>`__ (network topology visualization library based on d3.js)
* `aspath-graph <https://github.com/coxley/aspath_graph>`__ (converts raw ASPATHs to NetJSON NetworkGraph)
* `netdiff <https://github.com/ninuxorg/netdiff#netjson-output>`__ (network topoogy parser)
* `netjsonconfig <https://github.com/openwisp/netjsonconfig>`__ (converts NetJSON DeviceConfiguration objects to native router configurations)
* `django-netjsonconfig <https://github.com/openwisp/django-netjsonconfig>`__ (reusable django app that provides a web interface to manage router configurations)
* `django-netjsongraph <https://github.com/interop-dev/django-netjsongraph>`__ (network topology visualizer & collector implemented as a django reusable app)
* `netengine-utils <http://netengine.readthedocs.org/en/latest/topics/netengine-utils.html#ifconfig-netjson-option>`__ (utilities for parsing the output from ``ifconfig``, ``iwconfig``, ecc.)

FAQs
====

Frequentedly Asked Questions.

Is this some kind of new SNMP?
------------------------------

Not exactly. Think about NetJSON as a possible common language that libraries
and applications
can adopt in order to interoperate on different levels.

NetJSON does not aim to define how the data is exchanged, it could be exposed
via an HTTP API, it could be sent through UDP packets, it could be copied from
application A and pasted into application B.

Can we avoid to expose sensitive data in order to protect privacy?
------------------------------------------------------------------

Yes definitely.

NetJSON does not impose to publish, send or collect sensitive information.

NetJSON only describes how to represent data, each implementer MAY decide:

* which optional members to publish (sensitive data can be omitted)
* how to publish it (public, basic auth, token auth, ecc.)
* how to collect it
* which parts should be collected

The goal is to find a way to output and parse this data in a standard
and (possibly) easy way.

Contact us
==========

You can contact us via the `Mailing List`_ or send feedback through
the `Issue tracker`_.
