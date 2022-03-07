import cmd
import enum

import pynames


class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"

gender_names = frozenset(map(lambda elem: elem.value, Gender))
languages = {'RU', 'EN', 'NATIVE'}


class Race(enum.Enum):
    ELVEN = 'elven'
    GOBLIN = 'goblin'
    IRON_KINGDOMS = 'iron_kingdoms'
    KOREAN = 'korean'
    MONGOLIAN = 'mongolian'
    ORC = 'orc'
    RUSSIAN = 'russian'
    SCANDINAVIAN = 'scandinavian'

race_names = frozenset(map(lambda elem: elem.value, Gender))


class Gen(cmd.Cmd):

    def __init__(self):
        self.language = pynames.LANGUAGE.NATIVE
        super().__init__()

    def do_language(self, command: str):
        self.language = eval(f"pynames.LANGUAGE.{command}")

    def do_generate(self, command: str):
        global gender
        global language

        # gen = None
        gen_name, *args = command.split()
        s = f"import pynames.generators.{gen_name} as gen"
        exec(s, globals())
        module_names = list(filter(lambda x: 'generator' in str(x).lower() and not 'From' in str(x), gen.__dict__))

        gender = Gender.MALE.value
        module_name = None
        if args:
            if args[0] in gender_names:
                gender = args[0]
            else:
                module_name = next(filter(lambda name: args[0].lower() in name.lower(), module_names))
        if not module_name:
            module_name = module_names[0]
        if gender == Gender.MALE.value:
            gender = pynames.relations.GENDER.MALE
        else:
            gender = pynames.relations.GENDER.FEMALE
        # print(module_name)
        language = self.language
        name = eval(f"gen.{module_name}().get_name_simple(gender, language)", globals())
        print(name)

    def do_info(self, command: str):
        global gender
        race, *args = command.split()
        s = f"import pynames.generators.{race} as gen"
        exec(s, globals())
        module_names = list(filter(lambda x: 'generator' in str(x).lower() and not 'From' in str(x), gen.__dict__))
        module_name = module_names[0]
        if not args:
            print(eval(f"gen.{module_name}().get_names_number(pynames.GENDER.MF)", globals()))
            return
        arg = args[0]
        if arg in gender_names:
            if arg == Gender.MALE.value:
                gender = pynames.GENDER.MALE
            else:
                gender = pynames.GENDER.FEMALE
            print(eval(f"gen.{module_name}().get_names_number(gender)", globals()))
            return
        else:
            print(eval(f"' '.join(gen.{module_name}().languages)", globals()))
            return

    def do_exit(self, *_):
        return True


if __name__ == "__main__":
    Gen().cmdloop()
