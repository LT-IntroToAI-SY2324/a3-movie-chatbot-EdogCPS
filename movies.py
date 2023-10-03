# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/movie.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and actors/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

movie_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "interstellar", #title
        "christoher nolan", #director
        2014, # year
        [
            "mathew mcconaughey",
            "jessica chastain",
            "anne hathaway",
            "mackenzie foy",
            "timothee chalamet",
            "matt damon",
            "micheal caine",
            #actors/actresses
        ]
    ),
    (
        "amarcord",  # title
        "federico fellini",  # director
        1974,  # year
        [
            "magali noel",
            "bruno zanin",
            "pupella maggio",
            "armando drancia",
        ],  # actors/actresses
    ),
    (
        "the big easy",
        "jim mcbride",
        1987,
        [
            "dennis quaid",
            "ellen barkin",
            "ned beatty",
            "lisa jane persky",
            "john goodman",
            "charles ludlam",
        ],
    ),
    (
        "boyz n the hood",
        "john singleton",
        1991,
        [
            "cuba gooding jr.",
            "ice cube",
            "larry fishburne",
            "tyra ferrell",
            "morris chestnut",
        ],
    ),
    (
        "dead again",
        "kenneth branagh",
        1991,
        [
            "kenneth branagh",
            "emma thompson",
            "andy garcia",
            "derek jacobi",
            "hanna schygulla",
        ],
    ),
    (
        "the godfather",
        "francis ford coppola",
        1972,
        ["marlon brando", "al pacino", "james caan", "robert duvall", "diane keaton"],
    ),
    (
        "an american in paris",
        "vincente minnelli",
        1952,
        ["gene kelley", "leslie caron", "oscar levant", "nina foch", "george guetary"],
    ),
    (
        "casablanca",
        "michael curtiz",
        1942,
        [
            "humphrey bogart",
            "ingrid bergman",
            "paul henreid",
            "claude rains",
            "sydney greenstreet",
            "peter lorre",
            "s z sakall",
            "conrad veidt",
            "dooley wilson",
        ],
    ),
    (
        "citizen kane",
        "orson welles",
        1941,
        [
            "orson welles",
            "joseph cotten",
            "dorothy comingore",
            "ray collins",
            "george coulouris",
            "agnes moorehead",
            "ruth warrick",
        ],
    ),
    (
        "gone with the wind",
        "victor fleming",
        1939,
        [
            "clark gable",
            "vivien leigh",
            "leslie howard",
            "olivia de havilland",
            "hattie mcdaniel",
            "butterfly mcqueen",
        ],
    ),
    (
        "lawrence of arabia",
        "david lean",
        1962,
        [
            "peter otoole",
            "alec guinness",
            "anthony quinn",
            "jack hawkins",
            "jose ferrer",
            "omar sharif",
            "anthony quayle",
            "claude rains",
            "arthur kennedy",
            "donald wolfit",
        ],
    ),
    (
        "the manchurian candidate",
        "john frankenheimer",
        1962,
        [
            "frank sinatra",
            "laurence harvey",
            "janet leigh",
            "angela lansbury",
            "henry silva",
            "james gregory",
            "leslie parrish",
            "john mcgiver",
            "khigh dhiegh",
            "james edwards",
        ],
    ),
    (
        "metropolis",
        "fritz lang",
        1926,
        [
            "alfred abel",
            "gustay frohlich",
            "brigitte helm",
            "rudolf kleinrogge",
            "heinrich george",
        ],
    ),
    (
        "othello",
        "orson welles",
        1952,
        [
            "orson welles",
            "michael mac liammoir",
            "robert coote",
            "suzanne cloutier",
            "faye compton",
            "doris dowling",
            "michael laurence",
        ],
    ),
    (
        "spartacus",
        "stanley kubrick",
        1960,
        [
            "kirk douglas",
            "laurence olivier",
            "jean simmons",
            "charles laughton",
            "peter ustinov",
            "john gavin",
            "tony curtis",
            "woody strode",
        ],
    ),
    (
        "a star is born",
        "george cuckor",
        1954,
        [
            "judy garland",
            "james mason",
            "jack carson",
            "tommy noonan",
            "charles bickford",
        ],
    ),
    (
        "after the rehearsal",
        "ingmar bergman",
        1984,
        ["erland josephson", "ingrid thulin", "lena olin", "nadja palmstjerna-weiss"],
    ),
    (
        "amadeus",
        "milos forman",
        1984,
        [
            "f murray abraham",
            "tom hulce",
            "elizabeth berridge",
            "simon callow",
            "roy dotrice",
            "christine ebersole",
            "jeffrey jones",
        ],
    ),
    (
        "blood simple",
        "joel coen",
        1985,
        [
            "john getz",
            "frances mcdormand",
            "dan hedaya",
            "m emmet walsh",
            "samm-art williams",
        ],
    ),
    (
        "chinatown",
        "roman polanski",
        1974,
        [
            "jack nicholson",
            "faye dunaway",
            "john huston",
            "perry lopez",
            "john hillerman",
            "darrell zwerling",
            "diane ladd",
            "roman polanski",
        ],
    ),
    (
        "the cotton club",
        "francis ford coppola",
        1984,
        [
            "richard gere",
            "gregory hines",
            "diane lane",
            "lonette mckee",
            "bob hoskins",
            "james remar",
            "fred gwynne",
        ],
    ),
    (
        "the crying game",
        "neil jordan",
        1992,
        [
            "stephen rea",
            "jaye davidson",
            "forest whitaker",
            "miranda richardson",
            "adrian dunbar",
            "breffini mckenna",
            "joe savino",
        ],
    ),
    (
        "the day of the jackal",
        "fred zinnemann",
        1973,
        [
            "edward fox",
            "terence alexander",
            "michel auclair",
            "alan badel",
            "tony britton",
            "denis carey",
            "olga georges-picot",
            "cyril cusack",
        ],
    ),
    (
        "diva",
        "jean-jacques beineix",
        1981,
        [
            "wilhelmenia wiggins fernandez",
            "frederic andrei",
            "richard bohringer",
            "thay an luu",
            "jacques fabbri",
            "chantal deruaz",
        ],
    ),
    (
        "the dresser",
        "peter yates",
        1984,
        ["albert finney", "tom courtenay", "edward fox", "zena walker"],
    ),
    (
        "el norte",
        "gregory nava",
        1983,
        [
            "zaide silvia gutierrez",
            "david villalpando",
            "ernesto gomez cruz",
            "alicia del lago",
            "trinidad silva",
        ],
    ),
    (
        "the exorcist",
        "william friedkin",
        1973,
        [
            "ellen burstyn",
            "linda blair",
            "jason miller",
            "max von sydow",
            "kitty winn",
            "lee j cobb",
        ],
    ),
    (
        "a fish called wanda",
        "michael chrichton",
        1988,
        [
            "john cleese",
            "jamie lee curtis",
            "kevin kline",
            "michael palin",
            "maria aitken",
            "tom georgeson",
            "patricia hayes",
        ],
    ),
    (
        "flirting",
        "john duigan",
        1992,
        [
            "noah taylor",
            "thandie newton",
            "nicole kidman",
            "bartholomew rose",
            "felix nobis",
            "josh picker",
            "kiri paramore",
        ],
    ),
    ("gates of heaven", "errol morris", 1978, []),
    (
        "house of games",
        "david mamet",
        1987,
        [
            "lindsay crouse",
            "joe mantegna",
            "mike nussman",
            "lilia skala",
            "j t walsh",
            "jack wallace",
        ],
    ),
    (
        "iceman",
        "fred schepisi",
        1984,
        ["timothy hutton", "john lone", "lindsay crouse"],
    ),
    (
        "jaws",
        "steven spielberg",
        1975,
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ],
    ),
    (
        "johnny got his gun",
        "dalton trumbo",
        1971,
        [
            "timothy bottoms",
            "kathy fields",
            "jason robards",
            "diane varsi",
            "donald sutherland",
            "eduard franz",
        ],
    ),
    (
        "local hero",
        "bill forsyth",
        1983,
        [
            "burt lancaster",
            "peter reigert",
            "peter capaldi",
            "fulton mckay",
            "denis lawson",
        ],
    ),
    (
        "malcolm x",
        "spike lee",
        1992,
        [
            "denzel washington",
            "angela basset",
            "albert hall",
            "al freeman jr",
            "delroy lindo",
            "spike lee",
        ],
    )
]
