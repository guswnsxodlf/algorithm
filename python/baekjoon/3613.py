# Created by Jello on 2017. 9. 20.
import sys

V = sys.stdin.readline().strip()
is_java = True
is_C = True
is_already_underbar = False

if V[0].isupper() or V[0] == '_' or V[-1] == '_':
    is_java, is_C = False, False

if is_java and is_C:
    for i in range(1, len(V)):
        if V[i] == '_':
            is_java = False

            if is_already_underbar:
                is_java, is_C = False, False

            is_already_underbar = True
        else:
            is_already_underbar = False

        if V[i].isupper():
            is_C = False

        if i == len(V)-1 and V[i] == '_':
            is_java, is_C = False, False

if is_C and is_java:
    sys.stdout.write(V)

elif is_C:
    change_upper = False
    for i in range(len(V)):
        if V[i] == '_':
            change_upper = True
        else:
            if change_upper:
                sys.stdout.write(V[i].upper())
                change_upper = False
            else:
                sys.stdout.write(V[i])

elif is_java:
    for i in range(len(V)):
        if V[i].isupper():
            sys.stdout.write('_'+V[i].lower())
        else:
            sys.stdout.write(V[i])

else:
    sys.stdout.write('Error!')
