# CS252-GroupProj

## About

This project, or infered internally as MGAF, is a course project of MUST CS252, semester 2202. 

This project is a forum framework that is used to implement a forum for students of MUST to share and exchange information regards their graduate application.

For more course related information, please refer to materials under `./documentation`.

**Important Note**

The security of the backend code was never considered during the development. This project should NOT be deployed on a public server under all circumstances.

## Requirements & Dependencies

* `MySQL 8.0.23`
* `Python 3.7`
  * Packages:
    * `Flask`
    * `PyMySQL`
    * `Jinja2`
* A modern desktop browser
* local port `8080`

This project also uses `jQuery`, bundled with source code under `./app/static/js/`

**Note:**

The bundled `venv` in the repository should contain all dependencies that this project requires.

This project was tested on macOS Monterey beta 12.4 on a M1 chip mac.

The browser used for testing was Firefox, version `101.0b7`.

## Usage

If this is the first time you run this project:
1. run `./tests/utils/init.sql` on your sql server.
2. [ optional ] run `./tests/utils/data_generation.sql` on your sql server to generate some placeholder data.
3. configure the connect parameters in `./app/init.py, lineno 7`

Then run `main.py`.

After a successful startup, visit `127.0.0.1:8080` or your IP address on your LAN from your browser.

## Commit Style Guidelines

> Note: GitHub supports markdown style rendering in commit messages. You may consider to use them to improve the readability of your commit.

The recommended commit style is shown as follows:

```
<jira-issue-key> [<type>](<scope>) <subject>  # This line is called as HEADER
# Blank line
<body>
# Blank line
<footer>
```

The field `<jira-issue-key>` is used to link the commit to existing jira issue board. For instance: `MGAF-1`

The field `<type>` is used to describe the type of the commit, and only the listed tags are allowed:

> - `feat`: new features
> - `fix`: bug-fixes
> - `docs`: documentations
> - `style`: formatting (changes that does not affect the functionality of the code)
> - `refactor`: refactoring（changes that does not add new features nor bug-fixes）
> - `test`: changes of test cases, test drivers and other test-related features
> - `chore`: changes of build tools or other assistive tools
> - `revert`: used to specify the commit is used to revert a previous commit, in this case this tag MUST be used. It is advised to attach the `HEADER` of the reverted commit

`<scope>`(optional): `scope is used to specify the affected parts of the code in this commit.

`<subject>`: `subject` is a short description of the commit.

`<body>`(optional): `body` is a detailed description of the commit and can be composed of multiple lines.

`<footer>`(optional)

**Example:**

```
MGAF-1 [chore] Link repo to jira
```

## Related Resources

Project Kanban: https://hexinyirona.atlassian.net/jira/software/projects/MGAF/issues/