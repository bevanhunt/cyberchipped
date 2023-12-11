from cyberchipped.assistants import Assistant


def main() -> int:
    with Assistant() as ai:
        return ai.say("1+1", user_id="123")


if __name__ == "__main__":
    print(main())
