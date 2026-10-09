# claude-code

## How To Install

```shell
npm install -g @anthropic-ai/claude-code
```

## Claude Code is a new kind of AI assistant

1. Terminal-based, not IDE
1. Works with all tools
1. Fits into all existing workflows
1. General purpose - you can use it for almost anything
1. Infinitely hackable

## Optimize your setup

Get set up:

| Command | Example |
| - | - |
| /allowed-tools | Customize tool permissions |
| /install-github-app | Tag @claude on your issues & PRs |
| /config | Turn on notifications |
| /terminal-setup | Enable shift+enter to insert newlines |
| /theme | Enable light/dark mode |
| | Turn on MacOS dictation |

## Claude Code Q&A: Use Claude Code to answer questions about your codebase

1. The easiest way for new users to start with code
1. Zero setup needed
1. Your data stays local

### Examples

```
> How is @RoutingController.py used?
```

```
> How do I make a new @app/services/ValidationTemplateFactory?
```

```
> Why does recoverFromException take so many arguments? Look through git history to answer
```

```
> Why did we fix issue #18363 by adding the if/else in @src/login.ts API?
```

```
> In which version did we release the new @api/ext/PreHooks.php API?
```

```
> Look at PR #9383, then carefully verify which app versions were impacted
```

```
> What did I ship last week?
```

### Tips

1. use codebase Q&A as a way to dip your feet into Claude Code
1. practice prompting, and start to understand what Claude Code "gets" immediately vs. what needs more specific instructions

## Editing Code: Use tools to get things done

- Claude Code ships with a dozen tools out of the box. Tool are what makes Claude Code so powerful.
- Built-in tools: bash, file search, file listing, file read and write, web fetch and search, TODOs, sub-agents

### Steer Claude to use tools your way

Example prompts

```
> Propose a few fixes for issue #8732, then implement the one I pick
```

```
> Identify edge cases that are not covered in `@app/tests/signupTest.ts`, then update the tests to cover these. think hard
```

```
> commit, push, pr
```

```
> Use 3 parallel agents to brainstorm ideas for how to clean up `@services/aggregator/feed_service.cpp`
```

### Plug in your team's tools

Tell Claude about your bash tools
```
> Use the barley CLI to check for error logs in the last training run. Use -h to check how to use it.
```

Tell Claude about your MCP tools
```shell
$ claude mcp add barley_server -- node myserver
```

```
> Use the barley MCP server to check for error logs in the last training run
```

### Common workflows

Explore > plan > confirm > code > commit
```
> Figure out the root cause for issue #983, then propose a few fixes. Let me choose an approach before you code. ultrathink
```

Write tests > commit > code > iterate > commit
```
> Write tests for @utils/markdown.ts to make sure links render properly (note the tests won't pass yet, since links aren't yet implemented). Then commit. Then update test code to make the tests pass.
```

Write code > screenshot result > iterate
```
> Implement [mock.png], Then screenshot it with Puppeteer and iterate till it looks like the mock.
```

### Tips

1. teach Claude to use your tools
1. tailor the workflow to the task

## Give Claude context: More context = better performance

Claude does better with more context

There are a number of ways to give Claude more context:
- CLAUDE.md
- Slash commands
- At-mentioning filenames
- MCP resources

### Auto-add common bash commands, files, and style conventions to every session:

| Command | Description |
| - | - |
| /\<enterprise root\>/CLAUDE.md | Shared across all projects |
| ~/.claude/CLAUDE.md | Shared across all projects |
| project-root/ | |
|   CLAUDE.md | Checked in |
|   CLAUDE.local.md | Not checked in |
(Shortcut: type #)

### Pull in context on demand:

| Context | Command |
| - | - |
| ~/.claude/commands/foo.md | Type /user:foo |
| project-root/ | |
|   .claude/commands/foo.md | Type /project:foo |
|   a/ | TYpe @a |
|     commands/foo.md | Type /project:a:foo |
|     CLAUDE.md | Pulled in on demand |
|     foo.py | Type @a/foo.py |

```
.claude
  | commands
    | create-release-pr.md
    | fix-github-issue.md
    | get-feedback.md
    | label-github-issues.md
    | lint.md
```

### Tips

5. the more context your give Claude, the smarter it will be
6. take time to tune context
    - Is it for you or your team?
    - Do you want to add it automatically or lazily?

## Work with your team: Share permissions, memory, and MCP servers with your team

Build once, user everywhere

Enterprise policy > Global (just me) > Project (checked in) > Project (just me)

## Share with your team

TODO

