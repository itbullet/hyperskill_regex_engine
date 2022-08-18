import sys
sys.setrecursionlimit(10000)


def regex_chr_cmp(rgx_, chr_):
    if bool((rgx_ == chr_) or (not rgx_ or rgx_ == '.')):
        return True
    return False


def regex_back_check(rgx_, default_str_):
    for i in reversed(range(len(default_str_))):
        # print(default_str_[i:])
        if regex_eq_str_cmp(rgx_, default_str_[i:], default_str_):
            if len(rgx_) == len(default_str_[i:]):
                return True
    return False


def regex_eq_str_cmp(rgx_, str_, default_str_, count=0):
    if rgx_ == '$' and not str_:
        return True
    elif not rgx_:
        return True
    else:
        if rgx_[0] == '\\':
            rgx_ = rgx_[1:]

        if not str_:
            if count == 0 and regex_back_check(rgx_[2:], default_str_):
                return True
            if count > 0 and regex_back_check(rgx_[:-1], default_str_):
                return True
            return False
        else:
            if len(rgx_) > 1 and rgx_[1] == '?' and rgx_[0] != '\\':
                if regex_chr_cmp(rgx_[0], str_[0]):
                    return regex_eq_str_cmp(rgx_[2:], str_[1:], default_str_)
                else:
                    return regex_eq_str_cmp(rgx_[2:], str_, default_str_)
            elif len(rgx_) > 1 and rgx_[1] == '*' and rgx_[0] != '\\':
                if len(str_) > 1 and regex_chr_cmp(rgx_[0], str_[0]):
                    return regex_eq_str_cmp(rgx_, str_[1:], default_str_, count+1)
                else:
                    return regex_eq_str_cmp(rgx_[2:], str_, default_str_, count+1)
            elif len(rgx_) > 1 and rgx_[1] == '+' and rgx_[0] != '\\':
                if regex_chr_cmp(rgx_[0], str_[0]):
                    if len(str_) > 1 and regex_chr_cmp(rgx_[0], str_[1]):
                        return regex_eq_str_cmp(rgx_, str_[1:], default_str_, count+1)
                    else:
                        return regex_eq_str_cmp(rgx_[2:], str_[1:], default_str_, count+1)
                else:
                    return False
            elif not regex_chr_cmp(rgx_[0], str_[0]):
                return False
            else:
                return regex_eq_str_cmp(rgx_[1:], str_[1:], default_str_)


def regex_str_cmp(rgx_, str_):
    default_str = str_
    if regex_eq_str_cmp(rgx_, str_, default_str):
        return True
    elif rgx_[0] == '^':
        return regex_eq_str_cmp(rgx_[1:], str_, default_str)
    else:
        if not str_:
            return False
        else:
            return regex_str_cmp(rgx_, str_[1:])


if __name__ == '__main__':
    regex, str_input = input().split('|')
    print(regex_str_cmp(regex, str_input))

