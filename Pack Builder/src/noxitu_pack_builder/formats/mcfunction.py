def mcfunction(generator, target_path):
    with open(target_path, "wt", encoding="utf-8") as fd:
        for command in generator():
            if "\n" in command:
                command = command.split("\n")
                command = [line.strip() for line in command]
                command = [line for line in command if line]
                command = " ".join(command)
            print(command, file=fd)
        print(file=fd)
