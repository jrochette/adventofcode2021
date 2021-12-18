import math

test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

puzzle_input = [
    "<{[[({([{<[[([()<>]<<><>>)<[[]()]{<>()}>][<(()[])<()<>>>]]<(<(<><>)(())>)[<([]()){<><>}>{{()<>}<{}>}]>>[({",
    "<<({<{{{[(<{([{}{}]{{}[]}){({}())}}<<[[][]](()<>)>[{<><>}<{}<>>]>>(<[[()]([]{})]((()<>)[()()",
    "({<<({[<[[<[([()])]<<<{}<>><()[]>>[[()<>]<[]()>]>>([((()[])[()])]{[[()()]<<><>>][{<>[]}(()<>)]})",
    "(([[<<[{(({{{(()<>)[()()]}[({}<>)[[][]]]}([{{}<>}<[]()}]{[[][]][()<>]})})(([({[]{}}{[][]})",
    "({{<[[<<{{[{[<{}{}>{[]{}}]<([]{}){()[]}>}]<{([<><>]([]<>)){({}())({}<>)}}[[<{}<>>([]{})][[()[]]]]>}}>>]]",
    "[(<<<{([[[<{(<()<>>{<><>})(<[]<>>([][]))}[<[{}[]]>{<[]>(<><>)}]>([{{[]()}{[]()}}([<>[]][{}<>",
    "<[{[{{([<(<{{[{}<>]({}{})}{{<>[]}(()())}}(<<<>{}>(<><>)>(<<>{}>[[]<>]))>)>[{[<[[()<>]{{}<>",
    "{(<<[([<{<<<({()()}(<><>)}{((){})([]())}>>[<{<[]<>>{[]{}}}([()()])>]>}>]{{([{<{{[]<>}(<>)}<({}(",
    "((<[{(({([<{(<[][]>)[<<>{}><()<>>]}<{<{}{}>}[{()[]}<{}[]>]>>])})<[{[{([{[]()}((){})][<<>()><()()>])>]}][[({{[",
    "[[{([[<<[({[<<[]{}>{[][]}>(<()<>>[{}()])][([{}[]}[<><>]){[{}()]}]}[<<<{}<>>{()<>}>(<{}()>([]()))>{[[<><>][",
    "{{{<[([[{<[<{([]{}>{<>()}}{<(){}><()()>}>[{[[][]](<>())}[{[]<>}[<>[]]]]]{<{{{}[]}{<><>}}[[()()](<",
    "(([{(({[[[[{(<<>[]>((){})){<()<>><[]{}>}}{[{{}()}(()[])]((()){()<>})}]]]<[<<{(()[])<{}[]>}{",
    "{<<([(<([{{(<(()<>)[[][]]>{[[]{}]{(){}}})[{<(){}>[[]<>]}]}}])[[[([[{()()}{<>[]}]{[()]{[][]}}]<[((",
    "[{<<{<([(<[<{<{}[]>{{}[]}}(([]()))>{([(){}]<()[]>)(<[][]>{[]<>})}]>[{<<{<>()}[{}[]]>{(<><>)}>{[<[]<>>{()[]}]<",
    "<{{<{[[{{([({<()>{(){}}}((<>[])(<><>)))[(<[]<>>[()[]])<<()()>{<>{}}>]])<[{[{[]<>}{()()}][[{}{}]<[]>]}<{{{",
    "[(<[{([{({<<[<<>()>[[]()]]{<<>{}><{}<>>}><{<()()>{{}{}}}(({}<>)<()<>>)>>})({(([<{}<>>{[][]",
    "{(([{[<{{[({{[{}<>][()]}<{{}<>}>}(({<>[]})))]{((<[<>{}][<>[])>[[<>()]{[][]}]))<<<({}<>){{}<>}>(",
    "{[<{({((([[{[(<>{}){<>()}][([]{}}]}]{[<(()()){[]()}>((<>[])<(){}>)]}]){<(<<{{}<>}>>)([[{<><>}<",
    "{<{[(<{<[({<<[<><>]{()()}>[{()<>}<{}>]>[[<[]>][{()[]}{()}]]}(<(({}()){<><>})<(()())[<>()]>>{",
    "<[({[[{<([[{<{{}}>(<<><>>{[]()}}}[{{<>{}}<()<>>}{[[][]]{[]<>}}]]<((([][])<<>{}>)<((){})[{}()",
    "{{[{<[{<<{<<(<{}[]><(){}>)<{<>[]}[{}()]>>[{{[]<>}<()<>>}[{{}<>}(<>())]]><[(({}<>)({}<>))<<{}<>><<",
    "{<<({(<[(<[[{{[][]}{{}}}<[[]()]<<>())>]](<{{{}<>}{()<>}}>)>)]<(({{[[[][]]]}<[[(){}]<[]{}>]>}))>",
    "({{([<<{[(<<{{<>()}<[]()>}<{(){}}{{}{}}>><(<{}[]>{<>{}})<([]<>)([]())>>>)]}>>[[{<{[<<(<>{})",
    "<{({{({<<[{<<{<>}{{}[]}>>[[{[]<>}{()()}]<<[][]>(()())>]}]{<<{[(){}><<><>>}{{<>[]}(()<>)}>[<<(){}>[[]",
    "<({<([[[([({<{(){}}([][])>}<[{[][]}{<>()}]<[(){}][{}<>]>>){<({{}()}{[]{}})>{[{[]{})[()[]]]<[",
    "{([({[(([<{((({}()){{}<>})(<()[]>{()()})){[({}{})<<>[]>]([{}][()])}}>]{<<[<[[][]]{[][]}>({[]{}}<{}()>)",
    "<<{[<({[(<[({<{}{}><()()>})]{<<[<><>]>>}>){{[((<<><>><{}[]>)){<{[]()}(<>())>}]{{{({}<>){[]<>}}{{",
    "<<({<[{(([{({({}())(<>{})}{((){})})[<[[][]]([][])>]}<<[[<>{}][[]<>]]<([]<>)[()()]>><<<{}[]>(()())>>]])[[[",
    "[{<({<(({([([{[]}]<{[]()}[()<>]>]{{(()())<{}()>}{{[]()}<()<>>}}][{(<[]<>>[<>{}])[<[]<>><<><>>]}<(<<",
    "<{{((<<(<{({<{<>{}}[[]{}]>})[[{{[][]}{{}<>}}]]}[(([(()[])<()<>>]((<>[])<<>{}>))<[[<>()][<>",
    "{[([<<<({[{<<[<>{}]<[]<>>>>({<<>{}>((){})}<{[][]}{[]{}}>)}<{(([]{})<<>>><{{}()}(<><>)>}<{<[]",
    "<({[[{{{([(({[{}<>]{[]<>}}[{()<>}<(){}>])<[<{}()>[[]<>]]>)]{{[<{<>()}[{}()]><<<><>>{[][]}>]([[[][]](<>())",
    "[<<{{<[[{[<(<{()[]}[(){}]><[()[]]<<>{}>>)>[[[[[]{}]{[][]}]{<[]{}><(){}>}]({{<>()}<<>{}>}({()<>",
    "[<[[(<[[[[<<<{()<>}[[]()]>>{[[<>[]]{[]{}}]{[<>[]][[]<>]}}>]]({[({[<><>]<{}<>>}<<(){}>[{}()]>)[[<<>",
    "<{{({<([{({({{{}()}((){})})([([][])[[]<>]](([])[{}<>]))}<(([()<>][()[]])[<[]><{}{}>])<{({}<>)<<>()>}",
    "{<[[[([{[<<(({{}<>})(<{}()](<>{}))){[[<>[]]({}<>)]}><[((<>()){[][]})[({}())<{}<>>]]<({<>[]}{{}<>",
    "{<[<[({<({(<(({}[])<{}>)((<>[])({}<>))><(([][])(()()))>)})({{({{<>())}<{<>()}([]{})>)[[(()<>)<<>[]>](<<",
    "{(<(<<{{({{<{(<>[])[[]]}{(<>{})>>{<(()())[{}{}]>{{[]{}}{{}<>}}}}(<{[{}[]]<(){}>}[[{}{}]{()<>}]>([{<>{}}[<>]]",
    "[{[{{[[[{([<(({}{})<[][]>)<([]{})<<>{}>>>[{[[]{}]([]<>)}{(()())[<>[]]}}]((<([]<>)[()<>]>(<{}()>)){<[<>[]](",
    "{<<<<{(({<<({(()())(<>{})}<([][])[[]()]>)[{{[]()}(<>)}]><{[<<>()>]{<[]()>[[]<>]}}>>}>[(<<<[{()<>}{{}<>",
    "[{[(<[<{<[({[{[]<>}<[][]>]{{<>()}}}[({<>[]}{{}{}}){[[]<>](<><>)}])({({{}<>}<{}<>>)}<[((){})[{",
    "{<[[{[(((<({([[]<>](()<>))}[{{()<>}({}())}(<[]{}>{[]{}})])<<(({})[{}{}])[(<>{})<()>]>>>))<[{{<[{{}<>}[[][]",
    "[[<<([{<{((([<{}{}>(<><>)][({}[])])[[(<>{}){{}<>}](<()[]>[[]()])])[{({()}{{}{}})(({}())([]{}))}({[{}[]]{",
    "<<((<[<(([<{[<{}<>>][<{}{}>{{}[]}]}[{<<>()>[[]{}]}{[()[]]([]{})}]><{({()()}{[]})<{[]()}[{}{}]>}{((<>(",
    "({<<{[(({{<<{[[]()]{{}()}}{[<>{}]<[][]>}>{(([]())[<>[]]){<[]{}>{<><>}}}>{{{{<>[]}{{}()]}{{<>{}}[{}{}",
    "{((<<{<<<((<(({}{})(()))[[()()]{{}<>}]>{(<()[]][{}[]])[[<>[]]<<>>]}))>([[{({()[]}{()[]})(<[][]><{}{}>)}[[[[][",
    "[(<<{<[(<([<(<[]()><()()>)>]{({[<><>]{[][]}})}}<[([(()())[{}]]<<(){}>[<><>]>)][<<((){})>>[[{<><>}[{}()]][([]",
    "[<{[<[[(({{{[<{}[]><<>{}}][[{}<>]<<>()>]}{[{[]}[{}[]]]{[()[]]<{}<>>}}}[({<(){}>{{}{}}}<(()[])(",
    "<{([{(<[<<<<[[{}{}]([])](<{}{}>[[][]])>{{(()[]){<>[]}}<[<><>][(){}]>}>(([[{}{}]{{}<>}](<()()>))<<(<>{})<<",
    "[(<[[[[(({[<<<<>{}><<><>>>>]<{[{{}<>}<()>]{{[]{}}[<>[]]}}<<<()[]>([]<>)><(<>{}){[]()}>>>}))[[([{<",
    "[([(({<{([<[({{}{}}<{}{}>)[[[]{}]({}<>)]]<[([]<>)({}[])]{(()[]){[]<>}}>>{[<{[]<>}>{[()[]]<()<>>}][<([",
    "{<[<[[<[{({{<[[]()][{}()]>({()[]}(()[]))}([[<>()]])})}{{<{{[<>]<[]()>}{<{}[]]}}<{{()[]}<[]<>>}([()()]<{}()>)>",
    "[{{(<(([([((<{{}{}}({}())>{{<>[]}<[]{}>})([{<>()}{{}<>}]{<()<>>[{}{}]})>]{{[<(<>){[]{}}>{<<>[]>[()[]]}]",
    "[<<(({[[({({[{[]{}}<<>[]]]{[()()]<<>()>}}{[{<>[]}<()>]}){{<<()[]>{[]{}}><<<>>[[]()]>}}})<[{{[<",
    "<([{{{(<{{{<<({}()){(){})>{<{}{}>{<>()}}>{(<()[]>({}()))<({}())<()()>>}}[(({[]{}}[<>{}])([{}<>])){{{{}}(<",
    "<<{[{[[<([[<(<{}<>><()[]>)<{<>()>[<>()]>>]][{{{{()<>}<{}[]>}[<[]()>[()[]]]}<{[{}](<>{})}>}[<[[<><>]<",
    "[{[([{<<[([[{<<>[]>(<>())}((()())({}{}))>{[({}())<<>()>]<(<><>){()<>}>}]({([(){}]<[]<>>){<[",
    "[{<<[[<((({[<[[]()]>(<<>>(<>{}))]<<([]<>)[<>{}]>{<[][]>(<>())}>}(([{{}<>}{{}[]}]{[()[]]{{}{}}})<",
    "([<<{[([[<{<{({}())}{(()<>)}>[<[{}<>][[]()]><[<>{}]({}[])>]}<[([<>()]){[()<>]([]{})}][[[{}[]]][",
    "<{[[{({<{(<[[(()[])<<>[]>]<<<>()>{[]<>}>]>{[<(<>()){<>[]}>(([][]))]([<[]<>><{}{}>]([<>{}](()()",
    "{[([{{(([[<{<[{}<>]([]{})>[((){})<()[]>]}[[{{}<>}<[][]>]<{[]<>}([]())>]>{<{{{}<>}{(){}}]{{[]",
    "[{{<[([<{[[({[{}[]][(){}]}<{<>()}<[]{}>>)]<<({()<>}[[]()]){[<>[]]<()()>}>>]{[<<(<>[])<[]<>>",
    "<[{<[<((<({[{[{}[])(<>{})}(({}[])[<>])]})>[[([{((){})<<>>}])[<((()<>)[{}{}])[[(){}]]>{<<{}()>{",
    "({[[[[[[[<((<[<><>][()[]]><(<><>)>))>{{<(<<>[]>{{}})[[[]<>]({}())]><{{()<>>[[]<>]}[<{}{}>{<>{}}]>}[{<(<",
    "([([(<[{<[[{<{<>[]}>{{{}()]<{}()>}}<([{}()]{{}<>})[([][]){{}<>}]>]{<{{[]{}}{{}<>}}<[[]()]>>[[{()[]}{(){}}]{[",
    "{<{([([{<<<<{[<>()]<[]>}[[()<>]<()>]>>(([[<>[]][{}{}]])((([][]){<><>})([[]{}]<()<>})))><{<<[()()]<[]()>",
    "[{({[{[(([([{{{}<>}{()<>}}(([]<>){{}{}})][<{()}{{}{}}>(<<>()>[<>()])])]))<<<({((<>()){[]{}})[{",
    "([([(<(({<(<<<{}[]>){{<><>}[[]{}]}>[{{[][]}<<><>>}])<{<<[]>(()[])>[[{}()]<[]<>>]}{({[]()}[<><>]){{{}[]}[{",
    "{{[{<{((<((<<<(){}>>{([]{})[[]()]}>([({}{})]{<()>{[]{}}}))[[(<<><>>)]<<<{}{}><(){}>>[({}[])({}",
    "<{[({{<<((([[[(){}][{}<>]]<(<>[])<[]()>>]<[[{}()]({}())]>)({<[(){}]>{(<><>){[]{}}}})){{{<<[]()>[()<>]>[<",
    "(<[[(<((<[[<{[[]()][()<>]}<[[][]]<[][]>>>((({}())((){}))(<{}<>]{()()}))]]>[[{<{[{}<>]}>([[{}<>](()",
    "<<<{<(<[<{[[([<>()][()<>])(<<>()>[{}()])][<{<>()}>]]}<<<({<>[]}([]{}))<<(){}>>>[[({}())(())]]>{({({}[",
    "([<<<{<{({<[{(()<>)<()()>}]<[({}<>)]>>{[[{<>{}}(()[])](<<>>[[]<>])]}}{<<{<<>()>}><{{<>()}<<><>>}{<(){}>[(){",
    "{{(<<[{{({({({[]()}<{}()>)(([][])[()<>])}<{(<>())[()<>]}>)[[(([]<>)[[]<>])]]}[({[({}()){{}>]})",
    "<((((<{{{{{[{[(){}]([][])}[{<>{}}([]<>)]]([((){})]<[[][]][<><>]>)}}<(<{(()<>)([]{})}><([()<>]{<>()",
    "<{<{<(<(<<<(<[[][]]<<>()>><[<>[]][[]]>)[<[<>{}][<>()]>]>{<{(()){{}()}}[<{}<>><<><>>]>[{<{}[]><<><>>}]}>{(",
    "{[{<<(<([({{<<[]<>>[<>{}]>{<{}<>>([]<>)}}([<<>{}>((){})}<{<>[]}>)}<<({{}()})<(<>[])[[]]>>[[<<>[]>{()[]}][[[]",
    "<<<<[<{<[{{(<[<>]<[]{}>><(<>{}){{}()}>)[[{<>{}}{{}[]}](<[]>[<>{}])]}{{[{{}[]}(()<>)]<([]())(",
    "[([({[[{<{{<<{()()}<{}{}>>({{}{}}[{}{}]>>[{(<>{})<()()>}[[<>[]]<{}()>]]}[<<{<><>}(()[])>(<{}[]>",
    "[<<[[(({<[[([(<>[]){()[]}][(<><>)[<>[]]])]<({<{}{}>(()[])}[<{}<>>({}())])((({}{})<{}[]>)[{{}<>}{{}{}}])",
    "(({({[<<[<[([<<><>){[]{}}][<()<>><[]<>>])({[{}<>]<[]<>>}<({}{})[{}[]]>)][{((<><>)(()[]))}[<<{}()>{<>",
    "<((<[(<(<[[([{(){}}<<>()>]({(){}}{(){}}))]][{{[{[][]]{<>{}}]{[{}<>]([]{})}}}[<{[[]{}][<>()]}[(()[])<",
    "{((<<{({<[([(([]())([]()))(<[][]>{()})])<<[<<>[]>[<>())](<()<>><()()>)>>]>{{[{<[<>{}]<[]<>>>}<{{<><>}<",
    "{<<<<[((<{({<{<>[]}{<>()}><{<><>){<>()}>}([[[]()][(){}]]<<()<>>{<><>}>)){[{{<>[]}{[]()}}{(<>())",
    "({<<<<[{<{<{(<{}{}><()[]>)[{<>{}}]}>(<[([]{}){<><>}]{<<><>>[()[]]}}<[{()[]}{()[]}][{{}[]}{[][]}]>)}>}]",
    "({({{<{{{[<{{(<><>)}({[]()}{<><>})}{<[{}[]]<[]<>>>[(<>[]){()()}]}><[[<<>()><[][]>]]>]<<[{[[]()](",
    "<{[<([<[({([{(<>{}){()}}<([]<>)[{}{}]>)[[<()[]><{}<>>][(<>{})[()()]]]){<{({}){{}{}}}<{<>()}[[",
    "{((({[{<{[<({[{}()]({}{})}<(<>)(()())>)({[[]{}](<><>)}[<<>[]>[<>[]]])><<[{[]<>}][([][])<[]()>]>(",
    "({[((([<[(<{[(<>[])(()[])]}<[([][])([]<>)]<(()())>>>((([(){}])<(<>())<<><>>>)<[[()<>>{{}{}",
    "[{{((<{[(<{[{{[][]}{<><>}}[[()[]]<[][]>]]<<({}[])((){})>>}>[(<([[]()]<{}[]>)([{}<>])>({<<>[]>(<>[])}[(",
    "((<((<[<(<[{(<[]()>[()[]])((())(()[]))}{[[{}<>]([]{})]<[[]()]>}]>)><([<[<{[]<>}<{}[]>>[[(){}]]]({[[][]]{",
    "[(([([(([<<(<{<>}{[][]}>)[{[()<>]{{}{}}}({{}{}}<[]()>)]>>{([({<><>}<[]>){<{}{}>[()<>]}]<<[[]{}]{{",
    "[(<{<[[{[<<{<[[]<>]<[]()>>{{[]<>}}}><[[{{}()}([]<>)]][({{}<>}{{}{}})<[[][]](()())>]>><<({([]{})<<>{}>}){",
    "<{[<[(<<[[[[{<{}[]><[]<>>](<{}[]>{()[]})](<[<>()][[][]]>([()()]<<>()>))]]({([<()[]>[{}()]])<{[[]()]}{<[][",
    "<{{{([[([{{{<({}[])>}}<<({<>{}}{{}()))<({}{}){[]{}}>>[[(<>())[{}[]]]<<[]{}>{<>[]}>]>}([{[<<",
    "[{<(({{<[{[[([<>{}]{<>{}})(((){})[{}[]])][{<{}<>>}[([]{})<{}>]]]}{<<([<>{}][()[]})[{{}}<{}()>]>(",
    "[((<[{<<[<[{[{{}()}[{}[]]]<[<>[]][{}<>]>}]>]{[([([[]<>]{{}[]})[<(){}>[()[]]]]<<({}[])<[]()>>[(",
    "[{([<{([(({(<[[]<>]>{({}()){<><>}})([([]())[[]<>]])}(<[({}())(<>())]<{()<>}[[]<>]>>)){{([[<><>][()[]>](<[][]>",
    "<<(<<<{{{<<(<<[]<>>{<>()}>[<[]>])<{<{}<>>}{[{}{}]<<>[]>}>><{<<<>{}>({}<>)>}{([()[]]<<>()>)(<<><>><[]{}>)}>><",
    "{[<<[{{(<<[((({}{})[{}{}])(({}<>)[{}()]))]>{([[[(){}]<{}<>>][[{}[]]{()[]}]](<{[]{}}(<>[]>>))}>)}[(<",
    "<{{[[<[[[(((({<><>}{{}{}})<[<>()]([]())>)[<{{}<>}>{((){})[[][]]}]))<{<{[[]()]<[][]>}{<[]<>>(<>",
    "{<[<<([[[[{{<({}<>)<{}()>>[(<>())({}[])]}<{([][])({}<>)}>}(({[<>{}]{[]{}}}<(<>{})>)[<{[][]}{[][]}>{({}()){",
    "[[({{[(((({<{{<><>]}{(<><>){<><>}}>(<[()<>]<{}{}>>((<><>){<>[]}))}{<[[{}[]]([][])][{{}[]}[",
    "[{{<([((<<{(((<><>)<(){}>))((({}[]){<>()})(<{}()}({}{})))}><[<<{<>[]}[()<>]>{[<>{}]{[]()}}>{{",
    "[<{<{{({{<<<{[<><>]<[][]>}<<(){}>(<>)>>>([<{[]()}{{}[]}>{<{}()><[]<>>}]([([]())[[]]]([[]()]<<>{}>)))>",
    "<[{<[(<{{([[<[{}{}]><([]<>)(()())>][<((){})[[]()]>[([]<>){<><>}]]]{<{<[]<>><<>>}{<{}<>><[]{}",
    "{[((((((({([([(){}]([]<>)){[{}](<>[])}]{[<<>()>([]<>)]<<[][]>{[]<>}>})<<[{{}[]}(<><>)]<[()<>]",
    "([({(([[[([[((<>{}){{}{}}]{[()<>]((){})}]((({})(<>[])){[{}{}]<<>()>})]{({(())[<>{}]}((<>{})",
    "{<[<{(<[{<[{(<{}()>)[<<>[]>(()<>)]}([{()[]}<{}<>>])}(({<[]{}><{}{}>}([[]<>]{{}()})){[[{}<>]",
    "<<({[[<<[([(<[<><>]{<>{}}>{<(){}>(()())})<{[<>{}]<()[]>}>]<{[{<>{}}<<>()>]<{{}()}[()<>]>}<[[{}<>][{",
]

ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

AUTOCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

CHAR_MAPPING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def calculate_syntax_error_score(chars_in_error: list) -> int:
    total = 0
    for char_in_error in chars_in_error:
        total += ERROR_SCORES[char_in_error]
    return total


# part 1
corrupted_lines_illegal_char = []

for line in list(puzzle_input):
    char_stack = []
    for character in line:
        if character in ["[", "(", "{", "<"]:
            char_stack.append(character)
        else:
            popped_char = char_stack.pop()
            if (
                (character == "]" and popped_char != "[")
                or (character == ")" and popped_char != "(")
                or (character == "}" and popped_char != "{")
                or (character == ">" and popped_char != "<")
            ):
                # part 1 - keep corrupted char
                print(f"Line '{line}' is corruped. Keeping '{character}'.")
                corrupted_lines_illegal_char.append(character)
                #
                # part 2 - remove corrupted line
                puzzle_input.remove(line)
                break

print(
    f"Total syntax error score: {calculate_syntax_error_score(corrupted_lines_illegal_char)}"
)

# part 2
completions = []
for line in list(puzzle_input):
    char_stack = []
    for character in line:
        if character in ["[", "(", "{", "<"]:
            char_stack.append(character)
        else:
            popped_char = char_stack.pop()
    completion = []
    while len(char_stack) != 0:
        completion.append(CHAR_MAPPING[char_stack.pop()])
    completions.append(completion)


autocomplete_scores = []
for completion in completions:
    total = 0
    for character in completion:
        total = (total * 5) + AUTOCOMPLETE_SCORES[character]
    autocomplete_scores.append(total)

autocomplete_scores.sort()

print(
    f"Middle autocomplete score: {autocomplete_scores[math.floor(len(autocomplete_scores)/2)]}"
)