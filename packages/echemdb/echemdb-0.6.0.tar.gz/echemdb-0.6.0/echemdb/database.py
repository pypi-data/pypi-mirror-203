r"""
A collection of datapackages with units.

EXAMPLES:

Create a database from local data packages in the `data/` directory::

    >>> from echemdb.local import collect_datapackages
    >>> database = Database(collect_datapackages('data/'))

Create a database from the data packages published in the echemdb::

    >>> database = Database()  # doctest: +REMOTE_DATA

Search the database for a single publication::

    >>> database.filter(lambda entry: entry.source.url == 'https://doi.org/10.1039/C0CP01001D')  # doctest: +REMOTE_DATA
    [Entry('alves_2011_electrochemistry_6010_f1a_solid'), ...

"""
# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2021-2023 Albert Engstfeld
#        Copyright (C) 2021      Johannes Hermann
#        Copyright (C) 2021-2022 Julian Rüth
#        Copyright (C) 2021      Nicolas Hörmann
#
#  echemdb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  echemdb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with echemdb. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************
import logging

logger = logging.getLogger("echemdb")


class Database:
    r"""
    A collection of [data packages](https://github.com/frictionlessdata/datapackage-py).

    Essentially this is just a list of data packages with some additional
    convenience wrap for use in the echemdb.

    EXAMPLES:

    An empty database::

        >>> database = Database([])
        >>> len(database)
        0

    """
    from echemdb.entry import Entry

    # Entries of this database are created from this type. Subclasses can replace this with a specialized entry type.
    Entry = Entry

    def __init__(self, data_packages=None):
        if data_packages is None:
            import os.path

            import echemdb.remote

            data_packages = echemdb.remote.collect_datapackages(
                os.path.join("website-gh-pages", "data", "generated", "svgdigitizer")
            )

        self._packages = data_packages

    @classmethod
    def create_example(cls):
        r"""
        Return a sample database for use in automated tests.

        EXAMPLES::

            >>> Database.create_example()  # doctest: +NORMALIZE_WHITESPACE
            [Entry('alves_2011_electrochemistry_6010_f1a_solid'),
            Entry('engstfeld_2018_polycrystalline_17743_f4b_1'),
            Entry('no_bibliography')]

        """

        entries = (
            cls.Entry.create_examples("alves_2011_electrochemistry_6010")
            + cls.Entry.create_examples("engstfeld_2018_polycrystalline_17743")
            + cls.Entry.create_examples("no_bibliography")
        )

        return cls(
            [entry.package for entry in entries],
        )

    @property
    def bibliography(self):
        r"""
        Return a pybtex database of all bibtex bibliography files.

        EXAMPLES::

            >>> database = Database.create_example()
            >>> database.bibliography
            BibliographyData(
              entries=OrderedCaseInsensitiveDict([
                ('alves_2011_electrochemistry_6010', Entry('article',
                ...
                ('engstfeld_2018_polycrystalline_17743', Entry('article',
                ...

        A database with entries without bibliography.

            >>> database = Database.create_example()["no_bibliography"]
            >>> database.bibliography
            ''

        """
        from pybtex.database import BibliographyData

        bib_data = BibliographyData(
            {
                entry.bibliography.key: entry.bibliography
                for entry in self
                if entry.bibliography
            }
        )

        if isinstance(bib_data, str):
            return bib_data

        # Remove duplicates from the bibliography
        bib_data_ = BibliographyData()

        for key, entry in bib_data.entries.items():
            if key not in bib_data_.entries:
                bib_data_.add_entry(key, entry)

        return bib_data_

    def filter(self, predicate):
        r"""
        Return the subset of the database that satisfies predicate.

        EXAMPLES::

            >>> database = Database.create_example()
            >>> database.filter(lambda entry: entry.source.url == 'https://doi.org/10.1039/C0CP01001D')
            [Entry('alves_2011_electrochemistry_6010_f1a_solid')]


        The filter predicate can use properties that are not present on all
        entries in the database. If a property is missing the element is
        removed from the database::

            >>> database.filter(lambda entry: entry.non.existing.property)
            []

        """

        def catching_predicate(entry):
            try:
                return predicate(entry)
            except (KeyError, AttributeError) as e:
                logger.debug(f"Filter removed entry {entry} due to error: {e}")
                return False

        return type(self)(
            data_packages=[
                entry.package for entry in self if catching_predicate(entry)
            ],
        )

    def __iter__(self):
        r"""
        Return an iterator over the entries in this database.

        EXAMPLES::

            >>> database = Database.create_example()
            >>> next(iter(database))
            Entry('alves_2011_electrochemistry_6010_f1a_solid')

        """
        # Return the entries sorted by their identifier. There's a small cost
        # associated with the sorting but we do not expect to be managing
        # millions of identifiers and having them show in sorted order is very
        # convenient, e.g., when doctesting.
        return iter(
            [
                self.Entry(package)
                for package in sorted(self._packages, key=lambda p: p.resources[0].name)
            ]
        )

    def __len__(self):
        r"""
        Return the number of entries in this database.

        EXAMPLES::

            >>> database = Database.create_example()
            >>> len(database)
            3

        """
        return len(self._packages)

    def __repr__(self):
        r"""
        Return a printable representation of this database.

        EXAMPLES::

            >>> Database([])
            []

        """
        return repr(list(self))

    def __getitem__(self, identifier):
        r"""
        Return the entry with this identifier.

        EXAMPLES::

            >>> database = Database.create_example()
            >>> database['alves_2011_electrochemistry_6010_f1a_solid']
            Entry('alves_2011_electrochemistry_6010_f1a_solid')

            >>> database['invalid_key']
            Traceback (most recent call last):
            ...
            KeyError: "No database entry with identifier 'invalid_key'."

        """
        entries = [entry for entry in self if entry.identifier == identifier]

        if len(entries) == 0:
            raise KeyError(f"No database entry with identifier '{identifier}'.")
        if len(entries) > 1:
            raise KeyError(
                f"The database has more than one entry with identifier '{identifier}'."
            )
        return entries[0]
