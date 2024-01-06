class OutofLimit(Exception):
    pass


def get_input():
    """Get input until you got a number which is an integer among 1,2,3."""
    while True:
        # Handle Exception
        try:
            times = int(input("Please enter a number among 1,2,3: "))
            # raise error if times is not among 1,2,3
            if times < 0 or times > 3:
                raise OutofLimit("Please choose among 1,2,3.")
        except ValueError:
            print('Please enter an integer.')
        except OutofLimit as e:
            print(e)
        else:
            return times


def get_rand_input():
    """Get input of random number of integer among 1,2,3"""
    import random
    times = random.randint(1, 3)
    return times


def playGame(player, times, num):
    """Display the number and return it"""
    for _ in range(times):
        num += 1
        print(f"{player}: {num}")
        if num == 31:
            return num
    return num


def Game(player1, player2):
    """Play the game"""
    num = 0
    round = 0
    while True:
        round += 1
        print(f"Round {round}:")
        # Player 1
        print(f"It's {player1}'s turn.")
        if player1 == 'Computer':
            times_p1 = get_rand_input()
        else:
            times_p1 = get_input()
        num = playGame(player1, times_p1, num)
        if num == 31:
            print(f"\n{player2} wins.")
            break
        # Player 2
        print(f"It's {player2}'s turn.")
        times_p2 = get_input()
        num = playGame(player2, times_p2, num)
        if num == 31:
            print(f"\n{player1} wins.")
            break
        print()


if __name__ == "__main__":
    # Two players mode: PlayerA & PlayerB
    Game('PlayerA', 'PlayerB')
    print('--------------------------------------')
    # Computer vs. Player mode
    Game('Computer', 'Player')
