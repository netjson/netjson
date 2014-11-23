JSON schemas for networkers
===========================

This repository is an attempt to define standard JSON schemas for the most basic
building blocks of networking:

* devices
* monitoring data
* routes

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

Once we get to a first version, we should implement these formats in softwares like:

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
