# This module, and all included code, is made available under the terms of
# the MIT Licence
#
# Copyright (c) 2023 Roz Wyatt-Millington, David Love
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Simple (decimal) numeric driver for a seven-segment display, requiring seven
GPIO pins.

Overview
--------

During initialisation the user must supply a list of exactly seven GPIO pins,
using the numeric pin identifier (e.g. 16 for GPIO Pin 16). Each entry in the
list corresponds to the segment 'a' (for the first entry) to 'g' (for the last
entry). Physically, each LED segment is also assumed to be laid out in the
standard pattern, shown below. Once the constructor has been called, no further
changes are possible: and the driver will also assume exclusive use of the
relevant GPIO pins.

````
     - A -
   |       |
   F       B
   | - G - |
   E       C
   |       |
     - D -
````

**Figure 1: Assumed Layout of the Seven Segment Display**

To display a character, the `display` method of the class is used: passing in an
integer in the range 0..9 representing the number to show on the seven segment.
Not that by default the `display` method assumes that GPIO pins must be held
*low* for the segment to display: i.e. the behaviour normally used by common
anode seven-segment displays. If you need the requested GPIO pin to be held
*high* to display a segment, pass in `True` to the `inverted` parameter of the
`display` method.

!!! Note
    This driver will only display characters in the range '0' to '9', and
    will raise a `ValueError` exception if the requested character is not in an
    appropriate range.

Examples
--------

* Examples Folder: `examples/drivers/seven_segment_example.py`
* [WokWi](https://wokwi.com/projects/360451068863047681)

Tested Implementations
----------------------

This version is written for MicroPython 3.4, and has been tested on:

* Raspberry Pi Pico H/W
"""

# Import MicroPython libraries for GPIO access if available
try:
    from machine import Pin
except ImportError:
    print("Ignoring MicroPython includes")

##
## Classes
##


class SegDisplay:
    """Simple (decimal) numeric driver for a seven-segment display, requiring
    seven GPIO pins.

    **Note:** This driver will only display characters in the range '0' to '9',
    and will raise a `ValueError` exception if the requested character is not in
    an appropriate range.
    """

    _char_list = [
        [False, False, False, False, False, False, True],
        [True, False, False, True, True, True, True],
        [False, False, True, False, False, True, False],
        [False, False, False, False, True, True, False],
        [True, False, False, True, True, False, False],
        [False, True, False, False, True, False, False],
        [False, True, False, False, False, False, False],
        [False, False, False, True, True, True, True],
        [False, False, False, False, False, False, False],
        [False, False, False, True, True, False, False],
    ]
    """Defines how characters are rendered, from zero ('0') in the first entry
    to nine ('9') as the last entry.

    Note that pins which are listed here as `False` will be *on* using the
    default options to the `display` method.
    """

    def __init__(self, gpio_request: list) -> None:
        """Initialise a seven-segment display, using the user supplied list of
        GPIO pins in `gpio_request` as reference for pins to drive.

        This class also assume a common anode seven-segment display by default,
        and so will assume that pulling a GPIO pin *low* will turn the relevant
        segment *on*. If you need to modify this behaviour, see the `inverted`
        parameter for the `display` method.

        !!! Note
            This list of entries in the `gpio_request` *must* be **exactly**
            seven entries long, or the class will throw a `ValueError` in the
            constructor.

        Parameters
        ----------

        gpio_request: list
            The pin-ordered list of GPIO pins to use for the segment positions
            'a' (as the first entry in the list) to 'g' (as the last entry in
            the list).

            **Note**: The `SegDisplay` class will also attempt to create the
            underlying GPIO object for each of the entries in the list. If
            the GPIO pins need to be initialised first, this must be done
            *before* calling this constructor.

        Raises
        ------

        ValueError
            The `gpio_request` is empty, or does not have exactly
            seven elements in the list.
        """
        self.pin_list = []

        if (gpio_request is None) or (not gpio_request):
            raise ValueError("The GPIO Request List is empty")
        elif len(gpio_request) != 7:
            raise ValueError("The GPIO Request List must be EXACTLY seven entries long")
        else:
            for segment in range(7):
                self.pin_list.append(Pin(gpio_request[segment], Pin.OUT))

    def display(self, character: int, inverted: bool = False) -> None:
        """Display the given `character` on the seven-segment display, using the
        `_char_list` as a guide for which pins to turn on or off. By default the
        `display` method will use the entries in the `_char_list` directly: if
        you need to invert the 'normal' sense, set the `inverted` parameter to
        `True`.

        Parameters
        ----------

        character: int
            The value to be displayed on the seven segment display, which must be
            between zero ('0') and nine ('9')
        inverted: bool, optional
            By default the `display` method assumes that pulling a GPIO pin *low*
            will turn the relevant segment *on*; i.e. the typical behaviour for a
            common anode display. If the attached display needs to raise a GPIO
            pin *high* to set the segment *on* (i.e. the typical behaviour for a
            common cathode display), call the `display` method with `inverted`
            set to `True`.

        Raises
        ------

        IndexError
            The `character` is not in a range that can be displayed.
        """
        # For a character in the valid range...
        if 0 <= character <= 9:
            if not inverted:
                # ... if the request is to display in the non-inverted form, then
                # select the row in `_char_list` corresponding to the character to
                # be displayed and then set in turn each of the GPIO pins corresponding
                # to the segment values either high or low depending on the column
                # value in `_char_list` for that segment value
                for pin in range(7):
                    self.pin_list[pin].value(self._char_list[character][pin])
            else:
                # ... if the request is to display in the inverted form, then
                # select the row in `_char_list` corresponding to the character to
                # be displayed and then set in turn each of the GPIO pins corresponding
                # to the segment values either high or low depending on the *inverse* of
                # the column value in `_char_list` for that segment value
                for pin in range(7):
                    self.pin_list[pin].value(not self._char_list[character][pin])
        else:
            raise IndexError(
                "The display character must be between zero ('0') and nine ('9')"
            )
