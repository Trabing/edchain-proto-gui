#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db')
cursor     = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname VARCHAR,
        lastname VARCHAR,
        username VARCHAR,
        password VARCHAR
        );'''
)
cursor.execute(
    '''CREATE TABLE courses(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        course_number VARCHAR,
        course_title VARCHAR,
        course_description VARCHAR
        );'''
)

if __name__ == '__main__':
    cursor.execute(
        '''INSERT INTO users(
            firstname,
            lastname,
            username,
            password
            )
            VALUES(
            "Kenso",
            "Trabing",
            "kensotrabing",
            "opensesame"
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.001",
            "Structure and Interpretation of Computer Programs",
            "This course introduces students to the principles of computation. Upon completion of 6.001, students should be able to explain and apply the basic methods from programming languages to analyze computational systems, and to generate computational solutions to abstract problems. Substantial weekly programming assignments are an integral part of the course. This course is worth 4 Engineering Design Points."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.006",
            "Introduction to Algorithms",
            "This course provides an introduction to mathematical modeling of computational problems. It covers the common algorithms, algorithmic paradigms, and data structures used to solve these problems. The course emphasizes the relationship between algorithms and programming, and introduces basic performance measures and analysis techniques for these problems."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.034 ",
            "Artificial Intelligence",
            "This course introduces students to the basic knowledge representation, problem solving, and learning methods of artificial intelligence. Upon completion of 6.034, students should be able to develop intelligent systems by assembling solutions to concrete computational problems; understand the role of knowledge representation, problem solving, and learning in intelligent-system engineering; and appreciate the role of problem solving, vision, and language in understanding human intelligence from a computational perspective."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.045J",
            "Automata, Computability, and Complexity",
            "This course provides a challenging introduction to some of the central ideas of theoretical computer science. Beginning in antiquity, the course will progress through finite automata, circuits and decision trees, Turing machines and computability, efficient algorithms and reducibility, the P versus NP problem, NP-completeness, the power of randomness, cryptography and one-way functions, computational learning theory, and quantum computing. It examines the classes of problems that can and cannot be solved by various kinds of machines. It tries to explain the key differences between computational models that affect their power."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.050J",
            "Information and Entropy",
            "This course explores the ultimate limits to communication and computation, with an emphasis on the physical nature of information and information processing. Topics include: information and computation, digital signals, codes and compression, applications such as biological representations of information, logic circuits, computer architectures, and algorithmic information, noise, probability, error correction, reversible and irreversible operations, physics of computation, and quantum computation. The concept of entropy applied to channel capacity and to the second law of thermodynamics."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.172",
            "Performance Engineering of Software Systems",
            "Modern computing platforms provide unprecedented amounts of raw computational power. But significant complexity comes along with this power, to the point that making useful computations exploit even a fraction of the potential of the computing platform is a substantial challenge. Indeed, obtaining good performance requires a comprehensive understanding of all layers of the underlying platform, deep insight into the computation at hand, and the ingenuity and creativity required to obtain an effective mapping of the computation onto the machine. The reward for mastering these sophisticated and challenging topics is the ability to make computations that can process large amount of data orders of magnitude more quickly and efficiently and to obtain results that are unavailable with standard practice. This class is a hands-on, project-based introduction to building scalable and high-performance software systems. Topics include performance analysis, algorithmic techniques for high performance, instruction-level optimizations, cache and memory hierarchy optimization, parallel programming, and building scalable distributed systems. The course also includes design reviews with industry mentors, as described in this MIT News article."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.189",
            "Multicore Programming Primer",
            "The course serves as an introductory course in parallel programming. It offers a series of lectures on parallel programming concepts as well as a group project providing hands-on experience with parallel programming. The students will have the unique opportunity to use the cutting-edge PLAYSTATION 3 development platform as they learn how to design and implement exciting applications for multicore architectures. At the end of the course, students will have an understanding of: Fundamental design philosophies that multicore architectures address. Parallel programming philosophies and emerging best practices. This course is offered during the Independent Activities Period (IAP), which is a special 4-week term at MIT that runs from the first week of January until the end of the month. The course can be tailored to a normal semester time line."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.911",
            "Transcribing Prosodic Structure of Spoken Utterances with ToBI",
            "This course presents a tutorial on the ToBI (Tones and Break Indices) system, for labelling certain aspects of prosody in Mainstream American English (MAE-ToBI). The course is appropriate for undergrad or grad students with background in linguistics (phonology or phonetics), cognitive psychology (psycholinguistics), speech acoustics or music, who wish to learn about the prosody of speech, i.e. the intonation, rhythm, grouping and prominence patterns of spoken utterances, prosodic differences that signal meaning and phonetic implementation. Please submit any feedback about the course content using the user survey."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "7.349",
            "Biological Computing: At the Crossroads of Engineering and Science",
            "Imagine you are a salesman needing to visit 100 cities connected by a set of roads. Can you do it while stopping in each city only once? Even a supercomputer working at 1 trillion operations per second would take longer than the age of the universe to find a solution when considering each possibility in turn. In 1994, Leonard Adleman published a paper in which he described a solution, using the tools of molecular biology, for a smaller 7-city example of this problem. His paper generated enormous scientific and public interest, and kick-started the field of Biological Computing, the main subject of this discussion based seminar course. Students will analyze the Adleman paper, and the papers that preceded and followed it, with an eye for identifying the engineering and scientific aspects of each paper, emphasizing the interplay of these two approaches in the field of Biological Computing. This course is appropriate for both biology and non-biology majors. Care will be taken to fill in any knowledge gaps for both scientists and engineers. This course is one of many Advanced Undergraduate Seminars offered by the Biology Department at MIT. These seminars are tailored for students with an interest in using primary research literature to discuss and learn about current biological research in a highly interactive setting."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "18.413",
            "Error-Correcting Codes Laboratory",
            "This course introduces students to iterative decoding algorithms and the codes to which they are applied, including Turbo Codes, Low-Density Parity-Check Codes, and Serially-Concatenated Codes. The course will begin with an introduction to the fundamental problems of Coding Theory and their mathematical formulations. This will be followed by a study of Belief Propagation--the probabilistic heuristic which underlies iterative decoding algorithms. Belief Propagation will then be applied to the decoding of Turbo, LDPC, and Serially-Concatenated codes. The technical portion of the course will conclude with a study of tools for explaining and predicting the behavior of iterative decoding algorithms, including EXIT charts and Density Evolution."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "18.433",
            "Combinatorial Optimization",
            "Combinatorial Optimization provides a thorough treatment of linear programming and combinatorial optimization. Topics include network flow, matching theory, matroid optimization, and approximation algorithms for NP-hard problems."
            );'''
    )
    cursor.execute(
        '''INSERT INTO courses(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "20.180",
            "Biological Engineering Programming",
            "In this course problems from biological engineering are used to develop structured computer programming skills and explore the theory and practice of complex systems design and construction. The official course Web site can be viewed at: BE.180 Biological Engineering Programming."
            );'''
    )
    connection.commit()
    connection.close()
