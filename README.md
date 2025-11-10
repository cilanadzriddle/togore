# evildoro
My first ever coding project! `evildoro` is a terminal user interface (TUI) timer tool with Pomodoro capabilities using Python and the Textual library. Heh heheh... heh... heh...
# Installation
Clone this repository and download the libraries (sorry):
- `argparse`
- `subprocess`
- `textual`
# Usage
Use `python` to compile the application. `evildoro` uses the `argparse` library, so make sure to add the necessary arguments. Yeah...
## Arguments
| Flag | Description              |
|------|--------------------------|
| -s   | Work seconds             |
| -m   | Work minutes             |
| -r   | Work hours               |
| -S   | Rest seconds             |
| -M   | Rest minutes             |
| -R   | Rest hours               |
| -c   | Number of cycles         |
| -t   | Title of task (required) |
## Example usage
```
python evildoro.py -m 25 -M 5 -t "Cry" -c 5
```
## `on_` files
You may add commands to the following files for extra and customizable functionality:
- `on_execution`
- `on_work`
- `on_rest`
- `on_finish`
# Help
Help.

