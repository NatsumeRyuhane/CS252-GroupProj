# CS360-GroupProj

## About

[Project description WIP]

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