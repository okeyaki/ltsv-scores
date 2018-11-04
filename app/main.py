import injector

import app.command


def main():
    container = injector.Injector()

    command = container.get(app.command.Command)

    command.run()


if __name__ == "__main__":
    main()
