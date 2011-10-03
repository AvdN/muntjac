# -*- coding: utf-8 -*-
from com.vaadin.demo.sampler.features.dates.DatePopupInputPrompt import (DatePopupInputPrompt,)
from com.vaadin.demo.sampler.features.selects.ComboBoxContains import (ComboBoxContains,)
from com.vaadin.demo.sampler.NamedExternalResource import (NamedExternalResource,)
from com.vaadin.demo.sampler.features.selects.ComboBoxStartsWith import (ComboBoxStartsWith,)
from com.vaadin.demo.sampler.features.selects.ComboBoxNewItems import (ComboBoxNewItems,)
from com.vaadin.demo.sampler.APIResource import (APIResource,)
from com.vaadin.demo.sampler.features.text.TextFieldInputPrompt import (TextFieldInputPrompt,)
from com.vaadin.demo.sampler.Feature import (Feature,)
Version = Feature.Version


class ComboBoxInputPrompt(Feature):

    def getSinceVersion(self):
        return Version.OLD

    def getName(self):
        return 'Combobox with input prompt'

    def getDescription(self):
        return 'ComboBox is a drop-down selection component with single item selection.' + ' It can have an <i>input prompt</i> - a textual hint that is shown within' + ' the select when no value is selected.<br/>' + ' You can use an input prompt instead of a caption to save' + ' space, but only do so if the function of the ComboBox is' + ' still clear when a value is selected and the prompt is no' + ' longer visible.'

    def getRelatedAPI(self):
        return [APIResource(ComboBox)]

    def getRelatedFeatures(self):
        return [ComboBoxStartsWith, ComboBoxContains, ComboBoxNewItems, TextFieldInputPrompt, DatePopupInputPrompt]

    def getRelatedResources(self):
        return [NamedExternalResource('UI Patterns, Input Prompt', 'http://ui-patterns.com/pattern/InputPrompt')]