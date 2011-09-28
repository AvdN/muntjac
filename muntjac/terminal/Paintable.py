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

from muntjac.util.event import EventListener, EventObject


class Paintable(EventListener):
    """Interface implemented by all classes that can be painted. Classes
    implementing this interface know how to output themselves to a UIDL stream
    and that way describing to the terminal how it should be displayed in the UI.

    @author IT Mill Ltd.
    @version @VERSION@
    @since 3.0
    """

    def paint(self, target):
        """<p>
        Paints the Paintable into a UIDL stream. This method creates the UIDL
        sequence describing it and outputs it to the given UIDL stream.
        </p>

        <p>
        It is called when the contents of the component should be painted in
        response to the component first being shown or having been altered so
        that its visual representation is changed.
        </p>

        @param target
                   the target UIDL stream where the component should paint itself
                   to.
        @throws PaintException
                    if the paint operation failed.
        """
        pass


    def requestRepaint(self):
        """Requests that the paintable should be repainted as soon as possible."""
        pass


    def setDebugId(self, idd):
        """Adds an unique id for component that get's transferred to terminal for
        testing purposes. Keeping identifiers unique throughout the Application
        instance is on programmers responsibility.
        <p>
        Note, that with the current terminal implementation the identifier cannot
        be changed while the component is visible. This means that the identifier
        should be set before the component is painted for the first time and kept
        the same while visible in the client.

        @param id
                   A short (< 20 chars) alphanumeric id
        """
        pass


    def getDebugId(self):
        """Get's currently set debug identifier

        @return current debug id, null if not set
        """
        pass


    def addListener(self, listener):
        """Adds repaint request listener. In order to assure that no repaint
        requests are missed, the new repaint listener should paint the paintable
        right after adding itself as listener.

        @param listener
                   the listener to be added.
        """
        pass


    def removeListener(self, listener):
        """Removes repaint request listener.

        @param listener
                   the listener to be removed.
        """
        pass


    def requestRepaintRequests(self):
        """Request sending of repaint events on any further visible changes.
        Normally the paintable only send up to one repaint request for listeners
        after paint as the paintable as the paintable assumes that the listeners
        already know about the repaint need. This method resets the assumtion.
        Paint implicitly does the assumtion reset functionality implemented by
        this method.
        <p>
        This method is normally used only by the terminals to note paintables
        about implicit repaints (painting the component without actually invoking
        paint method).
        </p>
        """
        pass


class RepaintRequestEvent(EventObject):
    """Repaint request event is thrown when the paintable needs to be repainted.
    This is typically done when the <code>paint</code> method would return
    dissimilar UIDL from the previous call of the method.
    """

    def __init__(self, source):
        """Constructs a new event.

        @param source
                   the paintable needing repaint.
        """
        super(RepaintRequestEvent, self)(source)


    def getPaintable(self):
        """Gets the paintable needing repainting.

        @return Paintable for which the <code>paint</code> method will return
                dissimilar UIDL from the previous call of the method.
        """
        return self.getSource()


class RepaintRequestListener(object):
    """Listens repaint requests. The <code>repaintRequested</code> method is
    called when the paintable needs to be repainted. This is typically done
    when the <code>paint</code> method would return dissimilar UIDL from the
    previous call of the method.
    """

    def repaintRequested(self, event):
        """Receives repaint request events.

        @param event
                   the repaint request event specifying the paintable source.
        """
        pass
