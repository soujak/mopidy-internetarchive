Configuration
========================================================================

This extension has a number of configuration values that can be
tweaked.  However, the :ref:`default configuration <defconf>` contains
everything to get you up and running, and will usually require only a
few modifications to match personal needs.


.. _confvals:

Configuration Values
------------------------------------------------------------------------

.. note::

   Configuration values are still subject to change at this point, so
   be warned before trying any of these.

.. confval:: internetarchive/base_url

   Base URL to access the Internet Archive.

.. confval:: internetarchive/collections

   Collections for searching/browsing.

.. confval:: internetarchive/mediatypes

   Media types for searching/browsing.

.. confval:: internetarchive/formats

   Audio file formats, in order of preference.

   This entry contains a list of Internet Archive media formats.  By
   default, only streaming formats are requested.  Note that the
   Internet Archive also contains a large number of high-quality media
   files in FLAC_ format, but for sake of bandwidth (both your's and
   the Archive's), it is recommended that you stick to the recommended
   streaming formats.  You can download FLAC files from the Archive
   and play them locally, of course.

.. confval:: internetarchive/excludes

   Collections to exclude from searching/browsing.

.. confval:: internetarchive/search_limit

   Maximum number of search results.

   This is used to limit the number of items returned for a search
   query.

.. confval:: internetarchive/search_order

   Sort order for searching.  See `Sort Order Fields`_.

.. confval:: internetarchive/browse_limit

   Maximum number of browse results.

   This is used to limit the number of items returned for a browse
   query.

.. confval:: internetarchive/browse_order

   Sort order for browsing.  See `Sort Order Fields`_.

.. confval:: internetarchive/browse_label

   The top-level directory name for browsing the Internet Archive.

.. confval:: internetarchive/bookmarks

   User names for bookmark browsing.

.. confval:: internetarchive/bookmarks_label

   Bookmark directory names for browsing; {0} is user name

.. confval:: internetarchive/cache_size

   Number of items and query results to cache.

.. confval:: internetarchive/cache_ttl

   Cache time-to-live in seconds.

.. confval:: internetarchive/timeout

   Optional http request timeout in seconds.

   This setting can be used to abort HTTP requests to the Internet
   Archive after a given timeout.  Since the best value for this
   highly depends on your configuration, network connection, and
   external factors such as the Internet Archive's current load, this
   is left blank in default configuration.


Sort Order Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sort order for searching/browsing: ``<fieldname> (asc|desc)``, where
``<fieldname>`` is one of:

   - avg_rating
   - creatorSorter
   - date
   - downloads
   - month
   - publicdate
   - stars
   - titleSorter
   - week
   - year


.. _defconf:

Default Configuration
------------------------------------------------------------------------

For reference, this is the default configuration shipped with
Mopidy-InternetArchive release |release|:

.. literalinclude:: ../mopidy_internetarchive/ext.conf
   :language: ini


.. _FLAC: http://en.wikipedia.org/wiki/FLAC