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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "6.080",
            "Great Ideas in Theoretical Computer Science",
            "This course provides a challenging introduction to some of the central ideas of theoretical computer science. It attempts to present a vision of "computer science beyond computers": that is, CS as a set of mathematical tools for understanding complex systems such as universes and minds. Beginning in antiquity—with Euclid's algorithm and other ancient examples of computational thinking—the course will progress rapidly through propositional logic, Turing machines and computability, finite automata, Gödel's theorems, efficient algorithms and reducibility, NP-completeness, the P versus NP problem, decision trees and other concrete computational models, the power of randomness, cryptography and one-way functions, computational theories of learning, interactive proofs, and quantum computing and the physical limits of computation. Class participation is essential, as the class will include discussion and debate about the implications of many of these ideas."
            );'''
    )
    cursor.execute(
        '''INSERT INTO users(
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
        '''INSERT INTO users(
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
        '''INSERT INTO users(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "",
            "",
            ""
            );'''
    )
    cursor.execute(
        '''INSERT INTO users(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "",
            "",
            ""
            );'''
    )
    cursor.execute(
        '''INSERT INTO users(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "",
            "",
            ""
            );'''
    )
    cursor.execute(
        '''INSERT INTO users(
            course_number,
            course_title,
            course_description
            )
            VALUES(
            "",
            "",
            ""
            );'''
    )
    connection.commit()
    connection.close()
