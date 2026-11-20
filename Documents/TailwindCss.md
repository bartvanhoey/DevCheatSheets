## TailwindCss

## Tailwind CLI Installation

### Install Tailwind CSS via npm

```bash
    npm install tailwindcss @tailwindcss/cli
```

### import Tailwind in your CSS file

```css
    /* src/input.css */
    @import "tailwindcss";
```

### Start the Tailwind CLI build process

```bash
    npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

### Start using Tailwind in your HTML

```html
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="./src/output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

### Add scripts section to package.json

```json
  "scripts": {
   "start": "npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch"
  }

// Run the Tailwind build process via npm
// npm start
```

## Tailwind Utility classes

| Extension                                   | Description                                                                |
|---------------------------------------------|----------------------------------------------------------------------------|
| `flex-auto`                                 | Intelligent Tailwind CSS tooling for VS Code                               |
| `flex-col` | Intelligent Tailwind CSS tooling for VS Code                               |
| `flex-row` | Intelligent Tailwind CSS tooling for VS Code                                |

## Tailwind VSCode Extensions

| Extension                                   | Description                                                                |
|---------------------------------------------|----------------------------------------------------------------------------|
| `Tailwind CSS Intellisense - Tailwind Labs` | Intelligent Tailwind CSS tooling for VS Code                               |
| `Tailwind Fold - Stivo`                     | Intelligent Tailwind CSS tooling for VS Code                               |
| `Headwind - Ryan Heybourn`                  | Sorts and organizes Tailwind CSS classes                                   |

### How to get rid off the underlined Unknown errors in tailwind

Go to File -> Preferences -> Settings
Search for **Unknown** and select **ignore** in CSS>Lint:Unknown At Rules

### How get Tailwind Intellisense when using Emmet

Go to  Settings of **Tailwind CSS Intellisense**
and enable **Tailwind CSS > Emmet Completions**
