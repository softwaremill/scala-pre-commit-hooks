# Pre-commit/Pre-push hooks for Scala

## Overview

To make your code go smoother while still maintaining high code quality.

## Why

Scala has a quite rich build ecosystem, and a myriad of tools to help you writ good code. However, the build system(s) are relatively slow, so any helpers executed via those build system run the risk of interrupting the flow of a developer.

Moreover, some of the code quality tools/features (like unused import checks) are actively in opposition to a "run-often" coding approach.

Moving relevant checks to the pre-commit/pre-push phases partially alleviates those two issues.

## How

This is a set of hooks defined in the excellent [pre-commit](https://pre-commit.com/) library.

Currently, they include the following:

- `sbt-fatal-warnings` - turns on `-Xfatal-warnings`, runs a clean compilation on the given scope.
- `sbt-unused-imports` - as above, but also adds the "unused imports" warning.
- `sbt-scalafmt` - runs `scalafmtCheckAll`.
- `sbt-wartremover` - runs the wartremover plugin.

To add one or more of the hooks into your repo:

 1. Have everyone on your team install [pre-commit](https://pre-commit.com/#install).
 2. Add a `.pre-commit-config.yaml` file to your repository, with the following syntax:

    ```yaml
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: {currentVersion}
        default_phase: push #change to commit if desired
        hooks: #mix and match any of the following:
        -   id: sbt-fatal-warnings #arguments optional
            args: [--scope={defaultScope}]
        -   id: sbt-unused-imports #includes fatal warnings, arguments optional
            args: [--scope={defaultScope}]
        -   id: sbt-scalafmt
        -   id: sbt-wartremover #arguments are optional
            args: [--warts=Warts.unsafe, --scope={defaultScope}]
    ```

 3. Run `pre-commit install` to apply your hooks to the repo.

### How to control hook run time

By default, the hooks defined here run on *both* pre-commit and pre-push. They do, however, require some time to get running
on large codebases, especially since each hook's execution is essentially a clean build.

To limit hook runs to e.g. `pre-push`, you need to add a `stages` argument with the relevant value:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: {currentVersion}
    hooks:
    -   id: sbt-fatal-warnings
        stages: [push] #or [commit, push] etc.
```