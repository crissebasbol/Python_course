class Lamp:
    _LAMPS = ["""
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    """, """
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    """]

    # All methods in a classes must to receive "self" that is the own instance
    # __init__ is the constructor of the class
    def __init__(self, status_lamp):
        self._is_turned = status_lamp

    def turn_on(self):
        self._is_turned = True
        self._display_image()

    def turn_off(self):
        self._is_turned = False
        self._display_image()

    def _display_image(self):
        if self._is_turned:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
