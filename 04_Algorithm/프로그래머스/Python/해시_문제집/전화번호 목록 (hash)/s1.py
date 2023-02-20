def solution(phone_book):
    answer = True
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            if temp in hash_map and temp != phone_number:
                answer = False
                print(temp, hash_map, phone_number, answer)
                break
        if not answer:
            break

    return answer

# phone_book
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false