def display_pages(display_list, n):
    if not display_list:
        return

    for i in range(len(display_list) // n + 1):
        print("Page: " + str(i))
        visited = set()
        ind = 0
        display_ind = 0
        while ind < n:
            host_id = display_list[display_ind].split(",")[0]
            if host_id not in visited:
                print(display_list[display_ind])
                visited.add(host_id)
                ind += 1
                display_list.pop(display_ind)
                display_ind -= 1
            if display_ind == len(display_list) - 1:
                for _ in range(n - ind):
                    if display_list:
                        print(display_list.pop(0))
                    else:
                        break
                break
            display_ind += 1
