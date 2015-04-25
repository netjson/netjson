JSON data interchange format for networks
=========================================

This repository is an attempt to define an open standard JSON data interchange format for
encoding the most basic building blocks of networking:

* devices
* monitoring data
* routes

`Reach us on the Mailing List`_ - `Consult the ML Archives`_

.. _Reach us on the Mailing List: https://lists.funkfeuer.at/mailman/listinfo/interop-dev
.. _Consult the ML Archives: https://lists.funkfeuer.at/pipermail/interop-dev/

Goals
-----

Define simple JSON data structures that contain the lowest common denominator of:

* network device configurations
* monitoring data extracted from devices
* routes of a routing protocol

The resulting JSON structures should follow these general principles:

* `KISS`_: keep it simple, proceed one step at time
* `Principle of least astonishment`_: use accepted terminology
* **Explicit names**: prefer verbose explicit names, eg: "operating_system" is better than "os"

Once we get to a first version, we should implement these formats in software like:

* Firwmares and linux modules
* Routing protocols
* Monitoring agents
* Node databases
* Monitoring tools

.. _KISS: http://en.wikipedia.org/wiki/KISS_principle
.. _Principle of least astonishment: http://en.wikipedia.org/wiki/Principle_of_least_astonishment

Motivations
-----------

Developing software that deal with networks is harder than it should.

One has to take into account all the differences between vendors, operating systems,
routing protocols, hardware and, when dealing with community networks, one has to
deal even with the different approaches of each community.

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

Definitions
-----------

* JavaScript Object Notation (JSON), and the terms object, name, value, array, and number, are defined in `IETF RTC 4627`_.

* The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in `IETF RFC 2119`_.

.. _IETF RTC 4627: http://www.ietf.org/rfc/rfc4627.txt
.. _IETF RFC 2119: http://www.ietf.org/rfc/rfc2119.txt

Network Device Configuration
============================

**Definition**: configuration and properties of a network device

**Example**: `device-configuration.json`_

A ``Network Device Configuration`` object must have a member with the name ``type`` and value ``DeviceConfiguration``.

The object should be composed of the following members:

* ``general``
* ``hardware``
* ``operating_system``
* ``resources``
* ``interfaces``
* ``physical_devices``
* ``routing``
* ``dns_servers``
* ``dns_search``

All the values of each member must be objects which further describe each component of a network device.

**Each object will be described more in detail in the future iterations of this project**.

Software providing this JSON format to should return all the information it is able to access from the system,
according to security and privacy rules defined by the device owner or network administrator.

Software consuming this JSON format must be able to handle missing attributes.

Software consuming this JSON format must ignore unrecognized attributes.

.. _device-configuration.json: https://github.com/interop-dev/network-device-schema/blob/master/examples/device-configuration.json

Device Monitoring Data
======================

**Definition**: information that indicates the behaviour of a device that changes constantly

**Example**: `monitoring-data.json`_

A ``Device Monitoring`` object must have a member with the name ``type`` and value ``DeviceMonitoring``.

The object should be composed of the following members:

* ``general``
* ``interfaces``
* ``resources``

**Each object will be described more in detail in the future iterations of this project**.

.. _monitoring-data.json: https://github.com/interop-dev/network-device-schema/blob/master/examples/monitoring-data.json

Network Routes
==============

**Definition**: a list of routes of a dynamic routing protocol or statically configured on the device. May be contained in a ``DeviceConfiguration`` object.

**Example**: `network-routes.json`_

A ``Network Routes`` object must have a member with the name ``type`` and value ``NetworkRoutes``.

It must define the following members:

* ``protocol``: the name of the routing protocol, can be ``static`` when representing static routes
* ``version``: the version of the routing protocol, can be ``null`` when representing static routes

It may also define the optional member ``router_id``, which represent the ID of the router on which the protocol is running.

When contained in a ``DeviceConfiguration``, a ``Network Routes`` object indicates
either that a routing protocol is running on the device or that static routes have been set; in this case the member ``routes`` is required only for static routes.

When self contained, a ``Network Routes`` object represents a routing table and must define the following members:

* ``metric``: a string which indicates the name of main routing metric used by the routing protocol to determine the best routes when sending packets **it can be omitted when representing static routes**
* ``routes``: an array containing a list of routes

Each ``route`` object must define the following members:

* ``destination``: a string indicating the ip address, prefix or mac address that will be matched to the destination of the traffic
* ``next``: a string indicating the ip address, prefix or mac address of the next hop
* ``device``: a string indicating the interface the traffic will be going to, **it can be omitted when representing static routes**
* ``cost``: the numeric value of the routing metric; lower cost is better, **it can be omitted when representing static routes**

A ``route`` object may also define a ``source`` member indicating the source (necessary for source-specific routing).

.. _network-routes.json: https://github.com/interop-dev/network-device-schema/blob/master/examples/network-routes.json
