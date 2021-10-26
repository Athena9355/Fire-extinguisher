import random

from flask import Blueprint, jsonify
from werkzeug.debug import console

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

comment1 = []
comment_list1 = [
    "Student A, who had Teacher A, really enjoyed their time in Math Class. "
    "Educational, interactive, and enjoyable are words they’d use to describe the class",
    "I really did not like this class. Would not take math by Teacher A - Student B",
    "911,  there’s an emergency, Teacher A and their math is absolute fire! Like in a good way. - Student C",
    "Hello, I really enjoyed Teacher A when they taught science - Student E",
    "I really like Teacher A because they are super nice, but they don't teach well - Student D",
    "Teacher A gave a lot of homework, but she taught very well. - Student F"

]

comment2 = []
comment_list2 = [
    "Student A, who had Teacher B, really enjoyed their time in Math Class. "
    "Educational, interactive, and enjoyable are words they’d use to describe the class",
    "I really did not like this class. Would not take math by Teacher B - Student B",
    "911,  there’s an emergency, Teacher B and their math is absolute fire! Like in a good way. - Student C",
    "Hello, I really enjoyed Teacher B when they taught science - Student E",
    "I really like Teacher B because they are super nice, but they don't teach well - Student D",
    "Teacher B gave a lot of homework, but she taught very well. - Student F"
]


def _find_next_id():
    return max(comment1["id"] for a in comment1) + 1




def _find_next_id():
    return max(comment2["id"] for a in comment2) + 1


def _init_comment1():
    id = 1
    for comment3 in comment_list1:
        comment1.append(comment3)
        id += 1


def _init_comment2():
    for comment in comment_list2:
        comment2.append(comment)

def get_comment1():
    if len(comment1) == 0:
        _init_comment1()
    return random.choice(comment1)



def get_comment2():
    if len(comment2) == 0:
        _init_comment2()
    return random.choice(comment2)



if __name__ == "__main__":
    print(random.choice(comment_list1))

if __name__ == "__main__":
    print(random.choice(comment_list2))
