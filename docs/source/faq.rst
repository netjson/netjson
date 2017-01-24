Frequentedly Asked Questions
============================

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

.. raw:: html

    <p>
        <iframe src="https://nodeshot.org/github-btn.html?user=netjson&amp;repo=netjson&amp;type=watch&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
        <iframe src="https://nodeshot.org/github-btn.html?user=netjson&amp;repo=netjson&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="140" height="33"></iframe>
    </p>

Is this some kind of new SNMP?
------------------------------

Not exactly. SNMP is a protocol that aims to allow management and monitoring
of a network, NetJSON is a format that aims to describe common data structures
in networking tools, so different tools written in different languages can interoperate
by exchanging text.

Think about NetJSON as a possible common language that libraries and applications
can adopt in order to talk, exchange their data structures and interoperate on different levels.

NetJSON does not aim to define how the data is exchanged, it could be exposed
via an HTTP API, it could be sent through UDP packets, it could be copied from
application A and pasted into application B.

Privacy: can I avoid to expose sensitive data?
----------------------------------------------

Yes definitely.

NetJSON does not impose to publish, send or collect sensitive information.

NetJSON only describes how to represent data, each implementer MAY decide:

* which optional members to publish (sensitive data can be omitted)
* how to publish it (public, basic auth, token auth, ecc.)
* how to collect it
* which parts should be collected

The goal is to find a way to output and parse this data in a standard
and (possibly) easy way.

Contributing: how to send proposals, improve or extend NetJSON?
---------------------------------------------------------------

NetJSON is a new format (born in the beginning of 2015), the specification does
not yet take in consideration each and every common scenario found in wired and
wireless networks, therefore **proposals to improve the specification are very welcome**.

Just be sure to read the :doc:`Contribution Guidelines <contributing>`.

How can I register a NetJSON extension?
---------------------------------------

See the dedicated :doc:`Extension Registry <extensions>` page.

How can I add an implementation to this website?
------------------------------------------------

Just `edit the implementations page on github <https://github.com/interop-dev/netjson/edit/master/docs/source/implementations.rst>`_,
add your implementation with a good description (images are welcome if relevant)
and send a pull request.
