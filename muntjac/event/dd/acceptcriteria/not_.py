# Copyright (C) 2011 Vaadin Ltd.
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
#
# Note: This is a modified file from Vaadin. For further information on
#       Vaadin please visit http://www.vaadin.com.

"""Criterion that wraps another criterion and inverts its return value."""

from muntjac.event.dd.acceptcriteria.client_side_criterion import \
    ClientSideCriterion


class Not(ClientSideCriterion):
    """Criterion that wraps another criterion and inverts its return value.
    """

    def __init__(self, acceptCriterion):
        self._acceptCriterion = acceptCriterion


    def paintContent(self, target):
        super(Not, self).paintContent(target)
        self._acceptCriterion.paint(target)


    def accept(self, dragEvent):
        return not self._acceptCriterion.accept(dragEvent)


    def getIdentifier(self):
        return 'com.vaadin.event.dd.acceptcriteria.Not'
