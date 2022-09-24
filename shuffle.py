import collections


def count_character(shuffled_string):
    char_count = dict()
    for char in shuffled_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def count_unique_char_digits(char_count, digit_count):
    digit_count[0] = char_count.get('z', 0) 
    digit_count[2] = char_count.get('w', 0)
    digit_count[4] = char_count.get('u', 0) 
    digit_count[6] = char_count.get('x', 0) 
    digit_count[8] = char_count.get('g', 0) 


def count_other_digits(char_count, digit_count):
    digit_count[1] = char_count.get('o', 0) - digit_count[0] - digit_count[2] - digit_count[4]
    digit_count[3] = char_count.get('h', 0) - digit_count[8]
    digit_count[5] = char_count.get('f', 0) - digit_count[4]
    digit_count[7] = char_count.get('s', 0) - digit_count[6]
    digit_count[9] = char_count.get('i', 0) - digit_count[5] - digit_count[6] - digit_count[8]


def count_digit(char_count):
    digit_count = [0] * 10
    count_unique_char_digits(char_count, digit_count)
    count_other_digits(char_count, digit_count)
    return digit_count


def find_smallest(digit_count):
    for number, count in enumerate(digit_count):
        if number != 0 and count > 0:
            return number


def smallest_number(digit_count):
    digit_list = []
    # first number
    smallest = find_smallest(digit_count)
    digit_list.append(str(smallest))
    digit_count[smallest] -= 1
    # other numbers
    for number, count in enumerate(digit_count):
        digit_list.extend([str(number)] * count)

    return "".join(digit_list)


def smallest_special_number(shuffled_string):
    char_count = count_character(shuffled_string)
    digit_count = count_digit(char_count)

    total_digits_count = sum(digit_count[1:])
    if total_digits_count <= 0:
        return "0"

    smallest_special_num = smallest_number(digit_count)
    return smallest_special_num


def main():
    T = int(input())
    for _ in range(T):
        shuffled_string = input()
        smallest_special_num = smallest_special_number(shuffled_string)
        print(smallest_special_num)


if __name__ == '__main__':
    main()