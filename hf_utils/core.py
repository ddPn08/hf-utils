import glob
import importlib
import os
import fire

commands = {}


def main():
    file_dir = os.path.dirname(os.path.abspath(__file__))

    print(file_dir)

    for file in glob.glob(os.path.join(file_dir, "commands", "*.py")):
        basename = os.path.basename(file).replace(".py", "")
        module = importlib.import_module(f"hf_utils.commands.{basename}")
        if hasattr(module, "cli"):
            commands[basename] = module.cli

    fire.Fire(commands)


if __name__ == "__main__":
    main()
