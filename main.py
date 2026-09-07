from game import Game


def main():
    game = Game()
    game.run_logic_test(seconds=5.0, step=0.1)


if __name__ == "__main__":
    main()
