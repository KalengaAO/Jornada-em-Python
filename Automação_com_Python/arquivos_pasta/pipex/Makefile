NAME = pipex
SRC = src/*.c
CC = cc
CFLAGS = -Wall -Wextra -Werror -I inc

all: $(NAME)

$(NAME): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(NAME)

clean:
	rm -f *.o

fclean: clean
	rm -f $(NAME)

re: fclean all
