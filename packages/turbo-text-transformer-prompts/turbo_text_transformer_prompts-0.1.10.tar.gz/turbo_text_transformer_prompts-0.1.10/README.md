# Turbo Text Transformer Prompts

Note this is automatically installed when you do `pip install turbo-text-transformer`. This repo is just for storing the templates.

Designed for use with [turbo-text-transformer](https://github.com/fergusfettes/turbo-text-transformer).

You pipe some text in, the template is applied, then you pipe it into `ttt` (from `pip install turbo-text-transformer`) which will process it with eg. OpenAI.

```
cat pyproject.toml tttp/__main__.py | tttp -t readme | ttt > README.md
```

Turbo Text Transformer Prompts is a command-line tool that allows users to generate text files from pre-configured templates using user input prompts. The tool uses Jinja2 templating engine to render text files from templates.

## How to Run

```sh
pip install turbo-text-transformer-prompts
```

You will also need to clone the repository containing the templates you want to use. For example:

```sh
mkdir -p ~/.config/ttt/
git clone https://github.com/fergusfettes/turbo-text-transformer-prompts ~/.config/ttt
```

## Template Structure

A template is a text file written in Jinja2 syntax. The file should have the `.j2` extension and be placed inside the `templates` directory. They will be installed in the `~/.config/ttt/templates` directory.

This is a smiple example of a template:

```jinja
Context: Provide only code as output.
Prompt: {{prompt}}
Code:
```

It will just output a code snippet based on the query.

You can also pass a list of flags to the prompt to fine tune the control, such as this:

```jinja
This is an example of minimally altering some given code to achieve a specific task.

I received the following code:

`{{language}}
{{prompt}}
`

My task was to make minimal alterations to this code to: "{{task}}".

The altered code is below.

`{{language}}
```

For this one, you can pass the 'task' and 'language' arguments to make it more specific.

## Contributing

PULL REQUESTS WITH MORE TEMPLATES VERY WELCOME!

If you find a bug or would like to contribute to Turbo Text Transformer Prompts, please create a new GitHub issue or pull request.

#  License

Turbo Text Transformer Prompts is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
