from hashlib import sha256

def create_csv(fname, start_num, count):
    """
    Create a csv named fname containing n count.
    Each row will contain:
        * number (starting at start_num)
            * incremented by 1 each row
        * the sha256.hexdigest() value of the string version of number
    """
    with open(fname, "w+") as f:
        result_str = ""

        end_num = start_num + count
        i = start_num

        while i < end_num:
            s = str(i)
            hex_str = hex(i)[2:] # drop the leading "0x"

            result_str += "{},{}\n".format(s, hex_str)
            i += 1

        f.write("string,hex\n")
        f.write(result_str)

# from 100_000 (0x186a0) to 899_999 (0xdbb9f)
create_csv('data.csv', 100_000, 800_000)
