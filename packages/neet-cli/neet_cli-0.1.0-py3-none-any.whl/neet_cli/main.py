from neet_cli.problems_data import problems
import typer
import random

app = typer.Typer()

@app.command()
def select_at_random(show_category: bool = False):
    random_category = random.choice(list(problems.keys()))
    random_problem = random.choice(problems[random_category])
    if show_category: print(random_category)
    print(random_problem)

if __name__ == "__main__":
    app()