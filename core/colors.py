import os, sys
ENABLED = sys.stdout.isatty() and os.getenv("NO_COLOR") is None
def c(code,s): return f"\033[{code}m{s}\033[0m" if ENABLED else s
def red(s): return c("91",s)
def green(s): return c("92",s)
def yellow(s): return c("93",s)
def blue(s): return c("94",s)
def magenta(s): return c("95",s)
def cyan(s): return c("96",s)
def bold(s): return c("1",s)
def dim(s): return c("2",s)
def paint_cmd(s): return bold(cyan(s))
def paint_opt(s): return yellow(s)
def paint_val(s): return magenta(s)
