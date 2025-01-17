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

"""Interface that implements a method for validating an object."""

from muntjac.terminal.error_message import IErrorMessage

from muntjac.terminal.gwt.server.abstract_application_servlet \
    import AbstractApplicationServlet


class IValidator(object):
    """Interface that implements a method for validating if an L{object} is
    valid or not.

    Implementors of this class can be added to any L{IValidatable} implementor
    to verify its value.

    L{isValid} and L{validate} can be used to check if a value is valid.
    L{isValid} and L{validate} must use the same validation logic so that iff
    L{isValid} returns false, L{validate} throws an L{InvalidValueException}.

    Validators must not have any side effects.

    @author: Vaadin Ltd.
    @author: Richard Lincoln
    @version: @VERSION@
    """

    def validate(self, value):
        """Checks the given value against this validator. If the value is valid
        the method does nothing. If the value is invalid, an
        L{InvalidValueException} is thrown.

        @param value:
                   the value to check
        @raise InvalidValueException:
                    if the value is invalid
        """
        raise NotImplementedError


    def isValid(self, value):
        """Tests if the given value is valid. This method must be symmetric
        with L{validate} so that L{validate} throws an error iff this method
        returns false.

        @param value:
                   the value to check
        @return: C{True} if the value is valid, C{False} otherwise.
        """
        raise NotImplementedError


class InvalidValueException(RuntimeError, IErrorMessage):
    """Exception that is thrown by a L{IValidator} when a value is invalid.

    The default implementation of InvalidValueException does not support HTML
    in error messages. To enable HTML support, override L{getHtmlMessage} and
    use the subclass in validators.

    @author: Vaadin Ltd.
    @author: Richard Lincoln
    @version: @VERSION@
    """

    def __init__(self, message, causes=None):
        """Constructs a new C{InvalidValueException} with a set of causing
        validation exceptions. The causing validation exceptions are included
        when the exception is painted to the client.

        @param message:
                   The detail message of the problem.
        @param causes:
                   One or more C{InvalidValueException}s that caused
                   this exception.
        """
        super(InvalidValueException, self).__init__(message)

        # Array of one or more validation errors that are causing this
        # validation error.
        if causes is not None:
            self._causes = causes
        else:
            self._causes = list()


    def isInvisible(self):
        """Check if the error message should be hidden.

        An empty (null or "") message is invisible unless it contains nested
        exceptions that are visible.

        @return: true if the error message should be hidden, false otherwise
        """
        msg = self.message

        if msg is not None and len(msg) > 0:
            return False

        if self._causes is not None:
            for i in range(len(self._causes)):
                if not self._causes[i].isInvisible():
                    return False

        return True


    def getErrorLevel(self):
        return IErrorMessage.ERROR


    def paint(self, target):
        target.startTag('error')
        target.addAttribute('level', 'error')

        # Error message
        message = self.getHtmlMessage()
        if message is not None:
            target.addText(message)

        # Paint all the causes
        for i in range(len(self._causes)):
            self._causes[i].paint(target)

        target.endTag('error')


    def getHtmlMessage(self):
        """Returns the message of the error in HTML.

        Note that this API may change in future versions.
        """
        return AbstractApplicationServlet.safeEscapeForHtml(self.message)


    def addListener(self, listener, iface=None):
        pass


    def addCallback(self, callback, eventType=None, *args):
        pass


    def removeListener(self, listener, iface=None):
        pass


    def removeCallback(self, callback, eventType=None):
        pass


    def requestRepaint(self):
        pass


    def requestRepaintRequests(self):
        pass


    def getDebugId(self):
        return None


    def setDebugId(self, idd):
        raise NotImplementedError('InvalidValueException cannot have '
                'a debug id')


    def getCauses(self):
        """Returns the C{InvalidValueExceptions} that caused this
        exception.

        @return: An array containing the C{InvalidValueExceptions} that
                caused this exception. Returns an empty array if this
                exception was not caused by other exceptions.
        """
        return self._causes


class EmptyValueException(InvalidValueException):
    """A specific type of L{InvalidValueException} that indicates that
    validation failed because the value was empty. What empty means is up to
    the thrower.

    @author: Vaadin Ltd.
    @author: Richard Lincoln
    @version: @VERSION@
    """

    def __init__(self, message):
        super(EmptyValueException, self).__init__(message)
