"""
Explain the differences between the attributes name, surname and profession,
and what values they can have in different instances of this class:
"""


class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession

"""
name - attribute that is different per instance. must be provided at init.
surname - member attribute. initially the same for all instances. can be changed by direct access to instance.surname
profession - member attribute. can be changed during initialization, but same default value for all instances.
"""

