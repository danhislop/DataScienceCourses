
import unittest
from submission import Graph, TMDBAPIUtils

response_anya = {'cast': [{'adult': False, 'backdrop_path': '/dEY6lCgiODGMDPY3Oo2j09ngPiq.jpg', 'genre_ids': [27, 18, 9648, 36], 'id': 310131, 'original_language': 'en', 'original_title': 'The Witch', 'overview': 'In 1630s New England, William and Katherine lead a devout Christian life with five children, homesteading on the edge of an impassable wilderness, exiled from their settlement when William defies the local church. When their newborn son vanishes and crops mysteriously fail, the family turns on one another.', 'poster_path': '/xMuUdeFX5RVlwQ1WTON1cqSSmIR.jpg', 'release_date': '2015-01-27', 'title': 'The Witch', 'video': False, 'vote_average': 6.8, 'vote_count': 4940, 'popularity': 39.571, 'character': 'Thomasin', 'credit_id': '54899944c3a3686f4e00171c', 'order': 0}, {'adult': False, 'backdrop_path': None, 'genre_ids': [18, 10749], 'id': 447900, 'original_language': 'en', 'original_title': 'The Sea Change', 'overview': 'The rocky marriage of famous London playwright and his wife takes an unexpected turn when they travel to a remote Greek island.', 'poster_path': '/ufYdWcV1IWzyGCBlkFSIJg0VQkd.jpg', 'release_date': '', 'title': 'The Sea Change', 'video': False, 'vote_average': 0.0, 'vote_count': 0, 'popularity': 0.6, 'character': 'Alberta', 'credit_id': '59c3fc4e9251415b6e018c03', 'order': 0}, {'id': 535471, 'video': False, 'vote_average': 0.0, 'overview': 'Weetzie is an ethereal pixie living in 1980s Los Angeles, where she grew up the child of an alcoholic starlet mother and a junkie screenwriter father. She teams up with her Mohawked best friend Dirk to find love, leading her to mysterious trenchcoat-wearing filmmaker Max and platinum-haired surfer Duck. But when their bliss is threatened by deaths, breakups and Max’s witchy and bitter ex-girlfriend Vixanne, Weetzie must take off her pink harlequin sunglasses in order to confront life’s darkness and find happiness in a city known as much for the glamour of fame and fortune as the darkness of cults and crime.', 'vote_count': 0, 'adult': False, 'backdrop_path': None, 'title': 'Weetzie Bat', 'genre_ids': [], 'poster_path': '/p2g7car9c48sSaA5eNFL9cHpWRo.jpg', 'original_language': 'en', 'original_title': 'Weetzie Bat', 'popularity': 0.96, 'character': 'Weetzie Bat', 'credit_id': '5b47f74a0e0a267ae500f09c', 'order': 0}, {'adult': False, 'backdrop_path': '/axmxVeX5R1FfN7w4LNFehskDxW1.jpg', 'genre_ids': [10751, 16, 35, 12], 'original_language': 'en', 'original_title': 'Playmobil: The Movie', 'poster_path': '/zPQzLZnfVw9fbXyxxglyOsmQBlu.jpg', 'vote_count': 190, 'video': False, 'vote_average': 5.7, 'title': 'Playmobil: The Movie', 'overview': 'Marla is forced to abandon her carefully structured life to embark on an epic journey to find her younger brother Charlie who has disappeared into the vast and wondrous animated world of Playmobil toys.', 'release_date': '2019-06-10', 'id': 366668, 'popularity': 11.26, 'character': 'Marla (voice)', 'credit_id': '5bc41f6f0e0a266e640599f6', 'order': 0}, {'original_language': 'en', 'original_title': 'Emma.', 'poster_path': '/uHpHzbHLSsVmAuuGuQSpyVDZmDc.jpg', 'title': 'Emma.', 'vote_average': 7.1, 'overview': 'In 1800s England, a well-meaning but selfish young woman meddles in the love lives of her friends.', 'id': 556678, 'vote_count': 981, 'adult': False, 'backdrop_path': '/5GbkL9DDRzq3A21nR7Gkv6cFGjq.jpg', 'video': False, 'genre_ids': [35, 18, 10749], 'release_date': '2020-02-13', 'popularity': 56.392, 'character': 'Emma Woodhouse', 'credit_id': '5bd2867f0e0a2616d8003dc6', 'order': 0}, {'original_language': 'en', 'original_title': "Creating The Queen's Gambit", 'poster_path': '/gKxPyeItCrOscP8On4y5sG3WY9A.jpg', 'title': "Creating The Queen's Gambit", 'video': False, 'vote_average': 7.9, 'overview': 'A fascinating character. Exquisite sets. A wig for every era. The stars, creators and crew reveal how the hit series about a chess prodigy came to life.', 'release_date': '2021-01-10', 'vote_count': 54, 'adult': False, 'backdrop_path': '/4aTonMQCSEgu5PV3n3xRaNMZmG1.jpg', 'id': 784047, 'genre_ids': [99, 10770], 'popularity': 10.551, 'character': 'Herself', 'credit_id': '5ff8b839efea7a003d6d4ff5', 'order': 0}, {'id': 377264, 'vote_average': 5.8, 'overview': "A corporate risk-management consultant must determine whether or not to terminate an artificial being's life that was made in a laboratory environment.", 'release_date': '2016-09-01', 'adult': False, 'backdrop_path': '/oh79Gio9FDZDqzCMqfgaMJq4o9v.jpg', 'vote_count': 1149, 'genre_ids': [27, 878, 53], 'video': False, 'original_language': 'en', 'original_title': 'Morgan', 'poster_path': '/v1Qb1I0wVvk8FQaNaat9DHlKFGc.jpg', 'title': 'Morgan', 'popularity': 21.137, 'character': 'Morgan', 'credit_id': '573346989251415468000961', 'order': 1}, {'id': 399366, 'genre_ids': [18, 53, 9648, 27], 'original_language': 'en', 'original_title': 'Marrowbone', 'poster_path': '/ykn2GWDINcbunWPoNVRQtMaybo7.jpg', 'video': False, 'vote_average': 7.2, 'overview': 'A young man and his three younger siblings are plagued by a sinister presence in the sprawling manor in which they live.', 'release_date': '2017-10-27', 'vote_count': 1010, 'title': 'Marrowbone', 'adult': False, 'backdrop_path': '/E3tbYSJyjOAPt1pcypyiEvrsCx.jpg', 'popularity': 16.029, 'character': 'Allie', 'credit_id': '57aa0e1892514111aa001359', 'order': 1}, {'overview': 'Though Kevin has evidenced 23 personalities to his trusted psychiatrist, Dr. Fletcher, there remains one still submerged who is set to materialize and dominate all the others. Compelled to abduct three teenage girls led by the willful, observant Casey, Kevin reaches a war for survival among all of those contained within him — as well as everyone around him — as the walls between his compartments shatter apart.', 'release_date': '2016-11-15', 'id': 381288, 'adult': False, 'backdrop_path': '/9pkZesKMnblFfKxEhQx45YQ2kIe.jpg', 'genre_ids': [27, 53], 'original_language': 'en', 'original_title': 'Split', 'poster_path': '/lli31lYTFpvxVBeFHWoe5PMfW5s.jpg', 'vote_count': 14191, 'video': False, 'vote_average': 7.3, 'title': 'Split', 'popularity': 87.483, 'character': 'Casey Cooke', 'credit_id': '57995cb092514124c70040e9', 'order': 1}, {'id': 397717, 'adult': False, 'backdrop_path': '/4hfR16UNtwVILhUCl1UPNg71VWC.jpg', 'genre_ids': [18], 'original_language': 'en', 'original_title': 'Barry', 'poster_path': '/1Dg6phOePOHc4DHA5I7qjXB3fvA.jpg', 'vote_count': 147, 'title': 'Barry', 'vote_average': 5.8, 'video': False, 'overview': 'A biopic of Barack Obama set during his time as a college student in New York City.', 'release_date': '2016-09-10', 'popularity': 7.096, 'character': 'Charlotte Baughman', 'credit_id': '573977ebc3a3685aa4003d11', 'order': 1}, {'adult': False, 'backdrop_path': '/99Rd26ceIhonpOP5JoqcXYqnkD.jpg', 'genre_ids': [18, 53], 'id': 397722, 'original_language': 'en', 'original_title': 'Thoroughbreds', 'overview': 'Two teenage girls in suburban Connecticut rekindle their unlikely friendship after years of growing apart. In the process, they learn that neither is what she seems to be, and that a murder might solve both of their problems.', 'poster_path': '/pIxZzTfITqBpZxbIGsV01DcoHsT.jpg', 'release_date': '2018-03-09', 'title': 'Thoroughbreds', 'video': False, 'vote_average': 6.4, 'vote_count': 791, 'popularity': 24.22, 'character': 'Lily Reynolds', 'credit_id': '5739820bc3a36813e20012a7', 'order': 1}, {'overview': 'Five young mutants, just discovering their abilities while held in a secret facility against their will, fight to escape their past sins and save themselves.', 'release_date': '2020-08-26', 'adult': False, 'backdrop_path': '/lrNbt21hRirjyTK0SeLA0L4RAVS.jpg', 'vote_count': 2242, 'genre_ids': [27, 878], 'original_language': 'en', 'id': 340102, 'original_title': 'The New Mutants', 'poster_path': '/xZNw9xxtwbEf25NYoz52KdbXHPM.jpg', 'video': False, 'title': 'The New Mutants', 'vote_average': 6.3, 'popularity': 140.981, 'character': 'Illyana Rasputin / Magik', 'credit_id': '58b15ab8c3a368076c009d54', 'order': 1}, {'adult': False, 'backdrop_path': None, 'genre_ids': [], 'id': 465005, 'original_language': 'en', 'original_title': 'Crossmaglen', 'overview': "In the aftermath of The Troubles in Northern Ireland, Conor Hurt confesses his involvement in the IRA to a reporter who is more involved in Conor's past than she realizes.", 'poster_path': '/ktKps3fsme3famrWZy1rYIzox2c.jpg', 'release_date': '2018-07-13', 'title': 'Crossmaglen', 'video': False, 'vote_average': 10.0, 'vote_count': 2, 'popularity': 1.18, 'character': 'Ana', 'credit_id': '595f36eb92514121f007ebd6', 'order': 1}, {'adult': False, 'backdrop_path': '/1W2txFf6PDLdwx7oEeYvlBeyHs2.jpg', 'genre_ids': [36, 18, 10770], 'id': 495036, 'original_language': 'en', 'original_title': 'The Miniaturist', 'overview': 'A woman moves to live with her new husband in 17th century Amsterdam, but soon discovers that not everything is what it seems.', 'poster_path': '/g91RfBcTuMGP1iHfuUjcOMdKoFs.jpg', 'release_date': '2017-12-26', 'title': 'The Miniaturist', 'video': False, 'vote_average': 7.2, 'vote_count': 25, 'popularity': 3.149, 'character': "Petronella 'Nella' Oortman", 'credit_id': '5a455922c3a3685844067a8b', 'order': 1}, {'original_language': 'en', 'original_title': 'Last Night in Soho', 'poster_path': '/5iGVofFc0mCr8aJYsVICm42ThIu.jpg', 'video': False, 'vote_average': 0.0, 'title': 'Last Night in Soho', 'overview': 'A young girl, passionate about fashion design, is mysteriously able to enter the 1960s where she encounters her idol, a dazzling wannabe singer. But 1960s London is not what it seems, and time seems to be falling apart with shady consequences.', 'release_date': '2021-10-21', 'id': 576845, 'backdrop_path': '/sHS563mxKAwwpRSxUEUgYQbtdXy.jpg', 'vote_count': 0, 'genre_ids': [27, 18, 53, 9648], 'adult': False, 'popularity': 13.933, 'character': 'Sandy', 'credit_id': '5c49cae00e0a264962cf1a65', 'order': 1}, {'adult': False, 'backdrop_path': '/50DiNdbL7SaGb29YMvWBsacBlJX.jpg', 'genre_ids': [28, 36, 53], 'id': 639933, 'original_language': 'en', 'original_title': 'The Northman', 'overview': 'From acclaimed director Robert Eggers, The Northman is an epic revenge thriller that explores how far a Viking prince will go to seek justice for his murdered father.', 'poster_path': '/9HSQrStWNcJe1IT9XxC6Lbfx2FQ.jpg', 'release_date': '2022-04-07', 'title': 'The Northman', 'video': False, 'vote_average': 0.0, 'vote_count': 0, 'popularity': 5.211, 'character': '', 'credit_id': '5e53ef55a93d2500134d18c1', 'order': 1}, {'original_language': 'en', 'original_title': 'Laughter in the Dark', 'poster_path': '/jApR0JFHNGhVV9xdZL1zOn72uXt.jpg', 'video': False, 'vote_average': 0.0, 'overview': 'A young theater usherette and her former lover devise a scheme to emotionally and financially destroy a wealthy art dealer.', 'release_date': '', 'id': 774151, 'adult': False, 'backdrop_path': None, 'vote_count': 0, 'genre_ids': [53, 18], 'title': 'Laughter in the Dark', 'popularity': 0.6, 'character': 'Margot Peters', 'credit_id': '5fd033c2f90b19003d8bcab7', 'order': 1}, {'original_language': 'en', 'original_title': 'Mad Max: Furiosa', 'poster_path': '/43YodvrEgU1iSRlzQmoXidsqUXp.jpg', 'title': 'Mad Max: Furiosa', 'vote_average': 0.0, 'overview': 'The origin story of renegade warrior Furiosa before she teamed up with Mad Max in ‘Mad Max: Fury Road’.', 'release_date': '2023-06-21', 'vote_count': 0, 'adult': False, 'backdrop_path': '/92owg8k8WfmKDq8O3Jfy2lchbAx.jpg', 'video': False, 'genre_ids': [28, 12], 'id': 786892, 'popularity': 4.428, 'character': 'Furiosa', 'credit_id': '60089d23e04d8a003fc1a908', 'order': 1}, {'adult': False, 'backdrop_path': None, 'genre_ids': [27, 53, 35], 'id': 593643, 'original_language': 'en', 'original_title': 'The Menu', 'overview': 'Set in the world of eccentric culinary culture, centering on a young couple who visit an exclusive restaurant on a remote island where an acclaimed chef has prepared a lavish tasting menu.', 'poster_path': '/ml5w2EqxH1WrIvF3L5jaDI9dUEE.jpg', 'release_date': '', 'title': 'The Menu', 'video': False, 'vote_average': 0.0, 'vote_count': 0, 'popularity': 0.638, 'character': '', 'credit_id': '60be6397f5c8240027fbfa1d', 'order': 1}, {'adult': False, 'backdrop_path': None, 'genre_ids': [14, 27, 9648], 'id': 426063, 'original_language': 'en', 'original_title': 'Nosferatu', 'overview': 'A loose reimagining of F. W. Murnau\'s 1922 classic (itself a loose adaptation of Bram Stoker\'s "Dracula"). This version will be set in the 1830s Biedermeier era in Baltic Germany and will be rooted in period-authentic vampire folklore.', 'poster_path': '/hNYRjXjNqnBIJnkMiAx4yEQQYns.jpg', 'release_date': '', 'title': 'Nosferatu', 'video': False, 'vote_average': 0.0, 'vote_count': 0, 'popularity': 1.42, 'character': '', 'credit_id': '612513945346610028cbd4cd', 'order': 1}, {'id': 540248, 'vote_average': 6.6, 'overview': 'Dublin teenagers Matthew, nihilistic Rez, and the deranged Kearney, leave school to a social vacuum of drinking and drugs, falling into shocking acts of transgression.', 'release_date': '2021-05-27', 'adult': False, 'backdrop_path': '/mOXKTwovpcLbpEAMguctP1JOcVB.jpg', 'vote_count': 10, 'genre_ids': [18], 'video': False, 'original_language': 'en', 'original_title': 'Here Are the Young Men', 'poster_path': '/c3mjUlMtRaV0jZMCButxI0g4Xkc.jpg', 'title': 'Here Are the Young Men', 'popularity': 4.085, 'character': 'Jen', 'credit_id': '5b649ad40e0a267eeb05e1a4', 'order': 2}, {'release_date': '2019-08-30', 'adult': False, 'backdrop_path': '/igYF4WOpzTYZdHKpPCOjo7w0aIO.jpg', 'id': 627133, 'genre_ids': [99], 'original_language': 'en', 'original_title': 'The Crystal Calls - Making The Dark Crystal: Age of Resistance', 'poster_path': '/drY7NV8NzgRdnFkCb8ettgrlc1d.jpg', 'vote_count': 20, 'video': False, 'vote_average': 7.5, 'title': 'The Crystal Calls - Making The Dark Crystal: Age of Resistance', 'overview': "Go behind the scenes with stars, puppeteers and creators as they bring Jim Henson's magical world of Thra back to life in a sweeping fantasy series.", 'popularity': 12.171, 'character': '', 'credit_id': '5d68e1fbca835459cff6ec52', 'order': 2}, {'genre_ids': [53, 18, 878], 'original_language': 'en', 'original_title': 'Glass', 'poster_path': '/svIDTNUoajS8dLEo7EosxvyAsgJ.jpg', 'video': False, 'vote_average': 6.7, 'vote_count': 6465, 'overview': 'In a series of escalating encounters, former security guard David Dunn uses his supernatural abilities to track Kevin Wendell Crumb, a disturbed man who has twenty-four personalities. Meanwhile, the shadowy presence of Elijah Price emerges as an orchestrator who holds secrets critical to both men.', 'release_date': '2019-01-16', 'id': 450465, 'title': 'Glass', 'adult': False, 'backdrop_path': '/ngBFDOsx13sFXiMweDoL54XYknR.jpg', 'popularity': 99.513, 'character': 'Casey Cooke', 'credit_id': '5900cc2f92514161e800db6b', 'order': 3}, {'adult': False, 'backdrop_path': '/iFFC0ILEzcCGI8fJzixI9lI5n8o.jpg', 'genre_ids': [18, 10749, 36], 'original_language': 'en', 'original_title': 'Radioactive', 'poster_path': '/akHIQu8W3rOgT28r25ggXaKcQIr.jpg', 'video': False, 'vote_average': 6.6, 'vote_count': 502, 'overview': 'The story of Nobel Prize winner Marie Curie and her extraordinary scientific discoveries—through the prism of her marriage to husband Pierre—and the seismic and transformative effects their discovery of radium had on the 20th century.', 'release_date': '2020-03-11', 'title': 'Radioactive', 'id': 480857, 'popularity': 11.481, 'character': 'Irene', 'credit_id': '5a8ea41b0e0a263e74012230', 'order': 3}, {'genre_ids': [99, 18, 53], 'original_language': 'en', 'original_title': "The Making of 'Split'", 'poster_path': '/u5B29EdugGRKgvbUsS5oUsjodfE.jpg', 'video': False, 'vote_average': 8.0, 'overview': "A piece in which Shyamalan discusses his growth as a person and a filmmaker, how the film reflects his growth, casting, script secrecy, characters, the film's style, influences (namely It Follows), locations and set design, and budget.", 'id': 685564, 'vote_count': 2, 'title': "The Making of 'Split'", 'adult': False, 'backdrop_path': None, 'release_date': '2017-04-18', 'popularity': 0.66, 'character': 'Herself', 'credit_id': '5e77cd532f3b1700175250d5', 'order': 3}, {'adult': False, 'backdrop_path': '/ffc8RVgAWdm3qNtJ5Eq9RKck9Ft.jpg', 'genre_ids': [28, 12, 14, 10770, 9648, 53], 'original_language': 'en', 'original_title': 'Viking Quest', 'poster_path': '/grma5z8uPKan8IR4DdtXm1g2BWz.jpg', 'video': False, 'vote_average': 4.4, 'vote_count': 21, 'overview': "Erick, a young Viking warrior, joins forces with a rival clan in order to rescue a kidnapped princess from the great Midgard Serpent. It's a perilous task with a risk far greater than merely their own lives; by rescuing the princess, they might cause Ragnarök - the end of the world.", 'release_date': '2014-10-07', 'title': 'Viking Quest', 'id': 317960, 'popularity': 31.523, 'character': 'Mani', 'credit_id': '54b633c792514166a2001104', 'order': 4}, {'adult': False, 'backdrop_path': None, 'genre_ids': [18], 'id': 664469, 'original_language': 'en', 'original_title': 'Canterbury Glass', 'overview': 'Revolves around a doctor and lawyer who form an unlikely partnership.', 'poster_path': '/dVxb69GQSmfaYfqjH7VWriNwUlW.jpg', 'release_date': '', 'title': 'Canterbury Glass', 'video': False, 'vote_average': 0.0, 'vote_count': 0, 'popularity': 2.008, 'character': '', 'credit_id': '6000e72e326c19003e80414c', 'order': 4}, {'adult': False, 'backdrop_path': '/l1f4jHom8cROv1YgQ8kHc6cgpYU.jpg', 'genre_ids': [35, 10770], 'id': 771301, 'original_language': 'en', 'original_title': 'Cinderella: A Comic Relief Pantomime for Christmas', 'overview': 'Olivia Colman leads a stellar cast of actors, entertainers and comedians in a very special ‘stay-at-home’ adaptation of Cinderella for Comic Relief.', 'poster_path': '/wQioZl3GAYrzuf3PbFAuC9ePPCn.jpg', 'release_date': '2020-12-24', 'title': 'Cinderella: A Comic Relief Pantomime for Christmas', 'video': False, 'vote_average': 7.5, 'vote_count': 2, 'popularity': 2.323, 'character': 'Cinderella', 'credit_id': '5fc8bdcfdcf87500423e29bd', 'order': 7}, {'original_title': 'Love, Antosha', 'poster_path': '/AntNP1sX7qKBT7hSYM4248RKMaL.jpg', 'video': False, 'vote_average': 7.1, 'overview': "From a prolific career in film and television, Anton Yelchin left an indelible legacy as an actor. Through his journals and other writings, his photography, the original music he wrote, and interviews with his family, friends, and colleagues, this film looks not just at Anton's impressive career, but at a broader portrait of the man.", 'release_date': '2019-08-02', 'title': 'Love, Antosha', 'adult': False, 'backdrop_path': '/271s2hYoC5gqkR3E2f9BTYz8Bjv.jpg', 'id': 565276, 'genre_ids': [99], 'vote_count': 28, 'original_language': 'en', 'popularity': 4.949, 'character': 'Self', 'credit_id': '5d42d1a995c0af0016d92191', 'order': 18}, {'id': 203739, 'adult': False, 'backdrop_path': '/7Ijb0PDkuL3GK2IHLLIs9acURM8.jpg', 'genre_ids': [35, 28, 14], 'original_language': 'en', 'original_title': 'Vampire Academy', 'poster_path': '/cJZpKgiFfjDZ6L5aOJvbmDhsGqY.jpg', 'title': 'Vampire Academy', 'vote_average': 6.3, 'vote_count': 1478, 'overview': 'Rose, a rebellious half-vampire/half-human guardian-in-training and her best friend, Lissa -- a mortal, royal vampire Princess - have been on the run when they are captured and returned to St. Vladamirs Academy, the very place where they believe their lives may be in most jeopardy. Rose will sacrifice everything to protect Lissa from those who intend to exploit her from within the Academy walls and the Strigoi (immortal, evil vampires) who hunt her kind from outside its sanctuary.', 'release_date': '2014-02-07', 'video': False, 'popularity': 17.639, 'character': 'Feeder Girl (uncredited)', 'credit_id': '6100da88c3926600456d1f0a', 'order': 30}], 'crew': [{'genre_ids': [99, 18, 53], 'original_language': 'en', 'original_title': "The Making of 'Split'", 'poster_path': '/u5B29EdugGRKgvbUsS5oUsjodfE.jpg', 'video': False, 'vote_average': 8.0, 'overview': "A piece in which Shyamalan discusses his growth as a person and a filmmaker, how the film reflects his growth, casting, script secrecy, characters, the film's style, influences (namely It Follows), locations and set design, and budget.", 'id': 685564, 'vote_count': 2, 'title': "The Making of 'Split'", 'adult': False, 'backdrop_path': None, 'release_date': '2017-04-18', 'popularity': 0.66, 'credit_id': '5f052d9420af770036e6d932', 'department': 'Sound', 'job': 'Assistant Dialogue Editor'}], 'id': 1397778}
response_cast = {'id': 201335, 'cast': [{'adult': False, 'gender': 2, 'id': 1107983, 'known_for_department': 'Acting', 'name': 'Martin Luther King', 'original_name': 'Martin Luther King', 'popularity': 1.661, 'profile_path': '/5AYILU60HVNMWmhDEhFtnJVv31O.jpg', 'cast_id': 2, 'character': 'Himself (archive footage)', 'credit_id': '52fe4ca7c3a368484e1c0de1', 'order': 0}, {'adult': False, 'gender': 2, 'id': 52057, 'known_for_department': 'Acting', 'name': 'Obba Babatundé', 'original_name': 'Obba Babatundé', 'popularity': 3.087, 'profile_path': '/6XKA5ExqC1HUxCCpNNWHIsCLsRM.jpg', 'cast_id': 1, 'character': 'Narrator', 'credit_id': '52fe4ca7c3a368484e1c0ddd', 'order': 1}, {'adult': False, 'gender': 2, 'id': 110380, 'known_for_department': 'Acting', 'name': 'Colin Powell', 'original_name': 'Colin Powell', 'popularity': 1.683, 'profile_path': None, 'cast_id': 3, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0de5', 'order': 2}, {'adult': False, 'gender': 2, 'id': 2975, 'known_for_department': 'Acting', 'name': 'Laurence Fishburne', 'original_name': 'Laurence Fishburne', 'popularity': 9.389, 'profile_path': '/8suOhUmPbfKqDQ17jQ1Gy0mI3P4.jpg', 'cast_id': 4, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0de9', 'order': 3}, {'adult': False, 'gender': 2, 'id': 89289, 'known_for_department': 'Acting', 'name': 'Jesse Jackson', 'original_name': 'Jesse Jackson', 'popularity': 0.6, 'profile_path': '/nVRZPBG8DqvTmSa6M2ptTNZSiTO.jpg', 'cast_id': 5, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0ded', 'order': 4}, {'adult': False, 'gender': 2, 'id': 19742, 'known_for_department': 'Acting', 'name': 'Malcolm X', 'original_name': 'Malcolm X', 'popularity': 2.131, 'profile_path': '/4gwdTBOA66KgCewZjERnGN9bJmf.jpg', 'cast_id': 6, 'character': 'Himself (archive footage)', 'credit_id': '52fe4ca7c3a368484e1c0df1', 'order': 5}, {'adult': False, 'gender': 2, 'id': 13301, 'known_for_department': 'Acting', 'name': 'Quincy Jones', 'original_name': 'Quincy Jones', 'popularity': 1.627, 'profile_path': '/q3MCBA0yKyrLGUm1XL8FJ0axYzA.jpg', 'cast_id': 7, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0df5', 'order': 6}, {'adult': False, 'gender': 2, 'id': 31309, 'known_for_department': 'Acting', 'name': 'Hugh Hefner', 'original_name': 'Hugh Hefner', 'popularity': 1.256, 'profile_path': '/7Qwu5fFUR6X9tJuKJdt2Vt6OBp6.jpg', 'cast_id': 9, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0dfd', 'order': 7}, {'adult': False, 'gender': 2, 'id': 23628, 'known_for_department': 'Acting', 'name': 'Eriq La Salle', 'original_name': 'Eriq La Salle', 'popularity': 5.517, 'profile_path': '/vFNYNLQyIoDtsSp3xQ2x1bs6Oud.jpg', 'cast_id': 11, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0e05', 'order': 8}, {'adult': False, 'gender': 2, 'id': 115768, 'known_for_department': 'Acting', 'name': 'Howard K. Smith', 'original_name': 'Howard K. Smith', 'popularity': 0.608, 'profile_path': None, 'cast_id': 10, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0e01', 'order': 9}, {'adult': False, 'gender': 2, 'id': 334719, 'known_for_department': 'Acting', 'name': 'Mike Douglas', 'original_name': 'Mike Douglas', 'popularity': 1.214, 'profile_path': '/xTs45aLyx4XXdkMDgdVHGp6V3iy.jpg', 'cast_id': 8, 'character': 'Himself', 'credit_id': '52fe4ca7c3a368484e1c0df9', 'order': 10}], 'crew': [{'adult': False, 'gender': 0, 'id': 31303, 'known_for_department': 'Production', 'name': 'Dante J. Pugliese', 'original_name': 'Dante J. Pugliese', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644aec68b6900123c869f', 'department': 'Production', 'job': 'Executive Producer'}, {'adult': False, 'gender': 2, 'id': 389123, 'known_for_department': 'Acting', 'name': 'Steve Stoliar', 'original_name': 'Steve Stoliar', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644b94ca676001a3ddd14', 'department': 'Production', 'job': 'Producer'}, {'adult': False, 'gender': 0, 'id': 1027048, 'known_for_department': 'Sound', 'name': 'Shawn Allen Klaiber', 'original_name': 'Shawn Allen Klaiber', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644df168935001833b99f', 'department': 'Sound', 'job': 'Sound Mixer'}, {'adult': False, 'gender': 0, 'id': 1351572, 'known_for_department': 'Directing', 'name': 'Eduardo Eguia Dibildox', 'original_name': 'Eduardo Eguia Dibildox', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e26449e4ca67600143de1ca', 'department': 'Production', 'job': 'Supervising Producer'}, {'adult': False, 'gender': 0, 'id': 1351573, 'known_for_department': 'Writing', 'name': 'Henry Stephens', 'original_name': 'Henry Stephens', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644871685da0017ddcae3', 'department': 'Writing', 'job': 'Writer'}, {'adult': False, 'gender': 0, 'id': 1351875, 'known_for_department': 'Editing', 'name': 'Kent Hagen', 'original_name': 'Kent Hagen', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e26446d1685da0011ddc98f', 'department': 'Directing', 'job': 'Director'}, {'adult': False, 'gender': 0, 'id': 1351875, 'known_for_department': 'Editing', 'name': 'Kent Hagen', 'original_name': 'Kent Hagen', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644c54ca67600143de241', 'department': 'Editing', 'job': 'Editor'}, {'adult': False, 'gender': 0, 'id': 1863747, 'known_for_department': 'Crew', 'name': 'Jeanette Pugliese', 'original_name': 'Jeanette Pugliese', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e26450ded2ac20010389cb6', 'department': 'Crew', 'job': 'Production Controller'}, {'adult': False, 'gender': 0, 'id': 2225633, 'known_for_department': 'Directing', 'name': 'Anthony Mercaldi', 'original_name': 'Anthony Mercaldi', 'popularity': 1.4, 'profile_path': None, 'credit_id': '5e264519389da100128e337a', 'department': 'Production', 'job': 'Business Affairs Coordinator'}, {'adult': False, 'gender': 0, 'id': 2516060, 'known_for_department': 'Art', 'name': 'Daryl Bailey', 'original_name': 'Daryl Bailey', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644d31685da0017ddcb6e', 'department': 'Art', 'job': 'Art Direction'}, {'adult': False, 'gender': 0, 'id': 2516062, 'known_for_department': 'Production', 'name': 'Kate Grady', 'original_name': 'Kate Grady', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644f2168935001833ba27', 'department': 'Production', 'job': 'Production Coordinator'}, {'adult': False, 'gender': 0, 'id': 2516064, 'known_for_department': 'Crew', 'name': 'Sean Kinnear', 'original_name': 'Sean Kinnear', 'popularity': 0.6, 'profile_path': None, 'credit_id': '5e2644fe168935001833ba6d', 'department': 'Crew', 'job': 'Motion Capture Artist'}]} 
node_simple = [('2975', 'Laurence Fishburne'), ('3333', 'Keanu Reeves'), ('4444', 'Carrie-Anne Moss')]

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_no_nodes(self):
        self.assertEqual([], self.graph.get_nodes() )

    def test_add_node_new(self):
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.assertEqual(self.graph.get_nodes(), [('2975', 'Laurence Fishburne')] )

    def test_add_node_comma(self):
        self.graph.add_node(id='2975', name='comma, name')
        self.assertEqual(self.graph.get_nodes(), [('2975', 'comma name')] )

    def test_add_node_two(self):
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.graph.add_node(id='3333', name='Keanu Reeves')
        self.assertEqual(self.graph.get_nodes(), [('2975', 'Laurence Fishburne'), ('3333', 'Keanu Reeves')])

    def test_add_node_exists(self):
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.assertEqual(self.graph.get_nodes(), [('2975', 'Laurence Fishburne')] )

    def test_count_no_nodes(self):
        self.assertEqual(self.graph.total_nodes(), 0)
 
    def test_count_no_nodes(self):
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.assertEqual(self.graph.total_nodes(), 1)       

    def test_count_no_nodes(self):
        self.graph.add_node(id='2975', name='Laurence Fishburne')
        self.graph.add_node(id='3333', name='Keanu Reeves')
        self.assertEqual(self.graph.total_nodes(), 2)

    def test_edge_exists(self):
        self.graph.add_edge(source='1', target='2')
        self.assertTrue(self.graph.edge_exists('1','2'))

    def test_edge_symmetrical(self):
        self.graph.add_edge(source='1', target='1')
        self.assertTrue(self.graph.edge_exists('1','1'))

    def test_edge_exists_reversed(self):
        self.graph.add_edge(source='1', target='2')
        self.assertTrue(self.graph.edge_exists('2','1'))

    def test_add_edge_new(self):
        self.graph.add_edge(source='2975', target='3333')
        self.assertEqual(self.graph.get_edges(), [('2975', '3333')] )

    def test_add_edge_exists(self):
        self.graph.add_edge(source='2975', target='3333')
        self.graph.add_edge(source='2975', target='3333')
        self.assertEqual(self.graph.get_edges(), [('2975', '3333')] )

    def test_add_edge_exists_reversed(self):
        self.graph.add_edge(source='2975', target='3333')
        self.graph.add_edge(source='3333', target='2975')
        self.assertEqual(self.graph.get_edges(), [('2975', '3333')] )

    def test_add_edge_exists_multiple(self):
        self.graph.add_edge(source='2975', target='3333')
        self.graph.add_edge(source='4444', target='2975')
        self.assertEqual(self.graph.get_edges(), [('2975', '3333'),('4444', '2975')] )

    def test_max_degree_nodes(self):
        self.graph.add_edge(source='2975', target='3333')
        self.graph.add_edge(source='4444', target='2975')
        self.assertEqual(self.graph.max_degree_nodes(), {'2975':2})

    def test_find_highest_degree(self):
        self.assertEqual(self.graph.find_highest_degree({'3333': 1, '4444': 1, '2975': 2}), {'2975': 2})

    def test_find_highest_degree_tie(self):
        self.assertEqual(self.graph.find_highest_degree({'3333': 1, '4444': 1, '2975': 2, '1111':2 }), {'2975': 2, '1111': 2})

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.tmdb_api_utils = TMDBAPIUtils(api_key='fake_key')

    def test_get_filtered_movie_credits_8(self):
        response = self.tmdb_api_utils.get_filtered_movie_credits(response_anya, 8.0)
        self.assertEqual(response, [{'id': 465005, 'title': 'Crossmaglen', 'vote_avg': 10.0}, {'id': 685564, 'title': "The Making of 'Split'", 'vote_avg': 8.0}])

    def test_get_filtered_movie_credits_7(self):
        response = self.tmdb_api_utils.get_filtered_movie_credits(response_anya, 7.0)
        self.assertEqual(len(response), 10)

    def test_get_filtered_movie_credits_none(self):
        response = self.tmdb_api_utils.get_filtered_movie_credits(response_anya)
        self.assertEqual(len(response), 30)

    def test_get_filtered_movie_credits_no_results(self):
        response = self.tmdb_api_utils.get_filtered_movie_credits(response_anya, 11.0)
        self.assertEqual(response, [])

    def test_get_filtered_movie_credits_no_cast(self):
        response = self.tmdb_api_utils.get_filtered_movie_credits({'success':'false'}, 11.0)
        self.assertEqual(response, [])
    
    def test_get_filtered_movie_cast_none(self):
        # Assumes no exclusions and function's default limit of 4
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast)
        self.assertEqual(len(response), 11)

    def test_get_filtered_movie_cast_limit3(self):
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast, 3)
        response_ids = [{'id':item['id']} for item in response] # narrow results to purpose of test; allows flexibility in returned fields for each id
        self.assertEqual(response_ids, [{'id': 1107983},{'id': 52057},{'id': 110380}])

    def test_get_filtered_movie_cast_limit3_exclude1_int(self):
        # Exclusions must be a list of strings. Here, a list of ints is passed, and are not excluded.
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast, 3, [1107983])
        response_ids = [{'id':item['id']} for item in response] # narrow results to purpose of test; allows flexibility in returned fields for each id
        self.assertNotEqual(response_ids, [{'id': 52057},{'id': 110380}])

    def test_get_filtered_movie_cast_limit3_exclude1(self):
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast, 3, ['1107983'])
        response_ids = [{'id':item['id']} for item in response] # narrow results to purpose of test; allows flexibility in returned fields for each id
        self.assertEqual(response_ids, [{'id': 52057},{'id': 110380}])

    def test_get_filtered_movie_cast_limit3_exclude2(self):
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast, 3, ['1107983','110380'])
        self.assertEqual(response, [{'id': 52057, 'character': 'Narrator', 'name': 'Obba Babatundé', 'credit_id': '52fe4ca7c3a368484e1c0ddd'}])

    def test_get_filtered_movie_cast_limitnone_excludelots(self):
        response = self.tmdb_api_utils.get_filtered_movie_cast(response_cast, None, ['1107983','110380', '52057', '2975', '89289','19742','13301','31309','23628','115768'])
        response_ids = [{'id':item['id']} for item in response] # narrow results to purpose of test; allows flexibility in returned fields for each id
        self.assertEqual(response_ids, [{'id': 334719}])
