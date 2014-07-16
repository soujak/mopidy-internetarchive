Introduction
========================================================================

About the Internet Archive Metdata Model
------------------------------------------------------------------------

.. note::

   This is just a brief introduction to get you accustomed to some
   basic Internet Archive concepts and terminology related to this
   Mopidy extension.  For more in-depth information, please refer to
   the FAQ_, or start with this `blog post`_.

Files published on the Internet Archive are organized in so-called
*items*.  An item is a directory or folder of files that includes the
originally uploaded content file(s) – audio, video, text, etc. – along
with any derivative files created from the originals and the metadata
that describes the item.  An item may contain a single audio file, or
a related set of audio files that represent a CD or a taped live
concert.  All the files within an item have the same metadata, such as
(album) title, creator, description, and so on.  For the purpose of
Mopidy, items are treated as *albums*, and the included audio files
show up as the album's *tracks*.

Every item also has a unique identifier, which can be used to access
the item on the Internet Archive's Web site::

  http://archive.org/details/{identifier}

In Mopidy, you may encounter item identifiers in an album URI's path,
while individual tracks also contain the file name as the URI's
fragment.

Besides items containing media files, there are also *collections*,
which are used to to group related items.  The `Live Music Archive`_,
for example, is really just a collection with the identifier "etree".
An item can be a member of one or more collections, and collections
may also have sub-collections.  Within the Live Music Archive, there
exist sub-collections for all artists that gave permission for live
show recordings to be hosted on archive.org, such as the `Grateful
Dead`_ or the `Smashing Pumpkins`_, while the Live Music Archive
itself is a sub-collection of the larger `Audio Archive`_.
Collections are used to confine search queries in Mopidy, and also
show up as top-level directories when browsing.


Searching the Internet Archive
------------------------------------------------------------------------

The Internet Archive only supports searching for items, but not for
individual files or tracks.  Therefore, only *albums* will show up
when searching in Mopidy, which may not be handled correctly by your
client.  This also means that only album-related search fields are
supported, i.e. searching for track names or numbers will yield no
results from the Internet Archive.

Searching can be fine-tuned using various :ref:`configuration values
<confvals>`.  Most important is probably
:confval:`internetarchive/collections`, which specifies a list of
collection identifiers.  Search results will only contain items that
are a member of at least one of the collections listed there.  By
default, these are the "top-level" sub-collections listed on the
`Audio Archive`_ page, but this can be changed to your own liking.


Browsing the Internet Archive
------------------------------------------------------------------------

Starting with version 0.18, Mopidy also provides the possiblity to
browse directories and tracks.  If your client supports this, there
should be a virtual directory named *Internet Archive* (or whatever
you set :confval:`internetarchive/browse_label` to).  When browsing,
Internet Archive items are structured into a hierarchy three levels
deep.  At the top level, you will find the collections configured
under :confval:`internetarchive/collections`, and you will be able to
browse individual audio items (albums) and files (tracks) within
these.

For practical and performance reasons, the number of audio items that
will be shown within a collection is limited, i.e. you will not see
all 125,247 [#footnote1]_ concerts in the Live Music Archive.  The
:ref:`default configuration <defconf>` sets this limit to 100, but
this can be changed with :confval:`internetarchive/browse_limit`.
Items are selected based on popularity by default, i.e. the 100 most
downloaded items will be listed for each collection.  This can also be
changed using :confval:`internetarchive/browse_order`, for example to
always show the latest additions to the Archive.

If you have an Internet Archive account - also termed a `Virtual
Library Card`_ - or know someone who does, you can also browse through
a user's favorite items using `Archive Bookmarks`_.  To do so, simply
add the respective user names to :confval:`internetarchive/bookmarks`.
Archive Bookmarks will appear as directories beside your collections,
and can be browsed just the same.


.. _FAQ: https://archive.org/about/faqs.php

.. _blog post: http://blog.archive.org/2011/03/31/how-archive-org-items-are-structured/

.. _Live Music Archive: http://archive.org/details/etree

.. _etree: http://archive.org/details/etree

.. _Grateful Dead: http://archive.org/details/GratefulDead

.. _Smashing Pumpkins: http://archive.org/details/SmashingPumpkins

.. _Audio Archive: https://archive.org/details/audio

.. _Virtual Library Card: https://archive.org/account/login.createaccount.php

.. _Archive Bookmarks: http://archive.org/bookmarks.php

.. rubric:: Footnotes

.. [#footnote1] As of 2014-02-26.