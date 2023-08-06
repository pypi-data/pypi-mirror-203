.. _analytics-changelog:

Changelog
=========

Unreleased
----------

Added
~~~~~
- Added MaxRowsPerGroupPerID contraint, which limits the number of rows each unique (ID, grouping column value) pair may appear in.
- Added MaxGroupsPerID constraint, which limits the number of unique grouping column values associated with each unique ID.
- Added a new :class:`tmlt.analytics.protected_change.AddRowsWithID` class, which protects the addition or removal of all rows with the same value in a specified column.
  When creating a session with AddRowsWithID for multiple tables, you must use the new :meth:`Session.Builder.with_id_space <tmlt.analytics.session.Session.Builder.with_id_space>` method to specify the identifier space(s) of the tables.
  See the documentation for :class:`tmlt.analytics.protected_change.AddRowsWithID` for more information.
- Added a new method, :meth:`tmlt.analytics.session.Session.describe`, which describes a session, query, or table.


Changed
~~~~~~~
- Argument ``max_num_rows`` of ``QueryBuilder.flat_map`` is now optional for tables with a :class:`tmlt.analytics.protected_change.AddRowsWithID` protected change.
- *Backwards-incompatible*: Argument ``max_num_rows`` is now the last parameter specified for ``QueryBuilder.flat_map``.
- *Backwards-incompatible*: Analytics no longer allows users to set lower bounds equal to upper bounds for quantile, sum, average, variance, and standard deviation queries. Now, the lower bound must be strictly less than the upper bound.
- *Backwards-incompatible*: Renamed ``QueryBuilder.filter`` argument from "predicate" to "condition".
- *Backwards-incompatible*: Renamed ``query_expr.Filter`` property from "predicate" to "condition".
- *Backwards-incompatible*: Renamed ``KeySet.filter`` argument from "expr" to "condition".
- ``QueryBuilder.join_private`` now accepts a string as a ``right_operand``. ``QueryBuilder("table").join_private("foo")`` is equivalent to ``QueryBuilder("table").join_private(QueryBuilder("foo"))``.
- *Backwards-incompatible*: Removed the ``attr_name`` argument from ``Session.partition_and_create``.

Fixed
~~~~~

- ``Session.add_public_datafame`` used to allow creation of a public table with the same name as an existing private table, even though doing so is disallowed elsewhere and is not fully supported by some ``Session`` methods.
  It now raises a ``ValueError`` when this happens, like it already did when there was a name conflict with an existing public table.

0.6.1 - 2022-12-07
------------------

This is a maintenance release which introduces a number of documentation improvements, but has no publicly-visible API changes.

0.6.0 - 2022-12-06
------------------

.. _changelog#protected-change:

This release introduces a new way to specify what unit of data is protected by the privacy guarantee of a :class:`~tmlt.analytics.session.Session`.
A new ``protected_change`` parameter is available when creating a :class:`~tmlt.analytics.session.Session`, taking an instance of the new :class:`~tmlt.analytics.protected_change.ProtectedChange` class which describes the largest unit of data in the resulting table on which the differential privacy guarantee will hold.
See the documentation for the :mod:`~tmlt.analytics.protected_change` module for more information about the available protected changes and how to use them.

The ``stability`` and ``grouping_column`` parameters which were used to specify this information are still accepted, and work as before, but they will be deprecated and eventually removed in future releases.
The default behavior of assuming ``stability=1`` if no other information is given will also be deprecated and removed, on a similar timeline to ``stability`` and ``grouping_column``; instead, explicitly specify ``protected_change=AddOneRow()``.
These changes should make the privacy guarantees provided by the :class:`~tmlt.analytics.session.Session` interface easier to understand and harder to misuse, and allow for future support for other units of protection that were not representable with the existing API.

Added
~~~~~
- As described above, :meth:`Session.Builder.with_private_dataframe <tmlt.analytics.session.Session.Builder.with_private_dataframe>` and :meth:`Session.from_dataframe <tmlt.analytics.session.Session.from_dataframe>` now have a new parameter, ``protected_change``.
  This parameter takes an instance of one of the classes defined in the new :mod:`~tmlt.analytics.protected_change` module, specifying the unit of data in the corresponding table to be protected.

0.5.1 - 2022-11-16
------------------

Changed
~~~~~~~

-  Updated to Tumult Core 0.6.0.

0.5.0 - 2022-10-17
------------------

Added
~~~~~

-  Added a diagram to the API reference page.
-  Analytics now does an additional Spark configuration check for users running Java 11+ at the time of Analytics Session initialization. If the user is running Java 11 or higher with an incorrect Spark configuration, Analytics raises an informative exception.
-  Added a method to check that basic Analytics functionality works (``tmlt.analytics.utils.check_installation``).

Changed
~~~~~~~

-  *Backwards-incompatible*: Changed argument names for ``QueryBuilder.count_distinct`` and ``KeySet.__getitem__`` from ``cols`` to ``columns``, for consistency. The old argument has been deprecated, but is still available.
-  *Backwards-incompatible*: Changed the argument name for ``Session.partition_and_create`` from ``attr_name`` to ``column``. The old argument has been deprecated, but is still available.
-  Improved the error message shown when a filter expression is invalid.
-  Updated to Tumult Core 0.5.0.
   As a result, ``python-flint`` is no longer a transitive dependency, simplifying the Analytics installation process.

Deprecated
~~~~~~~~~~

-  The contents of the ``cleanup`` module have been moved to the ``utils`` module. The ``cleanup`` module will be removed in a future version.

0.4.2 - 2022-09-06
------------------

Fixed
~~~~~

-  Switched to Core version 0.4.3 to avoid warnings when evaluating some queries.

0.4.1 - 2022-08-25
------------------

Added
~~~~~

-  Added ``QueryBuilder.histogram`` function, which provides a shorthand for generating binned data counts.
-  Analytics now checks to see if the user is running Java 11 or higher. If they are, Analytics either sets the appropriate Spark options (if Spark is not yet running) or raises an informative exception (if Spark is running and configured incorrectly).

Changed
~~~~~~~

-  Improved documentation for ``QueryBuilder.map`` and ``QueryBuilder.flat_map``.

Fixed
~~~~~

-  Switched to Core version 0.4.2, which contains a fix for an issue that sometimes caused queries to fail to be compiled.

0.4.0 - 2022-07-22
------------------

Added
~~~~~

-  ``Session.from_dataframe`` and ``Session.Builder.with_private_dataframe`` now have a ``grouping_column`` option and support non-integer stabilities.
   This allows setting up grouping columns like those that result from grouping flatmaps when loading data.
   This is an advanced feature, and should be used carefully.

0.3.0 - 2022-06-23
------------------

Added
~~~~~

-  Added ``QueryBuilder.bin_column`` and an associated ``BinningSpec`` type.
-  Dates may now be used in ``KeySet``\ s.
-  Added support for DataFrames containing NaN and null values. Columns created by Map and FlatMap are now marked as potentially containing NaN and null values.
-  Added ``QueryBuilder.replace_null_and_nan`` function, which replaces null and NaN values with specified defaults.
-  Added ``QueryBuilder.replace_infinite`` function, which replaces positive and negative infinity values with specified defaults.
-  Added ``QueryBuilder.drop_null_and_nan`` function, which drops null and NaN values for specified columns.
-  Added ``QueryBuilder.drop_infinite`` function, which drops infinite values for specified columns.
-  Aggregations (sum, quantile, average, variance, and standard deviation) now silently drop null and NaN values before being performed.
-  Aggregations (sum, quantile, average, variance, and standard deviation) now silently clamp infinite values (+infinity and -infinity) to the query’s lower and upper bounds.
-  Added a ``cleanup`` module with two functions: a ``cleanup`` function to remove the current temporary table (which should be called before ``spark.stop()``), and a ``remove_all_temp_tables`` function that removes all temporary tables ever created by Analytics.
-  Added a topic guide in the documentation for Tumult Analytics’ treatment of null, NaN, and infinite values.

Changed
~~~~~~~

-  *Backwards-incompatible*: Sessions no longer allow DataFrames to contain a column named ``""`` (the empty string).
-  *Backwards-incompatible*: You can no longer call ``Session.Builder.with_privacy_budget`` multiple times on the same builder.
-  *Backwards-incompatible*: You can no longer call ``Session.add_private_data`` multiple times with the same source id.
-  *Backwards-incompatible*: Sessions now use the DataFrame’s schema to determine which columns are nullable.

Removed
~~~~~~~

-  *Backwards-incompatible*: Removed ``groupby_public_source`` and ``groupby_domains`` from ``QueryBuilder``.
-  *Backwards-incompatible*: ``Session.from_csv`` and CSV-related methods on ``Session.Builder`` have been removed.
   Instead, use ``spark.read.csv`` along with ``Session.from_dataframe`` and other dataframe-based methods.
-  *Backwards-incompatible*: Removed ``validate`` option from ``Session.from_dataframe``, ``Session.add_public_dataframe``, ``Session.Builder.with_private_dataframe``, ``Session.Builder.with_public_dataframe``.
-  *Backwards-incompatible*: Removed ``KeySet.contains_nan_or_null``.

Fixed
~~~~~

-  *Backwards-incompatible*: ``KeySet``\ s now explicitly check for and disallow the use of floats and timestamps as keys.
   This has always been the intended behavior, but it was previously not checked for and could work or cause non-obvious errors depending on the situation.
-  ``KeySet.dataframe()`` now always returns a dataframe where all rows are distinct.
-  Under certain circumstances, evaluating a ``GroupByCountDistinct`` query expression used to modify the input ``QueryExpr``.
   This no longer occurs.
-  It is now possible to partition on a column created by a grouping flat map, which used to raise exception from Core.

0.2.1 - 2022-04-14 (internal release)
-------------------------------------

Added
~~~~~

-  Added support for basic operations (filter, map, etc.) on Spark date and timestamp columns.
   ``ColumnType`` has two new variants, ``DATE`` and ``TIMESTAMP``, to support these.
-  Future documentation will now include any exceptions defined in Analytics.

Changed
~~~~~~~

-  Switch session to use Persist/Unpersist instead of Cache.

0.2.0 - 2022-03-28 (internal release)
-------------------------------------

Removed
~~~~~~~

-  Multi-query evaluate support is entirely removed.
-  Columns that are neither floats nor doubles will no longer be checked for NaN values.
-  The ``BIT`` variant of the ``ColumnType`` enum was removed, as it was not supported elsewhere in Analytics.

Changed
~~~~~~~

-  *Backwards-incompatible*: Renamed ``query_exprs`` parameter in ``Session.evaluate`` to ``query_expr``.
-  *Backwards-incompatible*: ``QueryBuilder.join_public`` and the ``JoinPublic`` query expression can now accept public tables specified as Spark dataframes. The existing behavior using public source IDs is still supported, but the ``public_id`` parameter/property is now called ``public_table``.
-  Installation on Python 3.7.1 through 3.7.3 is now allowed.
-  KeySets now do type coercion on creation, matching the type coercion that Sessions do for private sources.
-  Sessions created by ``partition_and_create`` must be used in the order they were created, and using the parent session will forcibly close all child sessions.
   Sessions can be manually closed with ``session.stop()``.

Fixed
~~~~~

-  Joining with a public table that contains no NaNs, but has a column where NaNs are allowed, previously caused an error when compiling queries. This is now handled correctly.

0.1.1 - 2022-02-28 (internal release)
-------------------------------------

Added
~~~~~

-  Added a ``KeySet`` class, which will eventually be used for all GroupBy queries.
-  Added ``QueryBuilder.groupby()``, a new group-by based on ``KeySet``\ s.

Changed
~~~~~~~

-  The Analytics library now uses ``KeySet`` and ``QueryBuilder.groupby()`` for all
   GroupBy queries.
-  The various ``Session`` methods for loading in data from CSV no longer support loading the data’s schema from a file.
-  Made Session return a more user-friendly error message when the user provides a privacy budget of 0.
-  Removed all instances of the old name of this library, and replaced them with “Analytics”

Deprecated
~~~~~~~~~~

-  ``QueryBuilder.groupby_domains()`` and ``QueryBuilder.groupby_public_source()`` are now deprecated in favor of using ``QueryBuilder.groupby()`` with ``KeySet``\ s.
   They will be removed in a future version.

0.1.0 - 2022-02-15 (internal release)
-------------------------------------

Added
~~~~~

-  Initial release.
