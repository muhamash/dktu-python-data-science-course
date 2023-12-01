def morse_to_text(data: str) -> str:
    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
    }

    each_data = data.split("  ")
    # print(each_data)
    my_decoded_code = []
    for data in each_data:
        get_data = data.split(" ")
        print(get_data)
        my_code = ""
        for i in get_data:
            # print(i)
            my_code = my_code + morse_code_dict[i]
        # return my_code
        my_decoded_code.append(my_code)
    return " ".join(my_decoded_code)


print(morse_to_text("..  .- --  .-  ... --.- ..- .. .-. .-. . .-.."))
