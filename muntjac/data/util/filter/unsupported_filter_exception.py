# Copyright (C) 2010 IT Mill Ltd.
# Copyright (C) 2011 Richard Lincoln
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class UnsupportedFilterException(RuntimeError):
    """Exception for cases where a container does not support a specific
    type of filters.

    If possible, this should be thrown already when adding a filter to a
    container. If a problem is not detected at that point, an
    {@link UnsupportedOperationException} can be throws when attempting to
    perform filtering.

    @since 6.6
    """

    def __init__(self, *args):
        nargs = len(args)
        if nargs == 0:
            pass
        elif nargs == 1:
            if isinstance(args[0], Exception):
                cause, = args
                super(UnsupportedFilterException, self)(cause)
            else:
                message, = args
                super(UnsupportedFilterException, self)(message)
        elif nargs == 2:
            message, cause = args
            super(UnsupportedFilterException, self)(message, cause)
        else:
            raise ValueError