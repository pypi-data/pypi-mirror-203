# Uh Little Less Dumb Config Options


The configuration file for the Uh Little Less Dumb note taking framework is a python file, by default found at `$HOME/ulldConfig.py`.

If you're new to the command line, Python, or code in general don't fret. While knowing a bit of Python opens the door to new possibilities for certain configuration options, it is by no means a requirement and most configuration options can be set with some very basic syntax knowledge that we'll cover right here. For those that are already familiar with Python or the command line, feel free to skip ahead to the _Options Overview_ section.

## For those new to the command line and/or Python

### Finding your home directory
Open up your terminal as you would any other app. There are only a handful of commands that are required to navigate a terminal, so let's start with `cd` for _'change directory'_. In many cases, entering `cd` without a direction as to where it should change to, it will default to your `$HOME` directory. If you run that without receiving an error, *congratulations*... you're in your home directory and now we can find or create that config file. If you did receive a message that a required argument wasn't supplied, we can print the name of that `$HOME` directory by using the command `echo $HOME`, which in my case on a MacOS operating system prints `/Users/bigsexy/`. While your file path might not provide the same ego boost and flattery, it should be of similar length. We can then combine the two commands and run `cd $HOME` to change to that directory.

### Editing or creating the Python file
While writing code in the case of runtime compiled languages like Python requires no special tools and can be done in the notes app on your phone or Microsoft Word, syntax highlighting makes a _world_ of difference. There are many great free tools out there for writing code, and the best of them have applications outside of the work a developer might do. Even if you only plan to use it for this one file, I'd heavily recommend downloading VS Code from Microsoft. It's a much less specific development environment that shares many of the same features that their super comprehensive Visual Studio software does, but also has a phenomenal community run collection of plugins that will help us both edit the python configuration file and write the markdown as well. 

Once you've downloaded VS Code, cruise around those menus a bit until you find the extension menu and install the most popular Python and Markdown extensions. While Uh Little Less Dumb is still _very_ new and under constant development, it does not have it's own VS Code plugin as of now. That is a plan in the works for the near future, but the majority of the features of Uh Little Less Dumb share exactly the same syntax as standard markdown and only differ in that it allows certain features that are not included in standard markdown parsers. Because of this you might run into certain errors that are indicated inside of VS Code through their markdown extensions that are not actual errors in Uh Little Less Dumb.  

### Basic Python syntax needed to set up the config file


# Config Overview


# Options Overview

### Alternative config location

`ULLD_CONFIG` is an environment variable that can be set system wide to override the location of the default configuration file. If you're new to the command line you will need to look into where this should be set on your specific operating system. On current MacOS systems that is in the home directory at `$HOME/.zshrc` and can be set by simply appending `ULLD_CONFIG="new/path/to/file"`. It's safe to add environment variables to your terminal that aren't as universal as `$HOME`... but for the love of sunsets, puppies and Giannis Antetokounmpo _please_ be careful of what you delete from these core system wide files, and make sure you only follow the instructions of platforms that you trust.

While the alternate location of Uh Little Less Dumb's configuration file is something that needs to be available system wide so ULLD can find the configuration itself, the rest of these will all be set as options in the various python classes supplied by ULLD. If this is your first time writing code just pay careful attention to the _type_ each option is expecting, to which class that option belongs, and to the syntax for that _type_ described above. Remember, when working with code `1` is not the same as `"1"`, and neither is the same as `[1]`.


### ULLD_Core

- `ULLD_Core.include_core_styles: bool = True`
    - Should the ULLD framework include a bare bones style sheet with the build process. This steel sheet does not reflect the overall style of any specific theme, but rather enforces certain alignment and layout rules as they apply to some of ULLD's core components. Unless you plan to write your own css from scratch or you plan to use a theme that recommends setting this to `False` you will likely always want this turned on.





### ULLD_DP 
(directory parser)
```python
def default_directory_to_title(directory_path: str) -> str:
    pd = str(directory_path).split("/")
    return ''.join([f'{x[0].upper()}' + f'{x[1:]} ' for x in f'{pd[-2] if pd[-2] is not None else "Notes"}'.split("_")]) if len(pd) >= 2 else f'{config.rootDirectoryName if config.rootDirectoryName is not None else "Notes"}'.replace("_", " ").capitalize()
```

- `ULLD_DP.filename_to_string: Callable = default_directory_to_title(directory_path: str)`
    - A function that will take each directory as a string representing that directory's absolute path and return a category title for the notes contained in that directory. By default this replaces underscores (_) with spaces and capitalizes the first letter of each word while leaving other capital letters remain capitalized. 
    - For example, the following tree would map to the category title's as described.

```zsh
/Users/bigsexy/notes/math/Calculus_I/derivatives.md
/Users/bigsexy/notes/math/Calculus_I/indefinate_integrals.md
/Users/bigsexy/notes/math/Calculus_II/integration_by_parts.md
/Users/bigsexy/notes/math/trig/identities.md
``` 

```
config.rootDirectoryName -> Math -> Calculus I -> Derivatives
config.rootDirectoryName -> Math -> Calculus I -> Indefinite Integrals
config.rootDirectoryName -> Math -> Calculus II -> Integration By Parts
config.rootDirectoryName -> Math -> Trig -> Identities
```


- `ULLD_DP.parsable_extensions: List[str] = ["md"]`
    - As of this writing this option isn't really much of an option at all and must be left unchanged, but options for "csv", "html", "npy", "json", and "xml" will be added in the near future along with some related components and features, while ways to integrate SQL, Excel, and PDF files directly will likely be added as this project grows.

- `ULLD_DP.ignore_regex: List[str] = [".config", "_build", "_static", "build", ".git", ".docs", "node_modules", ".obsidian", ".media", "__pycache__", ".virtual_documents"]`
    - File names or directory names added here will be compared using regular expressions with the absolute path of each file being parsed, and those evaluating to `True` will be ignored. Be aware that adding your own strings to this list and _*not*_ including the default options which include the build directory, node_modules, git and cache files could lead to horrendous build times. If you would like nothing to be ignored, simply set this to an empty list.

- `ULLD_DP.ignore_filenames: List[str] = []`
    - This is very similar to `ULLD_DP.ignore_regex` and accomplishes the same thing. The only difference is that this will be compared to each _file_ name, not the directory name and compared using a direct comparison as opposed to a regular expression. What is accomplished by this option can easily be accomplished with the `ignore_regex` option but this is available for convenience. This might be useful for keeping files located within a directory they apply to, but those that would only be useful while writing notes and not reviewing them.

- `ULLD_DP.parsable_files_shifted_index: dict = {"regex pattern": negative int}`
    - This option will map through the supplied dict and test each absolute file path against the pattern supplied in the key, and shift the matching files upwards $n$ levels for the value $-n$ of the matching pattern.
    - For example, setting this option to `{"*/markdown/**.md": -1}` would find every file in a directory called `markdown`, and shift the contents up to that directory's parent. This might be useful for keeping multiple file types in the same directory or parent directory, and stop the sub directory label from appearing in the rendered notes. This would move `notes/math/calc_I/markdown/derivatives.md` to `Notes -> Math -> Calc I -> Derivatives` and therefore removing the markdown categorization that would only be applicable while writing notes and not while reviewing them.
