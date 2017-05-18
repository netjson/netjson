Why NetJSON?
============

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

.. raw:: html

    <p>
        <iframe src="https://nodeshot.org/github-btn.html?user=netjson&amp;repo=netjson&amp;type=watch&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
        <iframe src="https://nodeshot.org/github-btn.html?user=netjson&amp;repo=netjson&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
    </p>

Motivations: why we started NetJSON
-----------------------------------

Developing software that deals with networks is harder than it should be.

Developers have to take into account all the differences between vendors,
operating systems, routing protocols, hardware and (when working with
community networks) with the countless approaches of different communities.

Very often, each vendor develops an entire stack that works exclusively with its
own hardware and software.

There exist many libraries and web apps for networking, but it is very hard to
make them interoperable, that is, making them talk and understand one another
with minimum effort.

Instead of creating an ecosystem, we have been creating silos that hardly talk
to each other.

This is an attempt to invert this trend, following the successful example
of the `GeoJSON`_ open standard in the GIS field.

By defining common data structures we can allow developers to focus on their goals
instead of having to struggle with the differences of each vendor, firmware,
routing protocol or community.

Moreover, we will lay the groundwork for an **ecosystem** to grow organically:
once the standard JSON structures are defined and adopted it will be easier to
write systems that work together, instead of creating silos.

.. _GeoJSON: http://en.wikipedia.org/wiki/GeoJSON

Goals: what we want to achieve with NetJSON
-------------------------------------------

We want to define simple JSON data structures that are able to represent
the lowest common denominator of:

* network device configurations
* monitoring data extracted from devices
* routes (dynamic and static)
* network topology

We are currently busy working to write :doc:`implementations <implementations>`
for the following kind of programs:

* Firmwares and linux modules
* Routing protocols
* Configuration management tools
* Monitoring agents
* Node databases
* Monitoring tools

These implementations should  be able to either produce or consume one or more
NetJSON objects.

Some implementations might be able to do both: produce NetJSON and consume it;
for example, think about an HTTP API that returns NetJSON but at the same time
also accepts a NetJSON object in the payload of a POST HTTP request in order to
store it into a database.

The final goal is to write small tools that solve specific problems and are able
to talk to one another with minimum effort.

These tools will form an ecosystem that will enable developers to build
networking applications faster and better.

You may want to :doc:`find more information about implementations in the
dedicated section <implementations>`.

Design principles
-----------------

There are a few design principles which we adopted while designing and refining
the NetJSON specification.

KISS
^^^^

`KISS`_ means "keep it simple stupid", we adopted this principle to reflect the
fact that we want to proceed one step at time, define priorities and use our resources wisely.

While we :doc:`welcome contributions and feedback with open arms <contributing>`, we also have to recognize
that opening too many issues and working on too many fronts at the same time is a form
of waste which leads nowhere.

Therefore, we want to stay focused and add complexity to the specification only if
the motivations and goals of each change are clear and the need for a specific
change is shared among the parties involved.

Principle of least astonishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `principle of least astonishment`_ is also known as "principle of least surprise" and
we use it to refer to the preference of using accepted and recognized terminology.

Explicit is better than implicit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are in favour of **explicit names** when this improves the readability and
understanding of the JSON objects.

Exceptions can be made when an abbreviation of a long word is widely used and accepted
in the field, for example, the use of ``frag_threshold`` to refer to the
802.11 fragmentation threshold.

Readability counts
^^^^^^^^^^^^^^^^^^

Readability of the `specification (RFC) <http://netjson.org/rfc.html>`_ is really important to us.

We want the RFC to be the main reference document for all kind of developers,
therefore it has to be readable and easy to understand.

If you think a specific part of the `NetJSON RFC <http://netjson.org/rfc.html>`_ is not clear,
not specific enough or particularly hard to read, please :doc:`let us know <get-in-touch>`.

.. _KISS: http://en.wikipedia.org/wiki/KISS_principle
.. _Principle of least astonishment: http://en.wikipedia.org/wiki/Principle_of_least_astonishment
