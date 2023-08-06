======
pymodd
======

|Build| |Version| |License|

pymodd is a python package used for creating modd.io games in python

.. |Build| image:: https://img.shields.io/github/actions/workflow/status/jeff5343/pymodd/CI.yml?label=CI&logo=github&style=plastic
   :alt: GitHub Workflow Status
.. |Version| image:: https://img.shields.io/pypi/v/pymodd?style=plastic
   :alt: PyPI
.. |License| image:: https://img.shields.io/pypi/l/pymodd?style=plastic
   :alt: PyPI - License

Features
--------

- edit global and entity scripts
- organize folders and scripts with a mapping file
- a command to generate and compile a pymodd project

Installing
----------

**Python 3.8 or higher is required**

To install the library run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U pymodd

    # Windows
    py -3 -m pip install -U pymodd


Getting Started
---------------

Export your modd game json file from the website and then generate a pymodd project by running the following command:

.. code:: sh

    pymodd generate-project [GAME_JSON_FILE_PATH]


Quick Script Example
--------------------

view the ``examples/froge directory`` for a generated pymodd project

.. code:: py

    @script(triggers=[Trigger.EVERY_SECOND])
    class EverySecond():
        def _build(self):
            self.actions = [
                if_else((NumberOfUnitsOfUnitType(UnitTypes.FROG) < 5), [
                    create_unit_for_player_at_position_with_rotation(UnitTypes.FROG, Variables.AI, RandomPositionInRegion(EntireMapRegion()), 0),
                ], [
                    if_else((NumberOfUnitsOfUnitType(UnitTypes.FROG_BOSS) == 0), [
                        if_else((Variables.BOSS_TIMER <= 0), [
                            create_unit_for_player_at_position_with_rotation(UnitTypes.FROG_BOSS, Variables.AI, RandomPositionInRegion(EntireMapRegion()), 0),
                            update_ui_target_for_player_for_miliseconds(UiTarget.CENTER, 'BOSS SPAWNED', Undefined(), 5000),
                            set_variable(Variables.BOSS_TIMER, 200),
                        ], [
                        ]),
                        decrease_variable_by_number(Variables.BOSS_TIMER, 1),
                    ], [
                    ]),
                ]),
            ]