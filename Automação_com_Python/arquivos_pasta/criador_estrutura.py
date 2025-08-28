from pathlib import Path

title = "Script para criar estruturas de projecto"
print(title.upper())
project = str(input("Digite o nome do projecto: ")).strip()

base = Path(project).expanduser().resolve()

src = base / "src"
inc = base / "inc"
base.mkdir(exist_ok=True)
src.mkdir(exist_ok=True)
inc.mkdir(exist_ok=True)
filesrc = (src / project).with_suffix(".c")
fileinc = (inc / project).with_suffix(".h")
filesrc.touch(exist_ok=True)
fileinc.touch(exist_ok=True)
makefile = base / "Makefile"
makefile.touch(exist_ok=True)

filesrc.write_text(
	f'#include "../inc/{project}.h"\n'
	"int main(void)\n"
	"{\n"
	'\tprintf("%s", "olá mundo");\n'
	"return (0);\n}"
)

fileinc.write_text(
			f"#ifndef FDF_H\n"
			"#define FDF_H\n"
			"\t#include <stdio.h>\n"
			"#endif"
)

makefile.write_text(
    f"NAME = {project}\n"
    "SRC = src/*.c\n"
    "CC = cc\n"
    "CFLAGS = -Wall -Wextra -Werror -I inc\n\n"
    "all: $(NAME)\n\n"
    "$(NAME): $(SRC)\n"
    "\t$(CC) $(CFLAGS) $(SRC) -o $(NAME)\n\n"
    "clean:\n"
    "\trm -f *.o\n\n"
    "fclean: clean\n"
    "\trm -f $(NAME)\n\n"
    "re: fclean all\n"
)
print(f"Projecto criado no caminho: {base.resolve()}")
