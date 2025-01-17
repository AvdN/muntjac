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

from muntjac.ui.themes.base_theme import BaseTheme


class Reindeer(BaseTheme):

    THEME_NAME = 'reindeer'

    # Label styles
    #
    #      ********************************************************************

    # Large font for main application headings
    LABEL_H1 = 'h1'

    # Large font for different sections in the application
    LABEL_H2 = 'h2'

    # Small and a little lighter font
    LABEL_SMALL = 'light'

    # @deprecated: Use L{#LABEL_SMALL} instead.
    LABEL_LIGHT = 'small'

    # Button styles
    #
    #      ********************************************************************

    # Default action style for buttons (the button that should get activated
    # when the user presses 'enter' in a form). Use sparingly, only one default
    # button per view should be visible.
    BUTTON_DEFAULT = 'primary'

    # @deprecated: Use L{#BUTTON_DEFAULT} instead
    BUTTON_PRIMARY = BUTTON_DEFAULT

    # Small sized button, use for context specific actions for example
    BUTTON_SMALL = 'small'

    # TextField styles
    #
    #      ********************************************************************

    # Small sized text field with small font
    TEXTFIELD_SMALL = 'small'

    # Panel styles
    #
    #      ********************************************************************

    # Removes borders and background color from the panel
    PANEL_LIGHT = 'light'

    # SplitPanel styles
    #
    #      ********************************************************************

    # Reduces the split handle to a minimal size (1 pixel)
    SPLITPANEL_SMALL = 'small'

    # TabSheet styles
    #
    #      ********************************************************************

    # Removes borders from the default tab sheet style.
    TABSHEET_BORDERLESS = 'borderless'

    # Removes borders and background color from the tab sheet, and shows the
    # tabs as a small bar.
    TABSHEET_SMALL = 'bar'

    # @deprecated: Use L{#TABSHEET_SMALL} instead.
    TABSHEET_BAR = TABSHEET_SMALL

    # Removes borders and background color from the tab sheet. The tabs are
    # presented with minimal lines indicating the selected tab.
    TABSHEET_MINIMAL = 'minimal'

    # Makes the tab close buttons visible only when the user is hovering over
    # the tab.
    TABSHEET_HOVER_CLOSABLE = 'hover-closable'

    # Makes the tab close buttons visible only when the tab is selected.
    TABSHEET_SELECTED_CLOSABLE = 'selected-closable'

    # Table styles
    #
    #      ********************************************************************

    # Removes borders from the table
    TABLE_BORDERLESS = 'borderless'

    # Makes the table headers dark and more prominent.
    TABLE_STRONG = 'strong'

    # Layout styles
    #
    #      ********************************************************************

    # Changes the background of a layout to white. Applies to
    # L{VerticalLayout}, L{HorizontalLayout}, L{GridLayout},
    # L{FormLayout}, L{CssLayout}, L{VerticalSplitPanel} and
    # L{HorizontalSplitPanel}.
    # <p>
    # <em>Does not revert any contained components back to normal if some
    # parent layout has style L{#LAYOUT_BLACK} applied.</em>
    LAYOUT_WHITE = 'white'

    # Changes the background of a layout to a shade of blue. Applies to
    # L{VerticalLayout}, L{HorizontalLayout}, L{GridLayout},
    # L{FormLayout}, L{CssLayout}, L{VerticalSplitPanel} and
    # L{HorizontalSplitPanel}.
    # <p>
    # <em>Does not revert any contained components back to normal if some
    # parent layout has style L{#LAYOUT_BLACK} applied.</em>
    LAYOUT_BLUE = 'blue'

    # <p>
    # Changes the background of a layout to almost black, and at the same time
    # transforms contained components to their black style correspondents when
    # available. At least texts, buttons, text fields, selects, date fields,
    # tables and a few other component styles should change.
    # </p>
    # <p>
    # Applies to L{VerticalLayout}, L{HorizontalLayout},
    # L{GridLayout}, L{FormLayout} and L{CssLayout}.
    # </p>
    LAYOUT_BLACK = 'black'

    # Window styles
    #
    #      ********************************************************************

    # Makes the whole window white and increases the font size of the title.
    WINDOW_LIGHT = 'light'

    # Makes the whole window black, and changes contained components in the
    # same way as L{#LAYOUT_BLACK} does.
    WINDOW_BLACK = 'black'
