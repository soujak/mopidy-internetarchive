Configuration
========================================================================

This extension has a number of configuration values that can be
tweaked.  However, the :ref:`default configuration <defconf>` contains
everything to get you up and running, and will usually require only a
few modifications to match personal preferences.


.. _confvals:

Configuration Values
------------------------------------------------------------------------

.. confval:: internetarchive/base_url

   Base URL to access the Internet Archive.

.. confval:: internetarchive/username

   Your Internet Archive user name, needed to provide your bookmarks
   as a playlist in Mopidy.

.. confval:: internetarchive/collections

   A list of collection identifiers to show as top-level directories
   when browsing.

.. confval:: internetarchive/audio_formats

   A list of audio file formats, in order of preference.

   This entry contains a list of `Internet Archive file formats`_.  By
   default, only audio formats suitable for streaming are requested.
   Note that the Internet Archive also contains a large number of
   high-quality media files in FLAC_ and other lossless formats, but
   for sake of bandwidth (both your's and the Archive's), it is
   recommended that you stick to lossy audio formats for streaming
   through Mopidy.

.. confval:: internetarchive/image_formats

   A list of image file formats, in order of preference.

   This entry contains a list of `Internet Archive file formats`_ to
   be considered when providing images for Internet Archive items.
   Note that some Mopidy clients, especially MPD clients, will ignore
   album art provided by Mopidy-InternetArchive or other Mopidy
   extensions.

.. confval:: internetarchive/browse_limit

   The maximum number of browse results.

   This is used to limit the number of items returned when browsing
   the Internet Archive.

.. confval:: internetarchive/browse_order

   The :ref:`sort order<sortorder>` used when browsing the Internet
   Archive.

.. confval:: internetarchive/search_limit

   The maximum number of search results.

   This is used to limit the number of items returned when searching
   the Internet Archive.

.. confval:: internetarchive/search_order

   The :ref:`sort order<sortorder>` used when searching the Internet
   Archive.

.. _exclude:

.. confval:: internetarchive/exclude_collections

   A list of collection identifiers to exclude when searching or
   browsing.

.. confval:: internetarchive/exclude_mediatypes

   A list of Internet Archive media types to exclude when searching or
   browsing.

.. confval:: internetarchive/cache_size

   The number of items and search results to cache.

.. confval:: internetarchive/cache_ttl

   The cache time-to-live in seconds.

.. confval:: internetarchive/timeout

   The request timeout in seconds for HTTP requests to the Internet
   Archive.


.. _sortorder:

Sort Order Fields
------------------------------------------------------------------------

The sort order for searching and browsing is given as ``<fieldname>
(asc|desc)``, where ``<fieldname>`` is one of:

  - addeddate
  - avg_rating
  - call_number
  - createdate
  - creatorSorter
  - date
  - downloads
  - foldoutcount
  - headerImage
  - identifier
  - imagecount
  - indexdate
  - languageSorter
  - licenseurl
  - month
  - nav_order
  - num_reviews
  - publicdate
  - reviewdate
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
.. _Internet Archive file formats: https://archive.org/help/derivatives.php
