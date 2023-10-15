def to_do():
    to_do_list = []

    while True:
        tasks = input()

        if tasks == 'End':
            break

        to_do_list.append(tasks)

    sorted_list = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    final_to_do_list = [x.split("-")[1] for x in sorted_list]
    return print(final_to_do_list)


to_do()
