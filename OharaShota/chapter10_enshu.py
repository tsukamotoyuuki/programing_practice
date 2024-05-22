import re
num_of_games = 48
num_of_wins = 31
print("Winning percentage: %.3f"%(num_of_wins/num_of_games))
print(F"Winning percentage: {num_of_wins/num_of_games:.3}")

phone = re.compile("((080|090)-\d{4}-\d{4})")
print(phone.findall("080-7962-4845,090-7788-7844,06-6969-7896"))

date = re.compile("\d{4}年\d{1,2}月\d{1,2}日")
print(date.findall("2020年12月30日は2000年12月30日に生まれた私の20回目の誕生日だった。2019年12月30日ぶりである"))