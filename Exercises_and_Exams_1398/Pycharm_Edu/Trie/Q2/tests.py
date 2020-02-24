from test_helper import *
from task import *

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    dic = ["am","axe","exam"
    ,"boy","colour","dam","dot","donkey",
    "fox","new","prim","prime","primeval","pry",
       "the","this","theory","van"]
    numpad = [['a','b','c'],['d','e','f'],['g','h'],['i','j','y'],
          ['l','m','n'],['o','p','q'],['r','s'],['t','u'],
          ['v','w','x'],['k','z']]
    keyset = [7,2,1,5,6,3,4,1,8,0,4]

    dic2 = ["am", "ant", "axe", "boy", "colour", "dam", "dot",
            "donkey", "exam", "exact", "fox", "new", "prim",
            "prime", "primeval", "pry", "the", "this", "theory", "van"]
    numpad2 = [['a','b','c'],['d','e','f'],['g','h'],['i','j','y'],
          ['l','m','n'],['o','p','q'],['r','s'],['t','u'],
          ['v','w','x'],['k','z']]
    keyset2 = [2,4,3,0,2]


    tests = [ (dic, numpad, keyset, 2),
          (dic2, numpad2, keyset2, -1)]
    for test in tests:
        test_function(test[-1], main, test[0], test[1], test[2])
