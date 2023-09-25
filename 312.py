def check_pattern(s):
    patterns = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]
    if s in patterns:
        return "Yes"
    else:
        return "No"

# テスト
print(check_pattern("ACE"))  # 出力: Yes
print(check_pattern("XYZ"))  # 出力: No
