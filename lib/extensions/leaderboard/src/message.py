def message(arr, max, usercount):
    sumFromUsers = 0

    string = f"""
**🏆 LEADERBOARD 🏆**
Za posledných {max} správ, najviac správ poslali:\n\n"""
    for user, count in sorted(arr.items(), key = lambda x: x[1], reverse=True):
        string = string + f'**{user}:** {count} správ\n'
        sumFromUsers += int(count)
        usercount -= 1
        if not usercount:
            break
    
    string = string + f"\n*({int(sumFromUsers/max * 100)}% všetkých správ)*"
    
    return string